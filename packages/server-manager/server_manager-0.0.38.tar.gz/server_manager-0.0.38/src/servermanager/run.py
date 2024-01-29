import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('host')
args = parser.parse_args()

os.system(f'python -m gunicorn -b {args.host} servermanager.wsgi:app')
