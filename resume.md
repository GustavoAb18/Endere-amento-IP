# Do que se trata o repositório

O repositório `GustavoAb18/enderecamento-ip` contém um programa projetado para extrair informações de rede a partir de um endereço IP. Conforme a descrição *(Programa que adquire informações do IP para o broadcast e bits)*, sua função principal é calcular dados como o endereço de broadcast da rede e informações sobre os bits da máscara de sub-rede.

# Estrutura do código

A composição de linguagens, com 62.6% de Python e 37.4% de HTML, sugere que esta é uma aplicação web simples:

* Python (Backend): Um script Python provavelmente contém a lógica para receber um endereço IP, realizar os cálculos de rede (como determinar a classe do IP, a máscara de sub-rede, o endereço de rede e o endereço de broadcast) e retornar os resultados.

* HTML (Frontend): A parte em HTML deve fornecer uma interface de usuário no navegador, com um formulário para que o usuário insira o endereço IP e uma área para exibir os resultados calculados pelo script Python.

---

Em resumo, é uma ferramenta prática para estudantes ou profissionais de redes que precisam calcular rapidamente informações de endereçamento IP. Infelizmente, sem acesso aos arquivos, não posso fornecer uma análise mais profunda do código-fonte.

---

# Explicação do Código
O repositório é composto por vários arquivos que trabalham em conjunto para fornecer as funcionalidades descritas.

`rede_analyzer.py`
Este é o arquivo principal que contém a lógica central da análise de rede. Suas principais funções são:

* `validar_ip(ip_str)`: Verifica se a string fornecida corresponde a um formato de endereço IPv4 válido, com quatro octetos numéricos entre 0 e 255.

* `cidr_para_mascara_decimal(bits)`: Converte o valor da máscara de rede em notação CIDR (um número de 0 a 32) para o seu equivalente em formato decimal, realizando operações de deslocamento de bits para o cálculo.

* `obter_endereco_rede(ip, mascara)`: Calcula o endereço de rede aplicando uma operação lógica "AND" bit a bit entre os octetos do endereço IP e da máscara de rede.

* `main()`: É a função que executa a versão de linha de comando do programa. Ela solicita as entradas do usuário, chama as funções de validação e análise, e exibe os resultados de forma clara no terminal.

---

`app.py`
Este arquivo implementa a aplicação web utilizando o framework Flask. Ele importa as funções do rede_analyzer.py para realizar a análise e renderizar os resultados em páginas HTML.

* `@app.route("/")`: Define a rota para a página inicial, que renderiza o template index.html e exibe o formulário para o usuário.

* `@app.route("/analisar", methods=["POST"])`: Processa os dados enviados pelo formulário. Ele valida as entradas do usuário e, se forem válidas, chama as funções de análise para calcular a máscara decimal e os endereços de rede. Em seguida, renderiza a página resultado.html para exibir os resultados.

---

`templates/`
Esta pasta contém os arquivos HTML que compõem a interface da aplicação web.

* `index.html`: É a página inicial da aplicação. Contém um formulário para que o usuário insira a máscara de rede e o IP de destino. A página também exibe mensagens de erro caso as entradas sejam inválidas.

* `resultado.html`: Exibe os resultados da análise, incluindo a máscara de rede convertida e os endereços de rede de origem e destino, concluindo se os IPs pertencem ou não à mesma rede.

`requirements.txt`
Este arquivo especifica as dependências do projeto, que neste caso é o framework Flask.

---

## Funcionalidades Principais

**IP de Origem Fixo**: O software utiliza o endereço IP 192.168.15.10 como um valor constante para a análise.

**Entrada de Dados**: O usuário fornece um IP de destino e uma máscara de rede em notação CIDR (por exemplo, /24).

**Conversão de Máscara**: A aplicação converte a máscara de rede de notação CIDR para o formato decimal (por exemplo, de /24 para 255.255.255.0).

**Análise de Rede**: O programa calcula e compara os endereços de rede do IP de origem e do IP de destino para determinar se ambos pertencem à mesma rede.

**Validação de Entradas**: Antes de realizar a análise, o software valida se o IP de destino e a máscara de rede fornecidos são válidos.