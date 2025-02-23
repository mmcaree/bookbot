def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha:
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def output_results(dict, count, path):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------\nFound {count} total words\n--------- Character Count -------")
    sorted_dict = sorted(dict, key=dict.get, reverse=True)
    for letter in sorted_dict:
        if letter.isalpha():
            count = dict[letter]
            print(f"{letter}: {count}")
    print("--- End report ---")