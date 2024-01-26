def divider(x):
    return int(x/2)

def splitter(x):
    return int(x*2)

def build(x):
    step = 0
    while x>0:
        step = step + 1
        x = divider(x)
        for i in range(splitter(step)):
            print(x, ",", end="")
        print("")

build(10000)