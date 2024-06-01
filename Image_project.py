from itertools import cycle
from PIL import Image,ImageTk
import time
import tkinter as tk
root = tk.Tk()
root.title("Image Viewer")


#List of the image path hera r is rowstring
image_paths=[
    r"C:\Users\singh\OneDrive\Desktop\vibes\20230307_112908.jpg",
    r"C:\Users\singh\OneDrive\Desktop\vibes\IMG_20230723_071754_020.jpg",
    r"C:\Users\singh\OneDrive\Desktop\vibes\IMG_0995.jpg",
    r"C:\Users\singh\OneDrive\Desktop\vibes\IMG_20230702_131329_307.jpg",
    r"C:\Users\singh\OneDrive\Desktop\vibes\IMG_20240104_180506_045.jpg",
    r"C:\Users\singh\OneDrive\Desktop\vibes\IMG20230702105241.jpg",
    r"C:\Users\singh\OneDrive\Desktop\vibes\annu\IMG_8949.JPG",
    r"C:\Users\singh\OneDrive\Desktop\vibes\20240501_215853.jpg"
]

#Resize the image to 1080x1080
image_size=(1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow=cycle(photo_images) 

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button=tk.Button(root,text='play Slideshow',command=start_slideshow)
play_button.pack()


root.mainloop()        
