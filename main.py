import os
from PIL import Image
import json

# Resimlerin bulunduğu klasör
image_folder = "greenmasks"

# Sonuçların saklanacağı JSON dosyası
output_file = "green_pixel_counts.json"

# Yeşil piksel sayımlarını tutacak sözlük
green_pixel_counts = {}

# Klasördeki tüm dosyalar arasında döngü yap
for filename in os.listdir(image_folder):
    if filename.endswith(".png"):
        # Dosya yolunu oluştur
        filepath = os.path.join(image_folder, filename)

        # Resmi aç ve RGB moduna çevir
        image = Image.open(filepath).convert("RGB")

        # Piksel verilerini al
        pixels = image.load()

        # Resmin genişliği ve yüksekliği
        width, height = image.size

        # Yeşil piksel sayısını başlat
        green_pixel_count = 0

        # Her pikseli kontrol et
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                # Yeşil olarak sayılması için r ve b düşük, g yüksek olmalı
                if r < 100 and g > 150 and b < 100:
                    green_pixel_count += 1

        # Yeşil piksel sayısını sözlüğe ekle
        green_pixel_counts[filename] = green_pixel_count

# Sonuçları JSON dosyasına kaydet
with open(output_file, "w") as json_file:
    json.dump(green_pixel_counts, json_file, indent=4)

print(f"Yeşil piksel sayıları '{output_file}' dosyasına kaydedildi.")
