
target = 9
lista = [11, 15, 2, 7]

# força bruta O(n²):
def brute_force(lista: list[int], target: int) -> None:
    for index_i, i in enumerate(lista):
        for index_j, j in enumerate(lista):
            if (i+j == target):
                return print(f"os index para a combinação: [{index_i}, {index_j}]")

brute_force(lista, target)

# sorting + 2 pointer O(nlog n):
def sorting(_lista: list[int], target: int) -> None:
    lista = _lista[:]
    lista.sort()
    index_i, index_j = 0,-1
    for i in lista:
        
        if lista[index_i] + lista[index_j] > target:
            
            index_j -= 1
            
        if lista[index_i] + lista[index_j] < target:
            
            index_i += 1
            
        if lista[index_i] + lista[index_j] == target:
            
            return print(f"os index para a combinação: [{index_i}, {index_j+len(lista)}]")

sorting(lista, target)

# hash map O(n):

def hash_map(lista:list[int], target:int):
    list_diff = {}
    for index_i, i in enumerate(lista):
        if list_diff.get(i) is not None:
            return print(f"os index para a combinação: [{list_diff.get(i)}, {index_i}]")
        
        list_diff[target - i] = index_i

hash_map(lista, target)
