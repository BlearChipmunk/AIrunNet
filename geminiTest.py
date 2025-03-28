"""
Para instalar las librerías de gemini, usa el siguiente comando:
pip install -q -U google-genai

Para obtener tu API Key, visita:
https://aistudio.google.com/app/apikey
"""

from google import genai

client = genai.Client(api_key="TU API")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)