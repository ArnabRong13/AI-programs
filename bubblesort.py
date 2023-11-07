def bubblesort(list):
    n = len(list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True

        if not swapped:
            break

def main():
    size = int(input("Enter the size for the list: "))
    list = []
    for i in range(0, size):
        element = int(input("Enter an element to insert: "))
        list.append(element)
    
    print(list)
    bubblesort(list)
    print(list)
    
main()

