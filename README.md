# Thinking Spinner Generator

A single-file, zero-dependency HTML app for creating animated thinking-spinner GIFs and PNGs in the browser.

No server. No build step. No dependencies. Just open `index.html` and go.

## What It Does

You type in your thoughts, pick a visual style, and export an animated GIF of a spinner cycling through them. The active thought lights up, the rest fade back, and a trail shows recent thoughts winding down.

## Features

- **Thoughts as text, icons, or images** — arranged on a wheel, 6–16 thoughts
- **5 bar shapes** — rectangle, rounded, capsule, line, wedge
- **Full animation control** — speed, direction (CW/CCW), trail length, trail fade, glow, loop type (continuous, pause, hold, custom sequence)
- **Color & background** — solid color, image background, or transparent (transparent GIFs supported)
- **Built-in GIF encoder** — median-cut color quantization + LZW compression, entirely in-browser, no libraries
- **4 built-in presets** — Default Thinking, Collector Brain, Decision Loop, Overthinking
- **Save/load presets** — export your config as JSON, load it back later
- **Randomize style** — one-click palette + shape shuffle (thoughts untouched)
- **Basic and Advanced modes** — simple controls by default, full control when you need it
- **PNG export** — capture the current frame as a static image
- **Keyboard shortcut** — spacebar toggles playback
- **Reduced-motion aware** — respects `prefers-reduced-motion`, starts paused

## Presets

| Preset | Thoughts | Vibe |
|--------|----------|------|
| Default Thinking | Idea, Question, Maybe, No, Wait, What if?, Yes, Do it | Clean starter |
| Collector Brain | Artist, Provenance, Supply, Price, TDH, FOMO, Don't buy, Cool JPEG | NFT collector anxiety |
| Decision Loop | Notice, Weigh it, Ask a friend, Sleep on it, Second guess, Commit | Sequential decision process |
| Overthinking | That email, Was I rude?, Money, Should sleep, Old regret, Tomorrow, Was I rude?, Still awake, The email again, Was I rude?, Sleep, No | 3AM spiral, counterclockwise, fast |

## How to Use

1. Open `index.html` in any modern browser
2. Edit the thoughts — click a row and type
3. Customize bars, trail, colors, background, text as needed
4. Hit Export GIF (or Export PNG for a single frame)
5. The file downloads to your computer

## Saving & Sharing

- **Save preset** — downloads a `.preset.json` file with your full config
- **Load preset** — upload a saved preset file to restore your work
- **Copy JSON** — copies the config to your clipboard (Advanced mode)

## Technical Notes

- The GIF encoder is written from scratch (median-cut palette reduction + LZW compression) — no `gif.js`, no `pica`, no external libraries
- Frames are drawn on demand during encoding, not stored in memory — long animations at high resolution won't crash your browser
- Canvas-based rendering with auto-fit: the spinner scales to fill whatever output size you pick
- Works offline — save the HTML file anywhere, it runs without internet

## License

MIT