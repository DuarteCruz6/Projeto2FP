global stringletras
global goban_antigos
stringletras = "ABCDEFGHIJKLMNOPQRS"
goban_antigos = []

def cria_intersecao(coluna,linha):
    """
    Recebe um caracter e um inteiro correspondentes à coluna (argumento 1) e à linha (argumento 2) e devolve a interseção correspondente.
    O construtor verifica a validade dos seus argumentos, gerando um ValueError com a mensagem 'cria_intersecao: argumentos invalidos' 
    caso os seus argumentos não sejam válidos. 

    :param coluna: String
    :param linha: Integer
    :return: Tuple
    """

    if type(coluna) != str or len(coluna)!=1 or coluna not in stringletras:     #Verifica se o argumento 1 é válido, isto é, se é uma só letra de A a S (maiúsculo).
        raise ValueError ("cria_intersecao: argumentos invalidos")
    if type(linha) != int or linha < 1 or linha > 19:                           #Verifica se o argumento 2 é válido, isto é, se é um número de 1 a 19.
        raise ValueError ("cria_intersecao: argumentos invalidos")
    return (coluna,linha)

def obtem_col(intersecao):
    """
    Devolve a coluna da interseção.

    :param intersecao: Tuple
    :return: String
    """

    return intersecao[0]

def obtem_lin(intersecao):
    """
    Devolve a linha da interseção.

    :param intersecao: Tuple
    :return: Integer
    """

    return int(intersecao[1])

def eh_intersecao(intersecao):
    """
    Devolve True caso o seu argumento seja um TAD interseção e False caso contrário.

    :param intersecao: Universal
    :return: Boolean
    """

    if type(intersecao) == tuple:                                       #Verifica se o argumento é válido, isto é, se é um tuplo
        if len(intersecao) == 2:                                        #Verifica se o tuplo é válido, isto é, se tem dois elementos
            coluna = obtem_col(intersecao)
            if type(coluna) == str and coluna in stringletras:          #Verifica se o primeiro elemento é uma letra maiúscula de A a S
                linha = obtem_lin(intersecao)
                if type(linha)== int and linha >= 1 and linha <= 19:    #Verifica se o segundo elemento é um número de 1 a 19
                    return True
    return False

def intersecoes_iguais(i1,i2):
    """
    Devolve True apenas se ambos os argumentos forem interseções e forem iguais, e False caso contrário.

    :param i1: Universal
    :param i2: Universal
    :return: Boolean
    """

    if eh_intersecao(i1) and eh_intersecao(i2):                         #Verifica se ambos os argumentos são interseções
        if i1 == i2:                                                    #Verifica se ambas as interseções são iguais
            return True
    return False

def intersecao_para_str(intersecao):
    """
    Devolve a cadeia de caracteres que representa o seu argumento (intersecao).

    :param intersecao: Tuple
    :return: String
    """

    coluna = obtem_col(intersecao)
    linha = obtem_lin(intersecao)
    return f"{coluna}{linha}"                                           

def str_para_intersecao(string):
    """
    Devolve a interseção representada pelo seu argumento.

    :param string: String
    :return: Tuple
    """

    coluna = string[0]
    linha = int(string[1:])
    return cria_intersecao(coluna,linha)

def obtem_intersecoes_adjacentes(intersecao,intersecao_max):
    """
    Devolve um tuplo com as interseções adjacentes à interseção (argumento 1) de acordo com a ordem de leitura, 
    em que intersecao_max (argumento 2) corresponde à interseção superior direita do tabuleiro de Go.

    :param intersecao: Tuple
    :param intersecao_max: Tuple
    :return: Tuple
    """

    adjacentes = ()
    coluna = obtem_col(intersecao)
    linha = obtem_lin(intersecao)
    coluna_max = obtem_col(intersecao_max)
    linha_max = obtem_lin(intersecao_max)
    if coluna != "A":
        coluna_adjacente = stringletras[stringletras.index(coluna)-1]
        adjacentes += (cria_intersecao(coluna_adjacente,linha),)            #Obtém a interseção à esquerda.
    if coluna != coluna_max:
        coluna_adjacente = stringletras[stringletras.index(coluna)+1]
        adjacentes += (cria_intersecao(coluna_adjacente,linha),)            #Obtém a interseção à direita.
    if linha != 1:
        linha_adjacente = linha - 1
        adjacentes += (cria_intersecao(coluna,linha_adjacente),)            #Obtém a interseção embaixo.
    if linha != linha_max:
        linha_adjacente = linha + 1
        adjacentes += (cria_intersecao(coluna,linha_adjacente),)            #Obtém a interseção em cima.
    return ordena_intersecoes(adjacentes)                                   

def ordenador(intersecao):
    """
    Função auxiliar para ordenar as interseções de acordo com a ordem de leitura do tabuleiro de Go.
    
    :param intersecao: Tuple
    :return: Tuple
    """

    return obtem_lin(intersecao), obtem_col(intersecao)                     #Ordena as interseções primeiramente pela linha (número) e só depois pelas letras (colunas)

def ordena_intersecoes(tuplo_intersecoes):
    """
    Devolve um tuplo de interseções com as mesmas interseções de tuplo_intersecoes,
    ordenadas de acordo com a ordem de leitura do tabuleiro de Go.

    :param tuplo_intersecoes: Tuple
    :return: Tuple
    """

    return tuple(sorted(tuplo_intersecoes, key = ordenador))                #Ordena as interseções do seu argumento de acordo com a ordem de leitura do tabuleiro de Go (esquerda,direita,baixo,cima)

def cria_pedra_branca():
    """
    Devolve uma pedra que pertence ao jogador branco.

    :return: String
    """

    return "pedra branca"

def cria_pedra_preta():
    """
    Devolve uma pedra que pertence ao jogador preto.

    :return: String
    """

    return "pedra preta"

def cria_pedra_neutra():
    """
    Devolve uma pedra neutra, isto é, que não pertence a nenhum jogador.

    :return: String
    """

    return "pedra neutra"

def eh_pedra(arg):
    """
    Devolve True caso o seu argumento seja um TAD pedra e False caso contr ́ario.

    :param arg: Universal
    :return: Boolean
    """

    if arg in ["pedra branca", "pedra preta", "pedra neutra", "X", "O", "."]:           #Verifica se o argumento é uma pedra, seja ela de um jogador ou neutra
        return True
    return False

def eh_pedra_branca(pedra):
    """
    Devolve True caso a pedra (argumento) seja do jogador branco e False caso contrário.

    :param pedra: String
    :return: Boolean
    """

    if pedra == "pedra branca" or pedra == "O":                                         #Verifica se o argumento é uma pedra branca
        return True
    return False

def eh_pedra_preta(pedra):
    """
    Devolve True caso a pedra (argumento) seja do jogador preto e False caso contrário.

    :param pedra: String
    :return: Boolean
    """

    if pedra == "pedra preta" or pedra == "X":                                          #Verifica se o argumento é uma pedra preta
        return True
    return False

def eh_pedra_neutra(pedra):
    """
    Devolve True caso a pedra (argumento) seja netra (de nenhum jogador) e False caso contrário.

    :param pedra: String
    :return: Boolean
    """

    if pedra == "pedra neutra" or pedra == ".":                                         #Verifica se o argumento é uma pedra neutra
        return True
    return False

def pedras_iguais(pedra1, pedra2):
    """
    Devolve True apenas se pedra1 e pedra2 são pedras e são iguais.

    :param pedra1: Universal
    :param pedra2: Universal
    :return: Boolean
    """

    if eh_pedra(pedra1) and eh_pedra(pedra2):                                           #Verifica se ambos os argumentos são pedras 
        if eh_pedra_branca(pedra1) and eh_pedra_branca(pedra2):                         #Verifica se ambos os argumentos são pedras brancas
            return True
        elif eh_pedra_preta(pedra1) and eh_pedra_preta(pedra2):                         #Verifica se ambos os argumentos são pedras pretas
            return True
        elif eh_pedra_neutra(pedra1) and eh_pedra_neutra(pedra2):                       #Verifica se ambos os argumentos são pedras neutras
            return True
    return False

def pedra_para_str(pedra):
    """
    Devolve a cadeia de caracteres que representa o jogador dono da pedra, isto é, "O", "X" ou "."
    para pedras do jogador branco, preto ou neutra, respetivamente.

    :param pedra: String
    :return: String
    """

    if eh_pedra_branca(pedra):
        return "O"
    elif eh_pedra_preta(pedra):
        return "X"
    else:
        return "."
    
def eh_pedra_jogador(pedra):
    """
    Devolve True caso a pedra (argumento) seja de um jogador e False caso contrário

    :param pedra: String
    :return: Boolean
    """

    if eh_pedra_preta(pedra):
        return True
    elif eh_pedra_branca(pedra):
        return True
    return False

def cria_goban_vazio(num):
    """
    Devolve um goban de tamanho num x num, sem interseções ocupadas. O construtor verifica a validade do argumento,
    gerando um ValueError com a mensagem 'cria_goban_vazio: argumento invalido' caso o seu argumento não seja 
    válido. Considera-se que um goban pode ser de dimensão 9x9, 13x13 ou 19x19.

    :param num: Integer
    :return: List
    """

    if type(num) == int and num in [9,13,19]:                           #Verifica se o argumento é válido, isto é, se é um inteiro e se corresponde a 9, 13 ou 19
        return [num,[],[]]
    else:
        raise ValueError ("cria_goban_vazio: argumento invalido")
    
def cria_goban(num,tuplo_intersecoes_brancas,tuplo_intersecoes_pretas):
    """
    Devolve um goban de tamanho num x num, com as interseções do tuplo tuplo_intersecoes_brancas
    ocupadas por pedras brancas e as interseções do tuplo tuplo_intersecoes_pretas ocupadas por 
    pedras pretas. O construtor verifica a validade dos argumentos, gerando um ValueError com a 
    mensagem 'cria_goban: argumentos invalidos' caso os seus argumentos não sejam válidos. 
    Considera-se que um goban pode ser de dimensão 9x9, 13x13 ou 19x19.

    :param num: Integer
    :param tuplo_intersecoes_brancas: Tuple
    :param tuplo_intersecoes_pretas: Tuple
    :return: List
    """

    lista_intersecoes_brancas = []
    lista_intersecoes_pretas = []
    if type(num) != int or num not in [9,13,19]:                                                                                        #Verifica se o primeiro argumento é válido, isto é, se é um inteiro e se corresponde a 9, 13 ou 19
        raise ValueError ("cria_goban: argumentos invalidos")
    if type(tuplo_intersecoes_brancas) != tuple or type(tuplo_intersecoes_pretas) != tuple:                                             #Verifica se o segundo e o terceiro argumento são válidos, isto é, se correspondem a tuplos
        raise ValueError ("cria_goban: argumentos invalidos")
    for intersecao in tuplo_intersecoes_brancas:
        if type(intersecao) != str and type(intersecao) != tuple:                                                                       #Verifica se os elementos dentro do tuplo do segundo argumento são válidos, isto é, se são interseções
            raise ValueError ("cria_goban: argumentos invalidos")
        if len(intersecao) not in [2,3]:
            raise ValueError ("cria_goban: argumentos invalidos")
        if type(intersecao) == str:
            intersecao = str_para_intersecao(intersecao)
        if eh_intersecao(intersecao) and intersecao not in tuplo_intersecoes_pretas and intersecao not in lista_intersecoes_brancas:
            if obtem_lin(intersecao) > num or stringletras.index(obtem_col(intersecao))+1 > num:
                raise ValueError ("cria_goban: argumentos invalidos")
            else:
                lista_intersecoes_brancas += [intersecao,]                                                                              #Se os elementos dentro do tuplo do segundo argumento forem todos válidos, adiciona estes elementos à lista de interseções que têm pedras do jogador branco
        else:
            raise ValueError ("cria_goban: argumentos invalidos")
    for intersecao in tuplo_intersecoes_pretas:
        if type(intersecao) != str and type(intersecao) != tuple:                                                                       #Verifica se os elementos dentro do tuplo do terceiro argumento são válidos, isto é, se são interseções
            raise ValueError ("cria_goban: argumentos invalidos")
        if len(intersecao) not in [2,3]:
            raise ValueError ("cria_goban: argumentos invalidos")
        if type(intersecao) == str:
            intersecao = str_para_intersecao(intersecao)
        if eh_intersecao(intersecao) and intersecao not in tuplo_intersecoes_brancas and intersecao not in lista_intersecoes_pretas:
            if obtem_lin(intersecao) > num or stringletras.index(obtem_col(intersecao))+1 > num:
                raise ValueError ("cria_goban: argumentos invalidos")
            else:
                lista_intersecoes_pretas += [intersecao,]                                                                                #Se os elementos dentro do tuplo do segundo argumento forem todos válidos, adiciona estes elementos à lista de interseções que têm pedras do jogador branco
        else:
            raise ValueError ("cria_goban: argumentos invalidos")
    return [num,lista_intersecoes_brancas,lista_intersecoes_pretas]

def cria_copia_goban(goban):
    """
    Recebe um goban e devolve uma cópia do goban.

    :param goban: List
    :return: List
    """

    num = obtem_dimensao_goban(goban)
    intersecoes_brancas = obtem_pedras_brancas(goban).copy()
    intersecoes_pretas = obtem_pedras_pretas(goban).copy()
    return [num,intersecoes_brancas,intersecoes_pretas]

def obtem_ultima_intersecao(goban):
    """
    Devolve a interseção que corresponde ao canto superior direito do goban (argumento)

    :param goban: List
    :return: Tuple
    """

    num = obtem_dimensao_goban(goban)
    letra = stringletras[num-1]
    return cria_intersecao(letra,num)

def obtem_pedra(goban,intersecao):
    """
    Devolve a pedra na interseção (argumento 2) do goban (argumento 1). Se a posição não estiver ocupada, 
    devolve uma pedra neutra.

    :param goban: List
    :param intersecao: Tuple
    :return: String
    """

    intersecoes_brancas = obtem_pedras_brancas(goban)
    intersecoes_pretas = obtem_pedras_pretas(goban)
    if intersecao in intersecoes_brancas:
        return "O"
    elif intersecao in intersecoes_pretas:
        return "X"
    else:
        return "."
    
def obtem_cadeia(goban,intersecao):
    """
    Devolve o tuplo formado pelas interseções (em ordem de leitura) das pedras da cadeia 
    que passa pela interseção (argumento 2). Se a posição não estiver ocupada, devolve
    a cadeia de posições livres.

    :param goban: List
    :param intersecao: Tuple
    :return: Tuple
    """

    intersecao_max = obtem_ultima_intersecao(goban)
    simbolo_cor = obtem_pedra(goban,intersecao)
    porvisitar = [intersecao,]
    visitadas = []
    cadeia = (intersecao,)
    while len(porvisitar) != 0:                     #Enquanto houver interseções por visitar, este loop continua a correr
        intersecao_visitada = porvisitar[0]
        adjacentes = obtem_intersecoes_adjacentes(intersecao_visitada,intersecao_max)
        for intersecao_adjacente in adjacentes:
            if pedras_iguais(obtem_pedra(goban,intersecao_adjacente),simbolo_cor) and intersecao_adjacente not in cadeia:   #Se alguma das interseções adjacentes possuir uma pedra do mesmo jogador da interseção do segundo argumento, ou se forem ambas neutras, esta interseção é adicionada à lista de porvisitar (pois precisamos de analisar as suas adjacentes) e à cadeia
                porvisitar += [intersecao_adjacente,]
                cadeia += (intersecao_adjacente,)
        visitadas += [intersecao_visitada,]
        porvisitar.remove(intersecao_visitada)
    return ordena_intersecoes(cadeia)

def coloca_pedra(goban,intersecao,pedra):
    """
    Modifica destrutivamente o goban (argumento 1) colocando a pedra
    do jogador (pedra) na interseção (argumento 2), e devolve o próprio goban.

    :param goban: List
    :param intersecao: Tuple
    :param pedra: String
    :return: List
    """

    pedras_brancas = obtem_pedras_brancas(goban)
    pedras_pretas = obtem_pedras_pretas(goban)
    if eh_pedra_branca(pedra):
        if intersecao in pedras_pretas:
            remove_pedra(goban,intersecao)
        pedras_brancas.append(intersecao)
    elif eh_pedra_preta(pedra):
        if intersecao in pedras_brancas:
            remove_pedra(goban,intersecao)
        pedras_pretas.append(intersecao)     
    return goban
    
def remove_pedra(goban,intersecao):
    """
    Modifica destrutivamente o goban (argumento 1) removendo a pedra
    da interseção (argumento 2), e devolve o próprio goban.

    :param goban: List
    :param intersecao: Tuple
    :return: List
    """
    pedras_brancas = obtem_pedras_brancas(goban)
    pedras_pretas = obtem_pedras_pretas(goban)
    if eh_pedra_branca(obtem_pedra(goban,intersecao)):
        pedras_brancas.remove(intersecao)
    elif eh_pedra_preta(obtem_pedra(goban,intersecao)):
        pedras_pretas.remove(intersecao)
    return goban

def remove_cadeia(goban,cadeia):
    """
    Modifica destrutivamente o goban (argumento 1) removendo as pedras
    nas interseções do tuplo (cadeia), e devolve o próprio goban.

    :param goban: List
    :param cadeia: Tuple
    :return: List
    """

    for intersecao in cadeia:
        remove_pedra(goban,intersecao)
    return goban

def eh_goban(arg):
    """
    Devolve True caso o seu argumento seja um TAD goban e False
    caso contrário.

    :param arg: Universal
    :return: Boolean
    """

    if type(arg) != list:                                                           #Verifica se o argumento é válido, isto é, se é uma lista
        return False
    if len(arg) == 3:                                                               #Verifica se o argumento corresponde a uma lista de 3 elementos, tal como o TAD Goban
        num = obtem_dimensao_goban(arg)
        lista_intersecoes_brancas = obtem_pedras_brancas(arg)
        lista_intersecoes_pretas = obtem_pedras_pretas(arg)
        if type(num) == int and num in [9,13,19]:                                   #Verifica se o 1º elemento do argumento é uma dimensão de um tabuleiro de Go, isto é, se é um inteiro igual a 9,13 ou 19
            if type(lista_intersecoes_brancas) == list:                             #Verifica se o 2º elemento do argumento é uma lista 
                if len(lista_intersecoes_brancas) != 0:
                    for intersecao in lista_intersecoes_brancas:
                        if eh_intersecao(intersecao):                               #Verifica se os elementos dentro do 2º elemento do argumento correspondem a interseções válidas
                            if intersecao not in lista_intersecoes_pretas:    
                                if obtem_lin(intersecao) <= num:
                                    if type(lista_intersecoes_pretas) == list:      #Verifica se o 3º elemento é uma lista
                                        if len(lista_intersecoes_pretas) != 0:
                                            for intersecao in lista_intersecoes_pretas:
                                                if eh_intersecao(intersecao):       #Verifica se os elementos dentro desta lista são interseções
                                                    if obtem_lin(intersecao) <= num:
                                                        return True
                                        else:
                                            return True
                else:
                    if type(lista_intersecoes_pretas) == list:                      #Verifica se o 3º elemento é uma lista
                        if len(lista_intersecoes_pretas) != 0:
                            for intersecao in lista_intersecoes_pretas:
                                if eh_intersecao(intersecao):                       #Verifica se os elementos dentro desta lista são interseções
                                    if obtem_lin(intersecao) <= num:
                                        return True
                        return True
    return False

def eh_intersecao_valida(goban,intersecao):
    """
    Devolve True se intersecao (argumento 2) é uma interseção válida dentro do
    goban (argumento 1) e False caso contrário

    :param goban: List
    :param intersecao: Tuple
    :return: Boolean
    """

    if eh_goban(goban):
        if eh_intersecao(intersecao):
            num = obtem_dimensao_goban(goban)
            coluna = obtem_col(intersecao)
            linha = obtem_lin(intersecao)
            if num >= stringletras.index(coluna)+1>=1 and num >= linha >= 1:
                return True
    return False

def gobans_iguais(goban1,goban2):
    """
    Devolve True apenas se goban1 e goban2 forem gobans e forem iguais.

    :param goban1: Universal
    :param goban2: Universal
    :return: Boolean
    """
    if eh_goban(goban1) and eh_goban(goban2):
        goban1_dimensao = goban1[0]
        lista_intersecoes_brancas_goban1 = ordena_intersecoes(tuple(intersecao_branca_goban1) for intersecao_branca_goban1 in goban1[1])
        lista_intersecoes_pretas_goban1 = ordena_intersecoes(tuple(intersecao_preta_goban1) for intersecao_preta_goban1 in goban1[2])
        goban2_dimensao = goban2[0]
        lista_intersecoes_brancas_goban2 = ordena_intersecoes(tuple(intersecao_branca_goban2) for intersecao_branca_goban2 in goban2[1])
        lista_intersecoes_pretas_goban2 = ordena_intersecoes(tuple(intersecao_preta_goban2) for intersecao_preta_goban2 in goban2[2])
        if goban1_dimensao == goban2_dimensao and lista_intersecoes_brancas_goban1 == lista_intersecoes_brancas_goban2 and lista_intersecoes_pretas_goban1 == lista_intersecoes_pretas_goban2:
            return True
    return False

def goban_para_str(goban):
    """
    Devolve a cadeia de caracteres que representa o goban.

    :param goban: List
    :return: String
    """

    num = obtem_dimensao_goban(goban)
    string = "   "
    for coluna in range (0,num-1):
        string += f"{stringletras[coluna]} "
    string += f"{stringletras[num-1]}"
    final = string
    string += "\n"
    for linha in range(num,0,-1):
        if linha>= 10:
            string += f"{linha} "
            for coluna in range(num):
                if eh_pedra_branca(obtem_pedra(goban,cria_intersecao(stringletras[coluna],linha))):
                    string += "O "
                elif eh_pedra_preta(obtem_pedra(goban,cria_intersecao(stringletras[coluna],linha))):
                    string += "X "
                else:
                    string += ". "
            string += f"{linha}\n"
        else:
            string += f" {linha} "
            for coluna in range(num):
                if eh_pedra_branca(obtem_pedra(goban,cria_intersecao(stringletras[coluna],linha))):
                    string += "O "
                elif eh_pedra_preta(obtem_pedra(goban,cria_intersecao(stringletras[coluna],linha))):
                    string += "X "
                else:
                    string += ". "
            string += f" {linha}\n"
    string += final
    return string
    
def obtem_territorios(goban):
    """
    Devolve o tuplo formado pelos tuplos com as interseções de cada território de g. 
    A função devolve as interseções de cada território ordenadas em ordem de leitura 
    do tabuleiro de Go, e os territórios ordenados em ordem de leitura da primeira 
    interseção do territ ́orio.

    :param goban: List
    :return: Tuple
    """

    num = obtem_dimensao_goban(goban)
    porvisitar_nao_ordenado = ()
    porvisitar = []
    territorios = ()
    for coluna in range(0,num):
        coluna = stringletras[coluna]
        for linha in range(1,num+1):
            intersecao = cria_intersecao(coluna,linha)
            if not eh_pedra_jogador(obtem_pedra(goban,intersecao)):
                porvisitar_nao_ordenado += (intersecao,)                    #Adiciona todas as interseções livres do goban à lista porvisitar_nao_ordenado
    for intersecao_ordenada in ordena_intersecoes(porvisitar_nao_ordenado):
        porvisitar += [intersecao_ordenada,]                                #Adiciona as interseções por ordem de leitura de Go à lista porvisitar
    while len(porvisitar) != 0:                                             #Enquanto houver interseções por visitar, este loop corre
        intersecao_visitada = porvisitar[0]
        intersecoes_cadeia = obtem_cadeia(goban,intersecao_visitada)        #Obtém a cadeia da interseção que está a ser vista
        for intersecao in intersecoes_cadeia:
            porvisitar.remove(intersecao)                                   #Remove todas as interseções da cadeia daa lista porvisitar para não observar-mos a mesma cadeia duas vezes
        territorios += (intersecoes_cadeia,)                                #Adiciona a cadeia ao tuplo territórios
    return territorios

def obtem_adjacentes_diferentes(goban,tuplo_intersecoes):
    """
    Devolve o tuplo ordenado formado pelas interseções adjacentes às interseções do tuplo tuplo_intersecoes:
            (a) livres, se as interseções do tuplo estão ocupadas por pedras de jogador, isto é, as liberdades de uma cadeia de pedras;
            (b) ocupadas por pedras de jogador, se as interseções do tuplo estão livres, isto é, a fronteira de um território.

    :param goban: List
    :param tuplo_intersecoes: Tuple
    :return: Tuple
    """

    adjacentes_diferentes = ()
    for intersecao in tuplo_intersecoes:
        if eh_pedra_jogador(obtem_pedra(goban,intersecao)):
            adjacentes = obtem_intersecoes_adjacentes(intersecao,obtem_ultima_intersecao(goban))
            for intersecao_adjacente in adjacentes:
                if not eh_pedra_jogador(obtem_pedra(goban,intersecao_adjacente)):   #Se a intersecao visitada for de um jogador, então queremos retornar as interseções adjacentes que estão vazias
                    if intersecao_adjacente not in adjacentes_diferentes:
                        adjacentes_diferentes += (intersecao_adjacente,)
        else: 
            adjacentes = obtem_intersecoes_adjacentes(intersecao,obtem_ultima_intersecao(goban))
            for intersecao_adjacente in adjacentes:
                if eh_pedra_jogador(obtem_pedra(goban,intersecao_adjacente)):       #Caso contrário, caso a interseção visitada seja livre, queremos adicionar as interseções adjacentes que estiverem ocupadas pelos jogadores
                    if intersecao_adjacente not in adjacentes_diferentes:
                        adjacentes_diferentes += (intersecao_adjacente,)     
    return ordena_intersecoes(adjacentes_diferentes)    

def jogada(goban,intersecao,pedra):
    """
    Modifica destrutivamente o goban (argumento 1) colocando a pedra de jogador (pedra) na interseção (intersecao) 
    e remove todas as pedras do jogador contrário pertencentes a cadeias adjacentes à intersecão (intersecao) 
    sem liberdades, devolvendo o próprio goban.

    :param goban: List
    :param intersecao: Tuple
    :param pedra: String
    :return: List
    """

    porremover = []
    adjacentes_vazias = ()
    adjacentes = obtem_intersecoes_adjacentes(intersecao,obtem_ultima_intersecao(goban))
    for intersecao_adjacente in adjacentes:
        adjacentes_vazias = ()
        if obtem_pedra(goban,intersecao_adjacente) not in [pedra_para_str(pedra),"."]:  #Se as adjacentes forem ou livres, ou do outro jogador, então este loop corre, pois temos de verificar se temos de remover pedras que ficaram sem liberdade devido à jogada
            cadeia = obtem_cadeia(goban,intersecao_adjacente)
            adjacentes_diferentes = obtem_adjacentes_diferentes(goban,cadeia)
            for intersecao_adjacente_diferente in adjacentes_diferentes: 
                if not intersecoes_iguais(intersecao_adjacente_diferente,intersecao):
                    adjacentes_vazias += (intersecao_adjacente_diferente,)
            if adjacentes_vazias == ():                                     #Se não houverem interseções vazias junto à cadeia do outro jogador, então essas pedras ficaram sem liberdades, logo têm de ser removidas
                for intersecao_por_remover in cadeia:
                    if intersecao_por_remover not in porremover:
                        porremover += [intersecao_por_remover,]
    for intersecao_remover in porremover:
        remove_pedra(goban,intersecao_remover)
    return coloca_pedra(goban,intersecao,pedra)           

def obtem_extremos(goban,cadeia):
    """
    Função auxiliar que devolve os extremos de uma cadeia de pedras, isto é, as pedras de uma cadeia 
    cujas adjacentes não fazem parte da cadeia.

    :param goban: List
    :param cadeia: Tuple
    :return: List
    """

    extremos = []
    for intersecao in cadeia:
        adjacentes = obtem_intersecoes_adjacentes(intersecao,obtem_ultima_intersecao(goban))
        for intersecao_adjacente in adjacentes:
            if not pedras_iguais(obtem_pedra(goban,intersecao_adjacente), obtem_pedra(goban,intersecao)):
                if intersecao not in extremos:
                    extremos += [intersecao,]
    return extremos

def obtem_pedras_jogadores(goban):
    """
    Devolve um tuplo de dois inteiros que correspondem ao número de interseções ocupadas 
    por pedras do jogador branco e preto, respetivamente.

    :param goban: List
    :return: Tuple
    """
    pedras_brancas = 0
    pedras_pretas = 0
    num = obtem_dimensao_goban(goban)
    for linha in range(1,num+1):
        for coluna in range(num):
            letra = stringletras[coluna]
            intersecao = cria_intersecao(letra,linha)
            if eh_pedra_branca(obtem_pedra(goban,intersecao)):
                pedras_brancas += 1
            elif eh_pedra_preta(obtem_pedra(goban,intersecao)):
                pedras_pretas += 1
    return (pedras_brancas,pedras_pretas)

def calcula_pontos(goban):
    """
    Função auxiliar que recebe um goban e devolve o tuplo de dois inteiros com as 
    pontuações dos jogadores branco e preto, respetivamente.

    :param goban: List
    :return: Tuple
    """

    pontos_branco, pontos_preto = obtem_pedras_jogadores(goban)[0],obtem_pedras_jogadores(goban)[1]
    if pontos_branco != 0 or pontos_preto != 0:
        for territorio in obtem_territorios(goban):     #Verifica se o território é de um jogador, isto é, se a sua fronteira for ocupada apenas por pedras desse jogador
            fronteira = obtem_fronteira(goban,territorio)
            if fronteira_eh_jogador(goban,fronteira):
                simbolo_territorio = obtem_pedra(goban,fronteira[0])
                if eh_pedra_branca(simbolo_territorio):
                    pontos_branco += len(territorio)
                elif eh_pedra_preta(simbolo_territorio):
                    pontos_preto += len(territorio)
    return (pontos_branco,pontos_preto)

    
def obtem_fronteira(goban,territorio):
    """
    Função auxiliar que devolve a fronteira de um território (territorio).

    :param goban: List
    :param territorio: Tuple
    :return: List
    """

    fronteira = []
    extremos_territorio = obtem_extremos(goban,territorio)
    adjacentes = obtem_adjacentes_diferentes(goban,tuple(extremos_territorio))
    for intersecao_adjacente in adjacentes:
        if intersecao_adjacente not in fronteira:
            fronteira += [intersecao_adjacente,]
    return fronteira

def fronteira_eh_jogador(goban,fronteira):
    """
    Função auxiliar que devolve True se as pedras estão na fronteira de um 
    território são de um jogador e False se forem neutras.

    :param goban: List
    :param fronteira: List
    :return: Boolean
    """

    simbolo_fronteira = obtem_pedra(goban,fronteira[0])
    num_verificacoes = len(fronteira)
    verificacoes_feitas = 0
    for intersecao in fronteira:
        if pedras_iguais(obtem_pedra(goban,intersecao),simbolo_fronteira):
            verificacoes_feitas +=1 
    if verificacoes_feitas == num_verificacoes:
        return True
    return False
            
def eh_jogada_legal(goban,intersecao,pedra,goban_ilegal):
    """
    Função auxiliar que recebe um goban (argumento 1), uma interseção (intersecao), 
    uma pedra de jogador (pedra) e um outro goban (goban_ilegal) e devolve True se a jogada for 
    legal ou False caso contrário, sem modificar goban ou goban_ilegal. Para a deteção de repetição, 
    considera-se que goban_ilegal representa o estado de tabuleiro que não pode ser obtido 
    após a resolução completa da jogada.

    :param goban: List
    :param intersecao: Tuple
    :param pedra: String
    :param goban_ilegal: List
    :return: Boolean
    """
    if not eh_intersecao(intersecao) or not eh_intersecao_valida(goban,intersecao) or not eh_goban(goban):
        return False
    if eh_pedra_jogador(obtem_pedra(goban,intersecao)):
        return False
    goban_apos = jogada(cria_copia_goban(goban),intersecao,pedra)
    if gobans_iguais(goban_apos,goban_ilegal):
        return False
    goban_adicionar_antigo = cria_goban(9,ordena_intersecoes(obtem_pedras_brancas(goban)),ordena_intersecoes(obtem_pedras_pretas(goban)))
    goban_antigos.append(goban_adicionar_antigo)
    for goban_antigo in goban_antigos:
        if gobans_iguais(goban_apos,goban_antigo):
            return False
    cadeia = obtem_cadeia(goban_apos,intersecao)
    extremos = obtem_extremos(goban_apos,cadeia)
    fronteira = []
    verificacoes_feitas = 0
    for intersecao_extremo in extremos:
        adjacentes = obtem_intersecoes_adjacentes(intersecao_extremo,obtem_ultima_intersecao(goban_apos))
        for intersecao_adjacente in adjacentes:
            if not pedras_iguais(obtem_pedra(goban_apos,intersecao_adjacente),obtem_pedra(goban_apos,intersecao_extremo)) and eh_pedra_jogador(obtem_pedra(goban_apos,intersecao_adjacente))  and intersecao_adjacente not in fronteira and intersecao_adjacente not in cadeia:
                verificacoes_feitas += 1
            if intersecao_adjacente not in fronteira and intersecao_adjacente not in cadeia:
                fronteira += [intersecao_adjacente,]
    for intersecao_fronteira in fronteira:
        limite = len(obtem_intersecoes_adjacentes(intersecao_fronteira,obtem_ultima_intersecao(goban_apos))) 
        for intersecao_adjacente_fronteira in obtem_intersecoes_adjacentes(intersecao_fronteira,obtem_ultima_intersecao(goban_apos)):
            if pedras_iguais(obtem_pedra(goban_apos,intersecao_adjacente_fronteira),pedra_para_str(pedra)):
                limite -= 1
                if limite == 0:
                    return True
            else:
                if intersecao_adjacente_fronteira in obtem_cadeia(goban,intersecao_fronteira):
                    limite -=1                 
    if verificacoes_feitas == len(fronteira):
        return False
    return True
        
def turno_jogador(goban,pedra,goban_ilegal):
    """
    Função auxiliar que recebe um goban (argumento 1), uma pedra de jogador (pedra) e um 
    outro goban (goban_ilegal), e oferece ao jogador que joga com pedras pedra (argumento 2) 
    a opção de passar ou de colocar uma pedra própria numa interseção. Se o jogador passar, 
    a função devolve False sem modificar os argumentos. Caso contrário, a função devolve True e
    modifica destrutivamente o tabuleiro goban (argumento 1) de acordo com a jogada realizada. 
    A função apresenta a mensagem "Escreva uma intersecao ou 'P' para passar (símbolo do jogador):", 
    repetindo a mensagem até que o jogador introduza 'P' ou a representação externa de uma interseção do 
    tabuleiro de Go que corresponda a uma jogada legal. Considera-se que goban_ilegal representa o estado de 
    tabuleiro que não pode ser obtido após a resolução completa da jogada.

    :param goban: List
    :param pedra: String
    :param goban_ilegal: List
    :return: Boolean
    """

    while True:
        escolha = input(f"Escreva uma intersecao ou 'P' para passar [{pedra_para_str(pedra)}]:")
        if escolha == "P":
            return False
        if len(escolha) == 2:
            if escolha[0] in stringletras and escolha[1] in ["1","2","3","4","5","6","7","8","9"]:
                intersecao = str_para_intersecao(escolha)
                if eh_intersecao_valida(goban,intersecao):
                    if eh_jogada_legal(goban,intersecao,pedra,goban_ilegal):
                        jogada(goban,intersecao,pedra)
                        return True
        if len(escolha) == 3:
            if escolha[0] in stringletras and escolha[1] == "1" and escolha[2] in ["1","2","3","4","5","6","7","8","9","0"]:
                intersecao = str_para_intersecao(escolha)
                if eh_intersecao_valida(goban,intersecao):
                    if eh_jogada_legal(goban,intersecao,pedra,goban_ilegal):
                        jogada(goban,intersecao,pedra)
                        return True

def go(dimensao,tuplo_brancas,tuplo_pretas):
    """
    Função principal que permite jogar um jogo completo do Go de dois jogadores. 
    A função recebe um inteiro correspondente à dimensão do tabuleiro (dimensao), e dois
    tuplos potencialmente vazios com a representação externa das interseções ocupadas
    por pedras brancas (tuplo_brancas) e pretas (tuplo_pretas) inicialmente. O jogo termina 
    quando os dois jogadores passam a vez de jogar consecutivamente. A função devolve True se o 
    jogador com pedras brancas conseguir ganhar o jogo, ou False caso contrário. A função verifica 
    a validade dos seus argumentos, gerando um ValueError com a mensagem 'go: argumentos invalidos' 
    caso os seus argumentos não sejam válidos.

    :param dimensao: Integer
    :param tuplo_brancas: Tuple
    :param tuplo_pretas: Tuple
    :return: Boolean
    """

    if type(dimensao) != int or dimensao not in [9,13,19]:
        raise ValueError ("go: argumentos invalidos")
    if type(tuplo_brancas)!= tuple or type(tuplo_pretas)!= tuple:
        raise ValueError ("go: argumentos invalidos")
    if len(tuplo_brancas) != 0:
        for intersecao in tuplo_brancas:
            if type(intersecao) != str and type(intersecao) != tuple:
                raise ValueError ("go: argumentos invalidos")
            if len(intersecao) not in [2,3]:
                raise ValueError ("go: argumentos invalidos")
            else:
                if len(intersecao) == 2:
                    if intersecao[0] not in stringletras or str(intersecao[1]) not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]: #Se for um tuplo, intersecao[1] vai corresponder a um número de 1 ou 2 algarismos, se for uma string, intersecao[1] vai corresponder a um número de 1 algarismo 
                        raise ValueError ("go: argumentos invalidos")
                else:
                    if intersecao[0] not in stringletras or intersecao[1] != "1" or intersecao[2] not in ["1","2","3","4","5","6","7","8","9","0"]:
                        raise ValueError ("go: argumentos invalidos")
            if type(intersecao) == str:
                intersecao = str_para_intersecao(intersecao)
            if eh_intersecao(intersecao) and intersecao not in tuplo_pretas:
                if obtem_lin(intersecao) > dimensao or stringletras.index(obtem_col(intersecao)) > dimensao:
                    raise ValueError ("go: argumentos invalidos")
            else:
                raise ValueError ("go: argumentos invalidos")
    if len(tuplo_pretas) != 0:
        for intersecao in tuplo_pretas:
            if type(intersecao) != str and type(intersecao) != tuple:
                raise ValueError ("go: argumentos invalidos")
            if len(intersecao) not in [2,3]:
                raise ValueError ("go: argumentos invalidos")
            else:
                if len(intersecao) == 2:
                    if intersecao[0] not in stringletras or str(intersecao[1]) not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]: #Se for um tuplo, intersecao[1] vai corresponder a um número de 1 ou 2 algarismos, se for uma string, intersecao[1] vai corresponder a um número de 1 algarismo 
                        raise ValueError ("go: argumentos invalidos")
                else:
                    if intersecao[0] not in stringletras or intersecao[1] != "1" or intersecao[2] not in ["1","2","3","4","5","6","7","8","9","0"]:
                        raise ValueError ("go: argumentos invalidos")
            if type(intersecao) == str:
                intersecao = str_para_intersecao(intersecao)
            if eh_intersecao(intersecao) and intersecao not in tuplo_brancas:
                if obtem_lin(intersecao) > dimensao or stringletras.index(obtem_col(intersecao)) > dimensao:
                    raise ValueError ("go: argumentos invalidos")
            else:
                raise ValueError ("go: argumentos invalidos")
    goban = cria_goban(dimensao,tuplo_brancas,tuplo_pretas)
    vezes_passadas = 0
    jogador = 0 
    pontos_brancos = calcula_pontos(goban)[0]
    pontos_pretos = calcula_pontos(goban)[1]
    while vezes_passadas != 2:
        print(f"Branco (O) tem {pontos_brancos} pontos\nPreto (X) tem {pontos_pretos} pontos")
        print(goban_para_str(goban))
        if jogador == 0:
            if not turno_jogador(goban,cria_pedra_preta(),cria_goban_vazio(dimensao)):
                vezes_passadas += 1
                pontos_brancos = calcula_pontos(goban)[0]
                pontos_pretos = calcula_pontos(goban)[1]
            else:
                vezes_passadas = 0
                pontos_brancos = calcula_pontos(goban)[0]
                pontos_pretos = calcula_pontos(goban)[1]
            jogador += 1 
        else:
            if not turno_jogador(goban,cria_pedra_branca(),cria_goban_vazio(dimensao)):
                vezes_passadas += 1
                pontos_brancos = calcula_pontos(goban)[0]
                pontos_pretos = calcula_pontos(goban)[1]
            else:
                vezes_passadas = 0
                pontos_brancos = calcula_pontos(goban)[0]
                pontos_pretos = calcula_pontos(goban)[1]
            jogador = 0
    print(f"Branco (O) tem {pontos_brancos} pontos\nPreto (X) tem {pontos_pretos} pontos")
    print(goban_para_str(goban)) 
    if pontos_brancos > pontos_pretos:
        return True
    else:
        return False
    
def obtem_pedras_brancas(goban):
    """
    Função auxiliar que devolve uma lista com as interseções do goban (argumento) que têm pedras brancas.

    :param goban: List
    :return: List
    """
    
    return goban[1]

def obtem_pedras_pretas(goban):
    """
    Função auxiliar que devolve uma lista com as interseções do goban (argumento) que têm pedras pretas.

    :param goban: List
    :return: Tuple
    """

    return goban[2]

def obtem_dimensao_goban(goban):
    """
    Função auxiliar que devolve um inteiro que corresponde à dimensão do goban (argumento).

    :param goban: List
    :return: Integer
    """

    return goban[0]
