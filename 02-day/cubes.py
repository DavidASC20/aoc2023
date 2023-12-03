with open('input.txt', 'r') as file:
    total = 0
    for line in file:
        print(line)
        splitted_line = line.split(" ")
        red_val = 0
        blue_val = 0
        green_val = 0
        for x in range(2, len(splitted_line) - 1, 2):
            print(splitted_line[x+1])
            print(splitted_line[x])
            if splitted_line[x+1].find('red') != -1:
                red_val = max(int(splitted_line[x]), red_val)
            elif splitted_line[x+1].find('blue') != -1:
                blue_val = max(int(splitted_line[x]), blue_val)
            elif splitted_line[x+1].find('green') != -1:
                green_val = max(int(splitted_line[x]), green_val)
        total += (red_val * blue_val * green_val)
    print(total)    