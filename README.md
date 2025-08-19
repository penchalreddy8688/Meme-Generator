# 🖼️ Meme Generator  

A **Meme Generator App** built with **FastAPI** and **Pillow (PIL)**.  
Upload an image, add **top and bottom text**, and generate a meme instantly with a shareable link.  

---

## 🚀 Features
- Upload any image and add custom **Top** and **Bottom** text.  
- Text automatically **centered** with white font + black outline.  
- All memes stored in a `memes/` folder with unique filenames.  
- FastAPI serves memes via static URLs.  
- Simple **frontend (HTML)** for easy interaction.  

---

## 🛠️ Installation  

### 1. Clone the repository  
```bash
git clone https://github.com/your-username/meme-generator.git
cd meme-generator

# 2. Create virtual environment
  python -m venv venv
  source venv/bin/activate   # For Linux/Mac
  venv\Scripts\activate      # For Windows

#3. Install dependencies
    pip install -r requirements.txt

    #If you don’t have requirements.txt, install manually:
        pip install fastapi uvicorn pillow

▶️ Running the App
# Start the FastAPI server
    uvicorn main:app --reload
               #Open Frontend (HTML)

                 # Open index.html in your browser.

                  #Upload an image, enter top/bottom text → Click Generate Meme → See your meme instantly.

📂 Project Structure

meme-generator/
│── main.py             # FastAPI backend
│── index.html          # Frontend UI
│── memes/              # Folder storing generated memes
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
│── .gitignore          # Git ignore file

⚡ Tech Stack

    Backend: FastAPI
    Frontend: HTML, CSS, JavaScript
    Image Processing: Pillow (PIL)
