import os
from PIL import Image
from tqdm import tqdm


def read_images_from_directory(directory):
    images = []
    for filename in tqdm(os.listdir(directory), desc="Reading images"):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(directory, filename)
            try:
                image = Image.open(image_path)
                images.append(image)
            except IOError:
                print(f"Error opening {image_path}")
    return images


def convert_to_pdf(images, output_pdf_path):
    if images:
        images_converted = [image.convert('RGB') for image in images]
        images_converted[0].save(output_pdf_path, save_all=True, append_images=images_converted[1:])
    

directory = './Data'
output_pdf_path = './result.pdf'
images = read_images_from_directory(directory)
convert_to_pdf(images, output_pdf_path)
