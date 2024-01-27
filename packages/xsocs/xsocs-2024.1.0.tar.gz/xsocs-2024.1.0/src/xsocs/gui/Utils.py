import os


# TODO : something better!
def nextFileName(root, template, cntMax=10000):
    template = os.path.join(root, template)
    for fIdx in range(cntMax):
        nextFile = template.format(fIdx)
        if not os.path.exists(nextFile):
            return nextFile
    else:
        raise ValueError("No available file names.")
