num_arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
written = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('input.txt', 'r') as file:
    total = 0
    for line in file:
        print(line)
        first_val = len(line)
        len_first = 0
        last_val = -1
        len_last = 0
        for num in num_arr:
            if line.find(num) < first_val and line.find(num) != -1: 
                first_val = line.index(num)
                len_first = len(num)
            if line.rfind(num) > last_val and line.rfind(num) != -1:
                last_val = line.rindex(num)
                len_last = len(num)
        new_str = line[first_val:first_val + len_first] + line[last_val:last_val + len_last]
        print(new_str)
        for x in range(9):
            if(new_str.find(written[x]) != -1):
                new_str = new_str.replace(written[x], num_arr[x])
        total += int(new_str)
    print(total)