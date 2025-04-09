from PIL import Image, ImageEnhance
import os

# Handle backward compatibility for resampling filter
try:
    resample_filter = Image.Resampling.LANCZOS  # Pillow >=10
except AttributeError:
    resample_filter = Image.LANCZOS  # Pillow <10

def add_logo_watermark(main_image_folder, logo_path, output_folder):
    if not os.path.exists(main_image_folder):   
        print(f"Main image folder '{main_image_folder}' does not exist.")
        return
    if not os.path.exists(logo_path):
        print(f"Logo image '{logo_path}' does not exist.")
        return
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Output folder '{output_folder}' created.")
    
    main_images_list = os.listdir(main_image_folder)
    for main_image in main_images_list:
        main_image_path = os.path.join(main_image_folder, main_image)
        output_path = os.path.join(output_folder, f"watermarked_{main_image}")

        # Open the main image
        base_image = Image.open(main_image_path).convert("RGBA")
        base_width, base_height = base_image.size

        # Open and resize the logo
        logo = Image.open(logo_path).convert("RGBA")
        logo_ratio = 0.15  # 15% of the image width
        new_logo_width = int(base_width * logo_ratio)
        logo_aspect_ratio = logo.height / logo.width
        new_logo_height = int(new_logo_width * logo_aspect_ratio)
        logo_resized = logo.resize((new_logo_width, new_logo_height), resample=resample_filter)

        # Adjust opacity to 70%
        alpha = logo_resized.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(0.7)
        logo_resized.putalpha(alpha)

        # Position: Top-right with padding
        padding = int(base_width * 0.02)
        position = (base_width - new_logo_width - padding, padding)

        # Paste and save
        base_image.paste(logo_resized, position, logo_resized)
        base_image.convert("RGB").save(output_path, "PNG")
        print(f"Watermarked image saved as {output_path}")


if __name__ == "__main__":
    main_image_folder = "images"      # Folder with input images
    logo_path = "logo.png"            # Path to your logo image (must be PNG)
    output_folder = "output"          # Folder to save watermarked images

    add_logo_watermark(main_image_folder, logo_path, output_folder)
