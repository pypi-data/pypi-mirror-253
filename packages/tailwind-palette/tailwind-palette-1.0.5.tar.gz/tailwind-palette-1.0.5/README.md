# Python Tailwind Palette

## Introduction

Tailwind Palette is a Python package designed for working with the Tailwind CSS color palette. This library facilitates easy access and manipulation of Tailwind CSS colors in Python. It's an extension of the [python-tailwind-colors](https://github.com/dostuffthatmatters/python-tailwind-colors) library, originally developed by dostuffthatmatters, enhanced to provide additional functionality and improved user experience.

[View the Tailwind CSS color palette here](https://tailwindcss.com/docs/customizing-colors)

## Installation

To install Tailwind Palette, run:

```bash
pip install tailwind-palette
```

## Usage

### Import Statement

Use the following import statement to access the TailwindPalette class.

```python
from tailwind_palette import TailwindPalette as tp
```

### Accessing Colors

You can access color shades directly or use the '.get()' method.

**Direct Access:**

```python
slate_100 = tp.SLATE.shade_100
print(f"Slate 100 Hex: {slate_100.hex}, RGB: {slate_100.rgb}")
```

**Using '.get()' Method:**

```python
pink_500 = tp.get("pink-500")
print(f"Pink 500 Hex: {pink_500.hex}, RGB: {pink_500.rgb}")
```

### Overriding Colors

You can override color shades using hex or RGB values.

**Using Hex Value:**

```python
tp.SLATE.override_shade('shade_100', value="#abcdef")
```

**Using RGB Value:**

```python
tp.SLATE.override_shade('shade_200', value=(12, 34, 56))
```

## Features

- Easy access to all Tailwind CSS color shades.
- Ability to override specific color shades.
- Hex and RGB color format support.

## Dependencies

Tailwind Palette requires the following dependencies:
- Python 3.x

## Troubleshooting

If you encounter any issues, please refer to the [GitHub Issues](https://github.com/noahyoungs/tailwind-palette/issues) page for common problems and solutions.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
