"""
Rail Fence Cipher (Cipher de Transposição)
Sistema de criptografia e descriptografia usando o método de trilho
"""

class RailFenceCipher:
    """
    Classe que implementa o algoritmo Rail Fence Cipher
    para criptografar e descriptografar mensagens.
    """
    
    def __init__(self, num_rails):
        """
        Inicializa o cifrador com número de trilhos
        
        Args:
            num_rails (int): Número de trilhos (deve ser >= 2)
        """
        if num_rails < 2:
            raise ValueError("Número de trilhos deve ser >= 2")
        self.num_rails = num_rails
    
    def encrypt(self, message):
        """
        Criptografa uma mensagem usando Rail Fence Cipher
        
        Args:
            message (str): Mensagem a ser criptografada
            
        Returns:
            str: Mensagem criptografada
        """
        # Remove espaços e converte para maiúsculas
        message = message.replace(" ", "").upper()
        
        # Se a mensagem tem comprimento menor que o número de trilhos
        if len(message) <= self.num_rails:
            return message
        
        # Cria uma matriz de trilhos
        rails = [[] for _ in range(self.num_rails)]
        
        rail = 0
        direction = 1  # 1 para descer, -1 para subir
        
        # Distribui os caracteres nos trilhos
        for char in message:
            rails[rail].append(char)
            
            # Muda de direção nos extremos
            if rail == 0:
                direction = 1
            elif rail == self.num_rails - 1:
                direction = -1
            
            rail += direction
        
        # Concatena os trilhos para formar a mensagem criptografada
        encrypted = ''.join(''.join(rail_chars) for rail_chars in rails)
        
        return encrypted
    
    def decrypt(self, encrypted_message):
        """
        Descriptografa uma mensagem criptografada com Rail Fence Cipher
        
        Args:
            encrypted_message (str): Mensagem criptografada
            
        Returns:
            str: Mensagem original
        """
        # Remove espaços e converte para maiúsculas
        encrypted_message = encrypted_message.replace(" ", "").upper()
        
        # Se a mensagem tem comprimento menor que o número de trilhos
        if len(encrypted_message) <= self.num_rails:
            return encrypted_message
        
        # Cria uma matriz para armazenar posições
        rail_lengths = [0] * self.num_rails
        
        rail = 0
        direction = 1
        
        # Calcula o comprimento de cada trilho
        for _ in range(len(encrypted_message)):
            rail_lengths[rail] += 1
            
            if rail == 0:
                direction = 1
            elif rail == self.num_rails - 1:
                direction = -1
            
            rail += direction
        
        # Cria rails com os caracteres criptografados
        rails = []
        index = 0
        for length in rail_lengths:
            rails.append(list(encrypted_message[index:index + length]))
            index += length
        
        # Reconstrói a mensagem original
        decrypted = []
        rail = 0
        direction = 1
        rail_indices = [0] * self.num_rails
        
        for _ in range(len(encrypted_message)):
            decrypted.append(rails[rail][rail_indices[rail]])
            rail_indices[rail] += 1
            
            if rail == 0:
                direction = 1
            elif rail == self.num_rails - 1:
                direction = -1
            
            rail += direction
        
        return ''.join(decrypted)
    
    def visualize_encryption(self, message):
        """
        Visualiza o processo de criptografia mostrando os trilhos
        
        Args:
            message (str): Mensagem a ser visualizada
        """
        message = message.replace(" ", "").upper()
        
        print(f"\nMensagem Original: {message}")
        print(f"Número de Trilhos: {self.num_rails}\n")
        
        # Cria matriz para visualização
        rail_visual = [[] for _ in range(self.num_rails)]
        
        rail = 0
        direction = 1
        
        for i, char in enumerate(message):
            rail_visual[rail].append((i, char))
            
            if rail == 0:
                direction = 1
            elif rail == self.num_rails - 1:
                direction = -1
            
            rail += direction
        
        # Exibe os trilhos
        print("Distribuição nos Trilhos:")
        for i, rail_data in enumerate(rail_visual):
            chars = [char for _, char in rail_data]
            print(f"Trilho {i}: {' '.join(chars)}")
        
        encrypted = self.encrypt(message)
        print(f"\nMensagem Criptografada: {encrypted}")


def main():
    """Função principal com exemplos de uso"""
    
    print("=" * 60)
    print("SISTEMA DE CRIPTOGRAFIA RAIL FENCE CIPHER")
    print("=" * 60)
    
    # Exemplo 1: 3 trilhos
    print("\n--- EXEMPLO 1: 3 Trilhos ---")
    cipher3 = RailFenceCipher(3)
    
    mensagem1 = "HELLO WORLD"
    criptografada1 = cipher3.encrypt(mensagem1)
    descriptografada1 = cipher3.decrypt(criptografada1)
    
    print(f"Mensagem Original:      {mensagem1}")
    print(f"Mensagem Criptografada: {criptografada1}")
    print(f"Mensagem Descriptografada: {descriptografada1}")
    
    cipher3.visualize_encryption(mensagem1)
    
    # Exemplo 2: 4 trilhos
    print("\n" + "=" * 60)
    print("--- EXEMPLO 2: 4 Trilhos ---")
    cipher4 = RailFenceCipher(4)
    
    mensagem2 = "PYTHON ENCRYPTION"
    criptografada2 = cipher4.encrypt(mensagem2)
    descriptografada2 = cipher4.decrypt(criptografada2)
    
    print(f"Mensagem Original:      {mensagem2}")
    print(f"Mensagem Criptografada: {criptografada2}")
    print(f"Mensagem Descriptografada: {descriptografada2}")
    
    cipher4.visualize_encryption(mensagem2)
    
    # Exemplo 3: 2 trilhos (Zig-Zag)
    print("\n" + "=" * 60)
    print("--- EXEMPLO 3: 2 Trilhos (Zig-Zag) ---")
    cipher2 = RailFenceCipher(2)
    
    mensagem3 = "CRIPTOGRAFIA"
    criptografada3 = cipher2.encrypt(mensagem3)
    descriptografada3 = cipher2.decrypt(criptografada3)
    
    print(f"Mensagem Original:      {mensagem3}")
    print(f"Mensagem Criptografada: {criptografada3}")
    print(f"Mensagem Descriptografada: {descriptografada3}")
    
    cipher2.visualize_encryption(mensagem3)


if __name__ == "__main__":
    main()
