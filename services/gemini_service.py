from google import genai
from config.settings import GEMINI_API_KEY, MODEL_NAME
from utils.logger import logger

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_response(prompt):
    try:
        logger.info("Calling Gemini API")

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        logger.info("Gemini API success")
        return response.text

    except Exception as e:
        logger.error(f"Gemini API Error: {str(e)}")
        return "⚠️ Financial advisor is temporarily unavailable."