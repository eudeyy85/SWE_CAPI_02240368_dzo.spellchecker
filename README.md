# Dzongkha Spell Checker

## Project Overview
I created a spelling checker for the Dzongkha language. The program reads a Dzongkha text file (dictionary.txt) that contains spelling errors which was provided by the tutor. This program identify the english text and clear it and also dectects the spelling error in the dzongkha text.

## Table of Contents
-[Usage](#usage)
-[Implementation Details](#implementation-details)
-[Data Structures](#data-structures)
-[Algorithms](#algorithms)
-[Challenges and Solutions](#challenges-and-solutions)
-[Future Improvements](#future-improvements)
-[References](#references)

## Usage
-Specifies the input and output file paths and calls the clean_dictionary function with the specified file paths.
-The code provides a basic approach to identifying potentially incorrect words based on the dictionary. 

'''bash
python dzongkha_spell_checker.py input_file.txt
'''

## Implementation Details
The code effectively cleans a dictionary file by extracting the first word from each line and saving it in new file. It handles utf-8 encoding to ensure correct character for dzongkha text.
The code provides clear feedback by printing a message upon successful completion and effectively identifies words and errors.

## Data Structures
-List
-File Object
-String
-Set

## Algorithms
1. Regular Expressions: the code utilizes the re module and regular expression.
2. Set Operations: the code show the difference method on sets to identify words that are present in a set but not the other.
3. Looping : the code iterates through the elements of the unique_to_file1 set using a for loop.
 

## Challenges and Solutions
- Didn't know what code to use to have the output the tutor wanted. However, watched lesson in YouTube, got help and learned from AI and got helped from those who knew.

## Future Improvements
-I now know how to correct the error and auto correct using the code which can be use in future need.
-Can generate dzongkha text using the cleaned dictionary ensuring grammatical correctness.
-Learned the splits the line and to writes each word followed by a newline, so taht each word appears on a new line in the output file.

## References
-https://gemini.google.com/app/2e5f55efa23440de
-https://app.penseum.com/solution/-11010b63-7ee4-4704-bffd-5ef6e1057fd9
-https://youtube.com/shorts/zaKrIcCtmF4?si=FB2LobTQHE6UDBrl
-https://youtu.be/IYIJmZhEiOc?si=vy0UdZD9oUOpixtS
chatgpt

