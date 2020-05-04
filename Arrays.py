import numpy as np 
import sys, os
import pickle
import argparse

print ('make an array')
aa = np.array(np.arange(12)).reshape((6,2))
print (aa)
print('try differnt methods on the array')
print(np.sqrt(aa)) #square root 
print(aa.flatten())

#pickel stuff
# local imports
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

# make sure the output directory exists
this_dir = os.path.abspath('.').split('/')[-1]
this_parent = os.path.abspath('.').split('/')[-2]
out_dir = '../../' + this_parent + '_output/'
print('Creating ' + out_dir + ', if needed')
mymod.make_dir(out_dir)

# make an array
a = np.linspace(0,10,10000).reshape((2,5,1000))

# save it as a pickle file
out_fn = out_dir + 'pickled_array.p'
pickle.dump(a, open(out_fn, 'wb')) # 'wb' is for write binary

# read the array back in
b = pickle.load(open(out_fn, 'rb')) # 'rb is for read binary

print('\nThe shape of the loaded object is')
print(b.shape)

def boolean_string(s):
    # this function helps with getting Boolean input
    if s not in ['False', 'True']:
        raise ValueError('Not a valid boolean string')
    return s == 'True' # note use of ==

# create the parser object
parser = argparse.ArgumentParser()

# NOTE: argparse will throw an error if:
#     - a flag is given with no value
#     - the value does not match the type
# and if a flag is not given it will be filled with the default.
parser.add_argument('-a', '--a_string', default='hi', type=str)
parser.add_argument('-b', '--integer_b', default=10, type=int)
parser.add_argument('-c', '--float_c', default=1.5, type=float)
parser.add_argument('-v', '--verbose', default=True, type=boolean_string)
# Note that you assign a short name and a long name to each argument.
# You can use either when you call the program, but you have to use the
# long name when getting the values back from "args".

# get the arguments
args = parser.parse_args()

# output
print('\nYour string is ' + args.a_string)

if args.verbose:
    print('\nThe sum of b and c is:')
    
print(args.integer_b + args.float_c)