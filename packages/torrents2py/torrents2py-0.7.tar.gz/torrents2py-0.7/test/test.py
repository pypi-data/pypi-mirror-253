def sort_numbers(numbers, sort_order='asc'):
    """
    Sort a list of numbers.

    Parameters:
    - numbers (list): List of numbers to be sorted.
    - sort_order (str): Sort order ('asc' for ascending, 'desc' for descending).

    Returns:
    - list: Sorted list of numbers.
    """
    try:
        numbers = [int(num) for num in numbers]  # Convert strings to integers
        numbers.sort(reverse=(sort_order.lower() == 'desc'))  # Sort the list

        return numbers

    except ValueError as e:
        print(f"Error: {e}")
        return []

# Esempio di utilizzo
numbers_to_sort = ["5", "2", "8", "1", "3"]
sorted_numbers = sort_numbers(numbers_to_sort, sort_order='asc')

print("Numbers before sorting:", numbers_to_sort)
print("Numbers after sorting:", sorted_numbers)
