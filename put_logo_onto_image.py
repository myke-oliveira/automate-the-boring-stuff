import os
from PIL import Image

MAX_DIM = 1000

def main():

	directory_source = get_from_user('Directory of images: ', os.path.isdir)
	directory_destin = get_from_user('Directory of destiny: ', os.path.isdir)
	logo_path = get_from_user('Logo Path: ', os.path.isfile)

	logo_image = Image.open(logo_path)
	logo_width, logo_height = logo_image.size

	for filename in os.listdir(directory_source):
		if any(map(lambda extension: filename.endswith('extension'),
			('.jpg', '.jpeg', '.png', '.bmp', '.giff', '.JPG', '.JPEG', '.PNG', '.BMP', '.GIFF'))):
			image = Image.open(os.path.join(directory_source, filename))
			width, height = image.size
			if width > MAX_DIM or height > MAX_DIM:
				factor = MAX_DIM / max(width, height)
				width, height = int(width * factor), int(height * factor)
				image = image.resize((width, height))
			image.paste(logo_image, (width - logo_width, height - logo_height), logo_image)
			image.save(os.path.join(directory_destin, filename))


def get_from_user(prompt, validate):
	while True:
		entrace = input(prompt)
		if validate(entrace):
			return entrace


if __name__ == '__main__':
	main()