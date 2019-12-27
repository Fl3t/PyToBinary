from os import system
from sys import argv, exit

try:
    arquivo = argv[1]
except:
    print('Erro!')
    print(argv[0], 'arquivo.py')
    exit()

try:
    import PyInstaller
except:
    print('Instalando Requisitos...')
    system('pip3 install PyInstaller')

print('Compilando [{0}]'.format(arquivo))
cmd = ('pyinstaller '+arquivo)
system(cmd)
