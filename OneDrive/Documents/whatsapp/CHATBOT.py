from transformers import AutoModelForCausalLM, AutoTokenizer

def chatbot_response(user_input):
    model_name = "gpt2"  # Replace with a valid model like "gpt2"
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    inputs = tokenizer.encode(user_input, return_tensors='pt')
    outputs = model.generate(inputs, max_length=50)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(response)
    return response
