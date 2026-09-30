"""
Interface Interativa para Rail Fence Cipher
Menu para criptografar e descriptografar mensagens
"""

from rail_fence_cipher import RailFenceCipher


def exibir_menu():
    """Exibe o menu principal"""
    print("\n" + "=" * 60)
    print("SISTEMA DE CRIPTOGRAFIA RAIL FENCE CIPHER")
    print("=" * 60)
    print("\n1. Criptografar Mensagem")
    print("2. Descriptografar Mensagem")
    print("3. Visualizar Processo de Criptografia")
    print("4. Exemplos Predefinidos")
    print("5. Sair")
    print("\n" + "=" * 60)


def criptografar():
    """Função para criptografar uma mensagem"""
    print("\n--- CRIPTOGRAFAR MENSAGEM ---")
    
    try:
        num_trilhos = int(input("Digite o número de trilhos (2 ou mais): "))
        mensagem = input("Digite a mensagem a criptografar: ")
        
        if not mensagem:
            print("❌ Erro: Mensagem não pode estar vazia!")
            return
        
        cipher = RailFenceCipher(num_trilhos)
        criptografada = cipher.encrypt(mensagem)
        
        print(f"\n✅ Criptografia Realizada!")
        print(f"Mensagem Original:      {mensagem}")
        print(f"Mensagem Criptografada: {criptografada}")
        
    except ValueError as e:
        print(f"❌ Erro: {e}")


def descriptografar():
    """Função para descriptografar uma mensagem"""
    print("\n--- DESCRIPTOGRAFAR MENSAGEM ---")
    
    try:
        num_trilhos = int(input("Digite o número de trilhos (2 ou mais): "))
        mensagem_cripto = input("Digite a mensagem criptografada: ")
        
        if not mensagem_cripto:
            print("❌ Erro: Mensagem não pode estar vazia!")
            return
        
        cipher = RailFenceCipher(num_trilhos)
        descriptografada = cipher.decrypt(mensagem_cripto)
        
        print(f"\n✅ Descriptografia Realizada!")
        print(f"Mensagem Criptografada:    {mensagem_cripto}")
        print(f"Mensagem Descriptografada: {descriptografada}")
        
    except ValueError as e:
        print(f"❌ Erro: {e}")


def visualizar():
    """Função para visualizar o processo de criptografia"""
    print("\n--- VISUALIZAR PROCESSO ---")
    
    try:
        num_trilhos = int(input("Digite o número de trilhos (2 ou mais): "))
        mensagem = input("Digite a mensagem: ")
        
        if not mensagem:
            print("❌ Erro: Mensagem não pode estar vazia!")
            return
        
        cipher = RailFenceCipher(num_trilhos)
        cipher.visualize_encryption(mensagem)
        
    except ValueError as e:
        print(f"❌ Erro: {e}")


def exemplos():
    """Exibe exemplos predefinidos"""
    print("\n--- EXEMPLOS PREDEFINIDOS ---")
    
    exemplos_list = [
        {"mensagem": "HELLO WORLD", "trilhos": 3},
        {"mensagem": "PYTHON ENCRYPTION", "trilhos": 4},
        {"mensagem": "CRIPTOGRAFIA", "trilhos": 2},
        {"mensagem": "RAIL FENCE CIPHER", "trilhos": 5},
    ]
    
    for i, exemplo in enumerate(exemplos_list, 1):
        mensagem = exemplo["mensagem"]
        trilhos = exemplo["trilhos"]
        
        cipher = RailFenceCipher(trilhos)
        criptografada = cipher.encrypt(mensagem)
        
        print(f"\nExemplo {i}:")
        print(f"  Trilhos:              {trilhos}")
        print(f"  Mensagem Original:    {mensagem}")
        print(f"  Mensagem Criptografada: {criptografada}")


def main():
    """Função principal"""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            criptografar()
        elif opcao == "2":
            descriptografar()
        elif opcao == "3":
            visualizar()
        elif opcao == "4":
            exemplos()
        elif opcao == "5":
            print("\n✅ Encerrando o programa...")
            break
        else:
            print("❌ Opção inválida! Digite um número de 1 a 5.")


if __name__ == "__main__":
    main()
