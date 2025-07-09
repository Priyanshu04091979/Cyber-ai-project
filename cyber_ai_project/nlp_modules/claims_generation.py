from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")

claim = generator("Generate insurance claim for:", max_length=100)[0]['generated_text']
