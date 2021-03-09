def get_sv(f):
    """returns the list of supervocalic words in file f"""
    return {word.strip() for word in open(f) if set(list("aeiou")).issubset(set(word.lower()))}
 

print(get_sv("words.txt"))
