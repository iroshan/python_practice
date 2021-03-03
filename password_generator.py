def password_generation(letters):
    def create_pass_gen(n):
        from random import choice
        return "".join(choice(letters) for _ in range(n))
    return create_pass_gen

if __name__ == "__main__":
    print("testing...")
    s = password_generation("abcde")
    print(s)
    print(s(5))
    print(s(10))
    print('calling with "abcABC123!@#"')
    m = password_generation("abcABC123!@#")
    print(m(5))
    print(m(10))
    

