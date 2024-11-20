import google.generativeai as genai

genai.configure(api_key="AIzaSyBi75WdmAtcV9qlyBYUb8mo_Xwxc_-DvY4")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Hello, World!")
print(response.text)