from collections import defaultdict

def get_rainfall():
    """collect amount of rainfall for cities and print the summary"""
    # create the dict to collect data 
    # keeping the entered values in a list to use later.
    cities = defaultdict(list)
    while True:    
    # input for city name
        city = input("enter city name: ").lower().strip()
        # if input is empty break the loop and print the data
        if not city: 
            print("City \tRainfall")
            for city, values in cities.items():
                print(f"{city}\t{sum(values):>.2f}")
            break
        # if city name entered, add relevant value to dict as a float.
        else:
            value = input("enter the amount of rainfall: ")
            try:
                cities[city].append(float(value))
            except: # non numeric data
                print("invalid input. try again.")
                continue 
                   
 
if __name__ == "__main__":
    get_rainfall()
