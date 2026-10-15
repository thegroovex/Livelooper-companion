"""Generate the Stream Deck key icons (144x144 PNG). python3 tools/make_icons.py"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent.parent / "streamdeck" / "icons"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SRC, PRE, TR = (255, 140, 40), (60, 200, 230), (235, 70, 70)
KEYS = [  # file, label, sub, colour
    ("01_synth1", "SYNTH", "1", SRC), ("02_synth2", "SYNTH", "2", SRC),
    ("03_synth3", "SYNTH", "3", SRC), ("04_rhythm", "RHYTHM", "4", SRC),
    ("05_mic", "MIC", "5", SRC),
    ("06_preset1", "PRESET", "1", PRE), ("07_preset2", "PRESET", "2", PRE),
    ("08_preset3", "PRESET", "3", PRE), ("09_preset4", "PRESET", "4", PRE),
    ("10_src_off", "INPUT", "OFF", SRC),
    ("11_rec", "LOOP", "REC", TR), ("12_play", "LOOP", "PLAY", (80, 210, 120)),
    ("13_undo", "LOOP", "UNDO", TR), ("14_clear", "LOOP", "CLEAR", TR),
    ("15_next", "SOURCE", "NEXT", SRC),
]

def key(label, sub, col):
    im = Image.new("RGB", (144, 144), (24, 26, 31))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((6, 6, 138, 138), 18, outline=col, width=4)
    d.rectangle((26, 22, 118, 28), fill=col)
    f1 = ImageFont.truetype(FONT, 20)
    f2 = ImageFont.truetype(FONT, 40 if len(sub) <= 2 else 28)
    d.text((72, 56), label, font=f1, fill=(235, 235, 235), anchor="mm")
    d.text((72, 98), sub, font=f2, fill=col, anchor="mm")
    d.text((72, 128), "livelooper", font=ImageFont.truetype(FONT, 11), fill=(120, 120, 128), anchor="mm")
    return im

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, label, sub, col in KEYS:
        key(label, sub, col).save(OUT / f"{name}.png")
    tiles = [Image.open(OUT / f"{k[0]}.png") for k in KEYS]
    sheet = Image.new("RGB", (5 * 150 + 6, 3 * 150 + 6), (10, 10, 12))
    for i, t in enumerate(tiles):
        sheet.paste(t, (6 + (i % 5) * 150, 6 + (i // 5) * 150))
    sheet.save(OUT.parent / "layout.png")
    print("ok", len(tiles))
