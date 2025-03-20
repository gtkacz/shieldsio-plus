# Extra Shields.io Badges

A Python utility for generating customized [Shields.io](https://shields.io/) badges.

## Overview

This utility simplifies the creation and customization of badges that can be used in your README files, documentation, and websites. It:

1. Converts SVG icons to base64 for use in Shields.io badges
2. Supports both named colors and hex color codes
3. Handles multiple badge styles (flat, plastic, social, etc.)
4. Downloads generated badges for local use
5. Supports concurrent downloads for efficiency

## Usage

### Basic Usage

#### Static API
To use this repository as a static API, all you need to do is pass the `slug` you want to the URL: `https://raw.githubusercontent.com/gtkacz/extra-shieldsio-badges/refs/heads/main/assets/shields/{slug}.svg`. To add more icons to the static API, see [below](#filename-convention).

#### Available Slugs
- linkedin
- linkedin-white
- orcid
- orcid-white

## Expanding

To create a new badge in the static API, simply create a pull request to add your desired icon as an svg to the [icons](./assets/icons/) folder. And we'll do the rest for you!

### Filename Convention

SVG files should follow the naming convention: `slug_DisplayText_HexColor.svg`

Examples:
- `linkedin_LinkedIn_007EBB.svg` - Creates a LinkedIn badge with background color #007EBB and save it under the `linkedin` slug.
- `orcid-white_ORCID_FFF.svg` - Creates an ORCID badge with white background (#FFF) and save it under the `orcid-white` slug.

## License

[MIT License](LICENSE)