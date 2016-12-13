instructions = open("data.txt").read().splitlines()

i = 0
# Part 1
# reg = {"a":0, "b":0, "c":0, "d":0} 
# Part 2
reg = {"a":0, "b":0, "c":1, "d":0} 

while i < len(instructions):
    line = instructions[i]
    if 'cpy' in line:
        x = line.split("cpy ")[1].split(" ")[0]
        y = line.split("cpy ")[1].split(" ")[1]
        if x in reg.keys():
            reg[y] = reg[x]
        else:
            reg[y] = int(x)
        i += 1
    elif 'inc' in line:
        x = line.split("inc ")[1].split(" ")[0]
        reg[x] = reg[x] + 1
        i += 1
    elif 'dec' in line:
        x = line.split("dec ")[1].split(" ")[0]
        reg[x] = reg[x] - 1
        i += 1
    elif 'jnz' in line:
        x = line.split("jnz ")[1].split(" ")[0]
        y = line.split("jnz ")[1].split(" ")[1]
        if x in reg.keys():
            if reg[x] != 0:
                i += int(y)
            else:
                i += 1
        else:
            if x != 0:
                i += int(y)
            else:
                i += 1

print(reg['a'])

