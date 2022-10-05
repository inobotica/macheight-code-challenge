from sys import argv as parameters

ERROR_MESSAGES = [
    'Missing parameters',
    'Dataset too small',
    'Sum outside of dataset values'
]

def format_parameters(params):    
    if len(params) != 3:
        return 0, None

    int_array = [int(i) for i in params[1].split(',')]
    int_array.sort()
    total_to_calculate = int(params[2])

    if len(int_array)<2:
        return 1, None
    
    min_pair = sum(int_array[:2])
    max_pair = sum(int_array[-2:])

    if total_to_calculate < min_pair or total_to_calculate > max_pair:
        return 2, None

    int_set = set(int_array)
    return int_set, total_to_calculate
    
def pair_integers(integer_set, total_):
    
    paired_sums = set()
    already_paired = set()

    for row in integer_set:
        total_remainder = total_ - row
        
        if total_remainder in integer_set and total_remainder not in already_paired:
            paired_sums.add((row, total_remainder))
            already_paired.add(row)
            already_paired.add(total_remainder)

    return paired_sums    
    

if __name__ == '__main__':
    int_set, total_to_calculate = format_parameters(parameters)
    
    if isinstance(int_set, int):
        print(ERROR_MESSAGES[int_set])
        exit(0)
        
    paired_sums = pair_integers(int_set, total_to_calculate)
    
    if paired_sums:
        for pair in paired_sums:
            print('+ {},{}'.format(pair[0], pair[1]))
    else:
        print('No matches found')                