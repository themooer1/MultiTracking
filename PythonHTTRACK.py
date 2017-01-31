import multiprocessing
from time import sleep
import subprocess, shlex
import os

linkfile = "links.txt"
outputdir = os.getcwd()+"/output"
maxprocesses=100

if not os.path.isdir(outputdir):
    os.mkdir(outputdir)
try:
    with open(linkfile,'r') as linkf:
        links = linkf.read().split("\n")
except IOError:
    print("Cannot read input file.  Does it exist?")

print(str(len(links))+" "+str(links))
def httrack(link):
    global proc
    print(str(proc))
    print("Running HTTRACK")
    subprocess.Popen(shlex.split("httrack {} -r3 -M2000000 -c16 *c8 -%s -N '%t' .css+.js -O {} --disable-security-limits -AN 99999999999".format(link,'output/'+link)))
    proc-=1
proc=0
for i in links:
    if proc<maxprocesses:
        proc=+1
        httrack(i)
        print("Scan Started!")
    else: sleep(.5)


