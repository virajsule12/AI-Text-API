from openai import OpenAI
from config import OPENAI_API_KEY
from openai import RateLimitError, OpenAIError

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_text(text: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Summarize the following text in one concise sentence."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
    except RateLimitError:
        raise Exception("AI service temporarily unavailable")
    except OpenAIError as e:
        raise Exception(f"OpenAI error: {str(e)}")

def classify_text(text: str, labels: list[str]) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Classify the text into one of these labels: {labels}. Return JSON with label and confidence."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
    except RateLimitError:
        raise Exception("AI service temporarily unavailable")
    except OpenAIError as e:
        raise Exception(f"OpenAI error: {str(e)}")
