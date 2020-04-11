"""
Конвертация координат верхних левых углов квадратов,
в которые вписаны окружности из svg файла в список с координатами
"""

import sys
import fnmatch
import re

current_index = 0
points = []
letter = 'А'
with open(f'C:/Users/aleks/Desktop/letters_for_name_Leoshid/{letter}.svg') as f:
    for line in f:
        if fnmatch.fnmatch(line.strip(), 'cx="*"*'):
            if len(points) == current_index:
                points.append([int(float(re.findall('(\d+.\d+)', line)[0]))])
            else:
                points[current_index].insert(0, int(float(re.findall('(\d+.\d+)', line)[0])))
                current_index += 1
        elif fnmatch.fnmatch(line.strip(), 'cy="*"*'):
            if len(points) == current_index:
                points.append([int(float(re.findall('(\d+.\d+)', line)[0]))])
            else:
                points[current_index].insert(1, int(float(re.findall('(\d+.\d+)', line)[0])))
                current_index += 1

print(points)
