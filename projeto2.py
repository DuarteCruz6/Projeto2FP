global stringletras
stringletras = "ABCDEFGHIJKLMNOPQRS"

def cria_intersecao(coluna,linha):
    if type(coluna) != str or len(coluna)!=1 or coluna not in stringletras:
        raise ValueError ("cria_intersecao: argumentos invalidos")
    if type(linha) != int or linha < 1 or linha > 19:
        raise ValueError ("cria_intersecao: argumentos invalidos")
    return (coluna,linha)

def obtem_col(intersecao):
    return intersecao[0]

def obtem_lin(intersecao):
    return int(intersecao[1])

def eh_intersecao(intersecao):
    if len(intersecao) == 2:
        coluna = obtem_col(intersecao)
        if type(coluna) == str and coluna in stringletras:
            linha = obtem_lin(intersecao)
            if type(linha)== int and linha >= 1 and linha <= 19:
                return True
    return False

def intersecoes_iguais(i1,i2):
    if eh_intersecao(i1) and eh_intersecao(i2):
        if i1 == i2:
            return True
    return False

def intersecao_para_str(intersecao):
    coluna = obtem_col(intersecao)
    linha = obtem_lin(intersecao)
    return f"{coluna}{linha}"

def str_para_intersecao(string):
    coluna = string[0]
    linha = int(string[1:])
    return (coluna,linha)

def obtem_intersecoes_adjacentes(intersecao,intersecao_max):
    adjacentes = ()
    coluna = obtem_col(intersecao)
    linha = obtem_lin(intersecao)
    coluna_max = obtem_col(intersecao_max)
    linha_max = obtem_lin(intersecao_max)
    if coluna != "A":
        coluna_adjacente = stringletras[stringletras.index(coluna)-1]
        adjacentes += ((coluna_adjacente,linha),)
    if coluna != coluna_max:
        coluna_adjacente = stringletras[stringletras.index(coluna)+1]
        adjacentes += ((coluna_adjacente,linha),)
    if linha != 1:
        linha_adjacente = linha - 1
        adjacentes += ((coluna,linha_adjacente),)
    if linha != linha_max:
        linha_adjacente = linha + 1
        adjacentes += ((coluna,linha_adjacente),)
    return ordena_intersecoes(adjacentes)

def ordenador(intersecao):
    return intersecao[1], intersecao[0]

def ordena_intersecoes(tuplo_intersecoes):
    return sorted(tuplo_intersecoes, key = ordenador)

def cria_pedra_branca():
    return "pedra branca"

def cria_pedra_preta():
    return "pedra preta"

def cria_pedra_neutra():
    return "pedra neutra"

def eh_pedra(arg):
    if arg in ["pedra branca", "pedra preta", "pedra neutra"]:
        return True
    return False

def eh_pedra_branca(pedra):
    if pedra == "pedra branca" or pedra == "O":
        return True
    return False

def eh_pedra_preta(pedra):
    if pedra == "pedra preta" or pedra == "X":
        return True
    return False

def pedras_iguais(pedra1, pedra2):
    if pedra1 == pedra2 and eh_pedra(pedra1):
        return True
    return False

def pedra_para_str(pedra):
    if eh_pedra_branca(pedra):
        return "O"
    elif eh_pedra_preta(pedra):
        return "X"
    else:
        return "."
    
def eh_pedra_jogador(pedra):
    if eh_pedra_preta(pedra):
        return True
    elif eh_pedra_branca(pedra):
        return True
    return False

def cria_goban_vazio(num):
    if type(num) == int and num in [9,13,19]:
        return [num,[],[]]
    else:
        raise ValueError ("cria_goban_vazio: argumento invalido")
    
def cria_goban(num,tuplo_intersecoes_brancas,tuplo_intersecoes_pretas):
    lista_intersecoes_brancas = []
    lista_intersecoes_pretas = []
    if type(num) != int or num not in [9,13,19]:
        raise ValueError ("cria_goban: argumentos invalidos")
    for intersecao in tuplo_intersecoes_brancas:
        if eh_intersecao(intersecao):
            if obtem_lin(intersecao) > num:
                raise ValueError ("cria_goban: argumentos invalidos")
            else:
                lista_intersecoes_brancas += [intersecao,]
        else:
            raise ValueError ("cria_goban: argumentos invalidos")
    for intersecao in tuplo_intersecoes_pretas:
        if eh_intersecao(intersecao):
            if obtem_lin(intersecao) > num:
                raise ValueError ("cria_goban: argumentos invalidos")
            else:
                lista_intersecoes_pretas += [intersecao,]
        else:
            raise ValueError ("cria_goban: argumentos invalidos")
    goban = [num,lista_intersecoes_brancas,lista_intersecoes_pretas]
    return goban

def cria_copia_goban(goban):
    num = goban[0]
    intersecoes_brancas = goban[1].copy()
    intersecoes_pretas = goban[2].copy()
    return [num,intersecoes_brancas,intersecoes_pretas]

def obtem_ultima_intersecao(goban):
    num = goban[0]
    letra = stringletras[num-1]
    return (letra,num)

def obtem_pedra(goban,intersecao):
    intersecoes_brancas = goban[1]
    intersecoes_pretas = goban[2]
    if intersecao in intersecoes_brancas:
        return "O"
    elif intersecao in intersecoes_pretas:
        return "X"
    else:
        return "."

def obtem_intersecao_maxima(goban):
    num = goban[0]
    return (stringletras[num-1],num)
    
def obtem_cadeia(goban,intersecao):
    num = goban[0]
    intersecao_max = obtem_intersecao_maxima(goban)
    simbolo_cor = obtem_pedra(goban,intersecao)
    porvisitar = [intersecao,]
    visitadas = []
    cadeia = (intersecao,)
    while len(porvisitar) != 0:
        intersecao_visitada = porvisitar[0]
        adjacentes = obtem_intersecoes_adjacentes(intersecao_visitada,intersecao_max)
        for intersecao_adjacente in adjacentes:
            if obtem_pedra(goban,intersecao_adjacente) == simbolo_cor and (intersecao_adjacente not in cadeia):
                porvisitar += [intersecao_adjacente,]
                cadeia += (intersecao_adjacente,)
        visitadas += [intersecao_visitada,]
        porvisitar.remove(intersecao_visitada)
    return ordena_intersecoes(cadeia)

def coloca_pedra(goban,intersecao,pedra):
    num = goban[0]
    pedras_brancas = goban[1]
    pedras_pretas = goban[2]
    if eh_pedra_branca(pedra):
        pedras_brancas.append(intersecao)
    elif eh_pedra_preta(pedra):
        pedras_pretas.append(intersecao)     
    return [num,pedras_brancas,pedras_pretas]
    
def remove_pedra(goban,intersecao):
    if obtem_pedra(goban,intersecao)=="O":
        num = goban [0]
        pedras_brancas = goban[1]
        pedras_brancas.remove(intersecao)
        pedras_pretas = goban[2]
    else:
        num = goban [0]
        pedras_brancas = goban[1]
        pedras_pretas = goban[2]
        pedras_pretas.remove(intersecao)
    return cria_goban(num,pedras_brancas,pedras_pretas)

def remove_cadeia(goban,cadeia):
    for intersecao in cadeia:
        goban = remove_pedra(goban,intersecao)
    return goban

def eh_goban(arg):
    if len(arg) == 3:      
        num = arg[0]
        lista_intersecoes_brancas = arg[1]
        lista_intersecoes_pretas = arg[2]
        if type(num) == int and num in [9,13,19]:
            if len(lista_intersecoes_brancas) != 0:
                for intersecao in lista_intersecoes_brancas:
                    if eh_intersecao(intersecao):
                        if obtem_lin(intersecao) == num:
                            if len(lista_intersecoes_pretas) != 0:
                                for intersecao in lista_intersecoes_pretas:
                                    if eh_intersecao(intersecao):
                                        if obtem_lin(intersecao) == num:
                                            return True
                            else:
                                return True
            else:
                return True
    return False

def eh_intersecao_valida(goban,intersecao):
    if eh_goban(goban):
        if eh_intersecao(intersecao):
            num = goban[0]
            coluna = obtem_col(intersecao)
            linha = obtem_lin(intersecao)
            if num >= stringletras.index(coluna) and num >= linha:
                return True
    return False

def gobans_iguais(goban1,goban2):
    if eh_goban(goban1) and eh_goban(goban2):
        if goban1 == goban2:
            return True
    return False

def goban_para_str(goban):
    num = goban[0]
    lista_pedras_brancas = goban[1]
    lista_pedras_pretas = goban[2]
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
                if (stringletras[coluna],linha) in lista_pedras_brancas:
                    string += "O "
                elif (stringletras[coluna],linha) in lista_pedras_pretas:
                    string += "X "
                else:
                    string += ". "
            string += f"{linha}\n"
        else:
            string += f" {linha} "
            for coluna in range(num):
                if (stringletras[coluna],linha) in lista_pedras_brancas:
                    string += "O "
                elif (stringletras[coluna],linha) in lista_pedras_pretas:
                    string += "X "
                else:
                    string += ". "
            string += f" {linha}\n"
    string += final
    return string
    
def obtem_territorios(goban):
    num = goban[0]
    lista_intersecoes_brancas = goban[1]
    lista_intersecoes_pretas = goban[2]
    porvisitar = []
    territorios = ()
    for coluna in range(0,num):
        coluna = stringletras[coluna]
        for linha in range(1,num+1):
            intersecao = (coluna,linha)
            if intersecao not in (lista_intersecoes_brancas and lista_intersecoes_pretas):
                porvisitar += [intersecao,]
    while len(porvisitar) != 0:
        intersecao_visitada = porvisitar[0]
        intersecoes_cadeia = obtem_cadeia(goban,intersecao_visitada)
        for intersecao in intersecoes_cadeia:
            porvisitar.remove(intersecao)
        territorios += (intersecoes_cadeia,)
    return territorios

def obtem_adjacentes_diferentes(goban,tuplo_intersecoes):
    num = goban[0]
    lista_intersecoes_brancas = goban[1]
    lista_intersecoes_pretas = goban[2]
    adjacentes_diferentes = ()
    for intersecao in tuplo_intersecoes:
        if intersecao in lista_intersecoes_brancas or intersecao in lista_intersecoes_pretas:
            adjacentes = obtem_intersecoes_adjacentes(intersecao,obtem_intersecao_maxima(goban))
            for intersecao_adjacente in adjacentes:
                if intersecao_adjacente not in lista_intersecoes_brancas and intersecao_adjacente not in lista_intersecoes_pretas:
                    adjacentes_diferentes += (intersecao_adjacente,)
        else: 
            adjacentes = obtem_intersecoes_adjacentes(intersecao,obtem_intersecao_maxima(goban))
            for intersecao_adjacente in adjacentes:
                if intersecao_adjacente in lista_intersecoes_brancas or intersecao_adjacente in lista_intersecoes_pretas:
                    adjacentes_diferentes += (intersecao_adjacente,)     
    return ordena_intersecoes(adjacentes_diferentes)    

def jogada(goban,intersecao,pedra):
    porremover = []
    adjacentes = obtem_intersecoes_adjacentes(intersecao,obtem_intersecao_maxima(goban))
    for intersecao_adjacente in adjacentes:
        if obtem_pedra(goban,intersecao_adjacente) not in [pedra_para_str(pedra),"."]:
            cadeia = obtem_cadeia(goban,intersecao_adjacente)
            for intersecao_cad in cadeia:
                adjacentes_cad = obtem_intersecoes_adjacentes(intersecao_cad,obtem_intersecao_maxima(goban))
                for adjacente_da_cadeia in adjacentes_cad:
                    if obtem_pedra(goban,adjacente_da_cadeia) == pedra_para_str(pedra):
                        if intersecao_cad not in porremover:
                            porremover += [intersecao_cad]
    if porremover == obtem_extremos(goban,cadeia):
        for intersecao_cad in cadeia:
            remove_pedra(goban,intersecao_cad)
    else:
        for intersecao_remover in porremover:
                    remove_pedra(goban,intersecao_remover)         
    return coloca_pedra(goban,intersecao,pedra)

def obtem_extremos(goban,cadeia):
    extremos = []
    for intersecao in cadeia:
        adjacentes = obtem_intersecoes_adjacentes(intersecao,obtem_intersecao_maxima(goban))
        for intersecao_adjacente in adjacentes:
            if obtem_pedra(goban,intersecao_adjacente) != obtem_pedra(goban,intersecao):
                if intersecao not in extremos:
                    extremos += [intersecao,]
    return extremos

def obtem_pedras_jogadores(goban):
    lista_intersecoes_brancas = goban[1]
    lista_intersecoes_pretas = goban[2]
    return (len(lista_intersecoes_brancas),len(lista_intersecoes_pretas))

def calcula_pontos(goban):
    pontos_total_pedras = obtem_pedras_jogadores(goban)
    pontos_branco = pontos_total_pedras[0]
    pontos_preto = pontos_total_pedras[1]
    for territorio in obtem_territorios(goban):     #Território é de um jogador se a sua fronteira for ocupada apenas por pedras desse jogador
        fronteira = obtem_fronteira(goban,territorio)
        if fronteira_eh_jogador(goban,fronteira):
            simbolo_fronteira = obtem_pedra(goban,fronteira[0])
            if simbolo_fronteira == "O":
                pontos_branco += len(fronteira)
            elif simbolo_fronteira == "X":
                pontos_preto += len(fronteira)
    return (pontos_branco,pontos_preto)

    
def obtem_fronteira(goban,territorio):
    fronteira = []
    extremos_territorio = obtem_extremos(goban,territorio)
    adjacentes = obtem_adjacentes_diferentes(goban,extremos_territorio)
    for intersecao_adjacente in adjacentes:
        if intersecao_adjacente not in fronteira:
            fronteira += [intersecao_adjacente,]
    return fronteira

def fronteira_eh_jogador(goban,fronteira):
    simbolo_fronteira = obtem_pedra(goban,fronteira[0])
    num_verificacoes = len(fronteira)
    verificacoes_feitas = 0
    for intersecao in fronteira:
        if obtem_pedra(goban,intersecao) == simbolo_fronteira:
            verificacoes_feitas +=1 
    if verificacoes_feitas == num_verificacoes:
        return True
    return False
            
def eh_jogada_legal(goban,intersecao,pedra,goban_ilegal):
    if obtem_pedra(goban,intersecao) != ".":
        return False
    goban_apos = coloca_pedra(cria_copia_goban(goban),intersecao,pedra)
    if goban_apos == goban_ilegal:
        return False
    cadeia = obtem_cadeia(goban_apos,intersecao)
    extremos = obtem_extremos(goban_apos,cadeia)
    fronteira = []
    verificacoes_feitas = 0
    for intersecao_extremo in extremos:
        adjacentes = obtem_intersecoes_adjacentes(intersecao_extremo,obtem_intersecao_maxima(goban_apos))
        for intersecao_adjacente in adjacentes:
            if obtem_pedra(goban_apos,intersecao_adjacente) != obtem_pedra(goban_apos,intersecao_extremo) and obtem_pedra(goban_apos,intersecao_adjacente) != "."  and intersecao_adjacente not in fronteira and intersecao_adjacente not in cadeia:
                verificacoes_feitas += 1
            if intersecao_adjacente not in fronteira and intersecao_adjacente not in cadeia:
                fronteira += [intersecao_adjacente,]
    for intersecao_fronteira in fronteira:
        for intersecao_adjacente_fronteira in obtem_intersecoes_adjacentes(intersecao_fronteira,obtem_intersecao_maxima(goban_apos)):
            if obtem_pedra(goban_apos,intersecao_adjacente_fronteira) == pedra_para_str(pedra) and intersecao_adjacente_fronteira not in cadeia:
                return True            
    if verificacoes_feitas == len(fronteira):
        return False
    return True
        
def turno_jogador(goban,pedra,goban_ilegal):
    while True:
        jogada = input(f"Escreva uma intersecao ou 'P' para passar [{pedra_para_str(pedra)}]:")
        if jogada == "P":
            return False
        elif eh_intersecao_valida(goban,str_para_intersecao(jogada)):
            intersecao = str_para_intersecao(jogada)
            if eh_jogada_legal(goban,intersecao,pedra,goban_ilegal):
                coloca_pedra(goban,intersecao,pedra)
                return True

def go(dimensao,tuplo_brancas,tuplo_pretas):
    goban = cria_goban(dimensao,tuplo_brancas,tuplo_pretas)
    if type(dimensao) != int or dimensao not in [9,13,19]:
        raise ValueError ("go: argumentos invalidos")
    if type(tuplo_brancas)!= tuple or type(tuplo_pretas)!= tuple:
        raise ValueError ("go: argumentos invalidos")
    for intersecao in tuplo_brancas:
        if not(eh_intersecao_valida(goban,intersecao) and eh_intersecao(intersecao)):
            raise ValueError ("go: argumentos invalidos")
        if intersecao in tuplo_pretas:
            raise ValueError ("go: argumentos invalidos")
    for intersecao in tuplo_pretas:
        if not(eh_intersecao_valida(goban,intersecao) and eh_intersecao(intersecao)):
            raise ValueError ("go: argumentos invalidos")
        if intersecao in tuplo_brancas:
            raise ValueError ("go: argumentos invalidos")
    vezes_passadas = []
    while len(vezes_passadas) != 2:
        if turno_jogador(goban,cria_pedra_preta(),cria_goban_vazio(dimensao)) == False:
            vezes_passadas += [1,]
            pontos_brancos = calcula_pontos(goban)[0]
            pontos_pretos = calcula_pontos(goban)[1]
        else:
            vezes_passadas = []
            pontos_brancos = calcula_pontos(goban)[0]
            pontos_pretos = calcula_pontos(goban)[1]
        print(f"Branco (O) tem {pontos_brancos} pontos\nPreto (X) tem {pontos_pretos} pontos")
        print(goban_para_str(goban))
    if pontos_brancos > pontos_pretos:
        return True
    else:
        return False