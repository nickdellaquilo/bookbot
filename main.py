from stats import num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print(str(num_words(get_book_text("books/frankenstein.txt"))) + " words found in the document")

main()