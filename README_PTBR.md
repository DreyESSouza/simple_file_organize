# Organizador de Arquivos com Interface Simples

Uma aplicação simples em Python com interface gráfica que organiza arquivos automaticamente em pastas específicas com base em suas extensões.

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de tornar a organização de arquivos mais rápida e prática.  
A aplicação permite que o usuário selecione uma pasta e, em seguida, organiza automaticamente os arquivos em categorias predefinidas.

## Funcionalidades

- Interface gráfica simples
- Janela para seleção de pasta
- Organização automática de arquivos
- Separação por extensão
- Tratamento de nomes duplicados

## Tecnologias Utilizadas

- Python
- CustomTkinter
- Tkinter
- Módulo OS

## Estrutura do Projeto

```bash
project/
│
├── interface.py
├── logic.py
├── extensions.py
├── requirements.txt
├── .gitignore
├── README.md
└── README_PTBR.md
```

## Como Executar

1. Clone este repositório:
```bash
git clone [SEU_LINK_DO_GITHUB]
```

2. Entre na pasta do projeto:
```bash
cd [NOME_DA_PASTA_DO_PROJETO]
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
python interface.py
```

## Como Funciona

- O usuário clica no botão da interface
- Uma janela de seleção de pasta é aberta
- O programa lê os arquivos da pasta selecionada
- Os arquivos são movidos para suas respectivas pastas com base na extensão

## Melhorias Futuras

- Adicionar suporte a mais tipos de arquivos
- Melhorar o design da interface
- Adicionar log de atividades
- Adicionar suporte a categorias personalizadas

## Autor

Desenvolvido por Andrey Souza
