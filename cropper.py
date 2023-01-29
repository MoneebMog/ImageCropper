import tkinter as tk
import cv2
from tkinter import filedialog
import os

filepath = None
cropped = None

root = tk.Tk()
root.title("ImageCropper")

filepath = None
cropped = None

def select_image():
    global filepath
    # Open file dialog to select image
    filepath = filedialog.askopenfilename()
    select_label.config(text=f"Currently Selected: {filepath}")

select_label = tk.Label(root, text="No image selected.")
select_label.pack()


def process_image():
    global filepath, cropped
    # Open image and process it (this is where your image processing code goes)
    img = cv2.imread(filepath)
    # perform thresholding
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold, img_threshold = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # Find bounding box of object
    x,y,w,h = cv2.boundingRect(img_threshold)
    # Crop image
    cropped = img[y:y+h, x:x+w]

def save_image():
    global cropped
    # Open file dialog to save processed image
    filepath = filedialog.asksaveasfilename(defaultextension=".jpg")
    # Save processed image
    cv2.imwrite(filepath, cropped)


# Create a label to display the selected image filepath and filename
selected_label = tk.Label(root)
selected_label.pack()

# Create a button to select the input image
select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack()

# Create a button to run the image processing script
process_button = tk.Button(root, text="Process Image", command=process_image)
process_button.pack()

# Create a button to save the output image
save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack()

root.mainloop()



