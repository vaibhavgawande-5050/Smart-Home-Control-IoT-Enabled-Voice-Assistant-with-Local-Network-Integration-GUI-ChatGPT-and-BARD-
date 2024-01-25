from PIL import Image

def jpg_to_gif(input_file, output_file):
    # Open the JPG image
    with Image.open(input_file) as img:
        # Convert the image to GIF
        img.save(output_file, 'GIF')

# Example usage:
input_jpg_file = 'mic.jpg'
output_gif_file = 'mic.gif'

jpg_to_gif(input_jpg_file, output_gif_file)
