def run_timing():
    """ ask user to enter numeric inputs and print the average after a blank input """
    # make a total and count variables
    total, count = 0, 0
    while True:
        # get input
        run_time = input("Enter how long it took for you to run 10 km (Enter blank to continue): ")
        # exit the while loop, if no input entered.
        if not run_time:
            break
        if not run_time.isnumeric():
            print(f"{run_time} is not a valid input. Please try again.")
            continue
        # if there is input add it to the total and increment the counter.
        else:
            total += float(run_time)
            count += 1

    # print the results
    print(f"It took {total/count} minutes on average per run for all {count} your runs.")


def main():
    run_timing()


main()
