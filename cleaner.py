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
