def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letters = count_letters(text)
    build_report(book_path, word_count, letters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters_dict = {}
    lowered_text = text.lower()
    for character in lowered_text:
        if character in letters_dict:
            letters_dict[character] += 1
        else: 
            letters_dict[character] = 1

    return letters_dict

def get_alpha_letters(letters_dict):
    new_dict = {}
    for letter in letters_dict:
        if letter.isalpha():
            new_dict[letter] = letters_dict[letter]
    return new_dict

def list_of_dicts(dict):
    new_list = []
    for d in dict:
        new_list.append({"letter": d, "count": dict[d]}) 
    return new_list

def sort_on(dict):
    return dict["count"]

def build_report(path, word_count, letters_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    alpha_letters = get_alpha_letters(letters_dict)
    alpha_list = list_of_dicts(alpha_letters)
    alpha_list.sort(reverse=True, key=sort_on)

    for char in alpha_list:
        print(f"The '{char["letter"]}' was found {char["count"]} times")
    print("--- End report ---")


    

main()

