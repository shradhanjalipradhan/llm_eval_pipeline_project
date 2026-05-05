from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RESULTS_PATH = ROOT / "results" / "eval_results.csv"

df = pd.read_csv(RESULTS_PATH)

summary = (
    df.groupby("prompt_version")["judge_score"]
    .mean()
    .reset_index()
    .sort_values("judge_score", ascending=False)
)

print("\nPrompt Ranking:")
print(summary)

best_prompt = summary.iloc[0]["prompt_version"]
print(f"\nBest prompt version: {best_prompt}")
