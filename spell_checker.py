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
