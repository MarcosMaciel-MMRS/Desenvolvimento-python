#converter medidas
n = float(input('informe uma distância em metros: '))
km = n/1000
hm = n/100
dam = n/10
dm = n*10
cm = n*100
mm = n*1000
print('A medida de {} correspondente a :'.format(n))
print('é igual á {}km.\n igual a {}hm. \n igual a {}dam.'.format(km,hm,dam))
print(' igual a {}dm. \n igual a {}cm. \n igual a {}mm.'.format(dm,cm,mm))