from cx_Freeze import setup, Executable

base = None    

path1 = input("What is the name of the python script? (in the same directory!)")
name1 = input("What would you like the name in the metadata to be?")
version1 = input("What is the version of your program? Please numbers only!")
description1 = input("What would you like the description to be?")
plugins = input("What packages do your script use? (Seperated by parentheses and commas)")

executables = [Executable(path1, base=base)]
packages = ["idna", plugins]
options = {
    'build_exe': {    
        'packages':plugins
    },    
}

setup(
    name =  name1,
    options = options,
    version = version1,
    description = description1,
    executables = executables
)