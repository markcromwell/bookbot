import sys
from stats import get_num_words, get_character_frequency, sort_char_frequency

def main ():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_file_name = sys.argv[1]
    book_text = get_book_text(book_file_name)
    num_words = get_num_words(book_text)
    character_frequency = get_character_frequency(book_text)
    sorted_freq = sort_char_frequency(character_frequency)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_name}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for freq in sorted_freq:
        if freq[0].isprintable():
            print(f"{freq[0]}: {freq[1]}")

    print("============= END ===============")



def  get_book_text (filepath):

    file_contents = ""

    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


main()