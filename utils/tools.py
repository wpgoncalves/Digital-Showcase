from queue import Empty


def is_preposition(word: str) -> bool:
    """Returns a true value for the word contained in the list of
    prepositions, otherwise the return will be false.

    (pt-BR) Retorna um valor verdadeiro para palavra contida na lista de
    preposições, caso contrário o retorno será falso.

    Args:
        word (str): A word, which cannot be an empty or null value.

        (pt-BR) Uma palavra, não podendo esta ser um valor vazio ou nulo.

    Returns:
        bool: True or False.

        (pt-BR) Verdadeiro ou Falso.
    """

    if word is Empty or word is None:
        raise ValueError('É necessário informar uma palavra!')

    list_prepositions = [
        'por', 'a', 'para', 'de', 'em', 'pelo', 'ao', 'pro', 'do', 'no',
        'pela', 'à', 'pra', 'da', 'na', 'pelos', 'aos', 'pros', 'dos', 'nos',
        'pelas', 'às', 'pras', 'das', 'nas', 'dum', 'duma', 'duns', 'dumas',
        'dele', 'dela', 'deles', 'delas', 'deste', 'disto', 'desse', 'daquele',
        'daquilo', 'àquele', 'àquilo', 'praquilo', 'praquele', 'num', 'numa',
        'nuns', 'numas', 'nele', 'nela', 'neles', 'nelas', 'neste', 'nisto',
        'nesse', 'nisso', 'naquele', 'naquilo', 'de', 'e'
    ]
    return word.lower() in list_prepositions


def string_capitalize(value: str = None) -> str:
    """Converts the initial letters of each word, except for prepositions, so
    that all initials are capitalized.

    (pt-br) Realiza a conversão das letras iniciais de cada palavra, exceto
    as preposições, de modo que todas as iniciais passam a ser maiúsculas.

    Args:
        value (str, optional): Value of type string that will receive the
        treatment of the function so that its initials become uppercase.
        Defaults to None.

        (pt-br) Valor do tipo string que receberá o tratamento da função para
        que suas iniciais se tornem maiúsculas. O padrão é Nenhum.

    Raises:
        ValueError: Informs the user that the value must be informed.

        (pt-br) Informa ao usuário que o valor obrigatóriamente deva ser
        informado.

    Returns:
        str: Returns the string passed as a parameter (value) with all
        initials in uppercase.

        (pt-BR) Retorna a string passada como parâmetro (value) com todas as
        iniciais em maiúscula.
    """

    if value is None:
        raise ValueError('É necessário informar um valor do tipo string!')

    list_words = list(map(lambda w: w.lower() if is_preposition(w)
                      else w.capitalize(), value.split(' ')))
    return ' '.join(list_words)
