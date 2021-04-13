class mynew(object):
    def __init__(seft, name):
        seft.name = name
    
    def greet(seft, loud = False):
        if loud:
            print("HELLO, %s!" % seft.name.upper())
        else:
            print("HELLO, %s" % seft.name)

g = mynew("anh")
g.greet()
g.greet(loud=True)