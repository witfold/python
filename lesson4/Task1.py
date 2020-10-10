from sys import argv

args = argv[1:]

if len(args) != 3:
    print('incorrect num of arguments (must be three arguments with float type)')
else:
    try:
        print(round(float(args[0]) * float(args[1]) + float(args[2]), 4))
    except ValueError:
        print('argument must be a numeric!')
