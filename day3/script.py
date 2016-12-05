import itertools

# I know I know, I just wanted to play with itertools
def isTriangle(ar):
    indexes = list(itertools.combinations(range(0,3), 2))
    result = []

    for a,b in indexes:
        c = 3-a-b
        result.append(int(ar[c]) < int(ar[a]) + int(ar[b])) 

    return all(result)
        


def checkFile1():
    result = 0
    with open("data.txt") as inputData:
        content = inputData.readlines()

        for line in content:
            line = line.split("\n")[0].split(" ")
            line = list(filter(None, line))
            if isTriangle(line):
                result += 1

    print(result)

def checkFile2():
    result = 0
    with open("data.txt") as inputData:
        content = inputData.readlines()

        ar = []

        for line in content:
            line = line.split("\n")[0].split(" ")
            line = list(filter(None, line))

            ar.append(line)

            if len(ar) == 3:
                group1 = [ar[0][0], ar[1][0], ar[2][0]]
                group2 = [ar[0][1], ar[1][1], ar[2][1]]
                group3 = [ar[0][2], ar[1][2], ar[2][2]]

                if isTriangle(group1):
                    result += 1
                if isTriangle(group2):
                    result += 1
                if isTriangle(group3):
                    result += 1
                
                ar = []
            
    print(result)

# Part 1
checkFile1()
# Part 2
checkFile2()



