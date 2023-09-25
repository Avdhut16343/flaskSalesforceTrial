import openai 
import os
openai.api_key =os.getenv('OPENAI_KEY')
# model_engine = "text-davinci-003"
messages=[
        {"role": "system", "content": "When I give you the Chief compliant or History of Present illness i want you to provide me the ICD-10CM code.Give a detailed explanation as to why you think these are the problems with this patient\n Also provide a list of ICD10 diagnosis codes for any diagnosis you may detect"},
        {"role": "user", "content": "A patient is 70 years old compained with chest pain and has high body temperature."},
        {"role":"assistant","content":"Here is some sample soap note and potential diagnosis.On physical examination, patient appears diaphrotic and unconfortable. VItal signs BP, and oxygen saturation. Breath sounds clear.ICD-10CM list is I21.9 :Chest pain especialy when it radiate down the left arm can be indicative.;R07.2: Chest pain, unspecified;R06.02: Shortness of breath;I25.110: Atherosclerotic heart disease of native coronary artery with unstable angina pectoris;"},
	{"role": "user", "content": "The patient is a 41-year-old Vietnamese female with cough that started last week. She has had chest pain on right radiating to her back with fever starting yesterday. She has a history of pericarditis and pericardectomy in May 2006 and developed cough with chest pain on right, and went to an urgent care center. Chest x-ray revealed pleural effusion."},
        {"role":"assistant","content":"Based on the patient's symptoms and findings, a potential diagnosis for this patient could be pneumonia with pleural effusion.The patient's complaint of chest pain radiating to her back could be attributed to the underlying pneumonia and pleural effusion. It is important to note that these are potential diagnoses based on the provided information, and a thorough evaluation by a healthcare professional is necessary to confirm the diagnosis and determine the appropriate treatment plan for the patient. ICD-10CM list is J18.9 : Pneumonia, unspecified organism ;J86.9 : Pyothorax without fistula;J86.9 : Pyothorax without fistula"} 
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

