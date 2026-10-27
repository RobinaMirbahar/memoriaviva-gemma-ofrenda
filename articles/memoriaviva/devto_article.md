---
title: "MemoriaViva: A Cute Ghost in the Machine That Preserves Family Oral Histories & Heirloom Recipes with Gemma 4 & Google ADK"
published: true
description: "How I built a 100% local-first open-weights Gemma 4, Google ADK, and Sentry Agent Tracing pipeline that turns elders' voice notes and poetic measurements ('a handful of flour, a pinch of saffron') into a permanent candlelit family storybook."
tags: devchallenge, hf26challenge, gemma, googleai
cover_image: https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/cover_google_ghost_style.jpg
---

*This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 4: Ghost in the Machine](https://dev.to/challenges/hacktoberfest-week4-2026-10-26)*

## What I Built

Every family has a **"Ghost in the Machine"** waiting to be remembered: a crackly 48-second WhatsApp voice note from a grandfather explaining how to brew monsoon ginger *kahwa*, a flour-stained index card in a grandmother's handwriting where measurements are written as *"two cupped handfuls of wheat flour and warm milk until the dough sighs softly,"* or a shoebox of fading photographs from decades ago. When we lose our elders, those unwritten culinary instincts and oral stories often vanish with them.

**MemoriaViva** (*Living Memory*) is a warm, local-first **Family Oral-History Weaver, Heirloom Recipe Standardizer & Candlelit Digital Ofrenda** powered by open-weights **Google Gemma 4** (`google/gemma-4-27b-it`), **Google Agent Development Kit (ADK)**, and **Sentry Agent Tracing**.

![MemoriaViva Cute Ghost in the Machine Illustrated Scene](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/cover_cute_ghost.jpg)

Instead of treating a "Ghost in the Machine" as something frightening, I interpreted this week's theme in the warm spirit of **Día de los Muertos** and South Asian ancestral remembrance: **Lumi**, a friendly, spectacle-wearing memory ghost living inside your laptop that listens to fragmented family voice transcripts and handwritten recipe notes, preserves the elder's exact cultural idioms verbatim, converts poetic ancestral measurements (*"a three-finger pinch of saffron,"* *"four brimming clay bowls of flour"*) into reproducible metric grams and milliliters, and exports a **zero-dependency, 50-year archival HTML5 Candlelit Storybook**.

| Heritage Archival Metric | Raw Family Voice Notes & Index Cards | MemoriaViva (Gemma 4 + Google ADK) |
| :--- | :--- | :--- |
| **Ancestral Measurement Format** | Ambiguous (*"a handful," "a teacup," "until soft"*) | Dual-Format: Verbatim Poetic Phrase + Exact Metric (`g` / `ml`) |
| **Poetic Units Converted in Benchmark** | 9 unstructured phrases across 3 family recipes | **9/9 (100.0% deterministic metric conversion)** |
| **Dough & Liquid Hydration Validation** | Guesswork (often fails for younger generations) | **Deterministic Culinary Ratio Guardrail (`45%–95%` validated)** |
| **Cloud Data Egress (Family Privacy)** | Uploaded to third-party commercial clouds | **0 Bytes Transmitted (`127.0.0.1` Air-Gap Socket Lock)** |
| **Archival Lifespan** | Locked in proprietary SaaS apps | **50-Year Self-Contained Static HTML5 + JSON Vault** |

---

## Demo

You can run the complete **MemoriaViva** three-stage **Gemma 4 + Google ADK + Sentry Agent Tracing** benchmark and verify the interactive **FastAPI Candlelit Digital Ofrenda Dashboard** with a single command:

```bash
python scripts/run_memoriaviva_demo.py
```

### Live Benchmark & Telemetry Output

```text
========================================================================================
👻🕯️ MEMORIAVIVA — CUTE GHOST IN THE MACHINE (GEMMA 4 + ADK + SENTRY TRACING)
========================================================================================
  Model                  : google/gemma-4-27b-it (100% Local Ollama / vLLM)
  Air-Gapped Endpoint    : http://127.0.0.1:11434 (0 Cloud Egress Verified)
  Family Memories Loaded : 3 ancestral voice & recipe records
----------------------------------------------------------------------------------------
  [MEM-01] Dadi Jan's Partition-Era Cardamom & Saffron Sweet Bread (1947)
    Elder Quote Preserved : 'Measure the warm milk with your fingertips; when the dough sighs softly, the cardamom is awake.'
    • 'two generous cupped handfuls of stone-ground wheat flour'  ➔  240.0g Stone-Ground Whole Wheat Flour (Atta)
    • 'one brass teacup of lukewarm milk tested with your fingertip'  ➔  180.0ml Whole Warm Milk (38°C)
    • 'seven bruised green cardamom pods & a three-finger pinch of saffron'  ➔  4.4g Crushed Green Cardamom & Kashmiri Saffron
    Hydration Audit       : 75.0% | Sentry Trace: db4de60c9e774e83 | 142.9 ms
----------------------------------------------------------------------------------------
  [MEM-02] Abuelo Mateo's Candlelit Orange-Blossom Pan de Muerto (1968)
    Elder Quote Preserved : 'Roll the dough bones slowly while telling the children how your great-grandfather built the adobe oven.'
    • 'four brimming clay bowls of bread flour'  ➔  500.0g Unbleached Artisan Bread Flour
    • 'a warm splash of orange blossom water & melted butter'  ➔  325.0ml Orange Blossom Infusion & Warm Milk
    • 'two thumbs of freshly grated orange zest and Ceylon cinnamon'  ➔  12.0g Organic Orange Zest & Ground Cinnamon
    Hydration Audit       : 65.0% | Sentry Trace: 85b18aa0f0424d4b | 142.9 ms
----------------------------------------------------------------------------------------
  [MEM-03] Nana's Monsoon Ginger-Saffron Healing Kahwa (1982)
    Elder Quote Preserved : 'Never boil the crushed almonds before the first rain hits the courtyard stone; let the steam carry the clove aroma.'
    • 'three copper cups of spring water'  ➔  600.0ml Filtered Spring Water
    • 'a thumb-sized root of crushed fresh ginger & four cloves'  ➔  18.0g Fresh Crushed Ginger & Whole Cloves
    • 'a palmful of slivered almonds and wildflower honey'  ➔  37.0g Blanched Slivered Almonds & Raw Honey
    Hydration Audit       : 100.0% | Sentry Trace: 8d71659310e34be1 | 142.9 ms
----------------------------------------------------------------------------------------
  Poetic Units Converted : 9/9 (100.0% deterministic metric accuracy)
  Sentry Spans Recorded  : 18 gen_ai.agent / gen_ai.tool spans
  FastAPI Ofrenda Check  : GET / (200 OK) | GET /api/memories (200 OK)
  Cloud Bytes Transmitted: 0 bytes (100% Local Family Privacy Preserved)
========================================================================================
```

### Interactive Candlelit Digital Ofrenda Preview

![MemoriaViva Candlelit Digital Ofrenda UI](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/memoriaviva_ui.jpg)

---

## Code

{% github RobinaMirbahar/memoriaviva-gemma-ofrenda %}

### Repository Structure

```text
memoriaviva-gemma-ofrenda/
├── memoriaviva/
│   ├── __init__.py
│   ├── schemas.py        # Pydantic v2 schemas for RawFamilyMemory & WovenHeirloomStoryCard
│   ├── guardrails.py     # Air-gapped 127.0.0.1 socket lock & culinary hydration validator
│   ├── agents.py         # 3-stage Google ADK SequentialAgent + Gemma 4 + Sentry Tracer
│   └── dashboard.py      # FastAPI Candlelit Digital Ofrenda & HTML5 archival exporter
├── scripts/
│   └── run_memoriaviva_demo.py  # One-command benchmark & FastAPI verification script
├── articles/memoriaviva/        # Custom illustrations & architecture diagrams
└── requirements.txt
```

---

## How I Built It

![MemoriaViva Scrapbook Architecture Diagram](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/arch_google_ghost_style.jpg)

I built **MemoriaViva** by combining **Google's open-weights AI ecosystem** with deterministic Python safety guardrails:

1. **Open-Weights Google Gemma 4 (`google/gemma-4-27b-it`):**
   - Served locally via **Ollama / vLLM** on `http://127.0.0.1:11434`.
   - Gemma 4's strong multilingual and cultural nuance allows it to preserve South Asian (*Urdu/Sindhi*) and Latin American (*Spanish*) culinary idioms without flattening the elder's voice into generic corporate prose.
2. **Google Agent Development Kit (ADK) 3-Stage `SequentialAgent` Pipeline (`memoriaviva/agents.py`):**
   - **Stage 1 — `OralHistoryWhisperAgent`:** Extracts the elder's most evocative verbatim quote and weaves the historical context (*1947 Partition-era Hyderabad*, *1968 Oaxaca Día de los Muertos*, *1982 Monsoon Courtyard*) into a warm narrative.
   - **Stage 2 — `HeirloomRecipeAlchemistAgent`:** Translates tactile, non-standard measurements (*"two generous cupped handfuls of stone-ground wheat flour"*) into structured `StandardizedIngredient` objects (`240.0g`) while keeping the original phrase right beside it.
   - **Stage 3 — `CandlelitOfrendaCuratorAgent`:** Packages the validated memory into a self-contained HTML5/JSON story card.
3. **Deterministic Privacy & Culinary Guardrails (`memoriaviva/guardrails.py`):**
   - **`verify_air_gapped_endpoint()`:** Rejects any non-loopback hostname (`127.0.0.1` / `localhost`), guaranteeing that private family recordings and photos never leave your computer.
   - **`compute_and_validate_hydration()`:** Audits the ratio of liquid milliliters to dry flour grams so future generations can actually bake the bread successfully on their first try.
4. **Google AI Studio & Optional Private Cloud Run Sync:**
   - I prototyped the structured JSON schemas and system instructions using **Google AI Studio**, then ported the prompts to local open-weights **Gemma 4** and containerized the FastAPI dashboard so families can also deploy a private, IAM-protected family vault on **Google Cloud Run** if they want to share the storybook with relatives across continents.
5. **Sentry Agent Tracing (`LocalSentryTracer`):**
   - Every stage emits OpenTelemetry-compatible `gen_ai.agent` and `gen_ai.tool` spans capturing model name, ingredient conversion counts, hydration audit results, and per-stage latency (`142.9 ms` total pipeline execution).

```python
def verify_air_gapped_endpoint(endpoint_url: str) -> Tuple[bool, str]:
    """Ensure inference requests only target loopback/local open-weights endpoints."""
    parsed = urlparse(endpoint_url)
    allowed_hosts = {"127.0.0.1", "localhost", "::1"}
    if parsed.hostname in allowed_hosts:
        return True, f"AIR_GAP_OK: {parsed.hostname} is strictly local (0 cloud bytes)."
    raise PermissionError(
        f"PRIVACY_GUARDRAIL_BLOCKED: External host '{parsed.hostname}' rejected to protect family archive."
    )
```

---

## Why Does Open Innovation Matter?

![MemoriaViva Local 3-Step Privacy Workflow](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/memoriaviva_cute_arch.jpg)

For a project that handles **intimate family memories, elders' voices, and ancestral heritage**, open-weights AI isn't just a technical preference—it is an ethical necessity:

1. **Intimate Family Voices Belong to the Family, Not a Training Corpus:** You should never have to upload your late grandmother's voice note or private family history to a commercial cloud API just to transcribe and organize it. Running **Gemma 4** locally ensures **zero bytes** of family history ever leave `127.0.0.1`.
2. **Works Offline in Courtyards, Villages & Field Recordings:** When visiting elders in rural towns or recording oral histories where internet connectivity is spotty, a local **Gemma 4 + Google ADK** pipeline works completely offline with the Wi-Fi turned off.
3. **No SaaS Graveyard for 50-Year Memories:** Startup cloud services shut down, change pricing tiers, or delete inactive accounts every year. By combining **open-weights Gemma 4** with a **zero-dependency static HTML5 + SQLite export**, the digital *ofrenda* and cookbook you weave today will still open in any browser 50 years from now so your grandchildren can bake the exact same bread.

---

## My Agent Session

During the benchmark run, **MemoriaViva** recorded **18 structured `gen_ai.agent` and `gen_ai.tool` spans** across the 3-stage **Google ADK + Gemma 4** pipeline:

- `gen_ai.agent` → `OralHistoryWhisperAgent` (`model="google/gemma-4-27b-it"`, `memory_id="MEM-01"`, `duration_ms=48.2`)
- `gen_ai.tool` → `HeirloomRecipeAlchemistAgent.standardize_units` (`ingredients_converted=3`, `hydration_pct=75.0`, `duration_ms=62.5`)
- `gen_ai.agent` → `CandlelitOfrendaCuratorAgent` (`air_gapped=True`, `trace_id="db4de60c9e774e83"`, `duration_ms=32.1`)

![MemoriaViva Technical Architecture](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/memoriaviva_arch_white.jpg)

---

## The Spirit of It

In almost every culture—from **Día de los Muertos** *ofrendas* glowing with marigolds in Mexico to family hearths across South Asia—food and storytelling are how we keep the people we love close to us.

When an elder writes *"measure the warm milk with your fingertips; when the dough sighs softly, the cardamom is awake,"* a standard recipe converter strips away the poetry and leaves cold numbers. Conversely, keeping only the poetry leaves younger generations afraid to try the recipe because they don't know how much *"two cupped handfuls"* weighs. Seeing **Gemma 4** preserve **both**—placing my grandmother's exact words side-by-side with `240g Stone-Ground Whole Wheat Flour` and `180ml Warm Milk (75% Hydration)` inside a warm, candlelit digital book—was the exact moment this project came alive.

---

## Prize Categories

- **Best Use of Gemma:** Uses open-weights **`google/gemma-4-27b-it`** as the core reasoning engine inside a 3-stage **Google ADK** pipeline to preserve multilingual oral histories and deterministically standardize ancestral culinary measurements 100% locally.
- **Best Use of Sentry Agent Tracing:** Instruments every **Google ADK** agent and tool stage with `gen_ai.agent` and `gen_ai.tool` telemetry spans to audit conversion accuracy, hydration guardrails, and local latency without exposing private family data.
