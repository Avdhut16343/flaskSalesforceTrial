import openai 


# Ashish API
openai.api_key ="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"
model_engine = "text-davinci-003"

def generate_response(prompt):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text.strip()
    return response


