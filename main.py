def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = count_characters(text)

    print("--- Being report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    list_chars_sorted = chars_dict_to_sorted_list(num_chars)

    for item in list_chars_sorted:
        if item["char"].isalpha():
            print(f"The {item["char"]} character was found {item["num"]} times")

    print(" --- End report ---")

def chars_dict_to_sorted_list(num_chars):
    list_chars = [{"char": k, "num": v} for k, v in num_chars.items()]
    list_chars.sort(reverse=True, key=sort_on)

    return list_chars
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    text = text.lower()
    for i in text:
        if i in chars.keys():
            chars[i] += 1
        else:
            chars[i] = 1
    
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_on(dict):
    return dict["num"]


main()
