import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v','--verbose', help = 'increase output verbosity', action = 'store_true')
parser.add_argument('path', help = 'path of the folder to zip')
parser.add_argument('Minimum Size', help = 'Minimum size of the folder')
parser.add_argument('recepient_email', help = 'email of address of the recepient')
args = parser.parse_args()

if args.verbose:
    print('verbosity is turned on')
