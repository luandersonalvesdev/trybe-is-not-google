from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }
    for dictt in instance:
        if dictt["nome_do_arquivo"] == path_file:
            return None
    instance.enqueue(new_dict)
    sys.stdout.write(str(new_dict))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
