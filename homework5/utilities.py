def calculate_average(numbers):
    result = sum(numbers)/len(numbers)
    result = round(result) if result % 1 == 0 else result
    return result

def find_max(numbers):
    numbers = sorted(numbers)
    result = numbers[len(numbers) - 1]
    return result
