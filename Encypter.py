# This program is developed by Pooyan :D
import codecs

f = codecs.open('test.txt', encoding='utf-8')
contents = f.read()
contents = contents.lower()

contents = contents.replace('a', 'I')
contents = contents.replace('b', 'P')
contents = contents.replace('c', 'Z')
contents = contents.replace('d', 'H')
contents = contents.replace('e', 'L')
contents = contents.replace('f', 'Q')
contents = contents.replace('g', 'A')
contents = contents.replace('h', 'T')
contents = contents.replace('i', 'O')
contents = contents.replace('j', 'X')
contents = contents.replace('k', 'W')
contents = contents.replace('l', 'R')
contents = contents.replace('m', 'B')
contents = contents.replace('n', 'F')
contents = contents.replace('o', 'C')
contents = contents.replace('p', 'J')
contents = contents.replace('q', 'Y')
contents = contents.replace('r', 'D')
contents = contents.replace('s', 'G')
contents = contents.replace('t', 'E')
contents = contents.replace('u', 'K')
contents = contents.replace('v', 'N')
contents = contents.replace('w', 'S')
contents = contents.replace('x', 'U')
contents = contents.replace('y', 'V')
contents = contents.replace('z', 'M')


write = open('write.txt', 'w')
for i in contents:
    if i == 'A' or i == 'B' or i == 'C' or i == 'D' or i == 'E' or i == 'F' or i == 'G' or i == 'H' or i == 'I' or \
        i == 'J' or i == 'K' or i == 'L' or i == 'M' or i == 'N' or i == 'O' or i == 'P' or i == 'Q' or i == 'R' or \
            i == 'S' or i == 'T' or i == 'U' or i == 'V' or i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        write.write(i)

f.close()
write.close()
# Hope you like it ;)
