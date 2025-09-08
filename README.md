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
| lattes | ![lattes](./assets/shields/flat/lattes.svg) |
| lattes-white | ![lattes-white](./assets/shields/flat/lattes-white.svg) |
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
| flat | ![twitter](./assets/shields/flat/twitter.svg) |
| true_flat* | ![twitter](./assets/shields/true_flat/twitter.svg) |
| flat_square | ![twitter](./assets/shields/flat_square/twitter.svg) |
| plastic | ![twitter](./assets/shields/plastic/twitter.svg) |
| for_the_badge | ![twitter](./assets/shields/for_the_badge/twitter.svg) |
| social | ![windows-10](./assets/shields/social/twitter-white.svg) |

#### Available Fonts

| Family Name | Type | Sample |
| --- | --- | --- |
| Andale Mono | Monospace | ![twitter](./assets/shields/flat/andale_mono/twitter.svg) |
| Arial | Sans-Serif | ![twitter](./assets/shields/flat/arial/twitter.svg) |
| Arial Black | Sans-Serif | ![twitter](./assets/shields/flat/arial_black/twitter.svg) |
| Arial Narrow | Sans-Serif | ![twitter](./assets/shields/flat/arial_narrow/twitter.svg) |
| Arial Rounded Mt Bold | Sans-Serif | ![twitter](./assets/shields/flat/arial_rounded_mt_bold/twitter.svg) |
| Avant Garde | Sans-Serif | ![twitter](./assets/shields/flat/avant_garde/twitter.svg) |
| Baskerville | Serif | ![twitter](./assets/shields/flat/baskerville/twitter.svg) |
| Big Caslon | Serif | ![twitter](./assets/shields/flat/big_caslon/twitter.svg) |
| Bodoni Mt | Serif | ![twitter](./assets/shields/flat/bodoni_mt/twitter.svg) |
| Book Antiqua | Serif | ![twitter](./assets/shields/flat/book_antiqua/twitter.svg) |
| Brush Script Mt | Cursive | ![twitter](./assets/shields/flat/brush_script_mt/twitter.svg) |
| Calibri | Sans-Serif | ![twitter](./assets/shields/flat/calibri/twitter.svg) |
| Calisto Mt | Serif | ![twitter](./assets/shields/flat/calisto_mt/twitter.svg) |
| Cambria | Serif | ![twitter](./assets/shields/flat/cambria/twitter.svg) |
| Candara | Sans-Serif | ![twitter](./assets/shields/flat/candara/twitter.svg) |
| Century Gothic | Sans-Serif | ![twitter](./assets/shields/flat/century_gothic/twitter.svg) |
| Consolas | Monospace | ![twitter](./assets/shields/flat/consolas/twitter.svg) |
| Copperplate | Fantasy | ![twitter](./assets/shields/flat/copperplate/twitter.svg) |
| Courier New | Monospace | ![twitter](./assets/shields/flat/courier_new/twitter.svg) |
| Didot | Serif | ![twitter](./assets/shields/flat/didot/twitter.svg) |
| Franklin Gothic Medium | Sans-Serif | ![twitter](./assets/shields/flat/franklin_gothic_medium/twitter.svg) |
| Futura | Sans-Serif | ![twitter](./assets/shields/flat/futura/twitter.svg) |
| Garamond | Serif | ![twitter](./assets/shields/flat/garamond/twitter.svg) |
| Geneva | Sans-Serif | ![twitter](./assets/shields/flat/geneva/twitter.svg) |
| Georgia | Serif | ![twitter](./assets/shields/flat/georgia/twitter.svg) |
| Gill Sans | Sans-Serif | ![twitter](./assets/shields/flat/gill_sans/twitter.svg) |
| Goudy Old Style | Serif | ![twitter](./assets/shields/flat/goudy_old_style/twitter.svg) |
| Helvetica Neue | Sans-Serif | ![twitter](./assets/shields/flat/helvetica_neue/twitter.svg) |
| Hoefler Text | Serif | ![twitter](./assets/shields/flat/hoefler_text/twitter.svg) |
| Impact | Sans-Serif | ![twitter](./assets/shields/flat/impact/twitter.svg) |
| Lucida Bright | Serif | ![twitter](./assets/shields/flat/lucida_bright/twitter.svg) |
| Lucida Console | Monospace | ![twitter](./assets/shields/flat/lucida_console/twitter.svg) |
| Lucida Grande | Sans-Serif | ![twitter](./assets/shields/flat/lucida_grande/twitter.svg) |
| Lucida Sans Typewriter | Monospace | ![twitter](./assets/shields/flat/lucida_sans_typewriter/twitter.svg) |
| Optima | Sans-Serif | ![twitter](./assets/shields/flat/optima/twitter.svg) |
| Palatino | Serif | ![twitter](./assets/shields/flat/palatino/twitter.svg) |
| Papyrus | Fantasy | ![twitter](./assets/shields/flat/papyrus/twitter.svg) |
| Perpetua | Serif | ![twitter](./assets/shields/flat/perpetua/twitter.svg) |
| Rockwell | Serif | ![twitter](./assets/shields/flat/rockwell/twitter.svg) |
| Rockwell Extra Bold | Monospace | ![twitter](./assets/shields/flat/rockwell_extra_bold/twitter.svg) |
| Segoe Ui | Sans-Serif | ![twitter](./assets/shields/flat/segoe_ui/twitter.svg) |
| Tahoma | Sans-Serif | ![twitter](./assets/shields/flat/tahoma/twitter.svg) |
| Timesnewroman | Serif | ![twitter](./assets/shields/flat/timesnewroman/twitter.svg) |
| Trebuchet Ms | Sans-Serif | ![twitter](./assets/shields/flat/trebuchet_ms/twitter.svg) |
| Verdana | Sans-Serif | ![twitter](./assets/shields/flat/verdana/twitter.svg) |
| Monaco | Monospace | ![twitter](./assets/shields/flat/monaco/twitter.svg) |
##### Web-safe Fonts

| Family Name | Type | Sample |
| --- | --- | --- |
| Andale Mono | Monospace | ![twitter](./assets/shields/flat/andale_mono/twitter.svg) |
| Arial | Sans-Serif | ![twitter](./assets/shields/flat/arial/twitter.svg) |
| Arial Black | Sans-Serif | ![twitter](./assets/shields/flat/arial_black/twitter.svg) |
| Arial Narrow | Sans-Serif | ![twitter](./assets/shields/flat/arial_narrow/twitter.svg) |
| Arial Rounded Mt Bold | Sans-Serif | ![twitter](./assets/shields/flat/arial_rounded_mt_bold/twitter.svg) |
| Avant Garde | Sans-Serif | ![twitter](./assets/shields/flat/avant_garde/twitter.svg) |
| Baskerville | Serif | ![twitter](./assets/shields/flat/baskerville/twitter.svg) |
| Big Caslon | Serif | ![twitter](./assets/shields/flat/big_caslon/twitter.svg) |
| Bodoni Mt | Serif | ![twitter](./assets/shields/flat/bodoni_mt/twitter.svg) |
| Book Antiqua | Serif | ![twitter](./assets/shields/flat/book_antiqua/twitter.svg) |
| Brush Script Mt | Cursive | ![twitter](./assets/shields/flat/brush_script_mt/twitter.svg) |
| Calibri | Sans-Serif | ![twitter](./assets/shields/flat/calibri/twitter.svg) |
| Calisto Mt | Serif | ![twitter](./assets/shields/flat/calisto_mt/twitter.svg) |
| Cambria | Serif | ![twitter](./assets/shields/flat/cambria/twitter.svg) |
| Candara | Sans-Serif | ![twitter](./assets/shields/flat/candara/twitter.svg) |
| Century Gothic | Sans-Serif | ![twitter](./assets/shields/flat/century_gothic/twitter.svg) |
| Consolas | Monospace | ![twitter](./assets/shields/flat/consolas/twitter.svg) |
| Copperplate | Fantasy | ![twitter](./assets/shields/flat/copperplate/twitter.svg) |
| Courier New | Monospace | ![twitter](./assets/shields/flat/courier_new/twitter.svg) |
| Didot | Serif | ![twitter](./assets/shields/flat/didot/twitter.svg) |
| Franklin Gothic Medium | Sans-Serif | ![twitter](./assets/shields/flat/franklin_gothic_medium/twitter.svg) |
| Futura | Sans-Serif | ![twitter](./assets/shields/flat/futura/twitter.svg) |
| Garamond | Serif | ![twitter](./assets/shields/flat/garamond/twitter.svg) |
| Geneva | Sans-Serif | ![twitter](./assets/shields/flat/geneva/twitter.svg) |
| Georgia | Serif | ![twitter](./assets/shields/flat/georgia/twitter.svg) |
| Gill Sans | Sans-Serif | ![twitter](./assets/shields/flat/gill_sans/twitter.svg) |
| Goudy Old Style | Serif | ![twitter](./assets/shields/flat/goudy_old_style/twitter.svg) |
| Helvetica Neue | Sans-Serif | ![twitter](./assets/shields/flat/helvetica_neue/twitter.svg) |
| Hoefler Text | Serif | ![twitter](./assets/shields/flat/hoefler_text/twitter.svg) |
| Impact | Sans-Serif | ![twitter](./assets/shields/flat/impact/twitter.svg) |
| Lucida Bright | Serif | ![twitter](./assets/shields/flat/lucida_bright/twitter.svg) |
| Lucida Console | Monospace | ![twitter](./assets/shields/flat/lucida_console/twitter.svg) |
| Lucida Grande | Sans-Serif | ![twitter](./assets/shields/flat/lucida_grande/twitter.svg) |
| Lucida Sans Typewriter | Monospace | ![twitter](./assets/shields/flat/lucida_sans_typewriter/twitter.svg) |
| Optima | Sans-Serif | ![twitter](./assets/shields/flat/optima/twitter.svg) |
| Palatino | Serif | ![twitter](./assets/shields/flat/palatino/twitter.svg) |
| Papyrus | Fantasy | ![twitter](./assets/shields/flat/papyrus/twitter.svg) |
| Perpetua | Serif | ![twitter](./assets/shields/flat/perpetua/twitter.svg) |
| Rockwell | Serif | ![twitter](./assets/shields/flat/rockwell/twitter.svg) |
| Rockwell Extra Bold | Monospace | ![twitter](./assets/shields/flat/rockwell_extra_bold/twitter.svg) |
| Segoe Ui | Sans-Serif | ![twitter](./assets/shields/flat/segoe_ui/twitter.svg) |
| Tahoma | Sans-Serif | ![twitter](./assets/shields/flat/tahoma/twitter.svg) |
| Timesnewroman | Serif | ![twitter](./assets/shields/flat/timesnewroman/twitter.svg) |
| Trebuchet Ms | Sans-Serif | ![twitter](./assets/shields/flat/trebuchet_ms/twitter.svg) |
| Verdana | Sans-Serif | ![twitter](./assets/shields/flat/verdana/twitter.svg) |
| Monaco | Monospace | ![twitter](./assets/shields/flat/monaco/twitter.svg) |

##### External Fonts
| Family Name | Type | Sample |
| --- | --- | --- |
| Tektur | Sans-Serif | ![twitter](./assets/shields/flat/google/twitter.svg) |

## Expanding

To create a new badge in the static API, simply create a pull request to add your desired icon as an svg to the [icons](./assets/icons/) folder. And we'll do the rest for you!

### Filename Convention

SVG files should follow the naming convention: `slug_DisplayText_HexColor.svg`

Examples:
- `linkedin_LinkedIn_007EBB.svg` - Creates a LinkedIn badge with background color #007EBB and save it under the `linkedin` slug.
- `orcid-white_ORCID_FFF.svg` - Creates an ORCID badge with white background (#FFF) and save it under the `orcid-white` slug.

## License

[MIT License](LICENSE)
