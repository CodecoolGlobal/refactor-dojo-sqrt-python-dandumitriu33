import random
import math

sum_of_square_roots_of_lines = 0
dictionary_of_number_sequences = {}
with open('100.txt') as f:
    for line in f:
        constructed_number_in_line = ''
        for character in line:
            line_no_spaces = line.strip()
            if character != ',':
                constructed_number_in_line += character
            else:
                if line_no_spaces not in dictionary_of_number_sequences:
                    dictionary_of_number_sequences[line_no_spaces] = int(constructed_number_in_line)
                else:
                    dictionary_of_number_sequences[line_no_spaces] += int(constructed_number_in_line)
                constructed_number_in_line = ''
        if line_no_spaces not in dictionary_of_number_sequences:
            dictionary_of_number_sequences[line_no_spaces] = int(constructed_number_in_line)
        else:
            dictionary_of_number_sequences[line_no_spaces] += int(constructed_number_in_line)


for i in dictionary_of_number_sequences:
    sum_of_square_roots_of_lines += math.sqrt(dictionary_of_number_sequences[i])
# sum_of_square_roots_of_lines += math.sqrt(dictionary_of_number_sequences['23,21,5'])
# sum_of_square_roots_of_lines += math.sqrt(dictionary_of_number_sequences['342,2,5'])
# sum_of_square_roots_of_lines += math.sqrt(dictionary_of_number_sequences['32,1,777'])
# sum_of_square_roots_of_lines += math.sqrt(dictionary_of_number_sequences['234,645,223'])
# sum_of_square_roots_of_lines += math.sqrt(dictionary_of_number_sequences['243,646,2342'])
# sum_of_square_roots_of_lines += math.sqrt(dictionary_of_number_sequences['6346,3434,222'])
# sum_of_square_roots_of_lines += math.sqrt(dictionary_of_number_sequences['3,6,2'])

print(sum_of_square_roots_of_lines)
