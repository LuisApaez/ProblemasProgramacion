# Solucion problema 2

# Funcion
def twoSum(nums, target):
    for posicion, elemento in enumerate(nums):
        if target - elemento in nums and posicion != nums.index(target-elemento):
            return [posicion , nums.index(target-elemento)]
        
# Prueba
print(twoSum([2,7,11,15],9))
