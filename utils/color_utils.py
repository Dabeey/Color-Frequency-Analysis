import statistics
import re
from collections import Counter

def load_colors_from_file(filepath):
    with open(filepath, 'r') as file:
        data = file.read() .upper()
    colors = re.findall(r'\b[A-Z]+\b', data)
    return colors

def correct_spelling(colors):
    corrected = []
    for color in colors:
        if color == 'BLEW':
            corrected.append('BLUE')
        elif color == 'ARSH':
            corrected.append('ASH')
        else:
            corrected.append(color)
    return corrected

def analyze_colors(colors):
    '''Return mean, median, mode, frequency of colors and probability of red.'''
    if not colors:
        return None, None, None, None, 0.0
    color_counts = Counter(colors)
    color_values = list(color_counts.values())

    # statistical values
    mean = statistics.mean(color_values)
    median = statistics.median(color_values)
    mode = statistics.mode(color_values)
    frequency = color_counts.most_common()
    total_count = sum(color_values)
    red_probability = color_counts.get('RED', 0) / total_count if total_count > 0 else 0.0

    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'frequency': frequency,
        'red_probability': round(red_probability, 3)
    }

def binary_to_decimal(binary_str):
    '''Convert a binary string to decimal.'''
    try:
        return int(binary_str, 2)
    except ValueError:
        return None
    

def sum_fibonacci(n):
    '''Return the sum of the first n Fibonacci numbers.'''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1

    a, b = 0, 1
    total = a + b
    for _ in range(2, n):
        a, b = b, a + b
        total += b
    return total

def recursive_search(lst, target, index=0):
    '''Return True if target is found in lst, else False.'''
    if index >= len(lst):
        return False
    if lst[index] == target:
        return True
    return recursive_search(lst, target, index + 1)