import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF
from PIL import Image, ImageTk


def extract_text_and_image(pdf_path):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)

    # Extract text from the first page
    page = pdf_document.load_page(9)
    text = page.get_text()
    print("Extracted text from the first page:")
    print(text)

    # Extract image from the first page
    pixmap = page.get_pixmap()
    img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

    # Display image in a new window
    image_window = tk.Toplevel(root)
    image_window.title("Extracted Image")

    # Convert image to Tkinter PhotoImage
    tk_image = ImageTk.PhotoImage(img)

    # Display image in a label
    image_label = tk.Label(image_window, image=tk_image)
    image_label.pack()

    # Keep a reference to the image to prevent it from being garbage collected
    image_label.image = tk_image


def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        extract_text_and_image(file_path)


# Create Tkinter GUI
root = tk.Tk()
root.title("PDF Text and Image Extractor")

select_button = tk.Button(root, text="Select PDF File", command=select_pdf_file)
select_button.pack(pady=20)

root.mainloop()
