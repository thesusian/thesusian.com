import os
from PIL import Image, ExifTags

PATH = "./content/media"

for filename in os.listdir(PATH):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        file_path = os.path.join(PATH, filename)
        try:
            with Image.open(file_path) as image:
                exif_data = image._getexif() # type: ignore
                if exif_data is not None:
                    orientation_tag = next((tag for tag, value in ExifTags.TAGS.items() if value == 'Orientation'), None)
                    if orientation_tag in exif_data:
                        orientation = exif_data[orientation_tag] # type: ignore
                        if orientation == 3: image = image.rotate(180, expand=True)
                        elif orientation == 6: image = image.rotate(270, expand=True)
                        elif orientation == 8: image = image.rotate(90, expand=True)
                image.save(file_path, format='JPEG' if file_path.lower().endswith(('.jpg', '.jpeg')) else 'PNG', quality=95)
        except Exception as e: print(f"Error processing {filename}: {e}")
