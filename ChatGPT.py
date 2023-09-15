import openai 
import os
openai.api_key =os.getenv('OPENAI_KEY')
# model_engine = "text-davinci-003"
messages=[
        {"role": "system", "content": "Could you look at the below physician soap note and suggest what potential diagnosis could be associated with the patient. A patient is 70 years old compained with chest pain and has high body temperature \n Could you also provide a list of ICD10 diagnosis codes for any diagnosis you may detect. Give a detailed explanation as to why you think these are the problems with this patient"},
        {"role":"user","content":"Here is some sample soap note and potential diagnosis.On physical examination, patient appears diaphrotic and unconfortable. VItal signs BP, and oxygen saturation. Breath sounds clear. Based on patient history here are some icd10 codes Icd 10 Codes:i21.9 Explaination:Chest pain especialy when it radiate down the left arm can be indicative."} 
        ]
def generate_response(message):
    # completion = openai.Completion.create(
    #     engine=model_engine,
    #     prompt=prompt,
    #     max_tokens=1024,
    #     n=1,
    #     stop=None,
    #     temperature=0.5,
    # )
    # response = completion.choices[0].text.strip()
    # return response
    if message !='':
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", temperature = 0.1, messages=messages)
    response = chat.choices[0].message.content
    # print("ChatGPT:", reply)
    # messages.append({"role": "assistant", "content": reply})
    return response

