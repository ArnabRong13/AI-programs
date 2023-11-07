def push(element, list):
    list.append(element)
    return list

def pop(list):
    if(len(list) == 0):
        print("Cannot delete. Stack empty.")
        return list
    else:
        n = list.pop()
        print(n, " is popped.")
        return list

def display(list):
    if(len(list) == 0):
        print("Nothing to display.")
        return list
    else:
        print(list)


def main():
    list = []
    while(True):
        print("Enter your choice: ")
        print(" Press 1 to push a element.\n Press 2 to pop a element.\n Press 3 to display the stack.\n 0 to exit.")
        choice = int(input())

        if(choice == 0):
            return False
        elif(choice == 1):
            elem = int(input("Enter a element to push: "))
            list = push(elem, list)
        elif(choice == 2):
            list = pop(list)
        elif(choice == 3):
            display(list)
        else:
            print("Wrong input.")

main()