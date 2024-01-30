# er-person-generate: Biblioteca de Geração de Dados Pessoais Fictícios

![Build](https://img.shields.io/badge/Build-Pass-brightgreen.svg)
![Versão](https://img.shields.io/badge/Vers%C3%A3o-1.5.0-blue.svg) <br>

O pacote "person_generate" foi desenvolvido para auxiliar programadores na validação de seus códigos por meio da geração de dados realistas. Este pacote possibilita a criação de perfis de pessoas, tanto do sexo feminino quanto masculino, incluindo informações pessoais, endereço e características físicas.

## Funcionalidades

### Gerador Nome Completo de uma Pessoa

- A função `nome()` tem como finalidade gerar o nome completo de uma pessoa. O usuário tem a opção de aplicar restrições específicas, como gerar apenas nomes femininos com a função `nome('F')` ou nomes masculinos com a função `nome('M')`.

### Gerador de Informações Biométricas

- As funções `gerar_peso()` e `gerar_altura()` geram aleatoriamente o peso e a altura, respectivamente, considerando o sexo da pessoa. Basta passar como parâmetro as letras 'F' para dados femininos ou 'M' para dados masculinos.

### Gerador de CPF

- A função `cpf()` gera de maneira aleatória números de CPF que são validados, sendo uma ferramenta extremamente útil em situações de teste para programas que exigem a inserção de documentos autênticos. Com essa funcionalidade, torna-se mais eficiente e prático verificar a robustez e integridade de sistemas que demandam a validação de CPFs, facilitando assim a análise de casos de uso realistas.

### Gerador de Data de Nascimento

- A função `dataNascimento()` gera uma data de nascismento aleatória. O usuário tema opção de aplicar restrições específicas, como gerar apenas datas de pessoas maior idade `dataNascimento('+18')` e para uma pessoa menor de idade com a função `dataNascimento('-18')`.

### Gerador de Telefone

- A função `telefone()` se destaca ao gerar, de forma aleatória, números de telefone, com DDDs (Código de Discagem Direta) brasileiro. 

### Gerador de Pessoa 

- A função `pessoaF()` é responsável por gerar informações completas de uma pessoa do sexo feminino, incluindo dados pessoais, endereço, e características físicas. Isso proporciona um conjunto abrangente de informações, abarcando desde dados essenciais até detalhes específicos, como email e características físicas.
- A função `pessoaM()` é responsável por produzir todas as informações necessárias sobre um homem, como endereço, dados biográficos e atributos físicos. Isso oferece uma extensa coleção de dados, desde informações básicas até detalhes como endereços de e-mail e atributos físicos.

## Como usar

1. Instale a biblioteca er-person-generate utilizando o pip:

    ```bash
    pip install er-person-generate
2. Importe a biblioteca com todas as funções:

    ```bash
    from er_person_generate import *
3. Agora, todas as funcionalidades da biblioteca er-person-generate estão disponíveis para utilização.

## Exemplos de uso

Confira demonstrações de como aplicar as diversas funcionalidades da biblioteca er-person-generate:

### Gerar Nomes

```python 
   # Gera um nome de uma pessoa aleatória, pode ser feminino ou masculino 
   nome_pessoa = nome()
   print(nome_pessoa)

   # Gera um nome de uma pessoa aleatória, somente do sexo feminino.
   nome_pessoa_feminino = nome('F')
   print(nome_pessoa_feminino)

   # Gera um nome de uma pessoa aleatória, somente do sexo masculino.
   nome_pessoa_masculino = nome('M')
   print(nome_pessoa_masculino)
```
Saída
```Terminal
   Felipe Martins Cardoso
   Joana dos Santos Freitas
   Bruno Pereira Barros
```

### Gerar CPF

```python 
   # Gera um número de CPF válido.
   cpf_pessoa = cpf()
   print(cpf_pessoa)
```
Saída

```Terminal
   802.678.678-59
```

### Gerar Data de Nascimento

```python
    # Gera data de nascimento aleatória
    pessoa_data = dataNascimento()
    print(pessoa_data)

    # Gera data de nascimento aleatória de uma pessoa com a maior de idade 
    pessoa_maior_idade = dataNascimento('+18')
    print(pessoa_maior_idade)

    # Gera data de nascimento aleatória de uma pessoa com a menor de idade 
    pessoa_menor_idade = dataNascimento('-18')
    print(pessoa_menor_idade)
```
Saída

```Terminal
   10/10/1959
   04/12/1964
   18/07/2011
```

### Gerar Telefone

```python
    # Gera um número de telefone aleatório com o ddd brasileiro
    telefone_pessoa = telefone()
    print(telefone_pessoa)
```

Saída

```Terminal
   (48) 2201-8582
```

### Gerar Altura

```python
   # Gera uma altura aleatória
    altura_pessoa = altura()
    print(altura_pessoa)

    # Gera uma altura aleatória para o sexo feminino
    altura_pessoa_feminino = altura('F')
    print(altura_pessoa_feminino)

    # Gera uma altura aleatória para o sexo masculino
    altura_pessoa_masculino = altura('M')
    print(altura_pessoa_masculino)
```

Saída

```Terminal
    1.97
    1.57
    1.77
```

### Gerar Peso

```python
    # Gera o peso de uma pessoa
    peso_pessoa = peso()
    print(peso_pessoa)

    # Gera o peso de uma pessoa do sexo feminino
    peso_pessoa_feminino = peso('F')
    print(peso_pessoa_feminino)

    # Gera o peso de uma pessoa do sexo masculino
    peso_pessoa_masculino = peso('M')
    print(peso_pessoa_masculino)
```

Saída

```Terminal
    90.0
    81.2
    70.3
```

### Gerar Pessoa

Gerar dados de uma pessoa do sexo feminino.

```python
    dados_mulher = pessoaF()
    print(dados_mulher)
```

Saída

```Terminal
   --- Dados Pessoais ---
    Nome: Larissa da Silva Barros
    CPF: 894.965.626-47
    Data de Nascimento: 24/03/1987
    Idade: 36
    Sexo: Feminino
    --- Online ---
    E-mail: larissadasilvabarros1961@gmail.com
    Senha: GlQ0$5%gd,8U
    --- Endereço ---
    Campo Nascimento, 28
    UF: SC
    --- Telefone ---
    Celular: (47) 3103-0950
    --- Caracteristicas Físicas ---
    Altura: 1.65 cm
    Peso: 62.2 kg
    Tipo Sanguineo: AB-
```
Gerar dados de uma pessoa do sexo masculino.

```python
    dados_homem = pessoaM()
    print(dados_homem)
```

Saída

```Terminal
    --- Dados Pessoais ---
    Nome: Gabriel Oliveira Freitas
    CPF: 040.098.195-53
    Data de Nascimento: 09/11/1962
    Idade: 61
    Sexo: Masculino
    --- Online ---
    E-mail: gabrieloliveirafreitas1963@gmail.com
    Senha: kwQsE!/3S}7@
    --- Endereço ---
    Distrito Bryan Mendes
    UF: RR
    --- Telefone ---
    Celular: (95) 1044-1502
    --- Caracteristicas Físicas ---
    Altura: 1.73 cm
    Peso: 96.3 kg
    Tipo Sanguineo: O+
```

## Contato

Se houver dúvidas, sugestões ou desejo de colaboração no projeto, sinta-se à vontade para entrar em contato com o colaborador.

- Nome: Erlanny Rodrigues
- E-mail: erlanny.rego@ufpi.edu.br