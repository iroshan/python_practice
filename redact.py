import re

# This is my initial function.
# not case sensitive


def redact(write_file, word_file):
    # open the redact words list file and make a set of words
    with open(word_file, 'r') as f:
        word_list = set(f.read().lower().split())
    # open the file to replace
    with open(write_file, 'r+') as f:
        # read the file
        file_data = f.read()
        # replace each word in file if the word is in word_list
        for word in word_list:
            file_data = file_data.replace(word.lower(), '*'*len(word))
        f.truncate(0)
        f.write(file_data)


# This uses regex and case insensitive.
# issues:
# loads the file in to memory. read the entire file for each word.
# is there a better way?
def redact_ignore_case(write_file, word_file):
    with open(word_file) as f:
        word_list = set(f.read().lower().split())
    with open(write_file, 'r+') as f:
        file_data = f.read()
        for word in word_list:
            file_data = re.sub(word, '*'*len(word), file_data, flags=re.IGNORECASE)
            f.truncate(0)
            f.write(file_data)


def redact_to_file(read_file, word_file, write_file):
    with open(word_file) as f:
        word_list = set(f.read().lower().split())
    with open(read_file, 'r') as f:
        with open(write_file, 'w') as r:
            file_data = f.read()
            for word in word_list:
                file_data = re.sub(word, '*'*len(word), file_data, flags=re.IGNORECASE)
            r.write(file_data,)


def main():
    try:
        to_redact = input("enter file name to redact: ")
        words = input("enter the file name with the words to redact: ")
        write_file = input("enter a file name for redacted file. press enter to do in-place redaction: ")
        if write_file:
            redact_to_file(to_redact, words, write_file)
        else:
            redact_ignore_case(to_redact, words)
        print("redaction complete...")
    except Exception as e:
        print(f"error occured. \n{e}")



if __name__ == "__main__":
    main()
