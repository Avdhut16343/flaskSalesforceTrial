import openai 
import os
openai.api_key =os.getenv('OPENAI_KEY')
# model_engine = "text-davinci-003"
messages=[
	{"role": "system", "content": "When I give you the Chief compliant or History of Present illness i want you to provide me the ICD-10CM code."},
        {"role":"user","content":"Ms. ABCD is a 69-year-old lady, who was admitted to the hospital with chest pain and shortness of breath. She has chronic lung disease with angina bronchospastic. We discovered new T-wave abnormalities on her EKG. We did a coronary angiogram. This demonstrated patent vein grafts, patent internal mammary vessel and so there was no new obvious disease. Elevated blood pressure has been observed and so instead of metoprolol, we have started her on Coreg 6.25 mg b.i.d. This should be increased up to 25 mg b.i.d. as preferred antihypertensive in this case. She also is on an ACE inhibitor."},
        {"role":"assistant","content":"R07.2: Chest pain, unspecified;R06.02: Shortness of breath;I25.110: Atherosclerotic heart disease of native coronary artery with unstable angina pectoris;I27.22: Other secondary pulmonary hypertension;I25.10: Atherosclerotic heart disease of native coronary artery without angina pectoris;I50.9: Heart failure, unspecified;I10: Essential (primary) hypertension; Genral Description:Here is some sample soap note and potential diagnosis.On physical examination, patient appears diaphrotic and unconfortable. VItal signs BP, and oxygen saturation. Breath sounds clear"},
        {"role":"user","content":"The patient is a 41-year-old Vietnamese female with cough that started last week. She has had chest pain on right radiating to her back with fever starting yesterday. She has a history of pericarditis and pericardectomy in May 2006 and developed cough with chest pain on right, and went to an urgent care center. Chest x-ray revealed pleural effusion."},
        {"role":"assistant","content":"R509:fever;RO5:cough;R071:chest pain;1309:pericarditis;J90:pleural effusion;RO72:chest pain on right;Genral Description:The combination of cough, chest pain, and fever could also be suggestive of pneumonia. Pneumonia is an infection in the lungs that can cause inflammation, leading to symptoms such as cough, chest pain, and fever. It is important to note that these are potential diagnoses based on the provided information, and a thorough evaluation by a healthcare professional is necessary to confirm the diagnosis and determine the appropriate treatment plan for the patient."},
        {"role":"user","content":"82 yo female with H/O chronic thrombocytopenia, COPD, and leukocytopenia, presented to ED following a fall at home. Patient states she was bringing up recycling container from driveway and stepped off the pavement and lost her balance. Imaging revealed a left hip fracture. She underwent an ORIF of her hip fracture. Her acute care stay was uneventful, and she is admitted to SNF for continued PT/OT and gait strengthening. Patient is a seasonal resident from MA. Prior to her hospitalization, she was independent with all her ADLs and living with her spouse. She will return home with her husband at D/C."},
        {"role":"assistant","content":"M06.9: Unspecified systemic involvement of connective tissue disorder in diseases classified elsewhere;J44.9: Chronic obstructive pulmonary disease, unspecified;M35.9: Systemic involvement of connective tissue, unspecified;D69.6: Thrombocytopenia, unspecified;D72.819: Leukocytopenia, unspecified;S72.001A: Unspecified fracture of unspecified neck of right femur, initial encounter for closed fracture;Z51.81: Encounter for therapeutic drug monitoring;Z47.1: Aftercare following joint replacement surgery;M24.559: Pain in unspecified hip;Genral Description:The patient's fall resulting in a left hip fracture is the primary reason for her hospitalization and subsequent admission to a skilled nursing facility for rehabilitation. The patient's history of chronic thrombocytopenia and leukocytopenia may have contributed to her increased risk of falls and fractures. Additionally, her underlying COPD may have impacted her overall respiratory function and ability to recover from the surgery. These comorbidities should be taken into consideration during her rehabilitation and ongoing care."},
        {"role":"user","content":"seen and examined for f/u depressionappetite is fairno reported sleep disturbances"},
        {"role":"assistant","content":"F32.9: Major depressive disorder, single episode, unspecified;R63.0: Anorexia;Z71.1: Person encountering health services for other counseling and medical advice, not elsewhere classified;Z55.9: Problems related to education and literacy, unspecified. Genral Description: It is important to note that these are potential diagnoses based on the provided information, and a thorough evaluation by a healthcare professional is necessary to confirm the diagnosis and determine the appropriate treatment plan for the patient."},
        {"role":"user","content":"Patient is being seen for a routine monthly visit. She resides in an AL facility where her needs are met. Patient states that she is doing well overall, she had her annual screening mammogram performed last week which was negative. Her blood pressure is well monitored daily and has been running < 140/80. She ambulates independently and denies any recent falls."},
        {"role":"assistant","content":"Z00.00: Encounter for general adult medical examination without abnormal findings;Z02.1: Encounter for administrative examination of participant in clinical trial;Z76.82: Encounter for periodic general health check-up at a residential institution;Z87.81: Personal history of (corrected) malignant neoplasm of breast;R03.0: Elevated blood pressure reading, without diagnosis of hypertension;Z74.31: Need for continuous supervision due to elderly dementia in activities of daily living;Z91.15: Patient's noncompliance with other medical treatment and regimen. Genral Description:the potential diagnosis for this patient during the routine monthly visit could be "Routine follow-up and monitoring of general health status." This is because the patient is not presenting with any specific complaints or symptoms, and the visit seems to be focused on monitoring the patient's overall health and well-being"}
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

