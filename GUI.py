import os
import cv2
import imageio
import customtkinter
from customtkinter import filedialog

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()

app.title("GIF MAKER")
app.geometry("430x400")

def gif_button():
  image_folder_path = image_folder_entry.get()
  output_gif_path = output_gif_entry.get() + '.gif'
  duration_val = int(duration_entry.get()) or 500

  # Get list of image files
  image_files = [os.path.join(image_folder_path, filename) for filename in os.listdir(image_folder_path)
                 if filename.endswith('.png') or filename.endswith('.jpg')]

  # Read and resize images using OpenCV
  images = [] 

  for image_file in image_files:
    image = cv2.imread(image_file)

    # Get the size of the first image (assuming all should be the same size)
    if not images:
      width, height = image.shape[:2]  # Get width and height from the first image

    # Resize all images to match the target size
    resized_image = cv2.resize(image, (height, width), interpolation=cv2.INTER_AREA)
    images.append(resized_image)

  imageio.mimsave(output_gif_path, images, duration=duration_val, format='GIF')

# Lable
label = customtkinter.CTkLabel(app, text="GIF MAKER", font=("Consolas", 30), compound="center")
label.grid(row=0, column=0, padx=20, pady=20)

# Select Image Folder
image_folder_entry = customtkinter.CTkEntry(app, width=300)
image_folder_entry.grid(row=1, column=0, padx=20, pady=20)

image_folder_entry.configure(placeholder_text="Image Folder")

browse_button = customtkinter.CTkButton(app, text="Browse", command=lambda: [image_folder_entry.insert(0, filedialog.askdirectory())], width=50)
browse_button.grid(row=1, column=1, padx=10)

# Select Output GIF
output_gif_entry = customtkinter.CTkEntry(app, width=300)
output_gif_entry.grid(row=2, column=0, padx=20, pady=20)

output_gif_entry.configure(placeholder_text="Output GIF")

# Duration
duration_entry = customtkinter.CTkEntry(app, width=300)
duration_entry.grid(row=3, column=0, padx=20, pady=20)

duration_entry.configure(placeholder_text="Duration Of GIF")

# GIF Button

button = customtkinter.CTkButton(app, text="Make GIF", command=gif_button, width=300)
button.grid(row=4, column=0, padx=20, pady=20)

def change_theme():
  if customtkinter.get_appearance_mode() == "Light":
    customtkinter.set_appearance_mode("dark")
  else:
    customtkinter.set_appearance_mode("light")

# Theme Change Btton
theme_button = customtkinter.CTkButton(app, text="Theme", command=change_theme, width=50)
theme_button.grid(row=4, column=1, padx=10)

app.mainloop()
