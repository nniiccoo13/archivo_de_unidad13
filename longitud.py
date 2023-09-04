def metros_a_pulgadas(metros):
    return metros * 39.37

def pulgadas_a_pies(pulgadas):
    return pulgadas / 12

if __name__ =="__main__":
    metros=int(input("Ingrese la cantidad en metros: "))
    pulgadas = metros_a_pulgadas(metros)
    print(f"{metros} metros equivale a {pulgadas:.2f} pulgadas")
    