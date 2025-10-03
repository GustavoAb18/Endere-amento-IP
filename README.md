# Trabalho 01 - Analisador de Rede

## 📝 Descrição

Este projeto foi desenvolvido para a disciplina de **Desenvolvimento de Software de Rede**. O software tem como objetivo analisar informações de rede a partir de um IP de origem fixo, recebendo do usuário um IP de destino e uma máscara de rede em notação CIDR (bits).

Com base nesses dados, a aplicação realiza duas tarefas principais:

1. Converte a máscara de rede de bits para o formato decimal (ex: `/24` para `255.255.255.0`).
2. Verifica se o IP de destino pertence à mesma rede que o IP de origem.

O projeto foi implementado em duas versões: um script de linha de comando e uma aplicação web utilizando o micro-framework Flask.

---

## 👨‍💻 Autores/as

* **Gustavo Andrade Abilio- 2524290022**
* **Lucas Tomaz Braga - 2514290003**
* **Letícia Gomes Rodrigues - 2514290010**
* **Breno Brandão - 2514290011**

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework Web (Opcional):** Flask

---

## ⚙️ Funcionalidades

* **IP de Origem Fixo:** Utiliza o IP `192.168.15.10` como constante no código.
* **Entrada de Dados:** Coleta interativamente a máscara de rede e o IP de destino.
* **Conversão de Máscara:** Calcula e exibe a máscara em formato decimal.
* **Análise de Rede:** Determina o endereço de rede para ambos os IPs e compara-os.
* **Validação de Entradas:** Testa se a máscara e o IP de destino são válidos antes de prosseguir.
* **Interface Amigável:** Apresenta mensagens claras e resultados formatados para fácil compreensão.

---

## 📦 Como Executar

Existem duas maneiras de executar este projeto. Siga as instruções para a versão desejada.

### Versão 1: Script de Linha de Comando (Console)

Esta é a versão principal e mais simples, que roda diretamente no terminal.

1. **Pré-requisitos:**
    * Ter o [Python 3](https://www.python.org/downloads/) instalado.

2. **Execução:**
    * Navegue até o diretório do projeto pelo seu terminal.
    * Execute o seguinte comando:

        ```bash
        python rede_analyzer.py
        ```

    * Siga as instruções no terminal para inserir a máscara de rede e o IP de destino.

### Versão 2: Aplicação Web (Flask)

Esta versão implementa a funcionalidade extra de rodar como uma página web.

1. **Pré-requisitos:**
    * [Python 3](https://www.python.org/downloads/) e `pip` instalados.

2. **Passo a passo para configuração:**

    * **Clone ou baixe o projeto:**
        Certifique-se de que todos os arquivos (`app.py`, `rede_analyzer.py`, `requirements.txt` e a pasta `templates`) estão no mesmo diretório.

    * **Crie um ambiente virtual (recomendado):**

        ```bash
        python -m venv venv
        ```

    * **Ative o ambiente virtual:**
        * No Windows:

            ```cmd
            .\venv\Scripts\activate
            ```

        * No macOS/Linux:

            ```bash
            source venv/bin/activate
            ```

    * **Instale as dependências:**

        ```bash
        pip install -r requirements.txt
        ```

3. **Execução:**

    * Com o ambiente virtual ativado e as dependências instaladas, execute o seguinte comando:

        ```bash
        flask run
        ```

    * Abra seu navegador e acesse o endereço: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📂 Estrutura de Arquivos (Versão Web)

```plaintext
/seu\_projeto/
|-- app.py                  \# Lógica do servidor web Flask
|-- rede\_analyzer.py        \# Módulo com as funções de análise de rede
|-- requirements.txt        \# Dependências Python do projeto
|-- README.md               \# Este arquivo de documentação
|-- /templates/
|   |-- index.html          \# Página inicial com o formulário
|   |-- resultado.html      \# Página que exibe os resultados da análise
```


