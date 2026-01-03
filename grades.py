dic = {"ashu" : 39, "deepesh": 40, "monish": 31}


def add_stud():
    try:
        s_name = input("enter name")
        s_mark = int(input("enter marks : "))
        if 0<= s_mark <= 100:
            dic[s_name] = s_mark
        else:
            print("add marks in correct range")
    except ValueError:
        print("Error: Invalid Input please write in integer")


def view_stud(dic):
    for name in dic:
        print(f"{name} : {dic[name]}")
    sum1 = sum(dic.values())
    print(len(dic))
    print(sum1)
    avg = sum1/len(dic)
    print(f"Average score: {avg} ")


while True:
    prompt = input("Enter the task: ")
    
    if prompt == "add":
        add_stud()
    elif prompt == "view":
        view_stud(dic)
    elif prompt == "exit":
        break
        
    