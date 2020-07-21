#!/usr/bin/env python3
#################################################################################
#                                                                               #
#  SSLSCAN DEMO                                                                 #
#                                                                               #
#  Runs sslscan as a demo for Kali development containers.                      #
#                                                                               #
#  Author: Jakob Pennington                                                     #
#  Version: 1.0.0                                                               #
#                                                                               #
#################################################################################

#####################
# IMPORTS
#####################
import argparse
import os
import subprocess

#####################
# FUNCTIONS
#####################
def main():
    print(f'Running sslscan against {args.hostname}...')

    output = subprocess.check_output(['sslscan', args.hostname], universal_newlines=True)

    print(f'Scan complete, writing to file...')

    # Write to file
    os.mkdir(os.getcwd() + '/output')
    output_file = open(f'output/sslscan.txt', 'w')
    output_file.write(output)
    output_file.close()

    print(f'Done 😄')

#####################
# ARGUMENT PARSING
#####################
# Set up command line argument parsing
parser = argparse.ArgumentParser(description='Scan a single target with sslscan.')
parser.add_argument('hostname', help='A single target hostname')
# Parse the supplied arguments
args = parser.parse_args()

#####################
# MAIN
#####################
if __name__ == "__main__":
    main()
