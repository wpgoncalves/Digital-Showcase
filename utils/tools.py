from os import environ, name, path
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


def exists_dotenv(dotenv_path: str = None, dotenv_file: str = '.env') -> bool:
    """It checks for the existence of the .env file with the environment
    variables from the specified path and file. If no values are provided,
    the function will search from the user's personal folder for an .env file.

    (pt-br) Realiza a verificação da existência do arquivo .env com as
    variáveis de ambiente a partir do caminho e arquivo expecificado. Caso não
    seja fornecido valores a função buscará a partir da pasta pessoal do
    usuário por um arquivo .env.

    Args:
        dotenv_path (str, optional): Value of type string that will receive the
        initial path for the file. Defaults to None.

        (pt-br) Valor do tipo string que receberá o caminho inicial para o
        arquivo.

        dotenv_file (str, optional): String type value that will receive the
        file name.

        (pt-br) Valor do tipo string que receberá o nome do arquivo.

    Raises:
        KeyError: Informs the user that the key with the path to the local
        folder configured in the environment variables does not exist.

        (pt-br) Informa ao usuário que não existe a chave com o caminho para
        pasta local configurada nas variáveis de ambiente.

    Returns:
        bool: Returns a true or false value informing whether the .env file
        could be found.

        (pt-BR) Retorna um valor verdadeiro ou falso informando se foi possível
        localizar o arquivo .env.
    """

    dotenv_key = 'USERPROFILE' if name == 'nt' else 'HOME'

    try:
        if dotenv_path is None:
            dotenv_path = environ[dotenv_key]

        dotenv_path_file = path.abspath(path.join(dotenv_path, dotenv_file))

        return path.exists(dotenv_path_file) and path.isfile(dotenv_path_file)
    except KeyError as exc_keyerror:
        raise KeyError(
            f'{dotenv_key} not found in system variables.'
        )from exc_keyerror
