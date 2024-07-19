import os
import imageio

def create_gif(image_folder, output_gif, duration=0.5):
    images = []
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            file_path = os.path.join(image_folder, filename)
            images.append(imageio.imread(file_path))
    
    imageio.mimsave(output_gif, images, duration=duration)

if __name__ == "__main__":

    image_folder = "images_folder" # Location of Image Folder
    output_gif = "output.gif" # Location Of Output Folder
    duration = 0.5 # Duration
