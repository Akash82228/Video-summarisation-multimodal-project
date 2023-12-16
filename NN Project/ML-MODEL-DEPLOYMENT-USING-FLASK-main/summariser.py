from transformers import BartTokenizer

def summarize_text(text, max_length=5000):
    """
    Generates a summary for the given text using a pre-trained model.

    Args:
        text (str): The text to be summarized.
        max_length (int): The maximum length of the input text for the model.

    Returns:
        str: The generated summary of the input text.
    """
    # Encode the input text using the tokenizer. The 'pt' indicates PyTorch tensors.
    inputs = tokenizer.encode(text, return_tensors="pt", max_length=max_length, truncation=False)
    
    # Move the encoded text to the same device as the model (e.g., GPU or CPU)
    inputs = inputs

    # Generate summary IDs with the model. num_beams controls the beam search width.
    # early_stopping is set to False for a thorough search, though it can be set to True for faster results.
    summary_ids = model.generate(inputs, max_length=2000, num_beams=30, early_stopping=False)

    # Decode the generated IDs back to text, skipping special tokens like padding or EOS.
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Return the generated summary
    return summary



























































tokenizer = BartTokenizer.from_pretrained('facebook/bart-base')
