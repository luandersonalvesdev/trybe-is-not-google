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
    if not len(instance):
        return sys.stdout.write('Não há elementos\n')
    removed_file = instance.dequeue()
    sys.stdout.write(f'Arquivo {removed_file["nome_do_arquivo"]} removido com sucesso\n')


def file_metadata(instance, position):
    if position > len(instance) or position < 0:
        return sys.stderr.write('Posição inválida')
    data = instance.search(position)
    return sys.stdout.write(str(data))
