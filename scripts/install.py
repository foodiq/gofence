#!usr/bin/env python
from __future__ import print_function

'''
This script has not dependencies besides a conntection to github in order to run.
Therefore it can be copied from the repo and ran on any system
By default it will install to /usr/local/bin/. Change it by editing the INSTALL_LOCATION
Requires python 2, please file a ticket if this is an issue
'''
import json
import os
import os.path
import platform
import sys
import urllib

assert sys.version_info[0] < 3

if len(sys.argv) > 1:
    bindir = sys.argv[1]
else:
    bindir = '/usr/local/bin/'
binary = os.path.join(bindir, 'fence')
print("Installing fence into", binary, "...")

kernel, _, _, _, arch, _ = platform.uname()
ext = ''
if arch == 'x86_64':
    arch = 'amd64'
elif arch == 'i386':
    arch = '386'
if kernel == 'windows':
    ext = '.exe'
dist = "{0}_{1}".format(kernel.lower(), arch.lower())
artifact = "{0}_{1}{2}".format("fence", dist, ext)

content = urllib.urlopen('https://api.github.com/repos/foodiq/gofence/releases/latest').read()
release = json.loads(content)
link = [asset['browser_download_url'] for asset in release['assets'] if asset['name'] == artifact][0]
print("Downloading binary from", link)
urllib.urlretrieve(link, binary)
os.chmod(binary, 0o755)
print("Installed fence at", binary)
