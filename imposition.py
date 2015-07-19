#coding: UTF8
# Imposition es un programa per treure l'ordre de pàgines com cal per fer la impressió d'un llibret d'una signatura.

import sys

ordre = ""

pagines = raw_input("Inserir número de pàgines: ")

try:
    if int(pagines) % 4 == 0:
        i = 1
        newOrder = int(pagines)
        mig = int(pagines)/2
        while newOrder != mig+1:
            ordre = ordre + str(newOrder) + ","
            if newOrder % 2 == 0:
                if newOrder > mig:
                    newOrder = i
                else:
                    newOrder =  int(pagines) - i + 1
            else:
                if newOrder < mig:
                    newOrder = newOrder + 1
                    i = i + 1
                else:
                    newOrder = newOrder - 1
                    i = i + 1
        ordre = ordre + str(newOrder)
        print "Ordre: " + ordre
    else:
        print "No és divisible entre quatre!" 
except:
    print "No és un número"
    print "Unexpected error:", sys.exc_info()[0]
    raise
    sys.exit(1)
