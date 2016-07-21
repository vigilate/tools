#!/bin/python3

import argparse

def simulate(test_id):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('testNumber', type=int)

    args = parser.parse_args()
    simulate(testNumber)
