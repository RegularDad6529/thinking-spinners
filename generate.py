#!/usr/bin/env python3
"""
Thinking Spinner Generator CLI — render spinner GIFs from preset JSON.

Usage:
  python3 generate.py --preset preset.json -o output.gif
  python3 generate.py --preset preset.json -o output.gif --fps 25 --width 500
  python3 generate.py --list-presets
  python3 generate.py --preset overthinking -o output.gif

Works by loading the generator HTML in headless Chromium (via Playwright),
injecting the preset config, and capturing the GIF export as base64.

The generator HTML is not modified — humans use it exactly as before.
This script is a headless wrapper that drives the same code path.

Requirements:
  pip install playwright
  python -m playwright install chromium
"""
import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
GENERATOR_HTML = SCRIPT_DIR / "generator" / "index.html"
PRESETS_DIR = SCRIPT_DIR / "presets"

# Built-in presets (from the generator's own preset system)
BUILTIN_PRESETS = {
    "default": "Default Thinking",
    "overthinking": "Overthinking",
    "collector": "Collector Brain",
    "decision": "Decision Loop",
}


def load_preset(preset_arg: str) -> dict:
    """Load preset from file path or built-in name."""
    # Check if it's a file path
    preset_path = Path(preset_arg)
    if preset_path.exists():
        with open(preset_path) as f:
            return json.load(f)

    # Check presets directory
    if PRESETS_DIR.exists():
        preset_file = PRESETS_DIR / f"{preset_arg}.json"
        if preset_file.exists():
            with open(preset_file) as f:
                return json.load(f)

    # Check built-in presets
    if preset_arg in BUILTIN_PRESETS:
        return {"_builtin": preset_arg}

    print(f"Error: preset '{preset_arg}' not found.", file=sys.stderr)
    print(f"  File path: {preset_arg} (does not exist)", file=sys.stderr)
    print(f"  Presets dir: {PRESETS_DIR} (no {preset_arg}.json)", file=sys.stderr)
    print(f"  Built-in: {', '.join(BUILTIN_PRESETS.keys())}", file=sys.stderr)
    sys.exit(1)


def render_gif(preset: dict, output_path: str, fps: int = None, width: int = None) -> str:
    """Render a spinner GIF using headless Chromium via Playwright."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Error: playwright not installed. Run:", file=sys.stderr)
        print("  pip install playwright", file=sys.stderr)
        print("  python -m playwright install chromium", file=sys.stderr)
        sys.exit(1)

    # Apply CLI overrides
    if fps is not None:
        preset.setdefault("output", {})["fps"] = fps
    if width is not None:
        preset.setdefault("output", {})["width"] = width
        preset.setdefault("output", {})["height"] = width

    is_builtin = "_builtin" in preset
    builtin_name = preset.pop("_builtin", None)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 900, "height": 900})

        page.goto(f"file://{GENERATOR_HTML}")
        page.wait_for_load_state("networkidle")
        time.sleep(0.5)

        if is_builtin:
            # Load built-in preset via the dropdown
            page.select_option("#presetSelect", builtin_name)
            page.click("#loadPresetBtn")
            time.sleep(0.3)
        else:
            # Inject custom preset
            page.evaluate(f"""
            () => {{
                const preset = {json.dumps(preset)};
                if (typeof cfg !== 'undefined') {{
                    Object.assign(cfg, preset);
                    if (typeof syncFromState === 'function') syncFromState();
                    if (typeof draw === 'function') draw();
                    if (typeof play === 'function') play();
                }}
            }}
            """)
            time.sleep(0.3)

        # Override the download function to capture the blob
        page.evaluate("""
        () => {
            window._gifResult = null;
            window._gifDone = false;
            window.download = function(blob, filename) {
                const reader = new FileReader();
                reader.onload = function() {
                    window._gifResult = reader.result;
                    window._gifDone = true;
                };
                reader.readAsDataURL(blob);
            };
        }
        """)

        # Trigger GIF export
        page.click("#gifBtn")

        # Wait for completion
        start_time = time.time()
        timeout = 180  # 3 minutes max
        while time.time() - start_time < timeout:
            done = page.evaluate("() => window._gifDone")
            if done:
                break
            time.sleep(1)

        if not page.evaluate("() => window._gifDone"):
            print("Error: GIF rendering timed out after 180s", file=sys.stderr)
            browser.close()
            sys.exit(1)

        gif_data_url = page.evaluate("() => window._gifResult")
        browser.close()

        if not gif_data_url or not gif_data_url.startswith("data:image/gif"):
            print("Error: GIF export produced invalid data", file=sys.stderr)
            sys.exit(1)

        # Decode and save
        b64_data = gif_data_url.split(",")[1]
        gif_bytes = base64.b64decode(b64_data)

        with open(output_path, "wb") as f:
            f.write(gif_bytes)

        return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Generate thinking spinner GIFs from preset JSON"
    )
    parser.add_argument(
        "--preset", "-p",
        help="Preset file path, preset name from presets/ dir, or built-in name"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output GIF file path"
    )
    parser.add_argument(
        "--fps", type=int, default=None,
        help="Override FPS (0 = one frame per thought, 25 = smooth animation)"
    )
    parser.add_argument(
        "--width", type=int, default=None,
        help="Override output size (square, e.g. 500 or 800)"
    )
    parser.add_argument(
        "--list-presets", action="store_true",
        help="List available presets and exit"
    )

    args = parser.parse_args()

    if args.list_presets:
        print("Built-in presets:")
        for key, name in BUILTIN_PRESETS.items():
            print(f"  {key:15s} — {name}")
        if PRESETS_DIR.exists():
            print(f"\nCustom presets ({PRESETS_DIR}):")
            for f in sorted(PRESETS_DIR.glob("*.json")):
                print(f"  {f.stem:15s} — {f}")
        return

    if not args.preset:
        parser.error("--preset is required (use --list-presets to see options)")
    if not args.output:
        parser.error("--output is required")

    preset = load_preset(args.preset)
    print(f"Rendering spinner...", file=sys.stderr)
    if not args.preset.endswith(".json") and args.preset in BUILTIN_PRESETS:
        print(f"  Preset: {BUILTIN_PRESETS[args.preset]} (built-in)", file=sys.stderr)
    else:
        print(f"  Preset: {args.preset}", file=sys.stderr)
        if args.fps:
            print(f"  FPS override: {args.fps}", file=sys.stderr)
        if args.width:
            print(f"  Size override: {args.width}x{args.width}", file=sys.stderr)

    output = render_gif(preset, args.output, fps=args.fps, width=args.width)

    file_size = os.path.getsize(output)
    print(f"Done: {output} ({file_size / 1024:.1f} KB)", file=sys.stderr)


if __name__ == "__main__":
    main()