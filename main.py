import sys
from stats import num_words, char_count, sorted_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + filepath)
    print("----------- Word Count ----------")
    print("Found " + str(num_words(text)) + " total words in the document")
    print("--------- Character Count -------")
    sorted_char_dict = sorted_char_count(char_count(text))
    for key, val in sorted_char_dict.items():
        if(key.isalpha()):
            print(key + ": " + str(val))
    print("============= END ===============")

main()