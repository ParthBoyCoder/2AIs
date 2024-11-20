import google.generativeai as genai

convoLines=5

def AI1(pmt):
    genai.configure(api_key="AIzaSyBi75WdmAtcV9qlyBYUb8mo_Xwxc_-DvY4")

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(pmt)
    return response.text

def AI2(pmt):
    genai.configure(api_key="AIzaSyB-Tc04NNO_BcV84JhdJy3BdEi2fsraK08")

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(pmt)
    return response.text

for i in range(convoLines):
    if i==0:
        tmp=AI1("You will be talking to another AI. In the otput, give your first conversation starter. Act like he is your friend.")
    else:
        tmp=AI1(tmp)

    print(tmp)

    tmp=AI2(tmp)

    print(tmp)