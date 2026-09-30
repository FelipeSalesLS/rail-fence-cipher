"""
Testes Unitários para Rail Fence Cipher
Validação das funcionalidades de criptografia e descriptografia
"""

import unittest
from rail_fence_cipher import RailFenceCipher


class TestRailFenceCipher(unittest.TestCase):
    """Testes para a classe RailFenceCipher"""
    
    def test_initialization_valid(self):
        """Testa inicialização com número válido de trilhos"""
        cipher = RailFenceCipher(3)
        self.assertEqual(cipher.num_rails, 3)
    
    def test_initialization_invalid(self):
        """Testa inicialização com número inválido de trilhos"""
        with self.assertRaises(ValueError):
            RailFenceCipher(1)
        
        with self.assertRaises(ValueError):
            RailFenceCipher(0)
    
    def test_encrypt_3_rails(self):
        """Testa criptografia com 3 trilhos"""
        cipher = RailFenceCipher(3)
        message = "HELLO WORLD"
        encrypted = cipher.encrypt(message)
        self.assertEqual(encrypted, "HOWDELLORLWO")
    
    def test_encrypt_2_rails(self):
        """Testa criptografia com 2 trilhos"""
        cipher = RailFenceCipher(2)
        message = "CRIPTOGRAFIA"
        encrypted = cipher.encrypt(message)
        # Verificar que o comprimento permanece o mesmo
        self.assertEqual(len(encrypted), len(message.replace(" ", "")))
    
    def test_encrypt_4_rails(self):
        """Testa criptografia com 4 trilhos"""
        cipher = RailFenceCipher(4)
        message = "PYTHON ENCRYPTION"
        encrypted = cipher.encrypt(message)
        self.assertEqual(len(encrypted), len(message.replace(" ", "")))
    
    def test_decrypt_3_rails(self):
        """Testa descriptografia com 3 trilhos"""
        cipher = RailFenceCipher(3)
        original = "HELLO WORLD"
        encrypted = cipher.encrypt(original)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(decrypted, original.replace(" ", "").upper())
    
    def test_decrypt_2_rails(self):
        """Testa descriptografia com 2 trilhos"""
        cipher = RailFenceCipher(2)
        original = "CRIPTOGRAFIA"
        encrypted = cipher.encrypt(original)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(decrypted, original.upper())
    
    def test_decrypt_4_rails(self):
        """Testa descriptografia com 4 trilhos"""
        cipher = RailFenceCipher(4)
        original = "PYTHON ENCRYPTION"
        encrypted = cipher.encrypt(original)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(decrypted, original.replace(" ", "").upper())
    
    def test_encrypt_decrypt_roundtrip(self):
        """Testa que encrypt seguido por decrypt retorna mensagem original"""
        cipher = RailFenceCipher(3)
        original = "SISTEMA DE CRIPTOGRAFIA"
        encrypted = cipher.encrypt(original)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(decrypted, original.replace(" ", "").upper())
    
    def test_encrypt_removes_spaces(self):
        """Testa que espaços são removidos"""
        cipher = RailFenceCipher(3)
        message_with_spaces = "HELLO WORLD"
        message_without_spaces = "HELLOWORLD"
        
        encrypted1 = cipher.encrypt(message_with_spaces)
        encrypted2 = cipher.encrypt(message_without_spaces)
        
        self.assertEqual(encrypted1, encrypted2)
    
    def test_encrypt_converts_to_uppercase(self):
        """Testa que caracteres são convertidos para maiúsculas"""
        cipher = RailFenceCipher(3)
        lowercase = cipher.encrypt("hello")
        uppercase = cipher.encrypt("HELLO")
        
        self.assertEqual(lowercase, uppercase)
    
    def test_short_message(self):
        """Testa criptografia de mensagem mais curta que trilhos"""
        cipher = RailFenceCipher(5)
        message = "HI"
        encrypted = cipher.encrypt(message)
        decrypted = cipher.decrypt(encrypted)
        
        self.assertEqual(encrypted, "HI")
        self.assertEqual(decrypted, "HI")
    
    def test_single_character(self):
        """Testa criptografia de um único caractere"""
        cipher = RailFenceCipher(3)
        message = "A"
        encrypted = cipher.encrypt(message)
        decrypted = cipher.decrypt(encrypted)
        
        self.assertEqual(encrypted, "A")
        self.assertEqual(decrypted, "A")
    
    def test_different_rail_counts(self):
        """Testa criptografia com diferentes números de trilhos"""
        message = "RAILFENCECIPHER"
        
        for num_rails in range(2, 10):
            cipher = RailFenceCipher(num_rails)
            encrypted = cipher.encrypt(message)
            decrypted = cipher.decrypt(encrypted)
            
            self.assertEqual(decrypted, message)
    
    def test_encrypt_length_preserved(self):
        """Testa que comprimento da mensagem é preservado"""
        cipher = RailFenceCipher(3)
        message = "CRYPTOGRAPHY"
        encrypted = cipher.encrypt(message)
        
        self.assertEqual(len(encrypted), len(message))
    
    def test_encrypt_all_chars_present(self):
        """Testa que todos caracteres estão presentes na criptografia"""
        cipher = RailFenceCipher(3)
        message = "ABCDEFGH"
        encrypted = cipher.encrypt(message)
        
        # Verificar que todos os caracteres da mensagem estão no resultado
        for char in message:
            self.assertIn(char, encrypted)
    
    def test_encrypt_produces_different_order(self):
        """Testa que a criptografia muda a ordem dos caracteres"""
        cipher = RailFenceCipher(3)
        message = "ABCDEFGHIJKLMNOP"
        encrypted = cipher.encrypt(message)
        
        # Para mensagens longas, deve haver mudança significativa
        self.assertNotEqual(message, encrypted)
    
    def test_consistency(self):
        """Testa que múltiplas criptografias produzem mesmo resultado"""
        cipher = RailFenceCipher(3)
        message = "CONSISTENT"
        
        encrypted1 = cipher.encrypt(message)
        encrypted2 = cipher.encrypt(message)
        
        self.assertEqual(encrypted1, encrypted2)
    
    def test_special_characters_handling(self):
        """Testa manipulação de caracteres especiais"""
        cipher = RailFenceCipher(3)
        message = "HELLO-WORLD!"
        encrypted = cipher.encrypt(message)
        
        # Caracteres especiais devem ser mantidos
        self.assertIn("-", encrypted)
        self.assertIn("!", encrypted)


class TestRailFenceCipherEdgeCases(unittest.TestCase):
    """Testes de casos extremos"""
    
    def test_very_long_message(self):
        """Testa criptografia de mensagem muito longa"""
        cipher = RailFenceCipher(3)
        message = "A" * 1000
        encrypted = cipher.encrypt(message)
        decrypted = cipher.decrypt(encrypted)
        
        self.assertEqual(decrypted, message)
        self.assertEqual(len(encrypted), len(message))
    
    def test_many_rails(self):
        """Testa criptografia com muitos trilhos"""
        cipher = RailFenceCipher(50)
        message = "RAILWAY"
        encrypted = cipher.encrypt(message)
        decrypted = cipher.decrypt(encrypted)
        
        self.assertEqual(decrypted, message)
    
    def test_rails_equal_message_length(self):
        """Testa quando número de trilhos é igual ao comprimento da mensagem"""
        cipher = RailFenceCipher(5)
        message = "ABCDE"
        encrypted = cipher.encrypt(message)
        decrypted = cipher.decrypt(encrypted)
        
        self.assertEqual(decrypted, message)
    
    def test_rails_greater_than_message_length(self):
        """Testa quando número de trilhos é maior que comprimento da mensagem"""
        cipher = RailFenceCipher(10)
        message = "ABC"
        encrypted = cipher.encrypt(message)
        decrypted = cipher.decrypt(encrypted)
        
        self.assertEqual(decrypted, message)


def run_tests():
    """Executa todos os testes"""
    # Criar suite de testes
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Adicionar testes
    suite.addTests(loader.loadTestsFromTestCase(TestRailFenceCipher))
    suite.addTests(loader.loadTestsFromTestCase(TestRailFenceCipherEdgeCases))
    
    # Executar com verbosidade
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exibir resumo
    print("\n" + "=" * 60)
    print("RESUMO DOS TESTES")
    print("=" * 60)
    print(f"Testes Executados: {result.testsRun}")
    print(f"Sucessos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Falhas: {len(result.failures)}")
    print(f"Erros: {len(result.errors)}")
    print("=" * 60)
    
    return result


if __name__ == "__main__":
    result = run_tests()
    exit(0 if result.wasSuccessful() else 1)
