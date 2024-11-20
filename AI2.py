import google.generativeai as genai

genai.configure(api_key="key2")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("How are you?")
print(response.text)
