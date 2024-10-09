from pdfminer.high_level import extract_text


def count_word_in_pdf(pdf_path):
    text = extract_text(pdf_path)
    
    words=text.split()
    
    word_count= len(words)
    
    return word_count


pdf_path="Lab task 06 - Stack.pdf"

total_words=count_word_in_pdf(pdf_path)

print(f"Total number of words:",{total_words})