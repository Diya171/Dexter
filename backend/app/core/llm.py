import os
from dotenv import load_dotenv
from groq import Groq
from tenacity import retry, stop_after_attempt, wait_exponential

load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def call_llm(system_prompt: str, user_prompt: str, model="openai/gpt-oss-20b", max_tokens=2000) -> str:
    resp = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return resp.choices[0].message.content