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

