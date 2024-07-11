from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def main():
    # Load the tokenizer and the sequence-to-sequence model
    tokenizer = AutoTokenizer.from_pretrained('t5-small')
    model = AutoModelForSeq2SeqLM.from_pretrained('t5-small')

    # Prepare the text input
    text = "Translate English to French: Hello, how are you my friend ?."
    input_ids = tokenizer.encode(text, return_tensors='pt')  # 'pt' for PyTorch tensors

    print("\n" + "INPUT TEXT :::: " + text + "\n")

    print("\n" + "INPUT TOKENS :::: " + str(input_ids[0]) + "\n")

    # Generate the output
    outputs = model.generate(input_ids, max_length= 60)

    print("OUTPUT TOKENS :::: " + str(outputs) + "\n")

    # Decode and print the output
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("OUTPUT TEXT ::::" + result + "\n")

if __name__ == "__main__":
    main()
