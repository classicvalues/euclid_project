from extract_text import extract_text_from_pdf
from question_answer import answer_question
from summarize_text import summarize_text

def main():
    pdf_path = 'pdfs/euclid_first_print_latin.pdf'
    
    # Extract text from PDF
    pdf_text = extract_text_from_pdf(pdf_path)
    
    # Example questions
    question = "What is Euclid's most famous work?"
    answer = answer_question(question, pdf_text)
    print("Question:", question)
    print("Answer:", answer)
    
    # Summarize the text
    summary = summarize_text(pdf_text)
    print("\nSummary:")
    print(summary)

if __name__ == "__main__":
    main()
