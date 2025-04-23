# Importa a biblioteca matplotlib.pyplot para criação de gráficos
import matplotlib.pyplot as plt

def gerar_grafico(dados, tipo_grafico=1, titulo="Meu Gráfico", salvar=False):
    
    # Cria uma figura e um conjunto de eixos para o gráfico
    fig, ax = plt.subplots()
    
    # Verifica o tipo de gráfico selecionado
    if tipo_grafico == 1:
        # Gráfico de barras:
        # range(len(dados)) cria posições no eixo X (0, 1, 2, ...)
        # dados são os valores no eixo Y
        ax.bar(range(len(dados)), dados, color='blue')

        # Adiciona rótulos aos eixos
        ax.set_xlabel("Categorias")
        ax.set_ylabel("Valores")
    elif tipo_grafico == 2:
        # Gráfico de pizza:
        # dados são os valores de cada fatia
        # labels cria rótulos automáticos (Item 1, Item 2, ...)
        # autopct mostra porcentagens com 1 casa decimal
        ax.pie(dados, labels=[f'Item {i+1}' for i in range(len(dados))], autopct='%1.1f%%')
    else:
        # Tratamento de erro para tipo de gráfico inválido
        print("\nErro: Tipo de gráfico inválido! Digite apenas 1 ou 2.")
        print("Encerrando execução...\n")
        return False  
    
    ax.set_title(titulo) # Define o título
    plt.tight_layout() # Ajusta o layout para evitar sobreposições
    
    # Verifica se deve salvar o gráfico como imagem
    if salvar:
        nome_arquivo = titulo.replace(" ", "_").lower() + ".png"
        plt.savefig(nome_arquivo)
        print(f"Gráfico salvo como '{nome_arquivo}'!")
    
    # Exibe o gráfico na tela
    plt.show()

# Exemplo de uso
if __name__ == "__main__":

    print("\n")
    print("Opções de gráfico:")
    print("1 - Gráfico em barra")
    print("2 - Gráfico em pizza")
    print("\n")
    tipo=int(input("Escolha como quer seu gráfico (1 ou 2): "))

    print("\n")
    print("Digite os valores para o gráfico separando-os por espaço:")
    entrada = input("Exemplo: 10 25 80 43 --> ")
    # Converte a string de entrada em uma lista de números float
    dados = [float(x) for x in entrada.split()]

    # Chama a função principal para gerar o gráfico
    gerar_grafico(dados, tipo_grafico=tipo, titulo="Meu Gráfico", salvar=True)




