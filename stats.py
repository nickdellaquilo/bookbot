def num_words(text):
    return len(text.split())

def char_count(text):
    char_dict = {}
    for c in text.lower():
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sorted_char_count(unsorted_dict):
    return dict(sorted(unsorted_dict.items(), key=lambda item: item[1], reverse=True))