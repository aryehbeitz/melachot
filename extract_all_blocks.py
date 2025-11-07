#!/usr/bin/env python3
from PIL import Image
import os

# Open the chart image
img = Image.open('chart.jpg')
width, height = img.size

print(f"Image dimensions: {width}x{height}")

# Margins and spacing
left_margin = 43
top_margin = 77
gap_x = 13
gap_y = 15

# Block dimensions
block_width = 415
block_height = 475

# Define all block positions in the grid layout
melachot_positions = [
    # Row 1
    ("Choresh", 0, 0), ("Zoreah", 1, 0), ("Kotzair", 2, 0), ("Ma'amir", 3, 0),
    ("Dush", 4, 0), ("Zoreh", 5, 0), ("Ma'avir", 7, 0), ("Mechabeh", 8, 0),
    # Row 2
    ("Borer", 0, 1), ("Tochain", 1, 1), ("Miraked", 2, 1), ("Lush", 3, 1),
    ("Ofeh", 4, 1), ("Kotaiv", 7, 1), ("Mechait", 8, 1),
    # Row 3
    ("Goez", 0, 2), ("Melabain", 1, 2), ("Menafetz", 2, 2), ("Tzovayah", 3, 2),
    ("Toveh", 4, 2), ("Maisach", 5, 2), ("Oseh Bei Batel Neirin", 6, 2), ("Boneh", 8, 2),
    # Row 4
    ("Oraig", 0, 3), ("Potzi'ah", 1, 3), ("Koshair", 2, 3), ("Matir", 3, 3),
    ("Memacheik", 4, 3), ("Tofair", 5, 3), ("Ko'reah", 6, 3), ("Soiser", 8, 3),
    # Row 5
    ("Tzud", 0, 4), ("Shochet", 1, 4), ("Mafshit", 2, 4), ("Ma'aboid", 3, 4),
    ("Mechateich", 4, 4), ("Meshartois", 5, 4), ("Hatza'ah", 6, 4), ("Makeh b'Potash", 7, 4),
]

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Extract all blocks
for name, col, row in melachot_positions:
    x1 = left_margin + col * (block_width + gap_x)
    y1 = top_margin + row * (block_height + gap_y)
    x2 = x1 + block_width
    y2 = y1 + block_height

    # Crop the block
    block = img.crop((x1, y1, x2, y2))

    # Create filename (safe version)
    filename = name.lower().replace("'", "").replace(" ", "_")
    output_path = f'images/{filename}.png'

    # Save it
    block.save(output_path)
    print(f"Extracted '{name}' -> {output_path}")

print(f"\nTotal blocks extracted: {len(melachot_positions)}")
