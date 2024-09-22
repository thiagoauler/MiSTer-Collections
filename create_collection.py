import sys

# Verifica se há argumentos passados
if len(sys.argv) > 1:
    # sys.argv[0] é o nome do script
    # sys.argv[1] é o primeiro argumento passado
    argumento = sys.argv[1]
    print(f"Argumento recebido: {argumento}")
else:
    print("Nenhum argumento foi passado.")