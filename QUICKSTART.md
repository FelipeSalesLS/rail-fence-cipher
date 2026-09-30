# 🚀 Guia Rápido - Rail Fence Cipher

## Como Começar

### 1. Executar o Menu Interativo

```bash
python main.py
```

### 2. Executar os Testes

```bash
python test_rail_fence_cipher.py
```

### 3. Ver Exemplos Avançados

```bash
python exemplos_avancados.py
```

---

## Uso Rápido em Python

```python
from rail_fence_cipher import RailFenceCipher

# Criar cifrador com 3 trilhos
cipher = RailFenceCipher(3)

# Criptografar
mensagem = "HELLO WORLD"
cripto = cipher.encrypt(mensagem)
print(cripto)  # HOWDELLORLWO

# Descriptografar
original = cipher.decrypt(cripto)
print(original)  # HELLOWORLD
```

---

## Estrutura de Arquivos

```
📁 rail-fence-cipher/
├── 📄 rail_fence_cipher.py      # Algoritmo principal
├── 📄 main.py                   # Interface interativa
├── 📄 test_rail_fence_cipher.py # Testes unitários
├── 📄 exemplos_avancados.py     # Exemplos e casos de uso
├── 📄 requirements.txt           # Dependências
├── 📄 QUICKSTART.md             # Este arquivo
└── 📄 README.md                 # Documentação completa
```

---

## Funcionalidades Principais

✅ **Criptografia** - Transforma mensagens em texto cifrado  
✅ **Descriptografia** - Recupera mensagem original  
✅ **Visualização** - Mostra como o algoritmo funciona  
✅ **Flexível** - Suporta qualquer número de trilhos  
✅ **Sem dependências** - Usa apenas Python padrão

---

## Exemplos Rápidos

### Exemplo 1: 3 Trilhos
```python
cipher = RailFenceCipher(3)
print(cipher.encrypt("HELLO"))  # HLOEL
```

### Exemplo 2: 2 Trilhos
```python
cipher = RailFenceCipher(2)
print(cipher.encrypt("PYTHON"))  # PTYONH
```

### Exemplo 3: Visualizar
```python
cipher = RailFenceCipher(4)
cipher.visualize_encryption("CIPHER")
```

---

## Perguntas Frequentes

**P: Preciso instalar algo?**  
R: Não! O projeto usa apenas Python puro.

**P: Qual versão do Python?**  
R: Python 3.6 ou superior.

**P: O algoritmo é seguro?**  
R: Não! Rail Fence é apenas para fins educacionais.

**P: Posso modificar o código?**  
R: Sim! Está sob licença MIT.

---

## Próximos Passos

1. 📖 Leia o [README.md](README.md) completo
2. 🧪 Execute os testes: `python test_rail_fence_cipher.py`
3. 🎮 Experimente o menu interativo: `python main.py`
4. 📚 Veja exemplos avançados: `python exemplos_avancados.py`

---

**Desenvolvido com ❤️ para fins educacionais**
