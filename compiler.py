# -*- coding:utf-8 -*-

from posixpath import lexists
import re
import sys, os
from tokens import DIC_TOKENS, PALAVRA_RESERVADA 

# Variáveis Globais
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(PROJECT_PATH)
ARQUIVO_CODIGO = ''
COUNT_COLUNA = 0
COUNT_LINHA = 0
COUNT_QTD_CARACTER = 0
C = ''
LEX = ''
TK = ''


def proxC():
    global COUNT_LINHA, COUNT_COLUNA, C, COUNT_QTD_CARACTER
    COUNT_COLUNA += 1
    if C == '\n':
        COUNT_LINHA += 1
        COUNT_COLUNA = 1

    try:
        C = ARQUIVO_CODIGO[COUNT_QTD_CARACTER]
        COUNT_QTD_CARACTER += 1
    except:
        C = -1  # Fim do arquivo
        return
    print(C)

def getToken():
    global LEX, TK
    estado = 0
    while True:
        LEX += C
        if estado == 0:
            if C >= 'a' and C <= 'z' or C >= 'A' and C <= 'Z' or C == '_':
                proxC()
                estado = 1
                continue
            if C >= '0' and C <= '9':
                proxC()
                while C >= '0' and C <='9':
                    LEX += C
                    proxC()
                if C == '.':
                    LEX += C
                    proxC()
                    while C >= '0' and C <= '9':
                        LEX += C
                        proxC()
                    # lex[posl] = \0;
                    TK = DIC_TOKENS['TKCteDouble']
                    return
                else:
                    # lex[posl] = \0;
                    TK = DIC_TOKENS['TKCteInt']
                    return
            if C == ',':
                # lex[posl] = \0;
                proxC()
                TK = DIC_TOKENS['TKVirgula']
                return
            if C == '.':
                # lex[posl] = \0;
                proxC()
                TK = DIC_TOKENS['TKPonto']
                return
            if C == ':':
                # lex[posl] = \0;
                proxC()
                TK = DIC_TOKENS['TKDoisPontos']
                return
            if C == ';':
                # lex[posl] = \0;
                proxC()
                TK = DIC_TOKENS['TKPontoEVirgula']
                return
            if C == '(':
                # lex[posl] = \0;
                proxC()
                TK = DIC_TOKENS['TKAbreParenteses']
                return
            if C == ')':
                # lex[posl] = \0;
                proxC()
                TK = DIC_TOKENS['TKFechaParenteses']
                return
            if C == '[':
                # lex[posl] = \0;
                proxC()
                TK = DIC_TOKENS['TKAbreColchete']
                return
            if C == ']':
                # lex[posl] = \0;
                proxC()
                TK = DIC_TOKENS['TKFechaColchete']
                return
            if C == '{':
                # lex[posl] = \0;
                proxC()
                TK = DIC_TOKENS['TKAbreChaves']
                return
            if C == '}':
                # lex[posl] = \0;
                proxC()
                TK = DIC_TOKENS['TKFechaChaves']
                return
            if C == '+':
                proxC()
                if C == '+':
                    LEX += '+'
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKDuploMais']
                    return
                elif C == '=':
                    LEX += '='
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKMaisIgual']
                    return
                else:
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKSoma']
                    return
            if C == '-':
                proxC()
                if C == '-':
                    LEX += '-'
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKDuploMenos']
                    return
                elif C == '=':
                    LEX += '='
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKMenosIgual']
                    return
                elif C == '>':
                    LEX += '>'
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKStructAcesso']
                    return
                else:
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKMenos']
                    return
            if C == '*':
                proxC()
                if C == '=':
                    LEX += '='
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKMultIgual']
                    return
                else:
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKMult']
                    return
            if C == '/':
                proxC()
                if C == '=':
                    LEX += '='
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKDivIgual']
                    return
                else:
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKDiv']
                    return
            if C == '%':
                proxC()
                if C == '=':
                    LEX += '='
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKRestoIgual']
                    return
                else:
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKResto']
                    return
            if C == '=':
                proxC()
                if C == '=':
                    LEX += '='
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKCompare']
                    return
                else:
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKIgual']
                    return
            if C == '!':
                proxC()
                if C == '=':
                    LEX += '='
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKDiferent']
                    return
                else:
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKLogicalNot']
                    return
            if C == '<':
                proxC()
                if C == '<':
                    proxC()
                    LEX += '<'
                    if C == '=':  # <<=
                        LEX += '='
                        # lex[posl] = \0;
                        proxC()
                        TK = DIC_TOKENS['TKBitWiseLeftShiftIgual']
                        return
                    else:
                        # lex[posl] = \0;
                        proxC()
                        TK = DIC_TOKENS['TKBitWiseLeftShift']
                        return
                elif C == '=':  # <=
                    LEX += '='
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKMenorIgual']
                    return
                else:
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKMenor']
                    return
            if C == '>':
                proxC()
                if C == '>':
                    proxC()
                    LEX += '>'
                    if C == '=':  # <<=
                        LEX += '='
                        # lex[posl] = \0;
                        proxC()
                        TK = DIC_TOKENS['TKBitwiseRightShiftIgual']
                        return
                    else:
                        # lex[posl] = \0;
                        proxC()
                        TK = DIC_TOKENS['TKBitWiseRightShift']
                        return
                elif C == '=':  # <=
                    LEX += '='
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKMaiorIgual']
                    return
                else:
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKMaior']
                    return
            if C == '&':
                proxC()
                if C == '&':
                    LEX += '&'
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKLogicalAnd']
                    return
                elif C == '=':
                    LEX += '='
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKBitWiseAndIgual']
                    return
                else:
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKBitWiseAnd']
                    return
            if C == '|':
                proxC()
                if C == '|':
                    LEX += '|'
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKLogicalOr']
                    return
                elif C == '=':
                    LEX += '='
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKBitWiseOrIgual']
                    return
                else:
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKBitWiseOr']
                    return
            if C == '^':
                proxC()
                if C == '=':
                    LEX += '='
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKBitWiseXorIgual']
                    return
                else:
                    # lex[posl] = \0;
                    proxC()
                    TK = DIC_TOKENS['TKBitWiseXor']
                    return
            if C == '~':
                # lex[posl] = \0;
                proxC()
                TK = DIC_TOKENS['TKBitWiseNot']
                return
            if C == "":
                proxC()
                if C >= 'a' and C <='Z' or C >= 'A' and C <= 'Z':
                    LEX += C
                    proxC()
                    if C == "":
                        LEX += ""
                        proxC()
                        TK = DIC_TOKENS['TKAspasSimples']
                        return
            if C == '' or C == '\t' or C == '\r':
                proxC()
                break
            if C == '\n':
                proxC()
                break
            if C == -1:
                 # lex[posl] = \0;
                proxC()
                TK = DIC_TOKENS['TKFimArquivo']
                return
            if C == '\0':
                 # lex[posl] = \0;
                proxC()
                TK = DIC_TOKENS['TKFimArquivo']
                return
            print("Erro léxico: encontrou o caractere %s (%s).\n" % (C,C))
            while C != '\n': 
                proxC()
            break
        if estado == 1:
            if C >= 'a' and C <= 'z' or C >= 'A' and C <= 'Z' or C == '_' or C >= '0' and C <= '9':
                proxC()
                break
            # lex[posl] = \0;
            if PALAVRA_RESERVADA.get(LEX):
                TK = PALAVRA_RESERVADA[LEX]
            else:
                TK = DIC_TOKENS['TKId']
            return
				





if __name__ == "__main__":
    
    ARQUIVO_CODIGO = open(PROJECT_PATH + '\prog.txt', 'r').read()
    proxC()
    getToken()
    print(TK)