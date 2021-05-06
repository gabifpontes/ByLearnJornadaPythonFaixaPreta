# Calculando o IMC

def calculo_imc(peso, altura):
  imc = peso / (altura ** 2)
  return imc

def classificacao(imc):
    if imc < 18.5:
      return "Baixo Peso"
    elif imc >= 18.5 and imc < 25:
      return "Peso Normal"    
    elif imc >= 25 and imc < 30:
      return "Sobrepeso"    
    elif imc >= 30 and imc < 35:
      return "Obesidade Grau I"    
    elif imc >= 35 and imc < 40:
      return "Obesidade Severa (Grau II)"    
    else:
      return "Obesidade Mórbida (Grau III)"

peso = float(input("Qual é o seu peso (kg)? "))
altura = float(input("Qual é a sua altura (m²)? "))

meu_imc = calculo_imc(peso, altura)

print('Seu IMC é ', meu_imc, 'e sua condição é ', classificacao(meu_imc))
