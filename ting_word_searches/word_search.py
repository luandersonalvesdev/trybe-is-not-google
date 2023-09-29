def exists_word(word, instance):
    found = list()
    for file in instance:
        occurrences = list()
        for i, line in enumerate(file["linhas_do_arquivo"]):
            if word in line.lower():
                occurrences.append({"linha": i + 1})

        if len(occurrences):
            found.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return found


def search_by_word(word, instance):
    found = list()
    for file in instance:
        occurrences = list()
        for i, line in enumerate(file["linhas_do_arquivo"]):
            if word in line.lower():
                occurrences.append({"linha": i + 1, "conteudo": line})

        if len(occurrences):
            found.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return found
