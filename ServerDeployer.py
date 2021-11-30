## this is the gadget bot server deployer 0.1a
## (C) - 0.1  F-CORP WEST 200XX
print('This is the gadget bot server deployer 0.1a')
import os 
import sys
## check if heroku cli is installed if not install it
if os.system('heroku --version') != 0:
  ## check if your mac is m1 or intel processer
    if os.system('uname -m') == 0:
        os.system('brew install heroku-toolbelt')
    else:
        os.system('brew cask install heroku-toolbelt')
## check if heroku cli is installed if not install it
if os.system('heroku --version') != 0:
  ## check if your mac is m1 or intel processer
    if os.system('uname -m') == 0:
        os.system('brew install heroku')
    else:
        os.system('brew cask install heroku-toolbelt')