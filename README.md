# Thinking Spinners

Network-created, network-governed animated spinners for The Memes collection.

Every spinner is submitted by a community member, voted on by the network on [6529.io](https://6529.io), and approved when it reaches 30,000,000 TDH. Approved spinners are released as CC0, minted into The Memes, and added to the [public gallery](https://arweave.net/DxbJyl-6xdtLtAuaJ0UQun3o3MmIdsK8TgkKXxgJDKE).

This is network art — created, iterated, and approved by the 6529 community, not by any single artist or curator. Anyone can submit. Anyone can vote. The network decides what makes the collection.

## Repository Structure

```
thinking-spinners/
├── generator/          # The Thinking Spinner Generator (HTML app)
│   ├── index.html      # Single-file app, runs in any browser
│   └── package.yaml    # Package metadata
├── presets/            # JSON presets for the CLI
├── generate.py         # CLI wrapper for headless rendering
├── players/            # Approved spinner players (HTML/CSS/JS)
│   └── README.md       # How to add a player
├── CONTRIBUTING.md     # How to submit spinners and code improvements
├── LICENSE             # MIT
└── README.md           # This file
```

## Components

### Generator

A single-file, zero-dependency HTML app for creating animated thinking-spinner GIFs in the browser. No server, no build step, no dependencies. Just open `generator/index.html` and go.

- Thoughts as text, icons, or images on a wheel (6–16 thoughts)
- 5 bar shapes, full animation control, color & background options
- Built-in GIF encoder (no external libraries)
- 4 built-in presets: Default Thinking, Collector Brain, Decision Loop, Overthinking
- Save/load presets as JSON
- PNG export for single frames

### CLI (for agents and automation)

A Python CLI wrapper that renders spinner GIFs from preset JSON — no browser interaction needed. Uses Playwright to drive the same generator HTML headlessly.

```bash
# List available presets
python3 generate.py --list-presets

# Render from a preset file
python3 generate.py --preset my-spinner.json -o output.gif

# Render a built-in preset
python3 generate.py --preset overthinking -o output.gif

# Override FPS and size
python3 generate.py --preset my-spinner.json -o output.gif --fps 25 --width 500
```

**Requirements:** `pip install playwright && python -m playwright install chromium`

The CLI does not modify the generator HTML — humans use it in the browser exactly as before. Custom presets go in the `presets/` directory as JSON files.

### Players

Each approved spinner lives here as an HTML file — not just a GIF, but living, remixable code. Anyone can fork, tweak, and submit improvements. Improvements go through the same community voting process as new spinners.

## How It Works

1. **Create** — Use the generator or write your own HTML/CSS/JS
2. **Submit** — Post your spinner to the [Thinking Spinner Wave](https://6529.io/waves/2e156526-042d-4b6c-9691-17c0cdd0bb9d) on 6529.io with a title, description, and your animated GIF
3. **Review** — @TheManager reviews code submissions and posts technical feedback
4. **Vote** — The community votes with TDH. 30,000,000 TDH needed for approval
5. **Approve** — When approved, the spinner is added to this repo, uploaded to GIPHY, minted into The Memes, and added to the gallery

## Submitting Code Improvements

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full process.

**Short version:** Fork this repo, make your change, post a link to your fork on the wave with a description of what changed. The community votes. If approved, it gets merged.

## Links

- **Generator (GitHub):** https://github.com/RegularDad6529/thinking-spinners/tree/main/generator
- **Generator (Arweave):** https://arweave.net/Oer1N3b86TrNaFlCLWasr8NZUdTGTdlq4U_7iwV97b0
- **Gallery:** https://arweave.net/DxbJyl-6xdtLtAuaJ0UQun3o3MmIdsK8TgkKXxgJDKE
- **GIPHY:** https://giphy.com/RegularDad/thinking-spinners
- **Wave:** https://6529.io/waves/2e156526-042d-4b6c-9691-17c0cdd0bb9d

## License

MIT for the generator and tooling. Approved spinner artwork is CC0 (public domain dedication).