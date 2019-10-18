import sys
from tkinter import*
from cx_freeze import setup, executable

base= None
if sys.platform == 'win32':
    base = 'win32joao'

executable = (
    Executable('O_jogo.py', base=base)
)

buildOptions = dict(
        packager = [],
        includes = ['tkinter'],
        includes_files = [],
        excludes = []
)



setup(
    name = "Pedra Papel ou Tesoura",
    version = "0.1",
    description = "Jogo do pedra papel ou tesoura",
    options = dict(build_exe = buildOptions),
    execultables = execultables
)
