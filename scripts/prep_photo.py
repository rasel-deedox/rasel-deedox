import sys
import io
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep_photo(input_path="source-photo.jpg", output_path="source-prepped.png"):
    print(f"Prepping photo from {input_path}...")
    with open(input_path, "rb") as f:
        input_data = f.read()

    subject = remove(input_data)
    img = Image.open(io.BytesIO(subject)).convert("RGBA")

    white_bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    composite = Image.alpha_composite(white_bg, img).convert("L")

    arr = np.array(composite)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(arr)

    alpha = np.array(img.split()[-1])
    enhanced[alpha < 30] = 255

    Image.fromarray(enhanced).save(output_path)
    print(f"Saved prepped photo to {output_path}")

if __name__ == "__main__":
    photo = sys.argv[1] if len(sys.argv) > 1 else "source-photo.jpg"
    prep_photo(photo)

