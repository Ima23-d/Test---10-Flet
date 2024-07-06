# import cv2
# import mediapipe as mp

# # Inicializa o módulo de detecção de pose do Mediapipe
# mp_pose = mp.solutions.pose
# pose = mp_pose.Pose()

# # Define a largura e a altura desejadas da tela
# largura_tela = 640
# altura_tela = 480

# # Função para detectar e desenhar a pose do corpo
# def detectar_pose_corpo():
#     cap = cv2.VideoCapture(0)  # Captura de vídeo da câmera

#     if not cap.isOpened():
#         print("Erro: Não foi possível abrir a câmera.")
#         return

#     # Define o tamanho do frame da câmera
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, largura_tela)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, altura_tela)

#     # Loop principal
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Erro: Não foi possível capturar o frame atual.")
#             break
#         frame = cv2.flip(frame, 1)  # Espelha o frame horizontalmente

#         # Convertendo a imagem para RGB (necessário para o Mediapipe)
#         image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         # Detecta a pose no frame atual
#         resultados = pose.process(image_rgb)

#         # Desenha as articulações na imagem
#         if resultados.pose_landmarks:
#             mp.solutions.drawing_utils.draw_landmarks(
#                 frame, resultados.pose_landmarks, mp_pose.POSE_CONNECTIONS)

#         # Mostra a imagem com as pose detectadas
#         cv2.imshow('Detecção de Pose do Corpo', frame)

#         # Condição de saída (tecla 'q' para sair)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Libera a captura e fecha todas as janelas
#     cap.release()
#     cv2.destroyAllWindows()

# # Chama a função principal para detectar e desenhar a pose do corpo
# detectar_pose_corpo()

# import flet as ft

# def main(page: ft.Page):
#     page.title = "AlertDialog example"
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

#     def handle_close(e):
#         page.close(dlg_modal)
#         page.remove(overlay)

#     def open_modal(e):
#         page.add(overlay)
#         page.open(dlg_modal)

#     dlg_modal = ft.AlertDialog(
#         modal=True,
#         title=ft.Text("Alert"),
#         content=ft.Text("This is just a message."),
#         actions=[],  # Nenhum botão de ação dentro do modal
#         on_dismiss=lambda e: page.remove(overlay),
#     )

#     overlay = ft.Container(
#         width="100%",
#         height="100%",
#         style={"background-color": "rgba(0, 0, 0, 0.5)"},  # Overlay transparente
#         on_click=handle_close,  # Fechar o modal ao clicar no overlay
#     )

#     page.add(
#         ft.ElevatedButton("Open modal dialog", on_click=open_modal),
#     )

# ft.app(target=main)

# import flet as ft


# def main(page: ft.Page):
#     page.window_width = 450
#     page.window_height = 700
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     sample_media = [
#         ft.VideoMedia("https://user-images.githubusercontent.com/28951144/229373720-14d69157-1a56-4a78-a2f4-d7a134d7c3e9.mp4",
#                      )]
#     def handle_play(e):
#         video.play()    
#     def handle_volume_change(e):
#         video.volume = e.control.value
#         page.update()
#     def handle_playback_rate_change(e):
#         video.playback_rate = e.control.value
#         page.update()
#     page.add(
#             video := ft.Video(expand=True,
#             playlist=sample_media[0:2],
#             playlist_mode=ft.PlaylistMode.LOOP,
#             fill_color=ft.colors.BLUE_400,
#             aspect_ratio=16/9,
#             volume=100,
#             autoplay=False,
#             filter_quality=ft.FilterQuality.HIGH,
#             muted=False))

# ft.app(target=main)

# import flet as ft

# def main(page):
#     text1 = ft.TextField(hint_text="digite",width=250,height=50,bgcolor="red",border_radius=20)
#     def nova(e):
#         page.clean()
#         texto2 = ft.Container(ft.Text(value=f"{text1.value}",size=30,color="black",weight="bold",text_align="center"),width=300,height=50,bgcolor="green",border_radius=20)
#         page.add(texto2)
#         page.update()
#     btn = ft.ElevatedButton("clique",width=250,height=50,bgcolor="blue",on_click=nova)
#     page.add(text1,btn)
#     page.update

# ft.app(target=main)
# import flet as ft 
 
 
# def janela(page):
#     def janela2(e):
#         page.clean()
#         segunda = ft.TextField(hint_text="Segunda",width=300,height=45,bgcolor="white",border_radius=20) 
#         terça = ft.TextField(hint_text="Terça",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#         quarta  = ft.TextField(label="Quarta",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#         quinta = ft.TextField(label="Quinta",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#         sexta = ft.TextField(label="Sexta",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#         sabado = ft.TextField(label="Sábado",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#         domingo = ft.TextField(label="Domingo",width=300,height=45,bgcolor="white",border_radius=20,border=None)
            
#         dia1 = ft.Container(ft.Text(value=f"{segunda.value}",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#         dia2 = ft.Container(ft.Text(value=f"{terça.value}",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#         dia3  = ft.Container(ft.Text(value=f"{quarta}",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#         dia4 = ft.Container(ft.Text(value=f"{quinta}",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#         dia5 = ft.Container(ft.Text(value=f"{sexta}",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#         dia6 = ft.Container(ft.Text(value=f"{sabado}",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#         dia7 = ft.Container(ft.Text(value=f"{domingo}",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
        
        
        
#         page.add(dia1)
#         page.update()
#         page.add()
#         page.update()
#     page.clean()
#     page.bgcolor = "#03B403" 
#     segunda = ft.TextField(hint_text="Segunda",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#     terça = ft.TextField(label="Terça",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#     quarta  = ft.TextField(label="Quarta",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#     quinta = ft.TextField(label="Quinta",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#     sexta = ft.TextField(label="Sexta",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#     sabado = ft.TextField(label="Sábado",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#     domingo = ft.TextField(label="Domingo",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
        
#     st = ft.Stack([ft.Container(ft.Image(src="plano semanal.png",width=600,height=500,
                                         
#                    fit=ft.ImageFit.COVER),width=600,height=500,border_radius=20),
                   
#                    ft.Container(content=ft.Column([ft.Text("Plano semanal",color="white",size=45,weight="bold"),
                                                   
#                   segunda,
#                   terça,
#                   quarta,
#                   quinta,
#                   sexta,
#                   sabado,
#                   domingo,

#                    ft.ElevatedButton(text="Começar",width=300,height=50,bgcolor="blue",color="white",on_click=janela2)],
                                                  
#                    alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),
                                
#                    alignment=ft.alignment.center,width=600,height=500)],width=600,height=500)
#     page.add(segunda)
#     page.update()
# ft.app(target=janela)

# import flet as ft 
# def janela(page):
#     page.vertical_alignment = "center"
#     page.horizontal_alignment = "center"
#     page.window_width = 450
#     page.window_height = 700
#     segunda = ft.TextField(hint_text="Segunda",width=300,height=45,bgcolor="white",border_radius=20)
#     terça = ft.TextField(hint_text="Terça",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#     quarta  = ft.TextField(label="Quarta",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#     quinta = ft.TextField(label="Quinta",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#     sexta = ft.TextField(label="Sexta",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#     sabado = ft.TextField(label="Sábado",width=300,height=45,bgcolor="white",border_radius=20,border=None)
#     domingo = ft.TextField(label="Domingo",width=300,height=45,bgcolor="white",border_radius=20,border=None)
    
#     cont = ft.Container((segunda,terça),width=300,height=500,bgcolor="blue")
#     def nova(e):
#         page.clean()
#         dia1 = ft.Container(ft.Text(value=f"{segunda.value}",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
#         dia2 = ft.Container(ft.Text(value=f"{terça.value}",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
        
#         page.add(dia1,dia2)
#         page.update()
#     btn = ft.ElevatedButton("clique",width=300,height=45,bgcolor="white",on_click=nova)
#     page.bgcolor = "red"
#     page.add(cont,btn)
#     page.update()
# ft.app(target=janela)

import flet as ft

# Variável global para armazenar o valor da segunda-feira
valor_segunda = ""

def plano_semanal(page):
    page.bgcolor = "#03B403"
    
    def nova(e):
        global valor_segunda  # Acessando a variável global
        page.clean()
        page.bgcolor = "#03B403"
        
        dia1 = ft.Container(ft.Text(value=f"{segunda.value}", size=30, color="black", weight="bold", text_align="center"),
                           width=300, height=45, bgcolor="white", border_radius=20, border=None)
        
        st = ft.Stack([
            ft.Container(ft.Image(src="verde,gif.gif", width=600, height=500, fit=ft.ImageFit.COVER),
                         width=600, height=500, border_radius=20),
            ft.Container(content=ft.Column([ft.Text("Seu Plano Semanal", color="white", size=40, weight="bold"),
                                            ],
                                           
                                           alignment=ft.MainAxisAlignment.CENTER,
                                           horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                         alignment=ft.alignment.center, width=600, height=500)],
            width=600, height=500, offset=ft.Offset(x=0, y=0.1))
        
        page.add(dia1)
        page.update()

    page.clean()
    
    segunda = ft.TextField(hint_text="Segunda", width=300, height=45, bgcolor="white", border_radius=20, border=None)
    st = ft.Stack([
        ft.Container(ft.Image(src="plano semanal.png", width=600, height=500, fit=ft.ImageFit.COVER),
                     width=600, height=500, border_radius=20),
        ft.Container(content=ft.Column([ft.Text("Plano semanal", color="white", size=45, weight="bold"),
                                        
                                        ft.ElevatedButton(text="Começar", width=300, height=50,
                                                           bgcolor="blue", color="white",
                                                           on_click=nova)],  # Adicionando o evento de clique
                                       alignment=ft.MainAxisAlignment.CENTER,
                                       horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                     alignment=ft.alignment.center, width=600, height=500)],
        width=600, height=500)
    button = ft.ElevatedButton(text="Começar", width=300, height=50,
                                                           bgcolor="blue", color="white",
                                                           on_click=nova)
    page.add(segunda,button)
    page.update()
ft.app(target=plano_semanal)
# Exemplo de uso:
# plano_semanal(minha_pagina)
