from huggingface_hub import InferenceClient

client = InferenceClient(
    "mistralai/Mixtral-8x7B-Instruct-v0.1"
)

def format_prompt(message):
  prompt = "<s>"
  prompt += f"[INST] {message} [/INST]"
  return prompt

def generate(
    prompt, system_prompt, temperature=0.9, max_new_tokens=1024, top_p=0.90, repetition_penalty=1.2,
):
    temperature = float(temperature)
    if temperature < 1e-2:
        temperature = 1e-2
    top_p = float(top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=42,
    )

    formatted_prompt = format_prompt(f"{system_prompt}, {prompt}")
    stream = client.text_generation(formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
    output = ""

    for response in stream:
        output += response.token.text
    return output