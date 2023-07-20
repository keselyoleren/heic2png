from PIL import Image
import pyheif
import os
import glob

def heic_to_png(heic_file, png_file):
    # Open the HEIC file using pyheif
    heif_file = pyheif.read(heic_file)

    # Extract metadata and pixel data from the HEIC file
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )

    # Save the image as PNG
    image.save(png_file)

# if __name__ == "__main__":
heic_folder = "/Users/admin/keselyoleren/neurabot/python/heic2png/dataset"
png_folder = "/Users/admin/keselyoleren/neurabot/python/heic2png/output"

# Create the output folder if it doesn't exist
if not os.path.exists(png_folder):
    os.makedirs(png_folder)

# Find all HEIC files in the folder
heic_files = glob.glob(os.path.join(heic_folder, "*.heic"))
print(heic_files)

for heic_file_path in heic_files:
    print(heic_files)
    # Get the filename without extension
    filename = os.path.splitext(os.path.basename(heic_file_path))[0]

    # Generate the corresponding PNG file path
    png_file_path = os.path.join(png_folder, f"{filename}.png")

    heic_to_png(heic_file_path, png_file_path)
