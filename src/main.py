from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-m', '--medals', action='store_true')
parser.add_argument('country')
parser.add_argument('year', type=int)
parser.add_argument('-t', '--total', required=False, type=int)
parser.add_argument('--overall', required=False, nargs='+')
parser.add_argument('-i', '--interactive', required=False, action='store_true')
parser.add_argument('-o', '--output', required=False)

values = parser.parse_args()