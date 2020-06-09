#!/home/ferrari/anaconda3/envs/python2/bin/python
import sys
import os
import argparse
import glob
from multiprocessing import Pool
import subprocess
import gzip
try:
    import editdistance as ed
except:
    sys.exit("You must install 'editdistance' first")



