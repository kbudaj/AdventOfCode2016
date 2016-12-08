def splitIP(ip):
    hypernets = []
    supernets = []

    for part in ip.split("["):
        if "]" in part:
            hypernets.append(part.split("]")[0])
            supernets.append(part.split("]")[1])
        else:
            supernets.append(part)

    return hypernets, supernets

def isABBA(part):
    for i in range(len(part)-3):
        a, b, c, d = part[i], part[i+1], part[i+3], part[i+2]
        if a + b == c + d and a != b:
            return True
    return False

def supportTLS(ip):
    hypernets, supernets = splitIP(ip)

    for part in hypernets:
        if isABBA(part):
            return False

    for part in supernets:
        if isABBA(part):
            return True

    return False

def getABAs(part):
    for i in range(len(part)-2):
        a, b, c = part[i], part[i+1], part[i+2]
        if a == c and b != a:
            yield (a, b, c)

def getBAB(ABA):
    return (ABA[1], ABA[0], ABA[1])

def supportSSL(ip):
    ABAs = set()
    hypernets, supernets = splitIP(ip)

    for part in supernets:    
        for aba in getABAs(part):
            ABAs.add(aba)
    
    for aba in ABAs:
        for part in hypernets:
            if "".join(getBAB(aba)) in part:
                return True

    return False

def countIps(file, part):
    counter = 0
    with open(file) as f:
        for line in f:
            line = line.strip("\n")
            
            if part == 1:
                if supportTLS(line):
                    counter += 1
            elif part == 2:
                if supportSSL(line):
                    counter += 1
    return counter







# Part 1
assert supportTLS("abba[mnop]qrst") == True
assert supportTLS("abcd[bddb]xyyx") == False
assert supportTLS("aaaa[qwer]tyui") == False
assert supportTLS("ioxxoj[asdfgh]zxcvbn") == True
print(countIps("data.txt", 1))

# Part 2
assert supportSSL("aba[bab]xyz") == True
assert supportSSL("xyx[xyx]xyx") == False
assert supportSSL("aaa[kek]eke") == True
assert supportSSL("zazbz[bzb]cdb") == True
print(countIps("data.txt", 2))


