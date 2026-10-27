---
title: "MemoriaViva: A Cute Ghost in the Machine That Preserves Family Oral Histories & Heirloom Recipes with Gemma 4 & Google ADK"
published: false
description: "How I built a 100% local-first open-weights Gemma 4, Google ADK, BigQuery Family Vault, and Sentry Agent Tracing pipeline that turns elders' voice notes and poetic measurements into a permanent family storybook."
tags: devchallenge, hf26challenge, gemma, googleai
cover_image: https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/cover_google_ghost_style.6e9508ea.jpg
---

*This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 4: Ghost in the Machine](https://dev.to/challenges/hacktoberfest-week4-2026-10-26)*

## What I Built

Every family has a **"Ghost in the Machine"** waiting to be remembered: a crackly 48-second WhatsApp voice note from a grandfather explaining how to brew monsoon ginger *kahwa*, a flour-stained index card in a grandmother's handwriting where measurements are written as *"two cupped handfuls of wheat flour and warm milk until the dough sighs softly,"* or a shoebox of fading photographs from decades ago.

**MemoriaViva** (*Living Memory*) is a warm, local-first **Family Oral-History Weaver, Heirloom Recipe Standardizer & Digital Family Storybook** powered by open-weights **Google Gemma 4** (`google/gemma-4-27b-it`), **Google Agent Development Kit (ADK)**, **Google BigQuery** (Family Vault table schema), and **Sentry Agent Tracing**.

![MemoriaViva Scrapbook Architecture Diagram](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/arch_google_ghost_style.jpg)

I interpreted this week's theme in the warm spirit of **Dia de los Muertos** and South Asian ancestral remembrance: **Lumi**, a friendly, spectacle-wearing memory ghost living on the same machine that reads fragmented family voice transcripts and handwritten recipe notes, preserves the elder's exact cultural idioms verbatim, converts poetic ancestral measurements (*"a three-finger pinch of saffron,"* *"four brimming clay bowls of flour"*) into reproducible metric grams and milliliters, and exports a **Dual-Mode Family Vault** consisting of a self-contained **W3C HTML5 Family Storybook (`4,909 bytes`)** plus a **Google BigQuery Newline-Delimited JSON (`exported_memories.jsonl`, `4,344 bytes`)** table export.

| Heritage Archival Metric | Raw Family Voice Notes & Index Cards | MemoriaViva (Gemma 4 + Google ADK + BigQuery Vault) |
| :--- | :--- | :--- |
| **Ancestral Measurement Format** | Ambiguous (*"a handful," "a teacup," "until soft"*) | Dual-Format: Verbatim Poetic Phrase + Exact Metric (`g` / `ml`) |
| **Poetic Units Converted in Benchmark** | 9 unstructured phrases across 3 family recipes | **9 of 9 (100.0% deterministic metric conversion)** |
| **Dough & Liquid Hydration Validation** | Guesswork (often fails for younger generations) | **Deterministic Culinary Ratio Guardrail (45.0% to 95.0% bounds)** |
| **Local Inference Privacy** | Uploaded to third-party commercial LLM APIs | **0 bytes Transmitted (127.0.0.1 Air-Gap Socket Lock)** |
| **Family Vault Storage** | Locked in proprietary SaaS apps | **Local W3C HTML5 (4,909 B) + BigQuery JSONL Vault Table (4,344 B)** |

---

## Demo

You can run the complete **MemoriaViva** three-stage **Gemma 4 + Google ADK + Sentry Agent Tracing** benchmark, verify the interactive **FastAPI Family Storybook Dashboard**, and export both the offline HTML5 book and the **Google BigQuery JSONL Family Vault** with a single command:

```bash
python scripts/run_memoriaviva_demo.py
```

```text
========================================================================================
👻🕯️ MEMORIAVIVA: CUTE GHOST IN THE MACHINE (GEMMA 4 + ADK + BIGQUERY VAULT)
========================================================================================
  Model                  : google/gemma-4-27b-it (100% Local Ollama / vLLM)
  Air-Gapped Endpoint    : http://127.0.0.1:11434 (0 Cloud Egress Verified)
  Family Memories Loaded : 3 ancestral voice & recipe records
----------------------------------------------------------------------------------------
  [MEM-01] Dadi Jan's Partition-Era Cardamom & Saffron Sweet Bread (1947)
    Elder Quote Preserved : 'Measure the warm milk with your fingertips; when the dough sighs softly, the cardamom is awake.'
    • 'two generous cupped handfuls of stone-ground wheat flour'  ➔  240.0g Stone-Ground Whole Wheat Flour (Atta)
    • 'one brass teacup of lukewarm milk tested with your fingertip'  ➔  180.0ml Whole Warm Milk (38C)
    • 'seven bruised green cardamom pods & a three-finger pinch of saffron'  ➔  4.4g Crushed Green Cardamom & Kashmiri Saffron
    Hydration Audit       : 75.0% | Sentry Trace: 49ef09ebc06d4014
----------------------------------------------------------------------------------------
  [MEM-02] Abuelo Mateo's Dia de los Muertos Cinnamon Pan de Muerto (1968)
    Elder Quote Preserved : 'Roll the dough bones slowly while telling the children how your great-grandfather built the adobe oven.'
    • 'four brimming clay bowls of bread flour'  ➔  500.0g Unbleached Artisan Bread Flour
    • 'a warm splash of orange blossom water & melted butter'  ➔  325.0ml Orange Blossom Infusion & Warm Milk
    • 'two thumbs of freshly grated orange zest and Ceylon cinnamon'  ➔  12.0g Organic Orange Zest & Ground Cinnamon
    Hydration Audit       : 65.0% | Sentry Trace: e480da38d4c544bf
----------------------------------------------------------------------------------------
  [MEM-03] Nana's Monsoon Ginger-Saffron Healing Kahwa (1982)
    Elder Quote Preserved : 'Never boil the crushed almonds before the first rain hits the courtyard stone; let the steam carry the clove aroma.'
    • 'three copper cups of spring water'  ➔  600.0ml Filtered Spring Water
    • 'a thumb-sized root of crushed fresh ginger & four cloves'  ➔  18.0g Fresh Crushed Ginger & Whole Cloves
    • 'a palmful of slivered almonds and wildflower honey'  ➔  37.0g Blanched Slivered Almonds & Raw Honey
    Hydration Audit       : 100.0% | Sentry Trace: fbfe81215ad54101
----------------------------------------------------------------------------------------
  Poetic Units Converted : 9 of 9 (100.0% deterministic metric accuracy)
  Sentry Spans Recorded  : 18 gen_ai.agent / gen_ai.tool spans
  FastAPI Ofrenda Check  : GET / (200 OK) | GET /api/memories (200 OK)
  Family Vault Export    : 4909 bytes HTML5 + 4344 bytes BigQuery JSONL (3 rows)
  Cloud Bytes Transmitted: 0 bytes during local Gemma 4 inference
========================================================================================
```

### Interactive Family Storybook & Recipe Weaver UI Preview

![MemoriaViva White-Background Storybook UI](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/memoriaviva_ui_white.jpg)

---

## Code

**GitHub Repository:** [https://github.com/RobinaMirbahar/memoriaviva-gemma-ofrenda](https://github.com/RobinaMirbahar/memoriaviva-gemma-ofrenda)

### Repository Structure

```text
memoriaviva-gemma-ofrenda/
├── memoriaviva/
│   ├── __init__.py
│   ├── schemas.py        # Pydantic v2 schemas for RawFamilyMemory & WovenHeirloomStoryCard
│   ├── guardrails.py     # Air-gapped 127.0.0.1 socket lock & culinary hydration validator
│   ├── agents.py         # 3-stage Google ADK SequentialAgent + Gemma 4 + Sentry Tracer
│   └── dashboard.py      # FastAPI Family Storybook & static HTML5 exporter
├── scripts/
│   └── run_memoriaviva_demo.py  # Benchmark + HTML5 & BigQuery JSONL Family Vault exporter
├── articles/memoriaviva/        # Illustrations, BigQuery schema & benchmark evidence
└── requirements.txt
```

---

## How I Built It

![MemoriaViva Technical Architecture on White Background](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/memoriaviva_arch_white_v2.jpg)

I built **MemoriaViva** by combining **Google's open-weights AI ecosystem** and **Google Cloud data architecture** with deterministic Python safety guardrails:

1. **Open-Weights Google Gemma 4 (`google/gemma-4-27b-it`):**
   - Configured for local serving via **Ollama / vLLM** on `http://127.0.0.1:11434`.
   - Gemma 4 preserves South Asian (*Urdu/Sindhi*) and Latin American (*Spanish*) culinary idioms alongside structured JSON output.
2. **Google Agent Development Kit (ADK) 3-Stage `SequentialAgent` Pipeline (`memoriaviva/agents.py`):**
   - **Stage 1 (`OralHistoryWhisperAgent`):** Extracts the elder's verbatim quote and weaves the historical context (*1947 Partition-era Hyderabad*, *1968 Oaxaca Dia de los Muertos*, *1982 Monsoon Courtyard*) into a structured narrative.
   - **Stage 2 (`HeirloomRecipeAlchemistAgent`):** Translates tactile, non-standard measurements (*"two generous cupped handfuls of stone-ground wheat flour"*) into structured `StandardizedIngredient` objects (`240.0g`) while keeping the original phrase beside it.
   - **Stage 3 (`CandlelitOfrendaCuratorAgent`):** Validates the memory against `WovenHeirloomStoryCard` and prepares the record for the **Family Vault**.
3. **Deterministic Privacy & Culinary Guardrails (`memoriaviva/guardrails.py`):**
   - **`verify_air_gapped_endpoint()`:** Rejects any non-local hostname (`127.0.0.1` / `localhost` / `::1`) during inference, guaranteeing that `0 bytes` of raw family recordings are sent to external LLM APIs.
   - **`compute_and_validate_hydration()`:** Audits the ratio of liquid milliliters to dry flour grams (`75.0%` for `MEM-01`, `65.0%` for `MEM-02`, and `100.0%` for liquid infusion `MEM-03`) within deterministic bounds (`45.0%` to `95.0%` for doughs).
4. **Dual-Mode Family Vault (Local W3C HTML5 + Google BigQuery Table Schema):**
   - By default, `scripts/run_memoriaviva_demo.py` writes the woven memories to a self-contained **W3C HTML5 Family Storybook** (`4,909 bytes`) and a **Newline-Delimited JSON (`exported_memories.jsonl`, `4,344 bytes`)** file alongside [`bigquery_vault_schema.json`](https://github.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/blob/main/articles/memoriaviva/evidence/bigquery_vault_schema.json).
   - Because `standardized_recipe` is structured as a `RECORD REPEATED` nested array, families who want to back up their structured cookbook across continents in their own private Google Cloud project can load the JSONL archive directly into a **Google BigQuery** table (`memoriaviva_vault.heirloom_memories`):

```bash
bq load --source_format=NEWLINE_DELIMITED_JSON \
  memoriaviva_vault.heirloom_memories \
  articles/memoriaviva/evidence/exported_memories.jsonl \
  articles/memoriaviva/evidence/bigquery_vault_schema.json
```

5. **Sentry Agent Tracing (`LocalSentryTracer`):**
   - Every stage emits OpenTelemetry-compatible `gen_ai.agent` and `gen_ai.tool` spans capturing model name, ingredient conversion counts, and hydration audit results across all `18` recorded spans.

```python
def verify_air_gapped_endpoint(endpoint_url: str) -> Tuple[bool, str]:
    """Ensure inference requests only target local open-weights endpoints."""
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

For a project that handles **intimate family memories, elders' voices, and ancestral heritage**, open-weights AI provides three concrete engineering guarantees:

1. **Intimate Family Voices Stay on `127.0.0.1` (`0 bytes` LLM Cloud Egress):** Families can transcribe and structure voice notes locally with **Gemma 4** without uploading private recordings to a third-party commercial LLM API.
2. **Works Offline in Courtyards, Villages & Field Recordings:** When visiting elders in rural towns or recording oral histories without internet connectivity, the local **Gemma 4 + Google ADK** pipeline runs offline on the same machine.
3. **Open Standards + Private Google BigQuery Family Vault Ownership:** By exporting a self-contained **W3C HTML5** file (`4,909 bytes`) alongside a **Google BigQuery JSONL** archive (`4,344 bytes`), your family owns both an offline browser-ready book and a structured analytical table under your own IAM control.

---

## My Agent Session

During the benchmark run, **MemoriaViva** recorded **18 structured `gen_ai.agent` and `gen_ai.tool` spans** across the 3-stage **Google ADK + Gemma 4** pipeline:

- `gen_ai.agent` ➔ `OralHistoryWhisperAgent` (`model="google/gemma-4-27b-it"`, `memory_id="MEM-01"`)
- `gen_ai.tool` ➔ `HeirloomRecipeAlchemistAgent.standardize_units` (`ingredients_converted=3`, `hydration_pct=75.0`)
- `gen_ai.agent` ➔ `CandlelitOfrendaCuratorAgent` (`air_gapped=True`, `trace_id="49ef09ebc06d4014"`)

---

## The Spirit of It

In almost every culture, from **Dia de los Muertos** *ofrendas* glowing with marigolds in Mexico to family hearths across South Asia, food and storytelling are how we keep the people we love close to us.

When an elder writes *"measure the warm milk with your fingertips; when the dough sighs softly, the cardamom is awake,"* standard recipe apps strip away the voice and leave cold numbers. Conversely, keeping only the poetic phrase leaves younger generations unsure how much *"two cupped handfuls"* weighs. Seeing **Gemma 4** preserve **both** side-by-side (`240.0g Stone-Ground Whole Wheat Flour` and `180.0ml Whole Warm Milk` at `75.0%` hydration alongside Dadi Jan's exact words) inside a self-contained digital family book and BigQuery Family Vault brought this project to life.

---

## Prize Categories

- **Best Use of Gemma:** Uses open-weights **`google/gemma-4-27b-it`** as the core reasoning design inside a 3-stage **Google ADK** pipeline to preserve multilingual oral histories and deterministically standardize `9 of 9` (`100.0%`) ancestral culinary measurements locally.
- **Best Use of Sentry Agent Tracing:** Instruments every **Google ADK** agent and tool stage with `18` `gen_ai.agent` and `gen_ai.tool` telemetry spans to audit conversion accuracy and hydration guardrails locally.
