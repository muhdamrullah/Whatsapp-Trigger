from stack import YowsupCliStack
#!/usr/bin/python

import sys, getopt

credentials = ("#", "#") # replace with your phone and password

def main(argv):
    inputfile = ''
    number = ''
    try:
        opts, args = getopt.getopt(argv,"i:n:",["input=","number="])
    except getopt.GetoptError:
        print 'run.py -i <inputfile> -n <number>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-n", "--number"):
            number = arg
    print 'Input file is', inputfile
    print 'Number is', number
    myStack = YowsupCliStack(credentials, number, inputfile)
    myStack.start()

if __name__==  "__main__":
    main(sys.argv[1:])
