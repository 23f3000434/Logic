import json


def load_data():
    try:
        # 1. Try to open the file in 'Read' mode ('r')
        with open('data.json', 'r') as f:
            # 2. If file exists, load the JSON into a variable
            data = json.load(f)
            return data
    except FileNotFoundError:
        # 3. If file does NOT exist (First time running), return empty dict
        return {}


dic = load_data()

def add_stud():
    s_name = input("enter name: ")
    while True:
        try:
            s_mark = int(input(f"Enter marks for {s_name}: "))
            
            if 0 <= s_mark <= 100:
                dic[s_name] = s_mark
                print("Saved!")
                break  
            else:
                print("Error: Marks must be 0-100.") 
                   
        except ValueError:
            print("Error: Please enter a number.")
    with open('data.json', 'w') as f:
        json.dump(dic, f)
        
        
def view_stud(dic):
    with open('data.json', 'r') as f:
        data = json.load(f)
    # print('All data', data)
    for name in data:
        print(f"{name} : {data[name]}")
    sum1 = sum(data.values())
    # print(len(dic))
    # print(sum1)
    avg = sum1/len(data)
    print(f"Average score: {avg} ")
    

            


while True:
    prompt = input("Enter the task: ")
    
    if prompt == "add":
        add_stud()
    elif prompt == "view":
        view_stud(dic)
    elif prompt == "exit":
        break
    
    
    

    