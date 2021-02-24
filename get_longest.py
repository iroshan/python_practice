import pathlib


def find_longest_word(file):
    """returns the longest word in file"""
    longest_word = ""
    with open(file, 'r', encoding='utf8') as f:
        for line in f:
            for word in line.strip().split():
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word


def find_all_longest_words(dir):
    """ returns a dictionary of the longest words for each file in the directory"""
    longest_word_for_file = {}
    try:
        for file in pathlib.Path(dir).iterdir():
            longest_word_for_file[file.name] = find_longest_word(file)
    except Exception as e:
        print(e)
    return longest_word_for_file


if __name__ == "__main__":
    dirname = input("enter file name: ")
    output = (find_all_longest_words(dirname))
    for k, v in output.items():
        print(f"{k}:\t{v}")
