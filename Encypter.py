f = open('test.txt', 'r')
write = open('write.txt', 'w')
t = f.read()
t = t.upper()
for i in t:
    if i == 'A' or i == 'B' or i == 'C' or i == 'D' or i == 'E' or i == 'F' or i == 'G' or i == 'H' or i == 'I' or \
        i == 'J' or i == 'K' or i == 'L' or i == 'M' or i == 'N' or i == 'O' or i == 'P' or i == 'Q' or i == 'R' or \
        i == 'S' or i == 'T' or i == 'U' or i == 'V' or i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        write.write(i)