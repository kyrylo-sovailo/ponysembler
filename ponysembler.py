import os, sys
import FreeCAD, importDAE

def generate(file):
    document = FreeCAD.openDocument(file)

    for object in document.Objects:
        if hasattr(object, "objectType") and object.objectType == "a2pPart":
            objects = [ object ]
            importDAE.export(objects, os.path.dirname(file) + '/' + object.Name + '.dae')

if __name__ == "__main__":
    if len(sys.argv) != 3: raise Exception("Invalid usage")
    generate(sys.argv[2])
    exit()