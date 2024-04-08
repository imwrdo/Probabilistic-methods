import math

cities = [
    [1, 'Rome', 2837, 41.90282, 12.4964],
    [2, 'Milan', 1366, 45.4642, 9.1900],
    [3, 'Naples', 959, 40.8522, 14.2681],
    [4, 'Turin', 878, 45.0703, 7.6869],
    [5, 'Palermo', 675, 38.1157, 13.3615],
    [6, 'Genoa', 583, 44.4056, 8.9463], 
    [7, 'Bologna', 393, 44.4949, 11.3426],
    [8, 'Florence', 383, 43.7696, 11.2558],
    [9, 'Bari', 325, 41.1171, 16.8719],
    [10, 'Catania', 311, 37.5079, 15.0830],
    [11, 'Venice', 260, 45.4408, 12.3155],
    [12, 'Verona', 257, 45.4384, 10.9916],
    [13, 'Messina', 236, 38.1938, 15.5540],
    [14, 'Padua', 209, 45.4064, 11.8768],
    [15, 'Trieste', 200, 45.6495, 13.7768]
]

def generate_combinations(N, K):
    combinations = []
    def backtrack(start, combination):
        if len(combination) == K:
            combinations.append(combination[:])
            return
        for i in range(start, N + 1):
            backtrack(i + 1, combination + [i])

    backtrack(1, [])
    return combinations

def generate_permutations(N, K):
    permutations = []
    def permute(combination, prefix=[]):
        if len(prefix) == K:
            permutations.append(prefix)
            return
        for i, city in enumerate(combination):
            permute(combination[:i] + combination[i+1:], prefix + [city])

    combinations = generate_combinations(N, K)
    for combination in combinations:
        permute(combination)
    
    return permutations

def generate_subsets(N, M):
    subsets = []
    def backtrack(start, subset):
        if len(subset) == M:
            subsets.append(subset[:])
            return
        for i in range(start, N + 1):
            backtrack(i, subset + [i])

    backtrack(1, [])
    return subsets

def townsDistance(permutations, data):
    shortest_distance = math.inf
    shortest_path = None
    
    for permutation in permutations:
        d = 0
        path = []
        for i in range(len(permutation) - 1):
            town_1 = data[permutation[i] - 1]
            town_2 = data[permutation[i+1] - 1]
            distance = distanceCalculating(town_1, town_2)
            d += distance
            path.append((town_1[1], town_2[1], distance))
        
        # Dodaj odległość z ostatniego miasta do pierwszego miasta
        town_1 = data[permutation[-1] - 1]
        town_2 = data[permutation[0] - 1]
        distance = distanceCalculating(town_1, town_2)
        d += distance
        path.append((town_1[1], town_2[1], distance))
        
        if d < shortest_distance:
            shortest_distance = d
            shortest_path = path
            
    return shortest_path, shortest_distance

def distanceCalculating(town_1, town_2):
    distance = math.sqrt((town_1[3] - town_2[3])**2 + (town_1[4] - town_2[4])**2)
    return distance

def townsPopulation(subsets, data):
    max_population = -math.inf
    max_population_subset = None
    
    for subset in subsets:
        population = 0
        for city_index in subset:
            population += data[city_index - 1][2]
        average_population = population / len(subset)
        if average_population > max_population:
            max_population = average_population
            max_population_subset = subset
            
    return max_population_subset, max_population


N = int(input("Podaj N: "))
K = int(input("Podaj K: "))
M = int(input("Podaj M: "))

# Showing
numbers = list(range(1, N+1))

print("\nWszystkie permutacje odwiedzenia", K, "miast z",N,":")
all_permutations = generate_permutations(N, K)
for i, permutation in enumerate(all_permutations):
    print(i+1, permutation)

print("\nWszystkie podzbiory o długości", M, "z", N, "elementów:")
subsets = generate_subsets(N, M)
for i, subset in enumerate(subsets):
    print(i+1, subset)

print("\nOdwiedziny miast:")
shortest_path, shortest_distance = townsDistance(all_permutations, cities)
print("\nNajkrótsza trasa:")
for path in shortest_path:
    print(path[0], "->", path[1], "(Długość:", round(path[2], 2), "km)")
print("Całkowita długość trasy:", round(shortest_distance, 2),"km")

max_population_subset, max_population = townsPopulation(subsets, cities)
print("\nPodzbiór z największą średnią liczbą mieszkańców:")
print(max_population_subset)
cities_in_order = [cities[i-1] for i in max_population_subset]
for city in cities_in_order:
    print(city[1], end=" -> ")
print("Średnia liczba mieszkańców:", max_population)
