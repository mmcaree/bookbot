
def main():
    path_to_file = "/home/memcaree/dev/projects/bookbot/books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
    word_count = string_to_word_count(file_contents)
    char_dict = return_char_dict(file_contents)
    output_results(char_dict, word_count, path_to_file)

def string_to_word_count(text):
    word_list = text.split()
    word_count = 0
    for word in word_list:
        word_count += 1
    return word_count
    

def return_char_dict(text):
    letter_dict = {}
    for item in text:
        if item.isalpha():
            if item.isupper():
                item = item.lower()
                if item not in letter_dict:
                    letter_dict[item] = 1
                else:
                    curr_val = letter_dict[item]
                    curr_val += 1
                    letter_dict[item] = curr_val
            else:
                if item not in letter_dict:
                    letter_dict[item] = 1
                else:
                    curr_val = letter_dict[item]
                    curr_val += 1
                    letter_dict[item] = curr_val
        else:
            if item not in letter_dict:
                letter_dict[item] = 1
            else:
                curr_val = letter_dict[item]
                curr_val += 1
                letter_dict[item] = curr_val
    return letter_dict     
           
def output_results(dict, count, path):
    print(f"--- Begin report of {path} ---\n{count} words found in the document")
    sorted_dict = sorted(dict, key=dict.get, reverse=True)
    for letter in sorted_dict:
        if letter.isalpha():
            count = dict[letter]
            print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

main()

