#criar uma tuple com os 20 primeiros colocados do brasileirão, na ordem de colocação. 
#depois mostre: A- Os 5 primeiros; B- Os últimos 4 colocados
#C- times em ordem alfabética; D- Em qual posição está o time chapecoense. 
#como 2020 nao teve brasileirão ate o momento, estou usando a tabela de 2019. 
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('-='*20)        
print(f'Lista do Brasileirão: {times}')
print('-='*20)
print(f'Os 5 primeiros colocados : {times[0:5]}')
print('-='*20)
print(f'Os lanterninhas : {times[16:]}')
print('-='*20)
print(f'Times em Ordem Alfabética: {sorted(times)}')
print('-='*20)
print(f'O time da Chapecoense está na posição : {times.index("Chapecoense")+1}ª Posição')
print('-='*20)
