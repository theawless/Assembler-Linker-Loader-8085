# from lin import linker
# from my_ass import test


def loader(fileNames):
    offset = 0
    fileName = fileNames[0].split('.')[0]
    inputFile = open(fileName + '.ls', 'r')
    code = inputFile.read()
    lines = code.split('\n')
    outFile = open(fileName + '.8085', 'w')
    linkCode = []
    for line in lines:
        if '#' in line:
            tag = line.split(' ')[1]
            newtag = str((int(tag.split('#')[1]) + offset))
            linkCode.append(line.replace(tag, newtag))
        else:
            linkCode.append(line)
    linkCode.append('HLT')
    print("Output of linkcode: ")
    print(linkCode)
    outFile.write('\n'.join(linkCode))
    outFile.close()

# test({"sampleCode1a.x", "sampleCode1b.x"})
# linker({"sampleCode1a.x", "sampleCode1b.x"})
