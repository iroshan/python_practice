

def sum_inputs():
    total = 0
    while True:
        s = input("Please enter a number: ").strip()
        if not s:
            print(f"Final total is {total}. Exiting...")
            break
        try:
            s = float(s)
            if s.is_integer():
                total += int(s)
            else:
                total += s
        except ValueError:
            print("Not a number...")
        print(f"Running total is {total}")


sum_inputs()
