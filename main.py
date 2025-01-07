total_words = 0

def count_characters(string):
    "Count characters, return dict"
    chars_map = {}
    for word in string.lower().split():
        for char in word:
            if char.isalpha():
                if char not in chars_map:
                    chars_map[char] = 0
                chars_map[char] += 1
    return chars_map

def count_words(string):
    return len(string.split())

def read_file(fpath):
    with open(fpath, "r") as f:
        return f.read()


def main():
    text = read_file("books/frankenstein.txt")
    total_words = count_words(text)
    chars_count = count_characters(text)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} found in the document")
    print()

    sorted_chars = sorted(chars_count.items(), key=lambda p: p[1], reverse=True)
    for k, v in sorted_chars:
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")
    return

main() if __name__ == "__main__" else None

