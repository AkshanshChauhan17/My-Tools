import os

for drive in range(97,123):
    print(os.walk(top="*"))
    print(chr(drive))
    try:
        os.chdir(":/" + chr(drive))
    except:
        print(":/" + chr(drive), "Not Exisit")
    dirs = os.listdir()
    print(dirs)