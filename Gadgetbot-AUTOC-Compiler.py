## hello welcome to autocmake
## get the version of cmake and gcc
## check if the version is 3.8.0
import os 
import sys 
print("Welcome to AutoCmake")
print("This is a simple tool to help you deploy your script to any m1 mac and port windows software to the mac m1 platform.")
gcc = os.getenv('G')
cmake = os.getenv('C')
print("The version you are running is:", gcc, cmake)

## check to see if gcc is installed if not install it
if os.system('gcc --version') != 0:
    ## check if your mac is m1 or intel processer
    if os.system('uname -m') == 0:
        os.system('brew install gcc')
    else:
        os.system('brew cask install gcc')
        ## check to see if cmake is installed if not install it
if os.system('cmake --version') != 0:
    ## check if your mac is m1 or intel processer
    if os.system('uname -m') == 0:
        os.system('brew install cmake')
    else:
        os.system('brew cask install cmake')
        print("Check what processer you are running then configure cmake and gcc configs for m1 mac setup to port windows x86 software to the m1 or ios platform.")
        print("If you are running on a windows x86 machine, you can port your software to the m1 platform by running the following command:")
        if os.system('uname -m') == 0:
            print("cmake -G \"Unix Makefiles\"")
        else:
            print("cmake -G \"MinGW Makefiles\"")
        print("If you are running on a windows x64 machine, you can port your software to the m1 platform by running the following command:")
        if os.system('uname -m') == 0:
            print("cmake -G \"Unix Makefiles\"")
        else:
            print("cmake -G \"MinGW Makefiles\"")
            ## if you want to compile the program into a dmg file for m1 devices on mac
            ## you can run the following command
print("Define the folder of your source code to build")
print("Example: /Users/$user/Documents/Stuff/Code~/Python 3.0x/GadgetBot-HQRips/DiscordBot.py")

print("Enter the code directory of the repo you want to compile from your local machine")
folderinput= os.getenv(input("Enter the code directory of the repo you want to compile from your local machine: "))
print("Syncing with folder: " + folderinput)
print("Enter the name of the folder you want to compile to")
cmakeoutput= os.getenv(input("Enter the name of the folder you want to compile to: "))
print("Syncing with folder: " + cmakeoutput)
print("Name the app and add it to the applications directory")
appname= os.getenv(input("Name the app and add it to the applications directory: "))
print("Syncing with folder: " + appname)
print("Enter the name of the dmg file you want to create")
dmgname= os.getenv(input("Enter the name of the dmg file you want to create: "))
print("The name of the file you gave was:", dmgname)
## get the name of the .c file from the application or if it is c++ get the cpp or if it is swift get the swift file from the selected folder 
def cmakeswift(appname):
    os.system('cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/Applications/' + appname + ' -DCMAKE_OSX_DEPLOYMENT_TARGET=10.13 ' + folderinput + ' && make -j4 && make install')
    os.system('dmgbuild --volname ' + appname + ' --pkg-name ' + appname + ' --target-name ' + dmgname + ' ' + appname + '.dmg')
def cmakecpp(appname):
    os.system('cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/Applications/' + appname + ' -DCMAKE_OSX_DEPLOYMENT_TARGET=10.13 ' + folderinput + ' && make -j4 && make install')
    os.system('dmgbuild --volname ' + appname + ' --pkg-name ' + appname + ' --target-name ' + dmgname + ' ' + appname + '.dmg')
   
def Greeting(Greeting): {
    ## this is the program script for all the functions in this module
    print("Welecome to Gadgetbot AutoCmake 0.1a")
 
}

print(cmakecpp('Trying to compile cmakecpp')
