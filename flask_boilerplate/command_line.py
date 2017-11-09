import os, sys
from optparse import OptionParser
from core import startproject

parser = OptionParser()
parser.add_option('-s', '--startproject', dest='startproject', help='Start flask project', type=str)

(options, args) = parser.parse_args()

if options.startproject:
    startproject(options.startproject, args[0] if args else None)
    

