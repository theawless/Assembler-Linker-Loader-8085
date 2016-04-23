import my_ass, lin, loader

x = []


def exec():
    x.append("sampleCode1a.x")
    x.append("sampleCode1b.x")
    runass()
    runlin()
    runload()


def runass():
    my_ass.test(x)


def runlin():
    lin.linker(x)


def runload():
    loader.loader(x)


exec()
