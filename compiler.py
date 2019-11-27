import os

try:
    from cx_Freeze import setup, Executable
except:
    print('Installing Lib...')
    os.system('pip3 install cx_Freeze')

py = input('File Script: ')
name = input('Name Executable: ')
version = float(input('Version Script: '))
descript = input('Description File: ')

setup (
    name = name,
    version= version,
    description= descript,
    executables = [Executable(py)]
)
