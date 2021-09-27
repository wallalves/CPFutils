def check_cpf(cpf):

    #inciando as variaveis de somatorio
    soma_a = soma_b = 0

    # Calcula o primeiro digito verificador 
                
    for n in range(9):
        soma_a += ((n+1)*int(cpf[n]))
    check_a = "0" if (soma_a%11 == 10) else str(soma_a%11)

    # Calcula o segundo digito verificador
    for m in range(10):
            soma_b += ((m)*int(cpf[m]))
    check_b = "0" if (soma_b%11 == 10) else str(soma_b%11)

    # Verifica se os dois digitos estão iguais aos calculados
    if(check_a == cpf[9] and check_b == cpf[10]):
        return True
    else:
        return False
