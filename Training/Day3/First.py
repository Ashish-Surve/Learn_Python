def dictVarArgs(arg1, arg2='defaultB', *theRest):
    """arguments in dictionary ,In this **theRest is dictionary"""
    print('formal arg 1:', arg1)
    print('formal arg 2:', arg2)
    print("----------------------------------------------------")
    print("Variable argument dictionary =",theRest)


dictVarArgs(10,"LOLS","I","M","Dead","TY")
