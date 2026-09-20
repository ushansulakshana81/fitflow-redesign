"""Generate docs/architecture-diagram.png for the FitFlow redesign.

Requires Pillow:  pip install pillow

Regenerate the PNG from this script:
    python scripts/generate-architecture-diagram.py
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "docs", "architecture-diagram.png")

W, H = 1600, 1080
BG = (255, 255, 255)

PALETTE = {
    "client": ("#E3F2FD", "#1565C0"),
    "gateway": ("#E8F5E9", "#2E7D32"),
    "backend": ("#FFF3E0", "#E65100"),
    "ai": ("#F3E5F5", "#6A1B9A"),
    "data": ("#ECEFF1", "#37474F"),
    "bus": ("#FFFDE7", "#F9A825"),
}


def font(size, bold=False):
    names = [
        "segoeuib.ttf" if bold else "segoeui.ttf",
        "arialbd.ttf" if bold else "arial.ttf",
        "calibrib.ttf" if bold else "calibri.ttf",
        "verdana.ttf",
    ]
    for name in names:
        p = os.path.join(r"C:\Windows\Fonts", name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def box(draw, x, y, w, h, title, subtitle, key, bold=False):
    fill, outline = PALETTE[key]
    draw.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=fill,
                           outline=outline, width=2)
    tf = font(25 if not bold else 27, bold=True)
    sf = font(18)
    tw = draw.textlength(title, font=tf)
    draw.text((x + (w - tw) / 2, y + 16), title, font=tf, fill=outline)
    if subtitle:
        sw = draw.textlength(subtitle, font=sf)
        draw.text((x + (w - sw) / 2, y + 56), subtitle, font=sf, fill=(80, 80, 80))


def arrow(draw, p1, p2, color="#546E7A", width=3):
    draw.line([p1, p2], fill=color, width=width)
    x1, y1 = p1
    x2, y2 = p2
    ang = math.atan2(y2 - y1, x2 - x1)
    length = 16
    spread = math.radians(22)
    for s in (1, -1):
        hx = x2 - length * math.cos(ang - s * spread)
        hy = y2 - length * math.sin(ang - s * spread)
        draw.line([(x2, y2), (hx, hy)], fill=color, width=width)


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

title_font = font(34, bold=True)
d.text((40, 24), "FitFlow Redesign — System Architecture", font=title_font, fill=(33, 33, 33))

# ---- Client layer ----
client_y, client_h = 90, 120
box(d, 140, client_y, 380, client_h, "React Native App", "iOS / Android", "client", bold=True)
box(d, 560, client_y, 380, client_h, "React Web App", "Browser", "client")

# ---- API Gateway ----
gw_x, gw_y, gw_w, gw_h = 340, 270, 900, 90
box(d, gw_x, gw_y, gw_w, gw_h, "API Gateway / BFF", "NestJS", "gateway", bold=True)

# ---- Backend services ----
by, bh, bw, gap = 430, 150, 300, 20
services = [
    ("Auth Service", "NestJS"),
    ("Workout Service", "NestJS"),
    ("Nutrition Service", "NestJS"),
    ("Social Service", "NestJS"),
]
bx = [140 + i * (bw + gap) for i in range(len(services))]
for x, (title, sub) in zip(bx, services):
    box(d, x, by, bw, bh, title, sub, "backend")

# ---- Message bus + AI service ----
mb_x, mb_y, mb_w, mb_h = 140, 660, 600, 70
box(d, mb_x, mb_y, mb_w, mb_h, "Message Bus (RabbitMQ)", None, "bus")

ai_x, ai_y, ai_w, ai_h = 820, 650, 640, 170
box(d, ai_x, ai_y, ai_w, ai_h, "AI Service", "FastAPI", "ai", bold=True)
box(d, ai_x + 30, ai_y + 90, 270, 60, "Recommendation Engine", None, "ai")
box(d, ai_x + 340, ai_y + 90, 270, 60, "Computer Vision", None, "ai")

# ---- Data layer ----
dy, dh, dw = 900, 140, 380
data = [
    ("PostgreSQL", "Primary datastore"),
    ("Redis", "Cache / sessions"),
    ("Object Storage", "Images / models"),
]
for i, (title, sub) in enumerate(data):
    box(d, 140 + i * (dw + 20), dy, dw, dh, title, sub, "data")

# ---- Arrows ----
arrow(d, (330, client_y + client_h), (500, gw_y))          # mobile -> gateway
arrow(d, (750, client_y + client_h), (900, gw_y))          # web -> gateway
for i in range(4):                                          # gateway -> services
    arrow(d, (420 + i * 120, gw_y + gw_h), (bx[i] + bw // 2, by))
arrow(d, (610, by + bh), (440, mb_y))                       # workout -> message bus
arrow(d, (1250, by + bh), (440, mb_y))                      # social -> message bus
arrow(d, (mb_x + mb_w, mb_y + mb_h // 2), (ai_x, ai_y + 40))  # bus -> AI
arrow(d, (ai_x + ai_w // 2, ai_y + ai_h), (1130, dy))      # AI -> object storage
arrow(d, (330, by + bh), (330, dy))                         # auth -> postgres
arrow(d, (730, by + bh), (730, dy))                         # nutrition -> redis

img.save(OUT)
print("Saved:", os.path.abspath(OUT))
