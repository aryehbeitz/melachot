#!/usr/bin/env python3
from PIL import Image
import numpy as np

# Open the chart image
img = Image.open('chart.jpg')
width, height = img.size
print(f"Image dimensions: {width}x{height}")

# Convert to numpy array
img_array = np.array(img)

# The background is the navy blue color
# Let's sample it from various edges
# Sample from top middle, bottom middle, left middle, right middle edges
edge_samples = []
edge_samples.append(img_array[20, width//2])  # top middle
edge_samples.append(img_array[height-20, width//2])  # bottom middle
edge_samples.append(img_array[height//2, 20])  # left middle
edge_samples.append(img_array[height//2, width-20])  # right middle

bg_color = np.median(edge_samples, axis=0).astype(int)
print(f"Detected background color (RGB): {bg_color}")

# Create a more accurate mask by checking which pixels are NOT the navy blue
def is_block_color(pixel, bg, tolerance=50):
    """Check if a pixel is significantly different from background"""
    diff = np.abs(pixel.astype(int) - bg.astype(int))
    return np.sum(diff) > tolerance

# Create binary mask
print("Creating mask...")
mask = np.zeros((height, width), dtype=np.uint8)
for y in range(height):
    if y % 100 == 0:
        print(f"Processing row {y}/{height}")
    for x in range(width):
        if is_block_color(img_array[y, x], bg_color, tolerance=80):
            mask[y, x] = 255

# Save mask for debugging
mask_img = Image.fromarray(mask)
mask_img.save('mask_debug.png')
print("Saved mask to mask_debug.png")

# Use a row-column projection method to find blocks
print("\nFinding blocks using projection method...")

# Find rows that have content
row_sums = np.sum(mask, axis=1)
rows_with_content = row_sums > width * 10  # Rows with significant content

# Find groups of rows (these are the block rows)
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

print(f"Found {len(block_rows)} rows of blocks")

# For each row, find the individual blocks
all_blocks = []
for row_idx, (start_y, end_y) in enumerate(block_rows):
    print(f"\nRow {row_idx + 1}: y={start_y} to {end_y}")

    # Get column sums for this row
    row_mask = mask[start_y:end_y+1, :]
    col_sums = np.sum(row_mask, axis=0)
    cols_with_content = col_sums > (end_y - start_y) * 10

    # Find groups of columns (these are individual blocks in this row)
    in_block = False
    start_col = 0

    for i, has_content in enumerate(cols_with_content):
        if has_content and not in_block:
            start_col = i
            in_block = True
        elif not has_content and in_block:
            # Found a block
            block = (start_col, start_y, i-1, end_y)
            block_width = i - start_col
            block_height = end_y - start_y + 1

            # Only add if it's a reasonable block size
            if block_width > 200 and block_height > 200:
                all_blocks.append(block)
                print(f"  Block: x={start_col}-{i-1} ({block_width}px) y={start_y}-{end_y} ({block_height}px)")
            in_block = False

    if in_block:
        # Last block in row
        block = (start_col, start_y, len(cols_with_content)-1, end_y)
        block_width = len(cols_with_content) - start_col
        block_height = end_y - start_y + 1
        if block_width > 200 and block_height > 200:
            all_blocks.append(block)
            print(f"  Block: x={start_col}-{len(cols_with_content)-1} ({block_width}px) y={start_y}-{end_y} ({block_height}px)")

print(f"\n\nTotal blocks found: {len(all_blocks)}")
print("\nBlock positions:")
for i, (x1, y1, x2, y2) in enumerate(all_blocks):
    print(f"{i+1}. x={x1}-{x2} ({x2-x1+1}px) y={y1}-{y2} ({y2-y1+1}px)")
