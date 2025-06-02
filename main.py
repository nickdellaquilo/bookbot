from stats import num_words, char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    print(str(num_words) + " words found in the document")
    char_dict = char_count(text)
    print("Count of characters: " + str(char_dict))

main()