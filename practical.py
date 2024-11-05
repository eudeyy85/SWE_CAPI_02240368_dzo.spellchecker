from docx import Document
def converter(docx_file, txt_file):
    doc = Document(docx_file)
    with open(txt_file, 'w', encoding='utf-8') as f:
        for para in doc.paragraphs:
            f.write(para.text + '\n')
docx_file = 'dictionary.docx'
txt_file = 'dictionary.txt'
converter(docx_file, txt_file)
print("The file has been converted")
