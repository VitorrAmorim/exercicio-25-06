def mostrar_equipe():
    equipe = [
        {"nome": "Bruno Giacomini", "função": "Desenvolvedor do Projeto"},
        {"nome": "Guilherme Pires", "função": "Desenvolvedor do Projeto"},
        {"nome": "Júlia Moisés", "função": "Desenvolvedor do Projeto"},
        {"nome": "Lucas Oliveira", "função": "Desenvolvedor do Projeto"},
        {"nome": "Mateus Antunes", "função": "Desenvolvedor do Projeto"},
        {"nome": "Vitor Amorim", "função": "Desenvolvedor do Projeto"},
    ]

    print("--- Equipe do Projeto ---")
    for membro in equipe:
        print(f"{membro['nome']} - {membro['função']}")

mostrar_equipe()



def enviar_mensagem(nome, email, mensagem):
    print(f"Mensagem recebiada de {nome} ({email}):")
    print(f"'{mensagem}'")
    print("Sua mensagem foi enviada com sucesso!")

enviar_mensagem("Exemplo", "exemplo@gmail.com", "Gostaria de saber quais os pontos de coleta")



def post_blog():
    post = [
        {"titulo": "O que fazer com seus eletrônicos antigos", "autor": "Lucas Oliveira", "data": "17/05/2025"},
        {"titulo": "Como identificar embalagens realmente sustentáveis", "autor": "Mateus Prince", "data": "19/05/2025"},
        {"titulo": "Compostagem em apartamento: é possível?", "autor": "Bruno Giacomini", "data": "18/05/2025"},
    ]

    print("--- Posts do Blog ---")
    for post in post:
        print(f"Título: {post['titulo']} | Autor: {post['autor']} | Data: {post['data']}")

post_blog()