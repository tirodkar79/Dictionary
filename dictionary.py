import json
from difflib import get_close_matches

data = json.load(open("F:/Pratham/Python/Python Projects/dictionary/data.json"))

def dict_search(search_word):

    word = search_word.lower()
    if word in data:
        return data[word]
    
    word = word.title()
    if word in data:
        return data[word]

    word = word.upper()
    if word in data:
        return data[word]

    result = get_close_matches(search_word, data.keys(), cutoff= 0.5)
    if len(result) != 0 :
        print("Did you mean ", end = "")
        print(*result, sep=", ", end="?\n")
        word = input("Enter: ")
        return dict_search(word)

    print("No such word in the dictionary. Please check the spelling again.")

def main():
    print("Welcome to the world of Dictionary")
    word = input("Enter the word whose meaning your are looking for..\t")

    meanings = dict_search(word)
    if meanings:
        index = 1
        for meaning in meanings:
            print(str(index) + ". " + meaning)
            index += 1


if __name__ == "__main__":
    main()