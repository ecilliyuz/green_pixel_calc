import os
from PIL import Image
import json

image_folder = "greenmasks"

output_file = "green_pixel_counts.json"

green_pixel_counts = {}

for filename in os.listdir(image_folder):
    if filename.endswith(".png"):
        filepath = os.path.join(image_folder, filename)

        image = Image.open(filepath).convert("RGB")

        pixels = image.load()

        width, height = image.size

        green_pixel_count = 0

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                if r < 100 and g > 150 and b < 100:
                    green_pixel_count += 1

        green_pixel_counts[filename] = green_pixel_count

with open(output_file, "w") as json_file:
    json.dump(green_pixel_counts, json_file, indent=4)

print(f"Yeşil piksel sayıları '{output_file}' dosyasına kaydedildi.")
