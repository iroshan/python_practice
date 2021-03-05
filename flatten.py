def flatten(lst):
    """returns flattened lst (one level deep) """
    return [item for sub in lst for item in sub]


print(flatten([[1,2,3], [4,5]]))
