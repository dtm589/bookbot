from collections import Counter

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    # print(file_contents)

    def count_words():
        words = file_contents.split()
        print(f"{len(words)} words found in the document.")

    def count_letters():
        # conver to lower case
        lower_case = file_contents.lower()
        
        print(dict(Counter(lower_case)))

    print("--- Begin report of books/frankenstein.txt ---")
    count_words()
    count_letters()
    print("--- End report ---")