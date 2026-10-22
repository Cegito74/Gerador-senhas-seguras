
import secrets
import string


def gerar_senha(tamanho, usar_maiusculas=True,
                usar_numeros=True, usar_especiais=True):
    """
    Gera uma senha aleatoria e segura.
    """

    if tamanho < 8:
        raise ValueError("A senha deve ter pelo menos 8 caracteres.")

    grupos = [string.ascii_lowercase]

    if usar_maiusculas:
        grupos.append(string.ascii_uppercase)

    if usar_numeros:
        grupos.append(string.digits)

    if usar_especiais:
        grupos.append("!@#$%&*?")

    caracteres = "".join(grupos)

    # Garante um caractere de cada grupo selecionado
    senha = [secrets.choice(grupo) for grupo in grupos]

    # Completa a senha ate atingir o tamanho desejado
    while len(senha) < tamanho:
        senha.append(secrets.choice(caracteres))

    # Embaralha a senha de forma segura
    for i in range(len(senha) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        senha[i], senha[j] = senha[j], senha[i]

    return "".join(senha)


def perguntar_sim_nao(pergunta):
    while True:
        resposta = input(pergunta).strip().lower()

        if resposta in ("s", "sim"):
            return True

        if resposta in ("n", "nao", "não"):
            return False

        print("Resposta invalida. Digite S ou N.")


def main():
    print("=" * 45)
    print("       GERADOR DE SENHAS SEGURAS")
    print("=" * 45)

    try:
        tamanho = int(input("Digite o tamanho da senha: "))

        maiusculas = perguntar_sim_nao(
            "Incluir letras maiusculas? (S/N): "
        )

        numeros = perguntar_sim_nao(
            "Incluir numeros? (S/N): "
        )

        especiais = perguntar_sim_nao(
            "Incluir caracteres especiais? (S/N): "
        )

        senha = gerar_senha(
            tamanho, maiusculas, numeros, especiais
        )

        print("\nSenha gerada com sucesso!")
        print("Sua senha:", senha)

    except ValueError as erro:
        print("Erro:", erro)


if __name__ == "__main__":
    main()
