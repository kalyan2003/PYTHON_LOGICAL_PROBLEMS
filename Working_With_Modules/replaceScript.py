
import sys

def replace_words(filename, word, replace_word):
    try:
        with open(filename, "r") as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return

    if word in data:
        data = data.replace(word, replace_word)
        with open(filename, "w") as file:
            file.write(data)
        print(f"Replaced '{word}' with '{replace_word}' in {filename}.")
    else:
        print(f"'{word}' not found in {filename}.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <filename> <word> <replace_word>")
        sys.exit(1)
        replace_words(sys.argv[1], sys.argv[2], sys.argv[3])