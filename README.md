# Shields.io+

A Python utility for generating customized [Shields.io](https://shields.io/) badges as well as a static API for additional icons not included in [Simple Icons](https://simpleicons.org/).

## Overview

This utility simplifies the creation and customization of badges in the style of Shields.io that can be used in your README files, documentation, websites, and wherever else you'd like. It:

1. Converts SVG icons to base64 for use in Shields.io badges
2. Supports both named colors and hex color codes
3. Downloads generated badges for local use
4. Supports concurrent downloads for efficiency

## Usage

### Basic Usage

#### Static API
To use this repository as a static API, all you need to do is pass the `slug` you want to the URL: `https://raw.githubusercontent.com/gtkacz/shieldsio-plus/refs/heads/main/assets/shields/{style}/{slug}.svg`. To add more icons to the static API, see [below](#filename-convention).

#### Available Slugs

| Slug | Sample |
| --- | --- |
| azure | ![azure](./assets/shields/flat/azure.svg) |
| azure-white | ![azure-white](./assets/shields/flat/azure-white.svg) |
| confluent | ![confluent](./assets/shields/flat/confluent.svg) |
| confluent-white | ![confluent-white](./assets/shields/flat/confluent-white.svg) |
| dot-net-core | ![dot-net-core](./assets/shields/flat/dot-net-core.svg) |
| dot-net-core-white | ![dot-net-core-white](./assets/shields/flat/dot-net-core-white.svg) |
| gitcode | ![gitcode](./assets/shields/flat/gitcode.svg) |
| gitcode-black | ![gitcode-black](./assets/shields/flat/gitcode-black.svg) |
| gitcode-white | ![gitcode-white](./assets/shields/flat/gitcode-white.svg) |
| gogs | ![gogs](./assets/shields/flat/gogs.svg) |
| gogs-white | ![gogs-white](./assets/shields/flat/gogs-white.svg) |
| hacktoberfest | ![hacktoberfest](./assets/shields/flat/hacktoberfest.svg) |
| hacktoberfest-black | ![hacktoberfest-black](./assets/shields/flat/hacktoberfest-black.svg) |
| hacktoberfest-white | ![hacktoberfest-white](./assets/shields/flat/hacktoberfest-white.svg) |
| ibm | ![ibm](./assets/shields/flat/ibm.svg) |
| ibm-cloud | ![ibm-cloud](./assets/shields/flat/ibm-cloud.svg) |
| ibm-cloud-white | ![ibm-cloud-white](./assets/shields/flat/ibm-cloud-white.svg) |
| ibm-white | ![ibm-white](./assets/shields/flat/ibm-white.svg) |
| ieee | ![ieee](./assets/shields/flat/ieee.svg) |
| ieee-white | ![ieee-white](./assets/shields/flat/ieee-white.svg) |
| linkedin | ![linkedin](./assets/shields/flat/linkedin.svg) |
| linkedin-blue | ![linkedin-blue](./assets/shields/flat/linkedin-blue.svg) |
| linkedin-white | ![linkedin-white](./assets/shields/flat/linkedin-white.svg) |
| linkedin-white-logo | ![linkedin-white-logo](./assets/shields/flat/linkedin-white-logo.svg) |
| magento | ![magento](./assets/shields/flat/magento.svg) |
| magento-grey | ![magento-grey](./assets/shields/flat/magento-grey.svg) |
| magento-white | ![magento-white](./assets/shields/flat/magento-white.svg) |
| microsoft | ![microsoft](./assets/shields/flat/microsoft.svg) |
| microsoft-white | ![microsoft-white](./assets/shields/flat/microsoft-white.svg) |
| oracle | ![oracle](./assets/shields/flat/oracle.svg) |
| oracle-cloud | ![oracle-cloud](./assets/shields/flat/oracle-cloud.svg) |
| oracle-cloud-white | ![oracle-cloud-white](./assets/shields/flat/oracle-cloud-white.svg) |
| oracle-white | ![oracle-white](./assets/shields/flat/oracle-white.svg) |
| orcid | ![orcid](./assets/shields/flat/orcid.svg) |
| orcid-grey-logo | ![orcid-grey-logo](./assets/shields/flat/orcid-grey-logo.svg) |
| orcid-logo | ![orcid-logo](./assets/shields/flat/orcid-logo.svg) |
| orcid-white | ![orcid-white](./assets/shields/flat/orcid-white.svg) |
| orcid-white-logo | ![orcid-white-logo](./assets/shields/flat/orcid-white-logo.svg) |
| phacility | ![phacility](./assets/shields/flat/phacility.svg) |
| play-framework | ![play-framework](./assets/shields/flat/play-framework.svg) |
| plnkr | ![plnkr](./assets/shields/flat/plnkr.svg) |
| plnkr-white | ![plnkr-white](./assets/shields/flat/plnkr-white.svg) |
| sbc | ![sbc](./assets/shields/flat/sbc.svg) |
| sbc-blue | ![sbc-blue](./assets/shields/flat/sbc-blue.svg) |
| sourcegraph | ![sourcegraph](./assets/shields/flat/sourcegraph.svg) |
| sourcegraph-black | ![sourcegraph-black](./assets/shields/flat/sourcegraph-black.svg) |
| sourcegraph-white | ![sourcegraph-white](./assets/shields/flat/sourcegraph-white.svg) |
| sql-developer | ![sql-developer](./assets/shields/flat/sql-developer.svg) |
| sql-developer-white | ![sql-developer-white](./assets/shields/flat/sql-developer-white.svg) |
| twitter | ![twitter](./assets/shields/flat/twitter.svg) |
| twitter-white | ![twitter-white](./assets/shields/flat/twitter-white.svg) |
| visual-studio | ![visual-studio](./assets/shields/flat/visual-studio.svg) |
| visual-studio-white | ![visual-studio-white](./assets/shields/flat/visual-studio-white.svg) |
| vs-code | ![vs-code](./assets/shields/flat/vs-code.svg) |
| vs-code-black | ![vs-code-black](./assets/shields/flat/vs-code-black.svg) |
| vs-code-dark | ![vs-code-dark](./assets/shields/flat/vs-code-dark.svg) |
| vs-code-white | ![vs-code-white](./assets/shields/flat/vs-code-white.svg) |
| windows-10 | ![windows-10](./assets/shields/flat/windows-10.svg) |
| windows-10-blue | ![windows-10-blue](./assets/shields/flat/windows-10-blue.svg) |
| windows-7 | ![windows-7](./assets/shields/flat/windows-7.svg) |
| windows-7-white | ![windows-7-white](./assets/shields/flat/windows-7-white.svg) |
| zeplin | ![zeplin](./assets/shields/flat/zeplin.svg) |
| zeplin-white | ![zeplin-white](./assets/shields/flat/zeplin-white.svg) |

#### Available Styles

| Style | Sample |
| --- | --- |
| flat | ![windows-10-blue](./assets/shields/flat/windows-10-blue.svg) |
| true_flat* | ![windows-10-blue](./assets/shields/true_flat/windows-10-blue.svg) |
| flat_square | ![windows-10-blue](./assets/shields/flat_square/windows-10-blue.svg) |
| plastic | ![windows-10-blue](./assets/shields/plastic/windows-10-blue.svg) |
| for_the_badge | ![windows-10-blue](./assets/shields/for_the_badge/windows-10-blue.svg) |
| social | ![windows-10](./assets/shields/social/windows-10.svg) |

#### Available Fonts

| Family Name | Type | Sample |
| --- | --- | --- |
| Andale Mono | Monospace | ![windows-10-blue](./assets/shields/true_flat/andale_mono/windows-10-blue.svg) |
| Arial | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/arial/windows-10-blue.svg) |
| Arial Black | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/arial_black/windows-10-blue.svg) |
| Arial Narrow | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/arial_narrow/windows-10-blue.svg) |
| Arial Rounded Mt Bold | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/arial_rounded_mt_bold/windows-10-blue.svg) |
| Avant Garde | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/avant_garde/windows-10-blue.svg) |
| Baskerville | Serif | ![windows-10-blue](./assets/shields/true_flat/baskerville/windows-10-blue.svg) |
| Big Caslon | Serif | ![windows-10-blue](./assets/shields/true_flat/big_caslon/windows-10-blue.svg) |
| Bodoni Mt | Serif | ![windows-10-blue](./assets/shields/true_flat/bodoni_mt/windows-10-blue.svg) |
| Book Antiqua | Serif | ![windows-10-blue](./assets/shields/true_flat/book_antiqua/windows-10-blue.svg) |
| Brush Script Mt | Cursive | ![windows-10-blue](./assets/shields/true_flat/brush_script_mt/windows-10-blue.svg) |
| Calibri | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/calibri/windows-10-blue.svg) |
| Calisto Mt | Serif | ![windows-10-blue](./assets/shields/true_flat/calisto_mt/windows-10-blue.svg) |
| Cambria | Serif | ![windows-10-blue](./assets/shields/true_flat/cambria/windows-10-blue.svg) |
| Candara | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/candara/windows-10-blue.svg) |
| Century Gothic | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/century_gothic/windows-10-blue.svg) |
| Consolas | Monospace | ![windows-10-blue](./assets/shields/true_flat/consolas/windows-10-blue.svg) |
| Copperplate | Fantasy | ![windows-10-blue](./assets/shields/true_flat/copperplate/windows-10-blue.svg) |
| Courier New | Monospace | ![windows-10-blue](./assets/shields/true_flat/courier_new/windows-10-blue.svg) |
| Didot | Serif | ![windows-10-blue](./assets/shields/true_flat/didot/windows-10-blue.svg) |
| Franklin Gothic Medium | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/franklin_gothic_medium/windows-10-blue.svg) |
| Futura | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/futura/windows-10-blue.svg) |
| Garamond | Serif | ![windows-10-blue](./assets/shields/true_flat/garamond/windows-10-blue.svg) |
| Geneva | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/geneva/windows-10-blue.svg) |
| Georgia | Serif | ![windows-10-blue](./assets/shields/true_flat/georgia/windows-10-blue.svg) |
| Gill Sans | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/gill_sans/windows-10-blue.svg) |
| Goudy Old Style | Serif | ![windows-10-blue](./assets/shields/true_flat/goudy_old_style/windows-10-blue.svg) |
| Helvetica Neue | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/helvetica_neue/windows-10-blue.svg) |
| Hoefler Text | Serif | ![windows-10-blue](./assets/shields/true_flat/hoefler_text/windows-10-blue.svg) |
| Impact | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/impact/windows-10-blue.svg) |
| Lucida Bright | Serif | ![windows-10-blue](./assets/shields/true_flat/lucida_bright/windows-10-blue.svg) |
| Lucida Console | Monospace | ![windows-10-blue](./assets/shields/true_flat/lucida_console/windows-10-blue.svg) |
| Lucida Grande | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/lucida_grande/windows-10-blue.svg) |
| Lucida Sans Typewriter | Monospace | ![windows-10-blue](./assets/shields/true_flat/lucida_sans_typewriter/windows-10-blue.svg) |
| Optima | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/optima/windows-10-blue.svg) |
| Palatino | Serif | ![windows-10-blue](./assets/shields/true_flat/palatino/windows-10-blue.svg) |
| Papyrus | Fantasy | ![windows-10-blue](./assets/shields/true_flat/papyrus/windows-10-blue.svg) |
| Perpetua | Serif | ![windows-10-blue](./assets/shields/true_flat/perpetua/windows-10-blue.svg) |
| Rockwell | Serif | ![windows-10-blue](./assets/shields/true_flat/rockwell/windows-10-blue.svg) |
| Rockwell Extra Bold | Monospace | ![windows-10-blue](./assets/shields/true_flat/rockwell_extra_bold/windows-10-blue.svg) |
| Segoe Ui | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/segoe_ui/windows-10-blue.svg) |
| Tahoma | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/tahoma/windows-10-blue.svg) |
| Timesnewroman | Serif | ![windows-10-blue](./assets/shields/true_flat/timesnewroman/windows-10-blue.svg) |
| Trebuchet Ms | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/trebuchet_ms/windows-10-blue.svg) |
| Verdana | Sans-Serif | ![windows-10-blue](./assets/shields/true_flat/verdana/windows-10-blue.svg) |
| Monaco | Monospace | ![windows-10-blue](./assets/shields/true_flat/monaco/windows-10-blue.svg) |

## Expanding

To create a new badge in the static API, simply create a pull request to add your desired icon as an svg to the [icons](./assets/icons/) folder. And we'll do the rest for you!

### Filename Convention

SVG files should follow the naming convention: `slug_DisplayText_HexColor.svg`

Examples:
- `linkedin_LinkedIn_007EBB.svg` - Creates a LinkedIn badge with background color #007EBB and save it under the `linkedin` slug.
- `orcid-white_ORCID_FFF.svg` - Creates an ORCID badge with white background (#FFF) and save it under the `orcid-white` slug.

## License

[MIT License](LICENSE)
