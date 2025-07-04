import sys

from stats import count_chars, get_num_words, sort_chars_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    text = get_book_text(file_path)
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")

    for item in sort_chars_dict(count_chars(text)):
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
        
    print("============= END ===============")
main()