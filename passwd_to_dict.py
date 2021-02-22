def passwd_to_dict(f):
    """ returns username and userid from a passwd file f"""
    output = {}
    for line in open(f):
        if not line.startswith(('#', '\n')):
            fields = line.strip().split(":")
            output[fields[0]] = [fields[2]]
    return output


if __name__ == "__main__":
    from pprint import pprint
    file_name = input("Enter the filename: ")
    try:
        pprint(passwd_to_dict(file_name))
    except Exception as e:
        print(e)
