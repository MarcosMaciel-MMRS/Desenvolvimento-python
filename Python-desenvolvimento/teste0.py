nome=input("Digite seu nome: ")
quantsim=0
quantnao=0
resposta=int(input("\nVamos começar?\nSe sim digite 1, se não digite 0\n"))
while True: 
    if resposta==0:
        print("ok, tchau!")
        break
    else:
        resposta==1
        print("ok, vamos lá!")
    print("Vamos saber agora se vc é ou não um psicopata\n")

    print("I- Vc gosta de tomar café sem açúcar e forte?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("II- Vc se sente bem em ver animais mortos?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1
    

    print("III- Vc prefere banhos frios a banhos quentes?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("IV- Vc é proprenso a desobedecer fácil as leis?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("V- Vc quase não sente culpa ou remorso?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("VI- Vc tende a ter atos violentos?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("VII- Vc não se apega fácil?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("VIII- É difícil sentir empatia?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("IX- Vc acha que tem boa lábia?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("X- Vc mente com frequência?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("XI- Vc sente muita sede por adrenalina?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("XII- Vc acha tem pavio curto?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("XIII- Vc geralmente age por impulso?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("XIV- Vc costuma ser mais afastado das pessoas?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("XV- Vc se acha irresponsavel?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("XVI- Vc tem um histórico de problemas comportamentais na infância?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("XVII- Vc tem um estilo de vida parasita, está sempre tirando proveito dos outros?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("XVIII- Vc já teve muitas relações conjugais de curto prazo?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("XIX- Vc necessita de estimulação constante, não gosta de monotonia e tem propensão ao tédio?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1

    print("XX- Vc não assume a responsabilidade por suas próprias ações, coloca sempre a culpa em outras pessoas?\n1- SIM\n2- NÃO\n ")    
    resp=int(input("Digite o número da resposta correspondente:\n"))
    if resp == 1:
        quantsim += 1
    else:
        quantnao += 1
    
    
    if quantsim > 10 and quantnao <= 9:
        print(nome, "vc é um psicopata!")
        break
    elif quantsim < 10 and quantnao >= 11:
        print(nome, "vc não é um psicopata!")
        break
    else:
        quantsim == 10 and quantnao == 10
        print(nome, "vc tá quase lá...")
        break
        