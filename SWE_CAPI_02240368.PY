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
    cleaned_words = []
    with open(input_file, "r", encoding = "utf-8") as file:
        for line in file:
            words = line.split()
            if words:
                dzongkha_word = words[0]
                cleaned_words.append(dzongkha_word)
    with open(output_file, "w", encoding = "utf-8") as file:
        for word in cleaned_words:
            file.write(word + "\n")
        print(f"cleaned words saved to {output_file}")
input_file = "dictionary.txt"
output_file = "cleaned_dictionary.txt"
clean_dictionary(input_file, output_file)
#converter
import docx2txt as d2t

docx_file = 'dictionary.docx'
txt_file = 'dictionary.txt'

docx = d2t. process(docx_file)

file=open(txt_file, 'w', encoding='utf-8')
file.write(docx)
file.close()

print("file converted")
#Spell checker
import re
def extract_words(text):
  
    words = re.findall(r'[\u0F00-\u0FFF]+', text)
    return set(words)  
with open("368.txt", encoding="utf-8") as file:
    content1 = file.read()
    word1 = extract_words(content1)
with open("cleaned_dictionary.txt", encoding="utf-8") as file:
    content2 = file.read()
    word2 =extract_words(content2)
unique_to_file1 = word1.difference(word2)  
for word in unique_to_file1:
    print(f"The word '{word}' from this sentence is incorrect.")