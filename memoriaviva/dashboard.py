"""FastAPI Candlelit Digital Ofrenda & Family Story Weaver Dashboard."""

from typing import List
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from memoriaviva.schemas import RawFamilyMemory, WovenHeirloomStoryCard
from memoriaviva.agents import MemoriaVivaSequentialPipeline

app = FastAPI(title="MemoriaViva: Cute Ghost in the Machine (Gemma 4 + ADK)")
pipeline = MemoriaVivaSequentialPipeline()

SAMPLE_MEMORIES: List[RawFamilyMemory] = [
    RawFamilyMemory(
        memory_id="MEM-01",
        elder_name="Dadi Jan (Fatima Begum)",
        year_recorded=1947,
        cultural_tradition="Partition-Era Family Hearth & Eid Morning Tradition",
        raw_voice_transcript="Two generous cupped handfuls of wheat flour, one brass teacup of warm milk... measure with your fingertips; when the dough sighs softly, the cardamom is awake.",
        poetic_measurements=[
            "two generous cupped handfuls of stone-ground wheat flour",
            "one brass teacup of lukewarm milk tested with your fingertip",
            "seven bruised green cardamom pods & a three-finger pinch of saffron",
        ],
    ),
    RawFamilyMemory(
        memory_id="MEM-02",
        elder_name="Abuelo Mateo Rivera",
        year_recorded=1968,
        cultural_tradition="Dia de los Muertos Candlelit Family Ofrenda (Oaxaca)",
        raw_voice_transcript="Four brimming clay bowls of bread flour, a warm splash of orange blossom water... roll the dough bones slowly while telling the children how your great-grandfather built the adobe oven.",
        poetic_measurements=[
            "four brimming clay bowls of bread flour",
            "a warm splash of orange blossom water & melted butter",
            "two thumbs of freshly grated orange zest and Ceylon cinnamon",
        ],
    ),
    RawFamilyMemory(
        memory_id="MEM-03",
        elder_name="Nana (Mirza Sahib)",
        year_recorded=1982,
        cultural_tradition="Monsoon Courtyard Storytelling & Winter Remembrance",
        raw_voice_transcript="Three copper cups of spring water, a thumb of crushed ginger... never boil the crushed almonds before the first rain hits the courtyard stone.",
        poetic_measurements=[
            "three copper cups of spring water",
            "a thumb-sized root of crushed fresh ginger & four cloves",
            "a palmful of slivered almonds and wildflower honey",
        ],
    ),
]

WOVEN_ARCHIVE: List[WovenHeirloomStoryCard] = [pipeline.weave_memory(m) for m in SAMPLE_MEMORIES]


@app.get("/api/memories", response_model=List[WovenHeirloomStoryCard])
def list_woven_memories() -> List[WovenHeirloomStoryCard]:
    return WOVEN_ARCHIVE


@app.post("/api/weave", response_model=WovenHeirloomStoryCard)
def weave_new_memory(raw: RawFamilyMemory) -> WovenHeirloomStoryCard:
    card = pipeline.weave_memory(raw)
    WOVEN_ARCHIVE.append(card)
    return card


@app.get("/", response_class=HTMLResponse)
def render_ofrenda_dashboard() -> str:
    cards_html = ""
    for c in WOVEN_ARCHIVE:
        ing_rows = "".join(
            f"<li><strong>{i.original_phrase}</strong> ➔ <code>{i.metric_grams_or_ml}{i.unit} {i.ingredient_name}</code> <em>({i.culinary_note})</em></li>"
            for i in c.standardized_recipe
        )
        cards_html += f"""
        <div class="card">
          <div class="badge">🕯️ {c.memory_id} • {c.year_recorded} • {c.cultural_tradition}</div>
          <h2>{c.title}</h2>
          <p class="quote">"{c.verbatim_elder_quote}" ({c.elder_name})</p>
          <p>{c.woven_narrative}</p>
          <ul>{ing_rows}</ul>
          <div class="meta">✓ 100% Local Gemma 4 • Hydration: {c.hydration_ratio_pct}% • Sentry Trace: {c.sentry_trace_id}</div>
        </div>
        """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>👻🕯️ MemoriaViva: Cute Ghost in the Machine (Gemma 4 + ADK)</title>
  <style>
    body {{ background:#ffffff; color:#0f172a; font-family:system-ui,sans-serif; max-width:960px; margin:0 auto; padding:28px; }}
    .card {{ background:#fffbeb; border:1.5px solid #f59e0b; border-radius:14px; padding:20px; margin-bottom:18px; }}
    .quote {{ color:#92400e; font-style:italic; font-size:1.08rem; }}
    .badge {{ color:#b45309; font-weight:700; font-size:0.85rem; }}
    .meta {{ color:#047857; font-family:monospace; font-size:0.85rem; margin-top:12px; }}
    code {{ color:#0369a1; font-weight:600; }}
  </style>
</head>
<body>
  <h1>👻🕯️ MemoriaViva: The Friendly Memory Ghost in Your Machine</h1>
  <p>Powered 100% locally by Open-Weights <strong>Gemma 4</strong>, <strong>Google ADK</strong>, and <strong>Sentry Agent Tracing</strong>.</p>
  {cards_html}
</body>
</html>"""
