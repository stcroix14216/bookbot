import sys

from stats import word_count
from stats import character_counts
from stats import character_sort

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        ptf = sys.argv[1]  

    text = get_book_text(ptf)
    num_words = word_count(text)
    num_character = character_counts(text)
    sorted_characters = character_sort(num_character)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {ptf}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_characters:
        ch = entry["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {entry['num']}")

def get_book_text(ptf):
    with open(ptf) as f:
        return f.read()

main()

