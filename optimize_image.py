from PIL import Image
import os

# Bild öffnen
img = Image.open('bilder/unnamed.jpg')

# Größe anpassen (für Web-Hintergrundbild)
img.thumbnail((2560, 1440), Image.Resampling.LANCZOS)

# Speichern mit Komprimierung
img.save('bilder/unnamed-optimized.jpg', 'JPEG', quality=85, optimize=True)

# Dateigröße anzeigen
original_size = os.path.getsize('bilder/unnamed.jpg') / 1024
optimized_size = os.path.getsize('bilder/unnamed-optimized.jpg') / 1024

print(f"Original: {original_size:.2f} KB")
print(f"Optimiert: {optimized_size:.2f} KB")
print(f"Ersparnis: {((original_size - optimized_size) / original_size * 100):.1f}%")
print("Bild erfolgreich optimiert!")

