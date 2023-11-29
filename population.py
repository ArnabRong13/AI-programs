import random

def chromosomeGenerator(list):
    for i in range(10):
        list.append(random.randint(0, 1))
    
    return list

def populationGenerator(population):
    for i in range(20):
        list=[]
        population.append(chromosomeGenerator(list))
    return population

def main():
    population=[]
    population = populationGenerator(population)
    print("Population: ", population)

main()