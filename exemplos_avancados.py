"""
Exemplos Avançados de Rail Fence Cipher
Demonstração de casos de uso e padrões de utilização
"""

from rail_fence_cipher import RailFenceCipher


def exemplo_1_basico():
    """Exemplo básico: criptografia e descriptografia simples"""
    print("\n" + "=" * 60)
    print("EXEMPLO 1: Criptografia e Descriptografia Básica")
    print("=" * 60)
    
    cipher = RailFenceCipher(3)
    
    mensagem_original = "HELLO WORLD"
    mensagem_criptografada = cipher.encrypt(mensagem_original)
    mensagem_descriptografada = cipher.decrypt(mensagem_criptografada)
    
    print(f"Original:      {mensagem_original}")
    print(f"Criptografada: {mensagem_criptografada}")
    print(f"Descriptografada: {mensagem_descriptografada}")
    
    # Verificar se é igual
    if mensagem_descriptografada == mensagem_original.replace(" ", "").upper():
        print("✅ Criptografia e descriptografia bem-sucedidas!")
    else:
        print("❌ Erro na descriptografia!")


def exemplo_2_diferentes_trilhos():
    """Exemplo 2: Comparar diferentes números de trilhos"""
    print("\n" + "=" * 60)
    print("EXEMPLO 2: Diferentes Números de Trilhos")
    print("=" * 60)
    
    mensagem = "CRIPTOGRAFIA SEGURA"
    print(f"\nMensagem Original: {mensagem}")
    print("\nResultados com diferentes números de trilhos:\n")
    
    for num_trilhos in range(2, 6):
        cipher = RailFenceCipher(num_trilhos)
        criptografada = cipher.encrypt(mensagem)
        print(f"Trilhos {num_trilhos}: {criptografada}")


def exemplo_3_processamento_lote():
    """Exemplo 3: Criptografar múltiplas mensagens"""
    print("\n" + "=" * 60)
    print("EXEMPLO 3: Processamento em Lote")
    print("=" * 60)
    
    mensagens = [
        "PYTHON",
        "CRIPTOGRAFIA",
        "SEGURANÇA",
        "ALGORITMO",
        "TRANSPOSIÇÃO"
    ]
    
    cipher = RailFenceCipher(3)
    
    print(f"\nCifrando {len(mensagens)} mensagens com 3 trilhos:\n")
    
    resultados = []
    for msg in mensagens:
        cripto = cipher.encrypt(msg)
        resultados.append({
            'original': msg,
            'criptografada': cripto
        })
        print(f"'{msg}' → '{cripto}'")
    
    print("\nDescifrando as mensagens:\n")
    
    for resultado in resultados:
        descripto = cipher.decrypt(resultado['criptografada'])
        print(f"'{resultado['criptografada']}' → '{descripto}'")


def exemplo_4_analise_padroes():
    """Exemplo 4: Análise de padrões"""
    print("\n" + "=" * 60)
    print("EXEMPLO 4: Análise de Padrões")
    print("=" * 60)
    
    mensagem = "ABCDEFGHIJKLMNOP"
    print(f"\nMensagem Original: {mensagem}\n")
    
    for num_trilhos in [2, 3, 4, 5]:
        cipher = RailFenceCipher(num_trilhos)
        criptografada = cipher.encrypt(mensagem)
        
        print(f"Com {num_trilhos} trilho(s):")
        print(f"  Entrada:  {mensagem}")
        print(f"  Saída:    {criptografada}")
        print(f"  Mudança:  {sum(1 for i, c in enumerate(mensagem) if c != criptografada[i])} caracteres")
        print()


def exemplo_5_simetria():
    """Exemplo 5: Demonstração da simetria do algoritmo"""
    print("\n" + "=" * 60)
    print("EXEMPLO 5: Simetria do Algoritmo")
    print("=" * 60)
    
    cipher = RailFenceCipher(4)
    original = "RAILFENCECIPHER"
    
    print(f"\nMensagem Original: {original}\n")
    
    # Encriptar
    cripto1 = cipher.encrypt(original)
    print(f"1ª Encriptação: {cripto1}")
    
    # Encriptar novamente (dupla encriptação)
    cripto2 = cipher.encrypt(cripto1)
    print(f"2ª Encriptação: {cripto2}")
    
    # Descriptografar uma vez
    descripto1 = cipher.decrypt(cripto1)
    print(f"\n1ª Descriptação: {descripto1}")
    
    # Verificar simetria
    print(f"\nVerificação:")
    print(f"  Original == 1ª Descriptação: {original.replace(' ', '').upper() == descripto1}")


def exemplo_6_comparacao_seguranca():
    """Exemplo 6: Comparação de segurança com diferentes trilhos"""
    print("\n" + "=" * 60)
    print("EXEMPLO 6: Segurança com Diferentes Números de Trilhos")
    print("=" * 60)
    
    mensagem = "CONFIDENCIAL"
    
    print(f"\nMensagem Original: {mensagem}\n")
    print("Quanto MAIS trilhos, MAIS seguro (para este algoritmo simples):\n")
    
    for trilhos in [2, 3, 4, 5, 6]:
        cipher = RailFenceCipher(trilhos)
        cripto = cipher.encrypt(mensagem)
        
        # Calcular "entropia" simples (quantos caracteres mudaram de posição)
        mudancas = sum(1 for i, c in enumerate(mensagem) if c != cripto[i])
        percentual = (mudancas / len(mensagem)) * 100
        
        print(f"Trilhos: {trilhos} | Criptografado: {cripto} | Mudança: {percentual:.1f}%")


def exemplo_7_visualizacao():
    """Exemplo 7: Visualização do processo"""
    print("\n" + "=" * 60)
    print("EXEMPLO 7: Visualização do Processo")
    print("=" * 60)
    
    cipher = RailFenceCipher(3)
    cipher.visualize_encryption("RAIL FENCE")
    
    print()
    
    cipher2 = RailFenceCipher(4)
    cipher2.visualize_encryption("CIPHER")


def exemplo_8_mensagens_longas():
    """Exemplo 8: Tratamento de mensagens longas"""
    print("\n" + "=" * 60)
    print("EXEMPLO 8: Mensagens Longas")
    print("=" * 60)
    
    mensagem_longa = "ESTE É UM EXEMPLO DE UMA MENSAGEM MUITO LONGA QUE SERÁ CRIPTOGRAFADA USANDO O ALGORITMO RAIL FENCE"
    
    cipher = RailFenceCipher(5)
    
    cripto = cipher.encrypt(mensagem_longa)
    descripto = cipher.decrypt(cripto)
    
    print(f"\nMensagem Original ({len(mensagem_longa)} caracteres):")
    print(f"  {mensagem_longa}")
    
    print(f"\nMensagem Criptografada ({len(cripto)} caracteres):")
    print(f"  {cripto}")
    
    print(f"\nMensagem Descriptografada ({len(descripto)} caracteres):")
    print(f"  {descripto}")
    
    # Validação
    original_sem_espacos = mensagem_longa.replace(" ", "").upper()
    if descripto == original_sem_espacos:
        print(f"\n✅ Descriptografia bem-sucedida!")
    else:
        print(f"\n❌ Erro na descriptografia!")


def exemplo_9_casos_extremos():
    """Exemplo 9: Casos extremos"""
    print("\n" + "=" * 60)
    print("EXEMPLO 9: Casos Extremos")
    print("=" * 60)
    
    casos = [
        ("A", 2, "Único caractere"),
        ("AB", 2, "Dois caracteres"),
        ("ABC", 5, "Trilhos > comprimento"),
        ("A" * 100, 3, "Mensagem repetida longa"),
    ]
    
    for mensagem, trilhos, descricao in casos:
        cipher = RailFenceCipher(trilhos)
        cripto = cipher.encrypt(mensagem)
        descripto = cipher.decrypt(cripto)
        
        print(f"\n{descricao} (trilhos={trilhos}, tamanho={len(mensagem)}):")
        if len(mensagem) <= 20:
            print(f"  Original:      {mensagem}")
            print(f"  Criptografada: {cripto}")
        else:
            print(f"  Original:      {mensagem[:20]}... (tamanho: {len(mensagem)})")
            print(f"  Criptografada: {cripto[:20]}... (tamanho: {len(cripto)})")
        
        valido = descripto == mensagem.upper()
        print(f"  Status: {'✅ OK' if valido else '❌ ERRO'}")


def main():
    """Executa todos os exemplos"""
    exemplos = [
        exemplo_1_basico,
        exemplo_2_diferentes_trilhos,
        exemplo_3_processamento_lote,
        exemplo_4_analise_padroes,
        exemplo_5_simetria,
        exemplo_6_comparacao_seguranca,
        exemplo_7_visualizacao,
        exemplo_8_mensagens_longas,
        exemplo_9_casos_extremos,
    ]
    
    print("\n" + "🔐" * 30)
    print("EXEMPLOS AVANÇADOS - RAIL FENCE CIPHER")
    print("🔐" * 30)
    
    for exemplo in exemplos:
        try:
            exemplo()
        except Exception as e:
            print(f"\n❌ Erro ao executar {exemplo.__name__}: {e}")
    
    print("\n" + "=" * 60)
    print("✅ Todos os exemplos foram executados!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
