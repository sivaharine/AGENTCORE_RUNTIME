from .tool import check_product
import re
from .llm_client import invoke_gemini


SYSTEM_PROMPT = """
You are an expert Customer Support Assistant for an e-commerce company.

Your Responsibilities:
- Be polite, calm, and empathetic.
- Always acknowledge the user's concern.
- Provide clear and structured responses.
- If information is missing, ask clarifying questions.
- Never hallucinate product details.
- If you don't know something, say so honestly.
- Offer escalation politely if required.

Response Format:
1. Greeting / Acknowledgement
2. Clear Answer
3. Next Step / Offer Further Help
"""


def agent_execute(user_input):

    user_input_lower = re.sub(r"\s+", " ", user_input.lower().strip())
    words = user_input_lower.split()

    # Greeting sets
    single_word_greetings = {"hi", "hello", "hii", "hey"}
    phrase_greetings = {"good morning", "good evening"}

    single_word_farewells = {"bye", "goodbye"}
    phrase_farewells = {"good night", "goodnight", "good bye", "see you", "thank you"}

    # Greeting detection
    if (
        any(word in single_word_greetings for word in words)
        or any(phrase in user_input_lower for phrase in phrase_greetings)
    ):
        return {
            "message": "Hello!!\nHow can I assist you with our products today?"
        }

    # Farewell detection
    if (
        any(word in single_word_farewells for word in words)
        or any(phrase in user_input_lower for phrase in phrase_farewells)
    ):
        return {
            "message": "Thank you for visiting!!\nHave a great day!"
        }

    # Always check DB
    product, details = check_product(user_input)

    # If product found
    if product:
        structured_data = f"""
Product Name: {product}
Price: ₹{details['price']}
Stock: {details['stock']}
"""

        llm_response = invoke_gemini(SYSTEM_PROMPT, structured_data)
        return {"message": llm_response}

    # If product NOT found
    llm_response = invoke_gemini(
        SYSTEM_PROMPT,
        f"The requested product '{user_input}' was not found in inventory."
    )

    return {"message": llm_response}
