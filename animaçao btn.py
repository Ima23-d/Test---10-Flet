# import flet as ft 
# def janela(page):
#     page.title = "Mendes - Fit"
#     page.window_width = 420
#     page.window_height = 700
#     page.vertical_alignment = "center"
#     page.horizontal_alignment = "center"
#     page.bgcolor = "#03B403"
#     logo = ft.Image(src="nova_logo.png",width=240,height=240,fit=ft.ImageFit.CONTAIN)

#     def animacao(e):
#         if e.data == "true":
#             container.width = 300
#             container.height = 300
#             container.background_color = ft.colors.YELLOW
#         else:
#             container.width = 250
#             container.height = 250
#             container.background_color = ft.colors.TRANSPARENT
#         page.update()
        
#     def cadastro(e):
#         page.clean()
#         cont_cadastro = ft.Container(width=360,height=500,bgcolor="red",border_radius=20)
#         page.add(cont_cadastro)
#         page.update()
#     container = ft.Container(content=ft.Image(src="nova_logo.png", fit=ft.ImageFit.CONTAIN),width=300,height=300,
#                              bgcolor=ft.colors.TRANSPARENT,animate=ft.Animation(duration=300, curve=ft.AnimationCurve.EASE),
#                              on_hover=animacao,on_click=cadastro)

#     page.add(container)
#     page.update()
#     pass
# ft.app(target=janela)

#nav-bar1
# import flet as ft

# def main(page: ft.Page):

#     # Função para atualizar o conteúdo da página baseado na seleção
#     def on_nav_change(e):
#         selected_index = e.control.selected_index
#         page.clean()  # Limpa o conteúdo da página
#         if selected_index == 0:
#             page.add(ft.Text("Você está na página Explore"))
#         elif selected_index == 1:
#             page.add(ft.Text("Você está na página Commute"))
#         elif selected_index == 2:
#             page.add(ft.Text("Você está na página Bookmark"))

#     # Configuração da NavigationBar com a função on_change
#     page.title = "NavigationBar Example"
#     page.navigation_bar = ft.NavigationBar(
#         destinations=[
#             ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
#             ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
#             ft.NavigationBarDestination(
#                 icon=ft.icons.BOOKMARK_BORDER,
#                 selected_icon=ft.icons.BOOKMARK,
#                 label="Bookmark",
#             ),
#         ],
#         on_change=on_nav_change,
#     )

#     # Adicionando um texto inicial no corpo da página principal
#     page.add(ft.Text("Clique nos ícones da NavigationBar para mudar o conteúdo da página."))

# # Executar a aplicação
# ft.app(target=main)

#nav-bar2
# import flet as ft

# def main(page: ft.Page):

#     # Função para atualizar o conteúdo da página baseado na seleção
#     def on_nav_change(e):
#         selected_index = e.control.selected_index
#         page.clean()  # Limpa o conteúdo da página
#         if selected_index == 0:
#             page.add(ft.Container(content=ft.Text("Você está na página Explore"), bgcolor=ft.colors.BLUE, expand=True))
#         elif selected_index == 1:
#             page.add(ft.Container(content=ft.Text("Você está na página Commute"), bgcolor=ft.colors.GREEN, expand=True))
#         elif selected_index == 2:
#             page.add(ft.Container(content=ft.Text("Você está na página Bookmark"), bgcolor=ft.colors.ORANGE, expand=True))

#     # Configuração da NavigationBar com a função on_change
#     page.title = "NavigationBar Example"
#     page.navigation_bar = ft.NavigationBar(
#         destinations=[
#             ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
#             ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
#             ft.NavigationBarDestination(
#                 icon=ft.icons.BOOKMARK_BORDER,
#                 selected_icon=ft.icons.BOOKMARK,
#                 label="Bookmark",
#             ),
#         ],
#         on_change=on_nav_change,
#     )

#     # Adicionando um texto inicial no corpo da página principal
#     page.add(ft.Text("Clique nos ícones da NavigationBar para mudar o conteúdo da página."))

# # Executar a aplicação
# ft.app(target=main)

#nav-bar 3
# import flet as ft

# def main(page: ft.Page):

#     # Função para atualizar o conteúdo da página baseado na seleção
#     def on_nav_change(e):
#         selected_index = e.control.selected_index
#         page.clean()  # Limpa o conteúdo da página
#         if selected_index == 0:
#             page.add(ft.Containerft.Text("Você está na página Explore"), bgcolor=ft.colors.BLUE, expand=True))
#         elif selected_index == 1:
#             page.add(ft.Container(content=ft.Text("Você está na página Commute"), bgcolor=ft.colors.GREEN, expand=True))
#         elif selected_index == 2:
#             page.add(ft.Container(content=ft.Text("Você está na página Bookmark"), bgcolor=ft.colors.ORANGE, expand=True))

#     # Configuração da NavigationBar com a função on_change
#     page.title = "NavigationBar Example"
#     page.navigation_bar = ft.NavigationBar(
#         destinations=[
#             ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
#             ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
#             ft.NavigationBarDestination(
#                 icon=ft.icons.BOOKMARK_BORDER,
#                 selected_icon=ft.icons.BOOKMARK,
#                 label="Bookmark",
#             ),
#         ],
#         on_change=on_nav_change,
#     )

#     # Adicionando um texto inicial no corpo da página principal
#     page.add(ft.Text("Clique nos ícones da NavigationBar para mudar o conteúdo da página."))

# # Executar a aplicação
# ft.app(target=main)

#nav bar 4
# import flet as ft

# def main(page: ft.Page):

#     # Função para criar e adicionar uma página vermelha
#     def add_red_page():
#         page.clean()
#         page.bgcolor = "red"
#         page.add(ft.Text("Você está na página Explore", bgcolor=ft.colors.RED, expand=True))
#         page.update()

#     # Função para atualizar o conteúdo da página baseado na seleção
#     def on_nav_change(e):
#         selected_index = e.control.selected_index
#         page.clean()  # Limpa o conteúdo da página

#         if selected_index == 0:
#             add_red_page()
#         elif selected_index == 1:
#             page.clean()
#             page.add(ft.Container(content=ft.Text("Você está na página Commute"), bgcolor=ft.colors.GREEN, expand=True))
#         elif selected_index == 2:
#             page.clean()
#             page.add(ft.Container(content=ft.Text("Você está na página Bookmark"), bgcolor=ft.colors.ORANGE, expand=True))

#         # Caso contrário, a cor de fundo padrão da página é restaurada
#         if selected_index != 0:
#             page.bgcolor = None
#             page.update()

#     # Configuração da NavigationBar com a função on_change
#     page.title = "NavigationBar Example"
#     page.navigation_bar = ft.NavigationBar(
#         destinations=[
#             ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
#             ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
#             ft.NavigationBarDestination(
#                 icon=ft.icons.BOOKMARK_BORDER,
#                 selected_icon=ft.icons.BOOKMARK,
#                 label="Bookmark",
#             ),
#         ],
#         on_change=on_nav_change,
#     )

#     # Adicionando um texto inicial no corpo da página principal
#     page.add(ft.Text("Clique nos ícones da NavigationBar para mudar o conteúdo da página."))

# # Executar a aplicação
# ft.app(target=main)

#nav bar funcional
# import flet as ft

# def main(page: ft.Page):

#     # Função para criar e adicionar uma página vermelha
#     def add_red_page():
#         page.clean()
#         page.bgcolor = "red"
#         page.add()
#         page.update()

#     # Função para criar e adicionar uma página verde
#     def add_green_page():
#         page.clean()
#         page.bgcolor = "green"
#         page.add()
#         page.update()

#     # Função para criar e adicionar uma página laranja
#     def add_orange_page():
#         page.clean()
#         page.bgcolor = "blue"
#         page.add()
#         page.update()

#     # Função para atualizar o conteúdo da página baseado na seleção
#     def on_nav_change(e):
#         selected_index = e.control.selected_index
#         page.clean()  # Limpa o conteúdo da página

#         if selected_index == 0:
#             add_red_page()
#         elif selected_index == 1:
#             add_green_page()
#         elif selected_index == 2:
#             add_orange_page()
#         page.update()

#     # Configuração da NavigationBar com a função on_change
#     page.title = "NavigationBar Example"
    
#     page.navigation_bar = ft.NavigationBar(destinations=[ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
#                                                          ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
#                                                          ft.NavigationBarDestination(icon=ft.icons.BOOKMARK_BORDER,selected_icon=ft.icons.BOOKMARK,label="Bookmark")],
#                                            on_change=on_nav_change)

#     # Adicionando um texto inicial no corpo da página principal
#     page.add()

# # Executar a aplicação
# ft.app(target=main)

import flet as ft 
def janela(page):
    page.title = "calcular nota "
    page.window_height = 700
    page.window_width = 400
    page.bgcolor="#FA4141"
    img = ft.Image(src="https://th.bing.com/th/id/OIG4.wLz1UqYyUpswyOgJuRcR?pid=ImgGn",width=200,height=200,fit=ft.ImageFit.CONTAIN)
    def abrir (e):
        page.clean()
        text = ft.Text(value="Escolha:",size=35,color="white")
        def inti(e):
            page.clean()
            i = ft.Text(value="Intinerário",color="white",size=30)
            começoint = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=abrir,bgcolor="white")
            def en(e):
                page.clean()
                sua  = ft.Text(value="Digite Suas Notas:",size=35,color="white")
                av1 = ft.TextField(hint_text="Prova objetiva",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                av2 = ft.TextField(hint_text="Prova Prática",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                inten = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=inti,bgcolor="white")
                def nen(e):
                    page.clean()
                    calcular_nota = (float(av1.value) + float(av1.value)) / 2
                    notafinal = ft.Text(value=f"Sua média final trimestral é:",size=25,color="white")
                    resultado = ft.Container(ft.Text(value=f"{calcular_nota}",size=35,color="white"))
                    voltaren = ft.ElevatedButton("Voltar",width=250,height=50,color="black",on_click=en,bgcolor="white")
                    page.add(notafinal,resultado,voltaren)
                    page.update()
                calcular = ft.ElevatedButton("Calcular",width=250,height=50,color="black",on_click=nen,bgcolor="white")
                page.add(sua,av1,av2,calcular,inten)
                page.update()
            engenharia = ft.ElevatedButton("Engenharia ||",width=250,height=50,color="black",on_click=en,bgcolor="white")
            def pen(e):
                page.clean()
                sua  = ft.Text(value="Digite Suas Notas:",size=35,color="white")
                av1 = ft.TextField(hint_text="Prova objetiva",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                av2 = ft.TextField(hint_text="Prova Prática",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                intpen = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=inti,bgcolor="white")
                def npen(e):
                    page.clean()
                    calcular_nota = (float(av1.value) + float(av1.value)) / 2
                    notafinal = ft.Text(value=f"Sua média final trimestral é:",size=25,color="white")
                    resultado = ft.Container(ft.Text(value=f"{calcular_nota}",size=35,color="white"))
                    voltarpen = ft.ElevatedButton("Voltar",width=250,height=50,color="black",on_click=pen,bgcolor="white")
                    page.add(notafinal,resultado,voltarpen)
                    page.update()
                calcular = ft.ElevatedButton("Calcular",width=250,height=50,color="black",on_click=npen,bgcolor="white")
                page.add(sua,av1,av2,calcular,intpen)
                page.update()
            Pensamento = ft.ElevatedButton("Pensamento Estatístico",width=250,height=50,color="black",on_click=pen,bgcolor="white")
            def ino(e):
                page.clean()
                sua  = ft.Text(value="Digite Suas Notas:",size=35,color="white")
                av1 = ft.TextField(hint_text="Prova objetiva",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                av2 = ft.TextField(hint_text="Prova Prática",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                intino = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=inti,bgcolor="white")
                def nino(e):
                    page.clean()
                    calcular_nota = (float(av1.value) + float(av1.value)) / 2
                    notafinal = ft.Text(value=f"Sua média final trimestral é:",size=25,color="white")
                    resultado = ft.Container(ft.Text(value=f"{calcular_nota}",size=35,color="white"))
                    voltarino = ft.ElevatedButton("Voltar",width=250,height=50,color="black",on_click=ino,bgcolor="white")
                    page.add(notafinal,resultado,voltarino)
                    page.update()
                calcular = ft.ElevatedButton("Calcular",width=250,height=50,color="black",on_click=nino,bgcolor="white")
                page.add(sua,av1,av2,calcular,intino)
                page.update()
            inovação = ft.ElevatedButton("Inovação",width=250,height=50,color="black",on_click=ino,bgcolor="white")
            def fi(e):
                page.clean()
                sua  = ft.Text(value="Digite Suas Notas:",size=35,color="white")
                av1 = ft.TextField(hint_text="Prova objetiva",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                av2 = ft.TextField(hint_text="Prova Prática",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                intfi = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=inti,bgcolor="white")
                def nfi(e):
                    page.clean()
                    calcular_nota = (float(av1.value) + float(av1.value)) / 2
                    notafinal = ft.Text(value=f"Sua média final trimestral é:",size=25,color="white")
                    resultado = ft.Container(ft.Text(value=f"{calcular_nota}",size=35,color="white"))
                    voltarnfi = ft.ElevatedButton("Voltar",width=250,height=50,color="black",on_click=fi,bgcolor="white")
                    page.add(notafinal,resultado,voltarnfi)
                    page.update()
                calcular = ft.ElevatedButton("Calcular",width=250,height=50,color="black",on_click=nfi,bgcolor="white")
                page.add(sua,av1,av2,calcular,intfi)
                page.update()
            finançãs = ft.ElevatedButton("Finanças",width=250,height=50,color="black",on_click=fi,bgcolor="white")
            page.add(i,engenharia,Pensamento,inovação,finançãs,começoint)
            page.update()
        intinerario = ft.ElevatedButton("Intinerário",width=250,height=50,color="black",on_click=inti,bgcolor="white")
        def mate(e):
            page.clean()
            m = ft.Text(value="Matérias",color="white",size=30)
            começomate = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=abrir,bgcolor="white")
            def ma(e):
                page.clean()
                sua  = ft.Text(value="Digite Suas Notas:",size=35,color="white")
                av1 = ft.TextField(hint_text="Avaliação 1",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                av2 = ft.TextField(hint_text="Avaliação 2",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                avt = ft.TextField(hint_text="Avaliação Trimestral",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                mama = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=mate,bgcolor="white")
                def nma(e):
                    page.clean()
                    calcular_nota = calcular_nota = (float(av1.value) * 25 + float(av2.value) * 25 + float(avt.value) * 50) / 100
                    notafinal = ft.Text(value=f"Sua média final trimestral é:",size=25,color="white")
                    resultado = ft.Container(ft.Text(value=f"{calcular_nota}",size=35,color="white"))
                    maman = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=ma,bgcolor="white")
                    page.add(notafinal,resultado,maman)
                    page.update()
                calcular = ft.ElevatedButton("Calcular",width=250,height=50,color="black",on_click=nma,bgcolor="white")
                page.add(sua,av1,av2,avt,calcular,mama)
                page.update()
            matematica = ft.ElevatedButton("Matemática",width=250,height=50,color="black",on_click=ma,bgcolor="white")
            def na(e):
                page.clean()
                sua  = ft.Text(value="Digite Suas Notas:",size=35,color="white")
                av1 = ft.TextField(hint_text="Avaliação 1",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                av2 = ft.TextField(hint_text="Avaliação 2",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                avt = ft.TextField(hint_text="Avaliação Trimestral",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                mana = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=ma,bgcolor="white")
                def nna(e):
                    page.clean()
                    calcular_nota  = (float(av1.value) * 25 + float(av2.value) * 25 + float(avt.value) * 50) / 100
                    notafinal = ft.Text(value=f"Sua média final trimestral é:",size=25,color="white")
                    resultado = ft.Container(ft.Text(value=f"{calcular_nota}",size=35,color="white"))
                    manan = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=na,bgcolor="white")
                    page.add(notafinal,resultado,manan)
                    page.update()
                calcular = ft.ElevatedButton("Calcular",width=250,height=50,color="black",on_click=nna,bgcolor="white")
                page.add(sua,av1,av2,avt,calcular,mana)
                page.update()
            natureza = ft.ElevatedButton("Natureza",width=250,height=50,color="black",on_click=na,bgcolor="white")
            def hu(e):
                page.clean()
                sua  = ft.Text(value="Digite Suas Notas:",size=35,color="white")
                av1 = ft.TextField(hint_text="Avaliação 1",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                av2 = ft.TextField(hint_text="Avaliação 2",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                avt = ft.TextField(hint_text="Avaliação Trimestral",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                mahu = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=mate,bgcolor="white")
                def nhu(e):
                    page.clean()
                    calcular_nota = calcular_nota = (float(av1.value) * 25 + float(av2.value) * 25 + float(avt.value) * 50) / 100
                    notafinal = ft.Text(value=f"Sua média final trimestral é:",size=25,color="white")
                    resultado = ft.Container(ft.Text(value=f"{calcular_nota}",size=35,color="white"))
                    mahun = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=ma,bgcolor="white")
                    page.add(notafinal,resultado,mahun)
                    page.update()
                calcular = ft.ElevatedButton("Calcular",width=250,height=50,color="black",on_click=nhu,bgcolor="white")
                page.add(sua,av1,av2,avt,calcular,mahu)
                page.update()
            humanas = ft.ElevatedButton("Humanas",width=250,height=50,color="black",on_click=hu,bgcolor="white")
            def li(e):
                page.clean()
                sua  = ft.Text(value="Digite Suas Notas:",size=35,color="white")
                av1 = ft.TextField(hint_text="Avaliação 1",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                av2 = ft.TextField(hint_text="Avaliação 2",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                avt = ft.TextField(hint_text="Avaliação Trimestral",width=250,height=50,border_radius=20,color="white",border_color="white",text_align="center")
                mali = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=mate,bgcolor="white")
                def nli(e):
                    page.clean()
                    calcular_nota = calcular_nota = (float(av1.value) * 25 + float(av2.value) * 25 + float(avt.value) * 50) / 100 
                    notafinal = ft.Text(value=f"Sua média final trimestral é:",size=25,color="white")
                    resultado = ft.Container(ft.Text(value=f"{calcular_nota}",size=35,color="white"))
                    malin = ft.ElevatedButton("Voltar ao começo",width=250,height=50,color="black",on_click=ma,bgcolor="white")
                    page.add(notafinal,resultado,malin)
                    page.update()
                calcular = ft.ElevatedButton("Calcular",width=250,height=50,color="black",on_click=nli,bgcolor="white")
                page.add(sua,av1,av2,avt,calcular,mali)
                page.update()
            linguagens = ft.ElevatedButton("Linguagens",width=250,height=50,color="black",on_click=li,bgcolor="white")
            page.add(m,matematica,natureza,humanas,linguagens,começomate)
            page.update()
        materias = ft.ElevatedButton("Matérias",width=250,height=50,color="black",on_click=mate,bgcolor="white")
        page.add(text,intinerario,materias)
        page.update()
    bnt = ft.ElevatedButton("Começar",width=250,height=50,on_click=abrir,color="black",bgcolor="white")
    page.add(img,bnt)
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.update()
    pass
ft.app(target=janela)