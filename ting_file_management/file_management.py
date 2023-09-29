import sys
import os


def txt_importer(path_file):
    if path_file[len(path_file) - 4:] != '.txt':
        return sys.stderr.write('Formato inválido\n')

    if not os.path.isfile(path_file):
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')

    with open(path_file, "r") as file:
        file_opened = [linha.rstrip('\n') for linha in file.readlines()]
        return file_opened
