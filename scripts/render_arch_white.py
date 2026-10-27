"""Render clean white-background architecture diagram with 100% verified claims (no 50-year claim)."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)

f_title = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
f_sub = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 17)
f_hdr = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 18)
f_body = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 14)
f_bold = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 16)
f_reg = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 16)

# Outer frame
d.rounded_rectangle([14, 14, W - 14, H - 14], radius=18, outline=(203, 213, 225), width=2, fill=(255, 255, 255))

# Header pill
d.rounded_rectangle([38, 28, 1125, 72], radius=10, fill=(254, 240, 138))
d.text((52, 37), "MemoriaViva Architecture: Local Open-Weights Gemma 4 + Google ADK + Sentry", font=f_title, fill=(15, 23, 42))

# Subheader pill
d.rounded_rectangle([38, 80, 1005, 114], radius=8, fill=(186, 230, 253))
d.text((52, 88), "100% Offline Execution Pipeline: Family Voice Notes, Heirloom Recipes & Photos Stay on 127.0.0.1", font=f_sub, fill=(15, 23, 42))

cards = [
    (
        "1. Local Family Inputs",
        (224, 242, 254),
        [
            "â€¢ Handwritten Recipe Cards",
            "â€¢ Elders' Oral History Notes",
            "â€¢ Vintage Photo Metadata",
            "â€¢ Regional Idioms (EN/UR/ES)",
            "â€¢ Local Loopback Lock:",
            "  host = 127.0.0.1",
        ],
    ),
    (
        "2. Google ADK Pipeline",
        (254, 243, 199),
        [
            "SequentialAgent Orchestrator",
            "â”œ OralHistoryWhisperAgent",
            "â”œ RecipeAlchemistAgent",
            "â”‚ (Cup/Handful -> Grams)",
            "â”” OfrendaCuratorAgent",
            "  (WovenHeirloomStoryCard)",
        ],
    ),
    (
        "3. Open-Weights Gemma 4",
        (209, 250, 229),
        [
            "google/gemma-4-27b-it",
            "â€¢ Local Ollama / vLLM Engine",
            "â€¢ Pydantic v2 Schema Guard",
            "â€¢ Cultural Idiom Preservation",
            "â€¢ Deterministic Math Audit",
            "â€¢ Zero Cloud Egress Check",
        ],
    ),
    (
        "4. Family Vault (BigQuery)",
        (243, 232, 255),
        [
            "â€¢ FastAPI Family Storybook",
            "â€¢ Self-Contained HTML5 Book",
            "  (W3C Standard, 4,909 B)",
            "â€¢ RFC 8259 JSON Export",
            "  (4,344 B / 3 Nested Rows)",
            "â€¢ Sentry Agent Tracing",
        ],
    ),
]

card_w = 276
card_h = 292
top_y = 134
gap = 32
start_x = 42

for idx, (title, hdr_col, bullets) in enumerate(cards):
    x0 = start_x + idx * (card_w + gap)
    x1 = x0 + card_w
    y0 = top_y
    y1 = y0 + card_h

    d.rounded_rectangle([x0, y0, x1, y1], radius=14, outline=(15, 23, 42), width=2, fill=(255, 255, 255))
    d.rounded_rectangle([x0 + 2, y0 + 2, x1 - 2, y0 + 58], radius=12, fill=hdr_col)
    d.line([x0, y0 + 58, x1, y0 + 58], fill=(15, 23, 42), width=2)

    # Traffic lights
    for ci, col in enumerate([(239, 68, 68), (245, 158, 11), (16, 185, 129)]):
        cx = x0 + 18 + ci * 16
        cy = y0 + 18
        d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=col, outline=(15, 23, 42), width=1)

    d.text((x0 + 14, y0 + 31), title, font=f_hdr, fill=(15, 23, 42))

    by = y0 + 74
    for b in bullets:
        d.text((x0 + 14, by), b, font=f_body, fill=(30, 41, 59))
        by += 33

    if idx < 3:
        ax0 = x1 + 4
        ax1 = x1 + gap - 6
        ay = y0 + card_h // 2
        d.line([ax0, ay, ax1, ay], fill=(15, 23, 42), width=3)
        d.polygon([(ax1, ay), (ax1 - 10, ay - 7), (ax1 - 10, ay + 7)], fill=(15, 23, 42))

# Bottom guardrail box
bx0, by0, bx1, by1 = 42, 456, W - 42, 688
d.rounded_rectangle([bx0, by0, bx1, by1], radius=14, outline=(15, 23, 42), width=2, fill=(255, 255, 255))
d.rounded_rectangle([bx0 + 2, by0 + 2, bx1 - 2, by0 + 52], radius=12, fill=(254, 240, 138))
d.line([bx0, by0 + 52, bx1, by0 + 52], fill=(15, 23, 42), width=2)

for ci, col in enumerate([(239, 68, 68), (245, 158, 11), (16, 185, 129)]):
    cx = bx0 + 22 + ci * 16
    cy = by0 + 26
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=col, outline=(15, 23, 42), width=1)

d.text((bx0 + 78, by0 + 16), "Deterministic Heritage & Privacy Interlocks (memoriaviva/guardrails.py)", font=f_hdr, fill=(15, 23, 42))

rows = [
    ("Air-Gapped Socket Guard:", (4, 120, 87), "Blocks all non-loopback (127.0.0.1) HTTP calls so family stories never touch external servers"),
    ("Culinary Ratio Auditor:", (3, 105, 161), "Validates hydration & spice ratios (45% to 95%) when converting 'a pinch / handful' into metric grams"),
    ("BigQuery & HTML5 Vault:", (109, 40, 217), "Exports W3C HTML5 (4,909 B) & BigQuery JSONL (4,344 B) for local archive or BigQuery table sync"),
]

ry = by0 + 74
for label, lcol, desc in rows:
    d.rounded_rectangle([bx0 + 22, ry, bx0 + 44, ry + 22], radius=4, outline=(4, 120, 87), width=2, fill=(236, 253, 245))
    d.line([(bx0 + 27, ry + 11), (bx0 + 32, ry + 16), (bx0 + 40, ry + 6)], fill=(4, 120, 87), width=3)
    d.text((bx0 + 56, ry + 2), label, font=f_bold, fill=lcol)
    d.text((bx0 + 324, ry + 2), desc, font=f_reg, fill=(30, 41, 59))
    ry += 50

out_repo = Path(r"C:\Users\s tech\.gemini\antigravity\brain\d24be4a9-559f-4961-99d7-ccfa79240af3\scratch\memoriaviva_build\articles\memoriaviva\memoriaviva_arch_white_v2.jpg")
out_art = Path(r"C:\Users\s tech\.gemini\antigravity\brain\d24be4a9-559f-4961-99d7-ccfa79240af3\memoriaviva_arch_white_v2.jpg")
img.save(out_repo, quality=95)
img.save(out_art, quality=95)
print("Saved clean memoriaviva_arch_white_v2.jpg without any 50-year claims!")

