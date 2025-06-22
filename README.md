# Color Frequency Analyzer

A command-line tool to analyze and visualize the most common colors in an image.

## Features

- Counts the frequency of each color in an image (supports common formats like PNG, JPG).
- Displays the top N most common colors.
- Optionally visualizes color frequencies as a bar chart.
- Simple command-line interface.

## Requirements

- Python 3.7+
- [Pillow](https://python-pillow.org/) (`pip install pillow`)
- [matplotlib](https://matplotlib.org/) (`pip install matplotlib`)

## Usage

```bash
python main.py path/to/image.png --top 10 --plot
```

- `path/to/image.png`: Path to your image file.
- `--top N`: Show the top N most common colors (default: 10).
- `--plot`: Show a bar chart of the top colors.

## Example

```bash
python main.py sample.jpg --top 5 --plot
```

Output:
```
Top 5 colors in sample.jpg:
 1. RGB(255, 255, 255): 10234 pixels
 2. RGB(0, 0, 0): 8342 pixels
 3. RGB(128, 128, 128): 2345 pixels
 4. RGB(255, 0, 0): 1234 pixels
 5. RGB(0, 255, 0): 987 pixels
```
A bar chart will also be displayed if `--plot` is used.

## Project Structure

```
color-frequency-analysis/
├── main.py
├── color