#!/usr/bin/env python3
from PIL import Image
import numpy as np
import os

# Open the chart image
img = Image.open('chart.jpg')
width, height = img.size
print(f"Image dimensions: {width}x{height}")

# Convert to numpy array
img_array = np.array(img)

# Sample background color from edges
edge_samples = []
edge_samples.append(img_array[20, width//2])  # top middle
edge_samples.append(img_array[height-20, width//2])  # bottom middle
edge_samples.append(img_array[height//2, 20])  # left middle
edge_samples.append(img_array[height//2, width-20])  # right middle

bg_color = np.median(edge_samples, axis=0).astype(int)
print(f"Detected background color (RGB): {bg_color}")

# Create mask - more sensitive to catch rounded edges
def is_block_color(pixel, bg, tolerance=60):
    """Lower tolerance to catch more edge pixels including rounded corners"""
    diff = np.abs(pixel.astype(int) - bg.astype(int))
    return np.sum(diff) > tolerance

print("Creating mask...")
mask = np.zeros((height, width), dtype=np.uint8)
for y in range(height):
    for x in range(width):
        if is_block_color(img_array[y, x], bg_color):
            mask[y, x] = 255

# Find blocks using projection method
print("Finding blocks...")

# Lower threshold to catch more edge content
row_sums = np.sum(mask, axis=1)
rows_with_content = row_sums > width * 5  # More sensitive

# Find groups of rows
block_rows = []
in_block = False
start_row = 0

for i, has_content in enumerate(rows_with_content):
    if has_content and not in_block:
        start_row = i
        in_block = True
    elif not has_content and in_block:
        block_rows.append((start_row, i-1))
        in_block = False

if in_block:
    block_rows.append((start_row, len(rows_with_content)-1))

# For each row, find individual blocks
all_blocks = []
for start_y, end_y in block_rows:
    row_mask = mask[start_y:end_y+1, :]
    col_sums = np.sum(row_mask, axis=0)
    cols_with_content = col_sums > (end_y - start_y) * 5  # More sensitive

    in_block = False
    start_col = 0

    for i, has_content in enumerate(cols_with_content):
        if has_content and not in_block:
            start_col = i
            in_block = True
        elif not has_content and in_block:
            block = (start_col, start_y, i-1, end_y)
            block_width = i - start_col
            block_height = end_y - start_y + 1
            if block_width > 200 and block_height > 200:
                all_blocks.append(block)
            in_block = False

    if in_block:
        block = (start_col, start_y, len(cols_with_content)-1, end_y)
        block_width = len(cols_with_content) - start_col
        block_height = end_y - start_y + 1
        if block_width > 200 and block_height > 200:
            all_blocks.append(block)

print(f"Found {len(all_blocks)} blocks")

# Define the melachot in order (left to right, top to bottom)
melachot_order = [
    # Row 1 (8 blocks)
    "Choresh", "Zoreah", "Kotzair", "Ma'amir", "Dush", "Zoreh", "Ma'avir", "Mechabeh",
    # Row 2 (7 blocks)
    "Borer", "Tochain", "Miraked", "Lush", "Ofeh", "Kotaiv", "Mechait",
    # Row 3 (8 blocks)
    "Goez", "Melabain", "Menafetz", "Tzovayah", "Toveh", "Maisach", "Oseh Bei Batel Neirin", "Boneh",
    # Row 4 (8 blocks)
    "Oraig", "Potzi'ah", "Koshair", "Matir", "Memacheik", "Tofair", "Ko'reah", "Soiser",
    # Row 5 (8 blocks)
    "Tzud", "Shochet", "Mafshit", "Ma'aboid", "Mechateich", "Meshartois", "Hatza'ah", "Makeh b'Potash",
]

# Create images directory
os.makedirs('images', exist_ok=True)

# Extract all blocks
for i, (x1, y1, x2, y2) in enumerate(all_blocks):
    if i >= len(melachot_order):
        print(f"Warning: More blocks than expected melachot names")
        break

    name = melachot_order[i]

    # Crop with a generous margin to ensure we get the full block including rounded corners
    # Rounded corners need extra space beyond the detected rectangular bounds
    margin = 20
    x1_crop = max(0, x1 - margin)
    y1_crop = max(0, y1 - margin)
    x2_crop = min(width, x2 + margin)
    y2_crop = min(height, y2 + margin)

    block = img.crop((x1_crop, y1_crop, x2_crop, y2_crop))

    # Create filename
    filename = name.lower().replace("'", "").replace(" ", "_")
    output_path = f'images/{filename}.png'

    # Save
    block.save(output_path)
    print(f"{i+1}. Extracted '{name}' -> {output_path}")

print(f"\n✓ Successfully extracted {len(all_blocks)} melacha blocks!")
