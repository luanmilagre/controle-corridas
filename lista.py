def somar_corridas(corridas):
    total = 0
    for v in corridas:
        total += v
    return total

def calcular_media(total, quantidade):
    return total / quantidade

def bateu_meta(total, meta):
    if total >= meta:
        return True
    else:
        return False

def valores_corrida():
    while True:
        try:
            valor = float(input("Digite o valor da corrida (Digite 0 para finalizar): "))
            if valor < 0:
                print("Valor não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Erro, digite somente números.")

def salvar_resultados(corridas, meta, total, media):
    with open("resultados.txt", "w") as f:
        f.write(f"Meta do dia: {meta}\n")
        f.write(f"Total de corridas: {len(corridas)}\n")
        f.write(f"Total ganho: {total}\n")
        f.write(f"Média por corrida: {media}\n")
        f.write(f"Maior corrida: {max(corridas)}\n")
        f.write(f"Menor corrida: {min(corridas)}\n")
        if total >= meta:
            f.write("Meta do dia batida!\n")
        else:
            f.write("Meta não batida!\n")

def ler_resultados():
    try:
        with open("resultados.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Nenhum resultado encontrado.")

# Código principal
corridas = []

meta = float(input("Digite qual vai ser a sua meta de hoje: "))
while True:
    valor = valores_corrida()
    if valor == 0:
        break
    corridas.append(valor)

total = somar_corridas(corridas)
print(f"Total do dia é: {total}")
print(f"Total de corridas feitas: {len(corridas)}")

if len(corridas) > 0:
    print(f"Maior corrida: {max(corridas)}")
    print(f"Menor corrida: {min(corridas)}")
    media = calcular_media(total, len(corridas))
    print(f"Média por corrida: {media}")
    
    if media >= 15:
        print("O dia foi bom")
    else:
        print("O dia foi fraco")

    if bateu_meta(total, meta):
        print("Meta do dia batida!")
    else:
        print("Meta não batida ainda, faça mais corridas")
else:
    print("Nenhuma corrida registrada.")
