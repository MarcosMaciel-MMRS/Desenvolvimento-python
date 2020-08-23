#um progama que recebe á altura e a largura de uma parede em metros,
#e informe quantos litros serão precisos para pintar a msm.
paredel = float(input('Informe a largura da parede:'))
paredeh = float(input('Informe a altura da parede:'))
area = paredeh*paredel
litros = area/2

print('A sua parede de diametro {}x{}, e possui uma área em metros de {}m²'.format(paredeh, paredel, area))
print('Será preciso {}L de tinta para pintala.'.format(litros))