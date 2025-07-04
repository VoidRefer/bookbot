
def get_num_words(text: str):
    return len(text.split())

def count_chars(text: str):
    char_counter = {}
    for character in text:
        character = character.lower()
        char_counter[character] = char_counter.get(character, 0) + 1
    return char_counter

def sort_chars_dict(dictionary):

    chars = [
        {"char": char, "num": num} for char, num in dictionary.items()
    ]
    chars.sort(reverse = True, key=lambda k: k["num"])
    
    return chars