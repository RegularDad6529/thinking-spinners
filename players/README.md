# Approved Thinking Spinner Players

Each approved spinner lives here as a single HTML file — living, remixable code, not just a frozen GIF.

## Adding a Player

When a spinner is approved by the community (30M TDH on the wave), @TheManager adds it here:

1. Create a new HTML file: `{spinner-name}.html` (lowercase, hyphenated)
2. The file must be single-file, zero-dependency, works offline
3. Include the spinner title, artist handle, and a link to the 6529.io drop in an HTML comment at the top
4. The GIF export is still used for minting and GIPHY — the HTML is the source of truth

## Player Format

```html
<!--
  Title: Self Doubt
  Artist: @RegularDad
  Wave Drop: https://6529.io/waves/2e156526-042d-4b6c-9691-17c0cdd0bb9d?serialNo=XXXXX
  Approved: 2026-08-01
  License: CC0
-->
<!DOCTYPE html>
<html>
  <!-- Spinner code here -->
</html>
```

## Remixing

Anyone can fork this repo, modify a player, and submit the improvement to the wave for community voting. See [../CONTRIBUTING.md](../CONTRIBUTING.md) for the full process.