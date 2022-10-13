import os
import pdb
import sys

path = sys.path
dir_path = path[0]
clrlog = open(r'Log.LOG', 'w')
clrlog.close()
clrBat = open(r'run.bat', 'w')
clrBat.close()
ln_1 = "@echo off\ncall cd /d " + dir_path + " >>Log.LOG"
ln_2 = "\ncall py -m pip install --user virtualenv >>Log.LOG"
ln_3 = "\ncall py -m venv env >>Log.LOG"
ln_4 = "\ncall .\\env\\Scripts\\activate >>Log.LOG"
ln_5 = "\ncall pip --proxy http://172.24.175.125:9090/ install selenium pytest openpyxl matplotlib " \
       "chromedriver_autoinstaller webdriver_manager >>Log.LOG "
ln_6 = "\ncall pytest -W ignore -v -s -l >>Log.LOG"
ln_7 = "\npause"
wrtBat = open(r'run.bat', 'a')
wrtBat.write(ln_1)
wrtBat.write(ln_2)
wrtBat.write(ln_3)
wrtBat.write(ln_4)
wrtBat.write(ln_5)
wrtBat.write(ln_6)
wrtBat.write(ln_7)
wrtBat.close()

os.startfile('run.bat')
