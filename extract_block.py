#!/usr/bin/env python3
from PIL import Image

# Open the chart image
img = Image.open('chart.jpg')
width, height = img.size

print(f"Image dimensions: {width}x{height}")

# Calculate approximate block dimensions
# The grid appears to be roughly 9 columns by 5 rows with some gaps
# Let's estimate the starting position and block size

# Margins from edges
left_margin = 40
top_margin = 75
right_margin = 40
bottom_margin = 40

# Calculate usable space
usable_width = width - left_margin - right_margin
usable_height = height - top_margin - bottom_margin

# Grid layout: 9 columns max, 5 rows
columns = 9
rows = 5

# Gap between blocks
gap = 10

# Calculate block dimensions
block_width = (usable_width - (columns - 1) * gap) // columns
block_height = (usable_height - (rows - 1) * gap) // rows

print(f"Calculated block size: {block_width}x{block_height}")
print(f"Gap: {gap}px")

# Extract the first block (top-left, "Choresh - Ch")
x1 = left_margin
y1 = top_margin
x2 = x1 + block_width
y2 = y1 + block_height

print(f"Extracting first block from ({x1},{y1}) to ({x2},{y2})")

# Crop the first block
first_block = img.crop((x1, y1, x2, y2))

# Save it
output_path = 'images/choresh_test.png'
first_block.save(output_path)
print(f"Saved to {output_path}")
print(f"Block size: {first_block.size}")
