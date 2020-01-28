def read(tasks):
    f = open('file.txt', 'r')
    for line in f:
        tasks.append(line.strip())
def addition(tasks):
    with open('file.txt', 'w') as f:
        for item in tasks:
            f.write("%s\n" % item)

def delete(tasks):
    with open('file.txt', 'w') as f:
        for item in tasks:
            f.write("%s\n" % item)

def edit(tasks):
    with open('file.txt', 'w') as f:
        for item in tasks:
            f.write("%s\n" % item)



