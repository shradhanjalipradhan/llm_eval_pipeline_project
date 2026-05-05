# LLM Eval Pipeline: Prompt Comparison + LLM-as-Judge

A lightweight evaluation pipeline that compares multiple prompts across a test dataset and scores responses using an LLM-as-judge.

## What this project shows

- Prompt evaluation
- LLM-as-judge scoring
- Prompt comparison
- Structured outputs
- Production-style logging
- Reusable AI engineering workflow

## Architecture

```text
eval_dataset.json
      |
      v
run_eval.py
      |
      +--> generate answer from Prompt A
      +--> generate answer from Prompt B
      |
      v
judge.py scores each answer
      |
      v
results/eval_results.csv
```

## Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Run

```bash
python src/run_eval.py
```

## Output

The pipeline creates:

```text
results/eval_results.csv
```

Each row includes:

- input question
- expected behavior
- prompt version
- model response
- judge score
- judge reasoning

## Resume Bullet

Built a lightweight LLM evaluation pipeline using Python, prompt versioning, and LLM-as-judge scoring to compare prompt quality, automate response evaluation, and generate structured CSV reports for model iteration.

## LinkedIn/GitHub Positioning

This project demonstrates how AI teams evaluate prompt quality before shipping LLM features to production.
