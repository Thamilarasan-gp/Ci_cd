import google.generativeai as genai

genai.configure(api_key="AIzaSyA85RfCX9b2kghHJ5mkunPEr-N5gEXHUx4")

model = genai.GenerativeModel("models/gemini-2.5-flash")

response = model.generate_content(
    "Explain CI/CD in one sentence."
)

print(response.text)