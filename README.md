# 🔐 Rail Fence Cipher - Sistema de Criptografia

Sistema completo de **criptografia e descriptografia** usando o método **Rail Fence Cipher** (Cipher de Transposição).

## 📋 Índice

- [O que é Rail Fence Cipher?](#o-que-é-rail-fence-cipher)
- [Como Funciona](#como-funciona)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Exemplos](#exemplos)
- [Funcionalidades](#funcionalidades)

---

## 🔍 O que é Rail Fence Cipher?

**Rail Fence Cipher** (Cifra de Trilho) é um algoritmo clássico de **criptografia de transposição** que reorganiza os caracteres de uma mensagem em um padrão em forma de trilho (zigzag) e depois os lê em uma ordem diferente.

### Características:
- ✅ Método de transposição (não substitui caracteres)
- ✅ Fácil de implementar
- ✅ Suporta qualquer número de trilhos
- ✅ Reversível (pode ser descriptografado)
- ⚠️ Segurança baixa (adequado apenas para fins educacionais)

---

## 🎨 Como Funciona

### Processo de Criptografia

**Exemplo: Mensagem "HELLO WORLD" com 3 trilhos**

```
Passo 1: Distribua a mensagem em zigzag entre os trilhos

H     O     W     D
 E   L   O   R   L
  L     W     O
```

**Passo 2: Leia os trilhos de cima para baixo**

```
Trilho 0: H O W D
Trilho 1: E L O R L
Trilho 2: L W O

Resultado: HOWDELLORLWO
```

### Processo de Descriptografia

1. Calcule quantos caracteres cada trilho deve ter
2. Distribua os caracteres criptografados entre os trilhos
3. Leia em zigzag para recuperar a mensagem original

---

## 📁 Estrutura do Projeto

```
rail-fence-cipher/
├── rail_fence_cipher.py    # Classe principal do algoritmo
├── main.py                 # Interface interativa
├── README.md              # Documentação
└── requirements.txt       # Dependências
```

---

## 🚀 Instalação

### Pré-requisitos
- Python 3.6 ou superior

### Passos

1. **Clone o repositório:**
```bash
git clone https://github.com/FelipeSalesLS/rail-fence-cipher.git
cd rail-fence-cipher
```

2. **Não há dependências externas!** O projeto usa apenas bibliotecas padrão do Python.

---

## 💻 Como Usar

### Opção 1: Interface Interativa

Execute o menu interativo:

```bash
python main.py
```

**Menu disponível:**
1. Criptografar Mensagem
2. Descriptografar Mensagem
3. Visualizar Processo de Criptografia
4. Exemplos Predefinidos
5. Sair

### Opção 2: Uso Programático

```python
from rail_fence_cipher import RailFenceCipher

# Criar cifrador com 3 trilhos
cipher = RailFenceCipher(3)

# Criptografar
mensagem = "HELLO WORLD"
criptografada = cipher.encrypt(mensagem)
print(f"Criptografada: {criptografada}")

# Descriptografar
descriptografada = cipher.decrypt(criptografada)
print(f"Descriptografada: {descriptografada}")

# Visualizar processo
cipher.visualize_encryption(mensagem)
```

---

## 📚 Exemplos

### Exemplo 1: 3 Trilhos

```python
cipher = RailFenceCipher(3)
original = "HELLO WORLD"
criptografada = cipher.encrypt(original)

# Output:
# Original:      HELLO WORLD
# Criptografada: HOWDELLORLWO
```

### Exemplo 2: 4 Trilhos

```python
cipher = RailFenceCipher(4)
original = "PYTHON ENCRYPTION"
criptografada = cipher.encrypt(original)

# Output:
# Original:      PYTHON ENCRYPTION
# Criptografada: PNRPYOHTECYTNINO
```

### Exemplo 3: 2 Trilhos (Zig-Zag)

```python
cipher = RailFenceCipher(2)
original = "CRIPTOGRAFIA"
criptografada = cipher.encrypt(original)

# Output:
# Original:      CRIPTOGRAFIA
# Criptografada: CITGAIARUPROGR
```

### Visualizar Processo

```python
cipher = RailFenceCipher(3)
cipher.visualize_encryption("HELLO WORLD")

# Output:
# Mensagem Original: HELLO WORLD
# Número de Trilhos: 3
#
# Distribuição nos Trilhos:
# Trilho 0: H O W D
# Trilho 1: E L O R L
# Trilho 2: L W O
#
# Mensagem Criptografada: HOWDELLORLWO
```

---

## ⚙️ Funcionalidades

### Classe `RailFenceCipher`

#### Métodos

| Método | Descrição | Parâmetros | Retorno |
|--------|-----------|-----------|---------|
| `__init__(num_rails)` | Inicializa o cifrador | `num_rails` (int) | - |
| `encrypt(message)` | Criptografa uma mensagem | `message` (str) | `str` (criptografada) |
| `decrypt(encrypted_message)` | Descriptografa uma mensagem | `encrypted_message` (str) | `str` (original) |
| `visualize_encryption(message)` | Mostra o processo de criptografia | `message` (str) | - (print) |

### Características

✨ **Tratamento Automático:**
- Remove espaços em branco
- Converte para maiúsculas
- Valida número de trilhos

🔍 **Visualização:**
- Mostra a distribuição nos trilhos
- Exibe a mensagem criptografada
- Facilita o aprendizado

---

## 📝 Notas Importantes

### Segurança

⚠️ **Aviso:** Rail Fence Cipher é um algoritmo **muito simples** e pode ser quebrado facilmente com análise de frequência. É recomendado apenas para:
- Fins educacionais
- Demonstração de conceitos criptográficos
- Proteção de dados não sensíveis

Para dados sensíveis, use algoritmos modernos como AES, RSA, etc.

### Formatação de Entrada

- Espaços são removidos automaticamente
- Caracteres são convertidos para maiúsculas
- Acentos e caracteres especiais são mantidos

---

## 🎓 Conceitos Aprendidos

Este projeto demonstra:

1. **Métodos de Transposição** - Reorganização de caracteres
2. **Algoritmos de Criptografia** - Cifra simples
3. **Programação Orientada a Objetos** - Uso de classes
4. **Estruturas de Dados** - Matrizes e listas
5. **Algoritmos Reversíveis** - Encriptação e desencriptação

---

## 🤝 Contribuições

Sinta-se livre para:
- Reportar bugs
- Sugerir melhorias
- Adicionar novos recursos

---

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

---

## 👨‍💻 Autor

**Felipe Sales**
- GitHub: [@FelipeSalesLS](https://github.com/FelipeSalesLS)

---

## 📖 Referências

- [Rail Fence Cipher - Wikipedia](https://en.wikipedia.org/wiki/Rail_fence_cipher)
- [Cryptography Methods](https://www.khanacademy.org/computing/computer-science/cryptography)

---

**Desenvolvido com ❤️ para fins educacionais**
