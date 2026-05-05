import json
from pathlib import Path
import pandas as pd

from prompts import PROMPTS
from llm_client import call_llm
from judge import judge_answer


ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = ROOT / "data" / "eval_dataset.json"
RESULTS_DIR = ROOT / "results"
RESULTS_PATH = RESULTS_DIR / "eval_results.csv"


def load_dataset() -> list[dict]:
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def run_eval() -> pd.DataFrame:
    dataset = load_dataset()
    rows = []

    for item in dataset:
        question = item["question"]
        expected_behavior = item["expected_behavior"]

        for prompt_name, prompt_template in PROMPTS.items():
            final_prompt = prompt_template.format(question=question)

            answer = call_llm(final_prompt)

            judge_result = judge_answer(
                question=question,
                expected_behavior=expected_behavior,
                answer=answer,
            )

            rows.append({
                "id": item["id"],
                "question": question,
                "expected_behavior": expected_behavior,
                "prompt_version": prompt_name,
                "answer": answer,
                "judge_score": judge_result.get("score"),
                "judge_reasoning": judge_result.get("reasoning"),
            })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    RESULTS_DIR.mkdir(exist_ok=True)

    df = run_eval()
    df.to_csv(RESULTS_PATH, index=False)

    print(f"Evaluation complete. Results saved to: {RESULTS_PATH}")
    print(df.groupby("prompt_version")["judge_score"].mean().sort_values(ascending=False))
