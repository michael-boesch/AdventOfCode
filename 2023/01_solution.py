import re

with open('01_input.txt') as f:
    codes = f.read().split()


translation = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
             '6': 6, '7': 7, '8': 8, '9': 9,
             'one': 1, 'two': 2, 'three': 3, 'four': 4,
             'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


regsearch_part1 = r"\d"
# 2tqbxgrrpmxqfglsqjkqthree6nhjvbxpflhr1eightwohr ->
# 22 (not 28, overlap between eight and two)
regsearch_part2 = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    
summe = 0
calibration_part1 = []
calibration_part2 = []

for code in codes:
    digits = re.findall(regsearch_part1, code.lower())
    calibration_part1.append(translation[digits[0]]*10 + translation[digits[-1]])

    digits = re.findall(regsearch_part2, code.lower())
    calibration_part2.append(translation[digits[0]]*10 + translation[digits[-1]])


print(sum(calibration_part1))
print(sum(calibration_part2))

