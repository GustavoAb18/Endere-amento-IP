# -*- coding: utf-8 -*-

"""
Trabalho 01 - Desenvolvimento de Software de Rede
Este script realiza a análise de redes com base em um IP de origem fixo,
um IP de destino e uma máscara de rede fornecidos pelo usuário.
"""

# --- 1. IP Fixo ---
# IP de origem definido como uma constante no código.
IP_ORIGEM_FIXO = "192.168.15.10"


def validar_ip(ip_str):
    """
    Valida se uma string está no formato de um endereço IPv4 válido.
    Retorna True se for válido, False caso contrário.
    """
    try:
        partes = ip_str.split(".")
        # Um IP deve ter 4 partes (octetos)
        if len(partes) != 4:
            return False
        # Cada octeto deve ser um número entre 0 e 255
        for parte in partes:
            if not 0 <= int(parte) <= 255:
                return False
        return True
    except (ValueError, IndexError):
        # Captura erros se a conversão para int falhar ou houver problemas de acesso
        return False


def cidr_para_mascara_decimal(bits):
    """
    Converte uma máscara de rede em notação CIDR (bits) para o formato decimal.
    Ex: 24 -> "255.255.255.0"
    """
    # Calcula o valor da máscara como um número inteiro de 32 bits
    # (1 << 32) cria um número com 33 bits (1 seguido de 32 zeros). Subtrair 1 cria 32 bits '1'.
    # (1 << (32 - bits)) cria um número com os bits de host (zeros à direita).
    # A operação (<<) é o deslocamento de bits para a esquerda.
    mascara_int = (1 << 32) - (1 << (32 - bits))

    # Converte o número inteiro para 4 octetos decimais
    octetos = []
    # O operador '>>' é o deslocamento de bits para a direita.
    # '& 0xff' garante que pegamos apenas os 8 bits mais à direita (1 byte).
    octetos.append(str((mascara_int >> 24) & 0xFF))
    octetos.append(str((mascara_int >> 16) & 0xFF))
    octetos.append(str((mascara_int >> 8) & 0xFF))
    octetos.append(str(mascara_int & 0xFF))

    return ".".join(octetos)


def obter_endereco_rede(ip, mascara):
    """
    Calcula o endereço da rede a partir de um IP e uma máscara.
    Isso é feito através de uma operação AND bit a bit entre o IP e a máscara.
    """
    ip_octetos = [int(o) for o in ip.split(".")]
    mascara_octetos = [int(o) for o in mascara.split(".")]

    rede_octetos = []
    # O zip() agrupa os octetos correspondentes do IP e da máscara.
    # A operação '&' (AND) é feita em cada par de octetos.
    for i in range(4):
        rede_octetos.append(str(ip_octetos[i] & mascara_octetos[i]))

    return ".".join(rede_octetos)


def main():
    """
    Função principal que executa o programa.
    """
    # --- 4. Usabilidade: Interface Clara ---
    print("===================================================")
    print("      Analisador de Rede - DEV de Software")
    print("===================================================")
    print(f"IP de Origem Fixo: {IP_ORIGEM_FIXO}\n")

    # --- 2. Entrada de Dados e 3. Testes de Entrada ---
    while True:
        try:
            mascara_bits_str = input("Digite a máscara de rede em bits (ex: 24): ")
            mascara_bits = int(mascara_bits_str)
            if not 0 <= mascara_bits <= 32:
                # Garante que o valor da máscara esteja no intervalo válido
                print(
                    "Erro: A máscara deve ser um número entre 0 e 32. Tente novamente.\n"
                )
                continue
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número inteiro.\n")

    while True:
        ip_destino = input("Digite o IP de destino (ex: 192.168.15.200): ")
        if validar_ip(ip_destino):
            break  # Sai do loop se o IP for válido
        else:
            print(
                "Erro: Formato de IP inválido. O IP deve ser no formato X.X.X.X, com valores de 0 a 255.\n"
            )

    print("\n--- Análise de Dados ---\n")

    # --- Saída A: Máscara de Rede em Decimais ---
    mascara_decimal = cidr_para_mascara_decimal(mascara_bits)
    print(f"A) Máscara de Rede para /{mascara_bits} bits:")
    print(f"   - Decimal: {mascara_decimal}")

    # --- Saída B: Verificação de Rede ---
    # Calcula o endereço de rede para ambos os IPs
    rede_origem = obter_endereco_rede(IP_ORIGEM_FIXO, mascara_decimal)
    rede_destino = obter_endereco_rede(ip_destino, mascara_decimal)

    print(f"\nB) Verificação de Rede:")
    print(f"   - Endereço de Rede (Origem):  {rede_origem}")
    print(f"   - Endereço de Rede (Destino): {rede_destino}")

    if rede_origem == rede_destino:
        print(
            "\n   [Conclusão]: O IP de destino PERTENCE à mesma rede do IP de origem."
        )
    else:
        print(
            "\n   [Conclusão]: O IP de destino NÃO PERTENCE à mesma rede do IP de origem."
        )

    print("\n===================================================")


# Ponto de entrada do script
if __name__ == "__main__":
    main()


