# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash
from rede_analyzer import (
    cidr_para_mascara_decimal,
    obter_endereco_rede,
    validar_ip,
    IP_ORIGEM_FIXO,
)

app = Flask(__name__)
# Chave secreta necessária para usar flash messages (mensagens de erro)
app.secret_key = "uma-chave-secreta-qualquer"


@app.route("/")
def index():
    """Renderiza a página inicial com o formulário."""
    return render_template("index.html", ip_fixo=IP_ORIGEM_FIXO)


@app.route("/analisar", methods=["POST"])
def analisar():
    """Processa os dados do formulário e exibe o resultado."""
    mascara_bits_str = request.form.get("mascara")
    ip_destino = request.form.get("ip_destino")

    # Validação de entradas
    try:
        mascara_bits = int(mascara_bits_str)
        if not 0 <= mascara_bits <= 32:
            flash("Erro: A máscara de rede deve ser um número entre 0 e 32.")
            return render_template("index.html", ip_fixo=IP_ORIGEM_FIXO)
    except (ValueError, TypeError):
        flash("Erro: A máscara de rede fornecida é inválida.")
        return render_template("index.html", ip_fixo=IP_ORIGEM_FIXO)

    if not validar_ip(ip_destino):
        flash("Erro: O formato do IP de destino é inválido.")
        return render_template("index.html", ip_fixo=IP_ORIGEM_FIXO)

    # Lógica de negócio (reutilizando funções do script de console)
    mascara_decimal = cidr_para_mascara_decimal(mascara_bits)
    rede_origem = obter_endereco_rede(IP_ORIGEM_FIXO, mascara_decimal)
    rede_destino = obter_endereco_rede(ip_destino, mascara_decimal)

    pertence_a_rede = rede_origem == rede_destino

    # Renderiza a página de resultados com os dados calculados
    return render_template(
        "resultado.html",
        ip_origem=IP_ORIGEM_FIXO,
        ip_destino=ip_destino,
        mascara_bits=mascara_bits,
        mascara_decimal=mascara_decimal,
        rede_origem=rede_origem,
        rede_destino=rede_destino,
        pertence_a_rede=pertence_a_rede,
    )


if __name__ == "__main__":
    # Para executar, use: flask run
    # Ou rode este script diretamente e acesse http://127.0.0.1:5000
    app.run(debug=True)
