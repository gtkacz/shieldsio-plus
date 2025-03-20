# Extra Shields.io Badges

A Python utility for generating customized [Shields.io](https://shields.io/) badges.

## Overview

This utility simplifies the creation and customization of badges that can be used in your README files, documentation, and websites. It:

1. Converts SVG icons to base64 for use in Shields.io badges
2. Supports both named colors and hex color codes
3. Handles multiple badge styles (flat, plastic, social, etc.)
4. Downloads generated badges for local use
5. Supports concurrent downloads for efficiency

## Installation

### Prerequisites

- Python 3.9+
- pip

### Setup

```bash
# Clone the repository
pip install shieldio-badges
```

## Usage

### Basic Usage


### Filename Convention

SVG files should follow the naming convention: `slug_DisplayText_HexColor.svg`

Examples:
- `linkedin_LinkedIn_007EBB.svg` - Creates a LinkedIn badge with background color #007EBB
- `orcid-white_ORCID_FFF.svg` - Creates an ORCID badge with white background (#FFF)

## Features

### Color Support

- Named colors (blue, red, green, etc.)
- Hex color codes (#FF5500, #007EBB)
- RGB/RGBA color values
- HSL/HSLA color values

### Badge Styles

All Shields.io styles are supported:

- `flat` (default)
- `flat-square`
- `plastic`
- `for-the-badge`
- `social`

## Development

### Setting up Development Environment

```bash
# Install development dependencies
pip install -r requirements.dev.txt

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# TODO: Add testing instructions
```

### Code Formatting

This project uses [Ruff](https://github.com/astral-sh/ruff) for code formatting and linting:

```bash
# Format code
ruff format

# Lint code
ruff check --fix
```

## License

[MIT License](LICENSE)