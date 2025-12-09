from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "static/memes"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Prejeta slika
        file = request.files["image"]
        top_text = request.form["top_text"].upper()
        bottom_text = request.form["bottom_text"].upper()

        # Odpri sliko
        img = Image.open(file.stream)
        draw = ImageDraw.Draw(img)

        # 🔥 VARNI FONT za Docker (Arial NE obstaja v kontejnerju)
        font = ImageFont.load_default()

        # Širina in višina slike
        w, h = img.size

        # Zgornji tekst
        draw.text(
            (w / 2, 10),
            top_text,
            fill="white",
            stroke_fill="black",
            stroke_width=3,
            anchor="ms",
            font=font
        )

        # Spodnji tekst
        draw.text(
            (w / 2, h - 50),
            bottom_text,
            fill="white",
            stroke_fill="black",
            stroke_width=3,
            anchor="ms",
            font=font
        )

        # Shrani novo sliko
        filename = f"{uuid.uuid4()}.jpg"
        path = os.path.join(UPLOAD_FOLDER, filename)
        img.save(path)

        return render_template("index.html", meme_path=path)

    return render_template("index.html", meme_path=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)