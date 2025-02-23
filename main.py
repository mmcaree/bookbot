from stats import get_num_words, get_chars_dict, output_results
import sys as s

def main():
    if len(s.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        s.exit(1)
    book_path = s.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    output_results(chars_dict, num_words, book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()