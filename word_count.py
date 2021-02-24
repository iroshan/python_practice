def wordcount(filename):
    """print the number of chracters, words, lines and unique words """
    counts = {'characters': 0, 'words': 0, 'lines': 0}
    unique_words = set()

    for line in open(filename):
        counts['lines'] += 1
        counts['characters'] += len(line)
        counts['words'] += len(line.split())
        unique_words.update(line.split())

    counts['unique words'] = len(unique_words)
    for key, value in counts.items():
        print(f'{key}: {value}')


if __name__ == "__main__":
    try:
        filename = input("enter the filename: ")
        wordcount(filename)
    except Exception as e:
        print(e)
