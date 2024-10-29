import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import fitz  # PyMuPDF for PDF handling
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Define functions first to avoid NameError
def generate_handwriting(text, font_style, sentiment):
    # Update the path to the Tania Kast Script Font
    font_path = "C:/Users/adars/OneDrive/Documents/ai project/fonts/TaniaKastScript.ttf"  
    image = Image.new("RGB", (800, 200), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Ballpoint pen blue color
    color = (0, 0, 255)

    # Try to load the Tania Kast Script font
    try:
        if not os.path.exists(font_path):
            raise FileNotFoundError("Tania Kast Script font file not found. Using default font instead.")
        font = ImageFont.truetype(font_path, 40)  # Adjust font size as needed for readability
    except (IOError, FileNotFoundError) as e:
        messagebox.showwarning("Font Warning", f"{str(e)}")
        font = ImageFont.load_default()

    # Draw text on image
    draw.text((10, 10), text, font=font, fill=color)
    image.show()  # Display the generated image

def upload_pdf():
    # Open PDF file and extract text content
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        text_input.set(text)  # Set extracted text to the input box

def save_to_pdf(text):
    # Save the text content to a PDF file
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter
        c.drawString(72, height - 72, text)  # Draw text in PDF at the specified location
        c.save()

# Initialize main window
root = tk.Tk()
root.title("AI Handwriting Converter")
root.geometry("800x600")

# Variables for user options
text_input = tk.StringVar()
font_style = tk.StringVar(value="Cursive")
sentiment = tk.StringVar(value="Neutral")

# Layout: text input and option menus
tk.Label(root, text="Enter your text:").pack()
text_entry = tk.Entry(root, textvariable=text_input, width=80)
text_entry.pack()

tk.Label(root, text="Choose Font Style:").pack()
font_menu = tk.OptionMenu(root, font_style, "Cursive", "Print", "Calligraphy")
font_menu.pack()

tk.Label(root, text="Select Sentiment:").pack()
sentiment_menu = tk.OptionMenu(root, sentiment, "Neutral", "Happy", "Urgent")
sentiment_menu.pack()

# Generate handwriting button
generate_button = tk.Button(root, text="Generate Handwriting", command=lambda: generate_handwriting(text_input.get(), font_style.get(), sentiment.get()))
generate_button.pack()

# Canvas for displaying results
result_canvas = tk.Canvas(root, width=600, height=400, bg="white")
result_canvas.pack()

# PDF upload and download buttons
upload_button = tk.Button(root, text="Upload PDF", command=upload_pdf)
upload_button.pack()

save_button = tk.Button(root, text="Download Handwriting as PDF", command=lambda: save_to_pdf(text_input.get()))
save_button.pack()

# Run the main loop
root.mainloop()
