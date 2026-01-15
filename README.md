# 🤖 Automação de Cadastro de Produtos (Python + PyAutoGUI)

Este projeto é uma ferramenta de **RPA (Robotic Process Automation)** desenvolvida durante a Jornada Python da Hashtag Treinamentos. O objetivo é automatizar o login e o preenchimento de formulários de um sistema web utilizando dados extraídos de um arquivo CSV.

## 🚀 Funcionalidades
- **Abertura automática** do navegador Chrome.
- **Seleção inteligente de perfil** no navegador via comandos de teclado.
- **Login automático** no sistema web.
- **Extração de dados** de um arquivo `.csv` utilizando a biblioteca Pandas.
- **Preenchimento em massa** de campos (Código, Marca, Tipo, Categoria, Preços e Obs).
- **Tratamento de dados** para ignorar valores vazios (NaN) e evitar erros de digitação.

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **PyAutoGUI:** Para automação de interface gráfica (mouse e teclado).
- **Pandas:** Para manipulação e leitura da base de dados.
- **Time:** Para gerenciamento de pausas e sincronização com o carregamento do site.

## 📋 Pré-requisitos
Antes de rodar o projeto, você precisará instalar as bibliotecas necessárias:

```bash
pip install pyautogui pandas openpyxl
```
Como utilizar
Clone este repositório:

```bash
git clone https://github.com/TiagoTReis/Automacao-cadastro-produtos.git
```
Certifique-se de que os arquivos estão na mesma pasta: O arquivo produtos.csv deve estar no mesmo diretório do script codigo.py.

Execute o script:

```bash

python codigo.py
```
⚠️ Aviso Importante: O PyAutoGUI assume o controle total do seu mouse e teclado. Não mexa no computador durante a execução. Para interromper o bot em caso de emergência, arraste o cursor do mouse rapidamente para qualquer um dos cantos da tela (Fail-Safe).

 
---


