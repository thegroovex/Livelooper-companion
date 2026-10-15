"""Generate the Stream Deck key icons (144x144 PNG). python3 tools/make_icons.py"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent.parent / "streamdeck" / "icons"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SRC, PRE, TR = (255, 140, 40), (60, 200, 230), (235, 70, 70)
NAV = (170, 170, 180)
PAGE1 = [(f"p1_{i:02d}_src{i}", "SOURCE", str(i), SRC) for i in range(1, 13)] + [
    ("p1_13_prev", "SOURCE", "PREV", SRC), ("p1_14_next", "SOURCE", "NEXT", SRC),
    ("p1_15_page", "PAGE", "2 >", NAV)]
PAGE2 = [(f"p2_{i:02d}_preset{i}", "PRESET", str(i), PRE) for i in range(1, 9)] + [
    ("p2_09_rec", "LOOP", "REC", TR), ("p2_10_play", "LOOP", "PLAY", (80, 210, 120)),
    ("p2_11_undo", "LOOP", "UNDO", TR), ("p2_12_clear", "LOOP", "CLEAR", TR),
    ("p2_13_off", "INPUT", "OFF", SRC), ("p2_14_next", "SOURCE", "NEXT", SRC),
    ("p2_15_page", "PAGE", "< 1", NAV)]

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

def sheet(keys, path):
    tiles = [key(l, sub, c) for _, l, sub, c in keys]
    im = Image.new("RGB", (5 * 150 + 6, 3 * 150 + 6), (10, 10, 12))
    for i, t in enumerate(tiles):
        im.paste(t, (6 + (i % 5) * 150, 6 + (i // 5) * 150))
    im.save(path)

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, label, sub, col in PAGE1 + PAGE2:
        key(label, sub, col).save(OUT / f"{name}.png")
    sheet(PAGE1, OUT.parent / "layout-page1.png")
    sheet(PAGE2, OUT.parent / "layout-page2.png")
    print("ok", len(PAGE1) + len(PAGE2))
