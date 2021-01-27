def redact(write_file, word_file):
    # open the redact words list file and make a set of words
    with open(word_file,'r') as f:
        word_list = set(f.read().lower().split())
    # open the file to replace
    with open(write_file,'r+') as f:
        # read the file
        file_data = f.read()
        # replace each word in file if the word is in word_list
        for word in word_list:
            file_data = file_date.replace(word, '*'*len(word))
        f.truncate()