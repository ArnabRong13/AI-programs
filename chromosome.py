import random

def chromosomeGenerator(list):
    for i in range(10):
        list.append(random.randint(0, 1))
    
    return list

def main():
    list=[]
    chromosomeGenerator(list)
    print(list)

main()