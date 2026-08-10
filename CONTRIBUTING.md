# Contributing to Thinking Spinners

There are two ways to contribute: submit a new spinner, or improve an existing one (generator or player).

All submissions go through community voting on the [Thinking Spinner Wave](https://6529.io/waves/2e156526-042d-4b6c-9691-17c0cdd0bb9d) on 6529.io. 30,000,000 TDH needed for approval.

## Submitting a New Spinner

1. Create your spinner — use the [generator](generator/index.html) or build your own
2. Export as animated GIF
3. Post to the wave with:
   - **Title** — name your spinner
   - **Description** — what mental state does it depict?
   - **Your GIF** — animated, not static
4. If your spinner is code-based (HTML/CSS/JS), also include:
   - A link to your fork/branch on GitHub, OR paste the code directly
   - A description of what changed vs the original
   - A demo link or screenshot if possible
5. All submissions must be CC0 (public domain dedication)

## Submitting a Code Improvement

Improvements to the generator or to an approved player follow the same voting process.

### Process

1. **Fork** this repository
2. **Make your change** — keep it focused, one improvement per submission
3. **Test locally** — open the HTML file in a browser and verify it works
4. **Post to the wave** with:
   - Link to your fork/branch
   - Description of what changed and why
   - Demo link or screenshot (if possible)
5. **TheManager review** — @TheManager will:
   - Pull your code and test it
   - Verify the animation works
   - Check for security issues (no XSS, no external data calls, no malicious code)
   - Confirm CC0 compatibility (no third-party copyrighted code)
   - Post a technical assessment as a reply on the wave
6. **Community votes** — the network decides with TDH
7. **If approved** — @TheManager merges your code into this repo and tags a new release

### What Counts as an Improvement

- New presets for the generator
- New animation modes or visual styles
- Performance improvements
- Accessibility improvements
- Bug fixes
- New players (remixes of existing spinners with modifications)

### Rules

- **CC0 only** — all submissions must be public domain. No third-party copyrighted code.
- **No external dependencies** — the generator and players must remain single-file, zero-dependency HTML. No CDN links, no npm packages, no external API calls.
- **No network calls** — players and the generator must work fully offline. No fetching data from external servers.
- **No tracking** — no analytics, no telemetry, no external data collection.
- **Keep it focused** — one improvement per submission so voters can understand what they're voting on.

### Code Review Criteria

@TheManager's technical assessment will cover:

- ✅ Does it work? (animation verified in a browser)
- ✅ What changed? (summary of the diff)
- ✅ Security check (no XSS, no exfiltration, no malicious code)
- ✅ CC0 compatible (no third-party copyrighted code)
- ✅ No external dependencies or network calls
- ⚠️ Any bugs or breaking changes noted

The assessment is informational — the community still makes the final call with their votes.

## Questions?

Ask on the [wave](https://6529.io/waves/2e156526-042d-4b6c-9691-17c0cdd0bb9d) or mention @TheManager.