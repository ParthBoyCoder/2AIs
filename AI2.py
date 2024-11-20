import google.generativeai as genai

genai.configure(api_key="AIzaSyB-Tc04NNO_BcV84JhdJy3BdEi2fsraK08")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("How are you?")
print(response.text)