```markdown
# 🚀 LLM Evaluation Pipeline (Prompt Comparison + LLM-as-Judge)

A lightweight, production-style evaluation pipeline to compare multiple prompts and automatically score LLM responses using an LLM-as-judge.

Built to simulate how real AI teams evaluate prompt quality before deploying LLM features.

---

## 🔥 Key Features

- Prompt versioning (multiple prompt strategies)
- Automated evaluation using LLM-as-judge
- Structured scoring (1–5 scale with reasoning)
- CSV-based benchmarking output
- Model flexibility (Groq-based LLMs)
- Clean, modular pipeline design

---

## 🧠 Why This Matters

In real-world AI systems:
- Prompt quality directly impacts product performance  
- Manual evaluation doesn’t scale  
- Automated evaluation pipelines are critical for:
  - reliability  
  - regression detection  
  - continuous improvement  

This project replicates that workflow.

---

## ⚙️ Architecture

```

eval_dataset.json
↓
run_eval.py
↓
Prompt Variants → LLM Response Generation
↓
LLM-as-Judge Scoring (judge.py)
↓
results/eval_results.csv

```

---

## 📊 Sample Results

| Prompt Version        | Avg Judge Score |
|----------------------|----------------|
| prompt_v3_structured | 4.67           |
| prompt_v1_basic      | 3.33           |
| prompt_v2_role_based | 3.33           |

**Best performing prompt:** `prompt_v3_structured`

---

## 📁 Project Structure

```

llm_eval_pipeline_project/
│
├── data/
│   └── eval_dataset.json
│
├── src/
│   ├── prompts.py
│   ├── llm_client.py
│   ├── judge.py
│   ├── run_eval.py
│   └── analyze_results.py
│
├── results/
│   └── eval_results.csv
│
├── requirements.txt
├── README.md
└── .env.example

````

---

## 🛠️ Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
````

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Evaluation

```bash
python src/run_eval.py
```

Output:

```
results/eval_results.csv
```

---

## 📈 What This Project Demonstrates

* LLM evaluation workflows used in production
* Prompt engineering experimentation
* Automated scoring systems
* Model abstraction (provider flexibility)
* Data-driven prompt optimization

---

## 💡 Future Improvements

* Multi-model comparison (Groq vs OpenAI vs Claude)
* Latency + cost tracking
* Streamlit dashboard for visualization
* Prompt optimization loop
* A/B testing framework

---

## 🧾 Resume Bullet

Built an LLM evaluation pipeline with prompt comparison and automated LLM-as-judge scoring, enabling structured benchmarking and improving prompt performance analysis.

---

## 🎯 Positioning

This project demonstrates real-world AI engineering practices used in:

* LLM product development
* prompt optimization systems
* evaluation pipelines for production AI

---

## 📬 Author

Shradhanjali Pradhan
AI/ML & Data Engineering

```
```
