from transformers import pipeline

summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    summary = summarization_pipeline(text, min_length=50, max_length=200)
    return summary[0]['summary_text']
