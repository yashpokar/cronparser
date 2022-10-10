"""Cron Parser command line utility to run"""
import sys
from .parser import parse

def main():
    """main will get invoked when command line interface will be used"""
    result = parse(sys.argv[1:])
    print(result)
