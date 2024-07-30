# auth.py

import sys

def autenticar(email, senha):
    """
    Função para autenticar um usuário com email/telefone e senha.
    
    :param email: Email ou número de telefone do usuário.
    :param senha: Senha do usuário.
    :return: Mensagem de status de autenticação.
    """
    # Dados de login válidos
    email_valido = "sergiowesley@gmail.com"
    telefone_valido = "99123-4567"
    senha_valida = "sergio123"
    
    if (email == email_valido or email == telefone_valido) and senha == senha_valida:
        return "Acesso concedido! É bom ver você novamente!"
    else:
        return "Acesso negado! Email ou senha incorreta."

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python auth.py <email/telefone> <senha>")
        sys.exit(1)

    email = sys.argv[1]
    senha = sys.argv[2]
    mensagem = autenticar(email, senha)
    print(mensagem)
