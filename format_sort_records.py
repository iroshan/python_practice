def format_sort_records(data):
    """Print the dictionay data,
        sorted by last name
        time formatted with a precision  of two. """
    # sorting by last name
    data.sort(key=lambda x: [x[1]])
    # for each field print second field,first field, and third field respectively.
    for item in data:
        print("{1:10} {0:10}{2:10.2f}".format(*item))



if __name__ == "__main__":
    # testing the function
    PEOPLE = [('Joe', 'Biden', 7.85), ('Vladimir', 'Putin', 3.626), ('Jinping', 'Xi', 10.603)]
    format_sort_records(PEOPLE)
