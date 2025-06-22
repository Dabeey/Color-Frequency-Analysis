from utils.color_utils import (
    load_colors_from_file,
    correct_spelling,
    analyze_colors,
    binary_to_decimal,
    sum_fibonacci,
    recursive_search
)

# Load & clean data
colors = load_colors_from_file('data/colors_raw.txt')
colors = correct_spelling(colors)

# Analyze colors
result = analyze_colors(colors)
print('Color Frequency Analysis Results:')
print('---------------------------------')
print(f"Most Frequent Color: {result['frequency'][0][0]} ({result['frequency'][0][1]} times)")
print(f"Mean Shirt Count: {result['mean']}")
print(f"Median Shirt Count: {result['median']}")
print(f"Mode Shirt Count: {result['mode']}")
print(f"Probability of Picking RED: {result['red_probability']}")

for color, count in result['frequency']:
    print(f"{color}: {count} times")

# Convert binary to decimal
binary_str = '1101'
decimal_value = binary_to_decimal(binary_str)
if decimal_value is not None:
    print(f"Binary '{binary_str}' to Decimal: {decimal_value}")
else:
    print(f"Invalid binary string: {binary_str}")

# Recursive search example
target_color = 'BLUE'
search_result = recursive_search(colors, target_color)
if search_result != -1:
    print(f"Color '{target_color}' found at index: {search_result}")
else:
    print(f"Color '{target_color}' not found in the list.")


