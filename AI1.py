import google.generativeai as genai

genai.configure(api_key="key1")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Hello, World!")
print(response.text)
