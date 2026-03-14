# llm_client.py

from google import genai

def invoke_gemini(system_prompt, user_input):

    client = genai.Client(
        api_key="AIzaSyARaqkhIfGSGUOAuZniT0Kd2D1YN9YrLMw"
    )

    full_prompt = (
        system_prompt +
        "\n\nCustomer: " + user_input +
        "\nSupport:"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    return response.text
