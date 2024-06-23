from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

def answer_question(question, text):
    result = qa_pipeline(question=question, context=text)
    return result['answer']
