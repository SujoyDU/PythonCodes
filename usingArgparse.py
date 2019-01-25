import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('-v','--verbose', help = 'increase output verbosity', action = 'store_true')
# parser.add_argument('path', help = 'path of the folder to zip')
# parser.add_argument('Minimum Size', help = 'Minimum size of the folder')
# parser.add_argument('recepient_email', help = 'email of address of the recepient')
# args = parser.parse_args()

# if args.verbose:
#     print('verbosity is turned on')

parser = argparse.ArgumentParser(description = "calculate x to the power of y")

group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action = "store_true")
group.add_argument("-q", "--quiet", action = "store_true" )

parser.add_argument("x", type = int, help = 'the base')
parser.add_argument("y", type= int, help = "the expotent")

args = parser.parse_args()
answer =args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power of {} equals to {}".format(args.x,args.y,answer))
else:
    print("{} ^ {} = {}".format(args.x,args.y,answer))

print("the answes is {}".format(answer))