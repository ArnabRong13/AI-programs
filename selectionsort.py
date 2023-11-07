def selection_sort(list):
    n = len(list)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if list[j] < list[min_index]:
                min_index = j
        
        list[i], list[min_index] = list[min_index], list[i]

def main():
    size = int(input("Enter the size for the list: "))
    list = []
    for i in range(0, size):
        element = int(input("Enter an element to insert: "))
        list.append(element)
    
    print(list)
    selection_sort(list)
    print(list)
    
main()