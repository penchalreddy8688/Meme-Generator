from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse  #(e.g., {"meme_url": "..."}).
from fastapi.staticfiles import StaticFiles #Lets FastAPI serve static files (like images, CSS, JS) directly.
from PIL import Image, ImageDraw, ImageFont #Pillow (PIL) → library for image processing, Image → to open and save images.ImageDraw → to draw text or shapes on images.ImageFont → to load custom fonts for drawing text.
import uuid  #Generates unique IDs for file names so no two uploads overwrite each other.
import os    #Interacts with the file system (create folders, join paths, etc.).

app = FastAPI()

UPLOAD_DIR = "memes"  #folder name to store memes.
os.makedirs(UPLOAD_DIR, exist_ok=True)  #create folder if it doesn’t already exist.

# Mount static files so we can access memes via URL
app.mount("/memes", StaticFiles(directory=UPLOAD_DIR), name="memes") #Serve any files in memes/ when someone goes to /memes/... in the browser.

@app.post("/generate-meme/")
async def generate_meme(
    file: UploadFile = File(...),  #File(...) → required file.
    top_text: str = Form(""),      #Form("") → optional text (defaults to empty string).
    bottom_text: str = Form("")
):
    # Save uploaded file
    image_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_{file.filename}")  #Combines the upload folder with a unique ID + original filename for safe storage.
    with open(image_path, "wb") as f:  #Saves the uploaded file to disk in binary mode (wb).
        f.write(await file.read())

    # Open image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)   #Creates a drawing object (draw) to write text onto it.

    # Load font (fallback to default if arial not found)
    try:
        font = ImageFont.truetype("arial.ttf", size=40) #Tries to load Arial font (size 40).
    except:
        font = ImageFont.load_default()  #If Arial is not found, uses default Pillow font.



    # Custom function to measure text size (Pillow 10+ replaced textsize() with textbbox()).
    def get_text_size(text, font):
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Text positions
    width, height = img.size
    top_w, top_h = get_text_size(top_text, font)     #Measures top & bottom text size.
    bottom_w, bottom_h = get_text_size(bottom_text, font)

    # Draw top text
    draw.text(
        ((width - top_w) / 2, 10),  #Draws top text, centered horizontally, 10px from the top.
        top_text,
        font=font,
        fill="white",
        stroke_width=2,
        stroke_fill="black"    #White text with black outline
    )

    # Draw bottom text
    draw.text(
        ((width - bottom_w) / 2, height - bottom_h - 10),
        bottom_text,
        font=font,
        fill="white",
        stroke_width=2,
        stroke_fill="black"
    )

    # Saves the modified image as a new file in the memes folder.
    meme_filename = f"meme_{uuid.uuid4()}.png"
    meme_path = os.path.join(UPLOAD_DIR, meme_filename)
    img.save(meme_path)

    # Return a shareable URL instead of direct file
    meme_url = f"http://127.0.0.1:8000/memes/{meme_filename}"
    # meme_url = f"/memes/{meme_filename}"
    return JSONResponse(content={"meme_url": meme_url})









