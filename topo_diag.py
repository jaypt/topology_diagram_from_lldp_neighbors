#!/usr/bin/env python2.7

import sys, logging, os, datetime, pprint, time, re
import argparse

from fabric.api import run, env, parallel, execute
from fabric.operations import local
import yaml
import pprint
from topo_utils import *
from dot_utils import *

ADMIN = 'admin'
ADMIN_PASS = 'admin'


env.password = ADMIN_PASS
env.user = ADMIN

@parallel
def task():
   
    try:
       op = run ('show lldp neighbors', shell=False)
    except:
       return None
    op = op.split("\r\n")
    retVal = []
    for line in op[4:-1]:
        val = re.split('\s+',line)
        rnode, lint, rint = val[0], val[1], val[4]
        retVal.append((lint, rnode, rint))
    return retVal
    
    
def main(setup):
    #print env
    with open(setup+'.yml', 'r') as f:
       yml_info = yaml.load(f)
    hosts = yml_info['nodes']
    op = execute (task, hosts=hosts)
    pprint.pprint(op)
    topo = Topology(op)
    topo.update_topo()
    print_topo = topo.print_info()
    with open(setup+'.txt', 'w') as f:
       f.write(print_topo)

    dot = dot_info(topo)
    print dot
    dotfile = setup+'.dot'
    with open(dotfile, 'w') as f:
       f.write(dot)

    #local('dot -Tpdf '+dotfile + ' -o ' + setup+'.pdf', capture=True, shell='/bin/bash')
   


if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument("setup", help="enter host name to connect to")
   args = parser.parse_args()

   main(args.setup)
