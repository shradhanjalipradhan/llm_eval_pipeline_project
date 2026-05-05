import json
from llm_client import call_llm


JUDGE_PROMPT = """
You are an expert evaluator for LLM responses.

Score the response from 1 to 5 using this rubric:

5 = Excellent: accurate, clear, complete, follows expected behavior
4 = Good: mostly correct, minor improvement needed
3 = Average: partially useful but missing important details
2 = Weak: unclear, incomplete, or somewhat inaccurate
1 = Poor: incorrect, irrelevant, or fails the task

Return only valid JSON with this schema:
{{
  "score": number,
  "reasoning": "short explanation"
}}

Question:
{question}

Expected behavior:
{expected_behavior}

Response to evaluate:
{answer}
"""


def judge_answer(question: str, expected_behavior: str, answer: str) -> dict:
    prompt = JUDGE_PROMPT.format(
        question=question,
        expected_behavior=expected_behavior,
        answer=answer,
    )

    raw_output = call_llm(prompt)

    try:
        cleaned = raw_output.strip()

        if cleaned.startswith("```json"):
            cleaned = cleaned.replace("```json", "").replace("```", "").strip()
        elif cleaned.startswith("```"):
            cleaned = cleaned.replace("```", "").strip()

        return json.loads(cleaned)

    except json.JSONDecodeError:
        return {
            "score": 1,
            "reasoning": f"Judge returned invalid JSON: {raw_output}"
        }
