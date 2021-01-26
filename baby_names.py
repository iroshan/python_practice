import glob
from collections import Counter
# done with pydroid3 from phone. so didn't put error handling. will update
def analyze(f):
    male = set()
    female = set()
    file_list = glob.glob(f+"/*.txt")
 #   print(file_list)
    for file in file_list:
        with open(file) as file:
            names = Counter()
            for line in file:
               # print(line)
                name, count = line.split()
                names[name] = int(count)
                c_name=names.most_common(1)[0][0]
               # print(c_name)
                if "Girls" in file.name:
                    female.add(c_name)
                else:
                    male.add(c_name)
    return male, female      
                    

def main():
    f = input("Please enter the folder name: default=BabyNames :")
    if f:
        mail, femail = analyze(f)
    else:
        mail, femail = analyze("BabyNames")
    print("Most common names for boys")
    for name in mail:
        print(name)
    
    print("\nMost common names for girls")
    for name in femail:
        print(name)
    
main()
