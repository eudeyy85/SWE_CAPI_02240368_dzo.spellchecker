############

#Tshering Euden
#A
#02240368
#######################
#https://github.com/eudeyy85/SWE_CAPI_02240368_dzo.spellchecker.git
#REFERENCE
#https://gemini.google.com/app/2e5f55efa23440de
#https://app.penseum.com/solution/11010b63-7ee4-4704-bffd-5ef6e1057fd9
#https://youtube.com/shorts/zaKrIcCtmF4?si=FB2LobTQHE6UDBrl
#https://youtu.be/IYIJmZhEiOc?si=vy0UdZD9oUOpixtS
#chatgpt
#PROBLEM: # Problem
# docx.file can't be read
# inputfile is from online
# The dictionary has many unwanted characters
# Dzongkha words have different unicode code and gives wrong format
# white space when seperating the words 
# the word '་' cant act like white space and dilimiter
# everyword is compared, not the wanted words
#SOLUTION: 

#cleaning_dictionary 
def clean_dictionary(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        cleaned_words = [line.split()[0] for line in f if line.split()]
    with open(output_file, "w", encoding="utf-8") as f:
        for word in cleaned_words:
            f.write(word + "\n")
    print(f"Cleaned words saved to {output_file}")
input_file = "dictionary.txt"
output_file = "cleaned_dictionary.txt"
clean_dictionary(input_file, output_file)
#converter
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

print("file converted")
#Spell checker
import re
def checker(text):
    words = re.findall(r'[\u0F00-\u0FFF]+', text)
    unique_word = {word for word in words}  
    return unique_word
words = checker(open("368.txt", encoding="utf-8").read())
words1 = checker(open("cleaned_dictionary.txt", encoding="utf-8").read())
unique_file = words - words1
for word in unique_file:
    print(f"The word '{word}' from this sentence is incorrect.")