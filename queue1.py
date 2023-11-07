def enqueue(element, list):
    list.append(element)
    return list

def dequeue(list):
    if(len(list) == 0):
        print("Cannot delete. Queue empty.")
        return list
    else:
        n = list.pop(0)
        print(n, " is deleted.")
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
        print(" Press 1 to push a element.\n Press 2 to pop a element.\n Press 3 to display the queue.\n 0 to exit.")
        choice = int(input())

        if(choice == 0):
            return False
        elif(choice == 1):
            elem = int(input("Enter a element to push: "))
            list = enqueue(elem, list)
        elif(choice == 2):
            list = dequeue(list)
        elif(choice == 3):
            display(list)
        else:
            print("Wrong input.")

main()