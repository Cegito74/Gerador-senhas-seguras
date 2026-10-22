
import secrets
import string


# ==========================================
# PROJETO: GERADOR DE SENHAS SEGURAS
# Tecnologia: Python
# Apoio: Inteligencia Artificial Generativa
# ==========================================


def gerar_senha(tamanho, usar_maiusculas=True,
                usar_numeros=True, usar_especiais=True):
    """
    Gera uma senha aleatoria e segura.

    Parametros:
    tamanho: quantidade de caracteres da senha
    usar_maiusculas: incluir letras maiusculas
    usar_numeros: incluir numeros
    usar_especiais: incluir caracteres especiais
    """

    # Verifica o tamanho minimo da senha
    if tamanho < 8:
        raise ValueError(
            "A senha deve ter pelo menos 8 caracteres."
        )

    # Letras minusculas sao obrigatorias
    grupos = [string.ascii_lowercase]

    # Adiciona os tipos de caracteres selecionados
    if usar_maiusculas:
        grupos.append(string.ascii_uppercase)

    if usar_numeros:
        grupos.append(string.digits)

    if usar_especiais:
        grupos.append("!@#$%&*?")

    # Junta os caracteres permitidos
    caracteres = "".join(grupos)

    # Garante pelo menos um caractere
    # de cada grupo selecionado
    senha = [
        secrets.choice(grupo)
        for grupo in grupos
    ]

    # Completa a senha ate atingir o tamanho
    while len(senha) < tamanho:
        senha.append(secrets.choice(caracteres))

    # Embaralha os caracteres com seguranca
    for i in range(len(senha) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        senha[i], senha[j] = senha[j], senha[i]

    return "".join(senha)


# ==========================================
# FUNCAO PARA TESTAR O GERADOR
# ==========================================

def testar_gerador():
    print("=" * 45)
    print("       GERADOR DE SENHAS SEGURAS")
    print("=" * 45)

    print("\nGerando senhas automaticamente...\n")

    # Senha de 8 caracteres
    senha1 = gerar_senha(8)

    # Senha de 12 caracteres
    senha2 = gerar_senha(12)

    # Senha de 16 caracteres
    senha3 = gerar_senha(16)

    # Senha apenas com letras minusculas
    senha4 = gerar_senha(
        10,
        usar_maiusculas=False,
        usar_numeros=False,
        usar_especiais=False
    )

    # Senha com letras e numeros
    senha5 = gerar_senha(
        12,
        usar_maiusculas=True,
        usar_numeros=True,
        usar_especiais=False
    )

    print("Senha de 8 caracteres: ", senha1)
    print("Senha de 12 caracteres:", senha2)
    print("Senha de 16 caracteres:", senha3)

    print("\nOutras configuracoes:")
    print("Apenas letras minusculas:", senha4)
    print("Letras e numeros:", senha5)

    # ======================================
    # TESTES AUTOMATICOS
    # ======================================

    print("\nExecutando testes automaticos...")

    assert len(senha1) == 8
    assert len(senha2) == 12
    assert len(senha3) == 16
    assert len(senha4) == 10
    assert len(senha5) == 12

    assert senha4.islower()
    assert senha4.isalpha()

    assert not any(
        caractere in string.punctuation
        for caractere in senha5
    )

    # Verifica se rejeita senhas curtas
    try:
        gerar_senha(5)
    except ValueError:
        print("Teste de tamanho minimo: OK")
    else:
        raise AssertionError(
            "Erro: senha curta foi aceita."
        )

    print("Testes de tamanho: OK")
    print("Testes de configuracao: OK")

    print("\nTodos os testes foram concluidos!")
    print("\nProjeto executado com sucesso!")


# ==========================================
# EXECUCAO PRINCIPAL
# ==========================================

if __name__ == "__main__":
    testar_gerador()
