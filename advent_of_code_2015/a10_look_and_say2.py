
def look_and_say(sequence):
    current_digit = sequence[0]
    current_count = 0
    output_sequence = ''
    for digit in sequence:
        if current_digit == digit:
            current_count += 1
        else:
            output_sequence += str(current_count)
            output_sequence += current_digit
            current_digit = digit
            current_count = 1
    output_sequence += str(current_count)
    output_sequence += current_digit
    return output_sequence

sequence = '1113122113'
sequence = '1'
print(1, len(sequence))
for x in range(50):
    sequence = look_and_say(sequence)
    print(x+1, len(sequence))


print('length of result: ', len(sequence))

    
        
    
    
