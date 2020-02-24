

f = open('data.txt')
while True:
        char = f.read(1)
        if not char: break
        print char
f.close()

print "-----------------------------------"
for char in open('data.txt').readline():
        print char
"""
#as opposed to
for char in open('data.txt').read():
        print char
"""
