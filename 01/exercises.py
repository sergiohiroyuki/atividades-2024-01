# Exercicio 01
def max_consecutive_sum(nums):
    maior = nums[0]
    for i in range(len(nums)):
        pivo = nums[i]
        soma = nums[i]
        for j in range(i + 1, len(nums)):
            pivo += nums[j]
            soma = max(pivo, soma)
        maior = max(maior, soma)
    return maior

# Testes 01
def test_max_consecutive_sum():
    print(max_consecutive_sum([1, -3, 2, 1, -1]) == 3)
    print(max_consecutive_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
    print(max_consecutive_sum([5, -1, -2, 3, -1, 2, -4]) == 7)
    print(max_consecutive_sum([1]) == 1)
    print(max_consecutive_sum([-1, -2, -3, -4, -5]) == -1)


# Exercício 02
def is_palindrome(word):
    inverso = word[::-1]
    if (inverso == word):
      return True
    else:
      return False

# Testes 02
def text_is_palindrome():
    print(is_palindrome("radar") == True)
    print(is_palindrome("racecar") == True)
    print(is_palindrome("level") == True)
    # Testes negativos
    print(is_palindrome("python") == False)
    print(is_palindrome("hello") == False)
    print(is_palindrome("12321") == False)
    print(is_palindrome("abccbaa") == False)


# Exercício 03
def count_increasing_subsets(nums):
    def backtrack(start, subset):
        nonlocal count
        if len(subset) > 0:
            count += 1
        for i in range(start, len(nums)):
            if not subset or nums[i] > subset[-1]:
                backtrack(i + 1, subset + [nums[i]])

    count = 0
    # Remover valores duplicados da lista
    nums = sorted(set(nums))
    backtrack(0, [])
    return count
# Testes 03
def test_count_increasing_subsets():
    # Teste com lista vazia
    print(count_increasing_subsets([]) == 0)
    # Teste com uma lista de um elemento
    print(count_increasing_subsets([1]) == 1)
    # Teste com uma lista de números aleatórios
    print(count_increasing_subsets([1, 3, 2, 4]) == 11)
    # Teste com uma lista de números ordenados
    print(count_increasing_subsets([1, 2, 3, 4, 5]) == 31)
    # Teste com uma lista de números em ordem decrescente
    print(count_increasing_subsets([5, 4, 3, 2, 1]) == 0)
    # Teste com uma lista contendo números repetidos
    print(count_increasing_subsets([1, 2, 2, 3, 3, 3, 4]) == 15)


# Run the tests
if __name__ == "__main__":
    test_max_consecutive_sum()
    text_is_palindrome()
    test_count_increasing_subsets()
