
def compress(value):
    last_char = ''
    count = 0
    output = ''
    for char in value:
        if last_char != char:
            output += (last_char + str(count)) if last_char else ''
            last_char = char
            count = 1
        else:
            count += 1
    output += (last_char + str(count)) if last_char else ''
    if len(output) < len(value):
        return output
    return value

def compress_faster(value):
    last_char = ''
    count = 0
    output_list = []
    for char in value:
        if last_char != char:
            if last_char:
                output_list.append(last_char+str(count))
            last_char = char
            count = 1
        else:
            count += 1
    output_list.append(last_char+str(count))
    output = ''.join(output_list)
    if len(output) < len(value):
        return output
    return value

if __name__ == "__main__":
    from timeit import timeit
    print(timeit("compress('abbbbbbbbccccccdddddmdsvddddsnkldddd')",
           setup='from __main__ import compress',
           number=1000000))
    print(timeit("compress_faster('abbbbbbbbccccccdddddmdsvddddsnkldddd')",
           setup='from __main__ import compress_faster',
           number=1000000))
    



