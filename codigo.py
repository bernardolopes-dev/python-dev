# Título: Hashzap
# Botão de iniciar chat
    # clicou no botão:
    # popup / modal
        # Título: Bem Vindo ao Hashzap
        # campo: escrever seu nome no chat
        # botão: entrar no chat
# chat
# embaixo do chat
    # campo de Digite sua mensagem
    # botão de enviar

# flet -> framework do Python 
# pip install flet

import flet as ft # importar

def main(pagina): # criar a função principal/main
    texto = ft.Text("Hashzap")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        print(mensagem)
        # adicione a mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print("Enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        # limpe o campo mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
        print("Entrar no chat")
        # fechar o popup
        popup.open = False
        # tirar o botão iniciar chat
        pagina.remove(botao_iniciar)
        # tirar o titulo hashzap
        pagina.remove(texto)
        # criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        # colocar o campo de digitar mensagem
        # criar o botão de enviar
        pagina.add(linha_enviar)
        pagina.update()

    titulo_popup = ft.Text("Bem Vindo ao Hashzap")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )
    
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER) # criar o app chamando a função principal