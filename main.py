import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_width = 450
    page.window_height = 700
    page.bgcolor = "#03B403"
    page.title = "Mendes - Fit"
    def nav_bar(e):
        page.clean()
        page.scroll = ft.ScrollMode.ALWAYS
        treinos_texto = ft.Text(value="Treinos:",color="white",weight="bold",size=45)
        page.bgcolor ="#03B403"
        
        #não e conteudo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        cont_braço = ft.Stack([ft.Container(ft.Image(src="treino de braço.png",width=400,height=120,fit=ft.ImageFit.COVER),width=400,height=120,border_radius=20),
                               
                               ft.Container(content=ft.Column([ft.Text("Treino de Braço",color="white",size=45,weight="bold")],  
                                                                                         
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),  
                                                      
                   alignment=ft.alignment.center,width=400,height=120,on_click=braço)],width=400,height=120)
        
        
        cont_costas = ft.Stack([ft.Container(ft.Image(src="treino de costa.png",width=400,height=120,fit=ft.ImageFit.COVER),width=400,height=120,border_radius=20),
                               
                               ft.Container(content=ft.Column([ft.Text("Treino de Costa",color="white",size=45,weight="bold")],  
                                                                                         
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),  
                                                      
                   alignment=ft.alignment.center,width=400,height=120,on_click=costa)],width=400,height=120,) 
        
        
        cont_abdomen = ft.Stack([ft.Container(ft.Image(src="treino de abdomen.png",width=400,height=120,fit=ft.ImageFit.COVER),width=400,height=120,border_radius=20),
                               
                               ft.Container(content=ft.Column([ft.Text("Treino de Abdomen",color="white",size=40,weight="bold")],  
                                                                                         
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),  
                                                      
                   alignment=ft.alignment.center,width=400,height=120,on_click=abdomen)],width=400,height=120)
        
        cont_perna = ft.Stack([ft.Container(ft.Image(src="treino de perna.png",width=400,height=120,fit=ft.ImageFit.COVER),width=400,height=120,border_radius=20),
                               
                               ft.Container(content=ft.Column([ft.Text("Treino de Perna",color="white",size=40,weight="bold")],  
                                                                                         
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),  
                                                      
                   alignment=ft.alignment.center,width=400,height=120,on_click=perna)],width=400,height=120)
        
        cont_peito = ft.Stack([ft.Container(ft.Image(src="treino de peito.png",width=400,height=120,fit=ft.ImageFit.COVER),width=400,height=120,border_radius=20),
                               
                               ft.Container(content=ft.Column([ft.Text("Treino de Peito",color="white",size=40,weight="bold")],  
                                                                                         
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),  
                                                      
                   alignment=ft.alignment.center,width=400,height=120,on_click=peito)],width=400,height=120)
        
        cont_ombros = ft.Stack([ft.Container(ft.Image(src="treino de ombros.png",width=400,height=120,fit=ft.ImageFit.COVER),width=400,height=120,border_radius=20),
                               
                               ft.Container(content=ft.Column([ft.Text("Treino de Ombros",color="white",size=40,weight="bold")],  
                                                                                         
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),  
                                                      
                   alignment=ft.alignment.center,width=400,height=120,on_click=ombros)],width=400,height=120)
        #não e conteudo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        
        def treino():
            page.clean()
            page.bgcolor ="#03B403"
            cont_braço = ft.Stack([ft.Container(ft.Image(src="treino de braço.png",width=400,height=120,fit=ft.ImageFit.COVER),width=400,height=120,border_radius=20),
                               
                               ft.Container(content=ft.Column([ft.Text("Treino de Braço",color="white",size=45,weight="bold")],  
                                                                                         
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),  
                                                      
                   alignment=ft.alignment.center,width=400,height=120,on_click=braço)],width=400,height=120)
        
        
            cont_costas = ft.Stack([ft.Container(ft.Image(src="treino de costa.png",width=400,height=120,fit=ft.ImageFit.COVER),width=400,height=120,border_radius=20),
                               
                               ft.Container(content=ft.Column([ft.Text("Treino de Costa",color="white",size=45,weight="bold")],  
                                                                                         
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),  
                                                      
                   alignment=ft.alignment.center,width=400,height=120,on_click=costa)],width=400,height=120,) 
        
        
            cont_abdomen = ft.Stack([ft.Container(ft.Image(src="treino de abdomen.png",width=400,height=120,fit=ft.ImageFit.COVER),width=400,height=120,border_radius=20),
                               
                               ft.Container(content=ft.Column([ft.Text("Treino de Abdomen",color="white",size=40,weight="bold")],  
                                                                                         
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),  
                                                      
                   alignment=ft.alignment.center,width=400,height=120,on_click=abdomen)],width=400,height=120)
        
            cont_perna = ft.Stack([ft.Container(ft.Image(src="treino de perna.png",width=400,height=120,fit=ft.ImageFit.COVER),width=400,height=120,border_radius=20),
                               
                               ft.Container(content=ft.Column([ft.Text("Treino de Perna",color="white",size=40,weight="bold")],  
                                                                                         
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),  
                                                      
                   alignment=ft.alignment.center,width=400,height=120,on_click=perna)],width=400,height=120)
        
            cont_peito = ft.Stack([ft.Container(ft.Image(src="treino de peito.png",width=400,height=120,fit=ft.ImageFit.COVER),width=400,height=120,border_radius=20),
                               
                               ft.Container(content=ft.Column([ft.Text("Treino de Peito",color="white",size=40,weight="bold")],  
                                                                                         
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),  
                                                      
                   alignment=ft.alignment.center,width=400,height=120,on_click=peito)],width=400,height=120)
        
            cont_ombros = ft.Stack([ft.Container(ft.Image(src="treino de ombros.png",width=400,height=120,fit=ft.ImageFit.COVER),width=400,height=120,border_radius=20),
                               
                               ft.Container(content=ft.Column([ft.Text("Treino de Ombros",color="white",size=40,weight="bold")],  
                                                                                         
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),  
                                                      
                   alignment=ft.alignment.center,width=400,height=120,on_click=ombros)],width=400,height=120)
        
        
            page.add(treinos_texto,cont_braço,cont_costas,cont_abdomen,cont_perna,cont_peito,cont_ombros)
            page.update()
            
        def alongamento():
            page.clean()
            page.bgcolor = "#03B403"
            texto_alongamento = ft.Text(value="Alongamento:",size=45,weight="bold",color="white",text_align="center")
            page.add(texto_alongamento)
            page.update()
            
        def nutrição():
            page.clean()
            page.bgcolor = "#03B403"
            page.add()
            page.update()
            
        def plano_semanal_tela():
            page.clean()
            page.bgcolor = "#03B403"
            
            dia1 = ft.Container(ft.Text(value=f"",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
            dia2 = ft.Container(ft.Text(value=f"",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
            dia3  = ft.Container(ft.Text(value=f"",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
            dia4 = ft.Container(ft.Text(value=f"",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
            dia5 = ft.Container(ft.Text(value=f"",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
            dia6 = ft.Container(ft.Text(value=f"",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
            dia7 = ft.Container(ft.Text(value=f"",size=30,color="black",weight="bold",text_align="center"),width=300,height=45,bgcolor="white",border_radius=20,border=None) 
        
            st = ft.Stack([ft.Container(ft.Image(src="verde,gif.gif",width=600,height=500,
                                         
                   fit=ft.ImageFit.COVER),width=600,height=500,border_radius=20),
                   
                   ft.Container(content=ft.Column([ft.Text("Seu Plano Semanal",color="white",size=40,weight="bold"),
                                                   dia1,
                                                   dia2,
                                                   dia3,
                                                   dia4,
                                                   dia5,
                                                   dia6,
                                                   dia7],
                                                  
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=10),
                                
                   alignment=ft.alignment.center,width=600,height=500)],width=600,height=500,offset=ft.Offset(x=0,y=0.1))
        
            page.add(st)
            page.update()
            
    # Função para criar e adicionar uma página laranja
       
            
        def on_nav_change(e):
            selected_index = e.control.selected_index
            page.clean()  # Limpa o conteúdo da página

            if selected_index == 0:
                treino()
            elif selected_index ==1:
                alongamento()
            elif selected_index == 2:
                nutrição()
            elif selected_index == 3:
                plano_semanal_tela()
        
        page.navigation_bar = ft.NavigationBar(destinations=[ft.NavigationDestination(icon=ft.icons.MAN, tooltip="Treinos",label="Treinos"),
                                                         ft.NavigationDestination(icon=ft.icons.HEALTH_AND_SAFETY_OUTLINED,tooltip="Alongamento", label="Alongamento"),
                                                         ft.NavigationDestination(icon=ft.icons.FOOD_BANK_SHARP,tooltip="Nutrição",label="Nutrição"),
                                                         ft.NavigationDestination(icon=ft.icons.CALENDAR_MONTH,tooltip="Plano semanal",label="Plano Semanal")],
                             on_change=on_nav_change,height=50,bgcolor="green",indicator_color="#0FE8E8",elevation=False)
        
        #não e conteudo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        page.add(treinos_texto,cont_braço,cont_costas,cont_abdomen,cont_perna,cont_peito,cont_ombros)
        page.update()
        #não e conteudo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
    #animação
    def animacao(e):
        if e.data == "true":
            container.width = 300
            container.height = 300
            container.background_color = ft.colors.YELLOW
        else:
            container.width = 250
            container.height = 250
            container.background_color = ft.colors.TRANSPARENT
        page.update()
        
    #ombros
    def ombros(e):
        page.clean()
        page.scroll = ft.ScrollMode.ALWAYS
        
        treino_costa = ft.Text(value="Treinos de Ombros:",color="white",weight="bold",size=45)
        
        btn_voltar = ft.Container((ft.Image(src="voltar.png",width=40,height=40,fit=ft.ImageFit.CONTAIN)),width=40,height=40,on_click=nav_bar,offset=ft.Offset(x=-4.5,y=0))
        
        braço_informacao = ft.Container((ft.Text(value="Treinar o peito pode ajudar a aumentar a massa muscular, o que é benéfico para a saúde metabólica, pois músculos maiores queimam mais calorias em repouso.",color = "white",weight="bold",size=20,text_align="center")),width=400,height=120,bgcolor="green",border_radius=20)
        
        quantidade = ft.Text(value="5 exercicios",color="white",weight="bold",size=25,offset=ft.Offset(x=-1,y=0)) 
        
        
        cont1 =  ft.Container(ft.Row([ft.Image(src="Supino inclinado com halter.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Supino .L Halter",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20)
        
        cont2 = ft.Container(ft.Row([ft.Image(src="supino-reto.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Supino .R Barra",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont3 = ft.Container(ft.Row([ft.Image(src="crossover-polia-média.webp",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="⁠Crossover .P Média",size=22,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.37,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont4 = ft.Container(ft.Row([ft.Image(src="Cross over polia baixa.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="⁠Crossover .P Baixa",size=22,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.36,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont5 = ft.Container(ft.Row([ft.Image(src="Crucifixo-Máquina-Pega.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Crucifixo na .M",size=22,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.35,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        
        page.add(btn_voltar,treino_costa,braço_informacao,quantidade,cont1,cont2,cont3,cont4,cont5)
        page.add()
        page.update()
        
    #peito
    def peito(e):
        page.clean()
        page.scroll = ft.ScrollMode.ALWAYS
        
        treino_costa = ft.Text(value="Treinos de Peito:",color="white",weight="bold",size=45)
        
        btn_voltar = ft.Container((ft.Image(src="voltar.png",width=40,height=40,fit=ft.ImageFit.CONTAIN)),width=40,height=40,on_click=nav_bar,offset=ft.Offset(x=-4.5,y=0))
        
        braço_informacao = ft.Container((ft.Text(value="Treinar o peito pode ajudar a aumentar a massa muscular, o que é benéfico para a saúde metabólica, pois músculos maiores queimam mais calorias em repouso.",color = "white",weight="bold",size=20,text_align="center")),width=400,height=120,bgcolor="green",border_radius=20)
        
        quantidade = ft.Text(value="5 exercicios",color="white",weight="bold",size=25,offset=ft.Offset(x=-1,y=0)) 
        
        
        cont1 =  ft.Container(ft.Row([ft.Image(src="Supino inclinado com halter.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Supino .L Halter",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20)
        
        cont2 = ft.Container(ft.Row([ft.Image(src="supino-reto.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Supino .R Barra",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont3 = ft.Container(ft.Row([ft.Image(src="crossover-polia-média.webp",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="⁠Crossover .P Média",size=22,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.37,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont4 = ft.Container(ft.Row([ft.Image(src="Cross over polia baixa.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="⁠Crossover .P Baixa",size=22,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.36,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont5 = ft.Container(ft.Row([ft.Image(src="Crucifixo-Máquina-Pega.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Crucifixo na .M",size=22,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.35,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        
        page.add(btn_voltar,treino_costa,braço_informacao,quantidade,cont1,cont2,cont3,cont4,cont5)
        page.update()
        
    #perna
    def perna(e):
        page.clean()
        page.scroll = ft.ScrollMode.ALWAYS
        
        treino_costa = ft.Text(value="Treinos de Pernas:",color="white",weight="bold",size=45)
        
        btn_voltar = ft.Container((ft.Image(src="voltar.png",width=40,height=40,fit=ft.ImageFit.CONTAIN)),width=40,height=40,on_click=nav_bar,offset=ft.Offset(x=-4.5,y=0))
        
        braço_informacao = ft.Container((ft.Text(value="Treinar grandes grupos musculares, como os das pernas, pode aumentar significativamente o metabolismo.",color = "white",weight="bold",size=20,text_align="center")),width=400,height=120,bgcolor="green",border_radius=20)
        
        quantidade = ft.Text(value="4 exercicios",color="white",weight="bold",size=25,offset=ft.Offset(x=-1,y=0)) 
        
        
        cont1 =  ft.Container(ft.Row([ft.Image(src="agachamento-barra.webp",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Agachamento .L .B",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20)
        
        cont2 = ft.Container(ft.Row([ft.Image(src="cadeira-extensora-homem.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Cadeira Extensora",size=23,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.36,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont3 = ft.Container(ft.Row([ft.Image(src="mesa-flexora-exercicio.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Mesa Flexora",size=22,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont4 = ft.Container(ft.Row([ft.Image(src="panturrilha. em pe.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Panturrilha em .P",size=22,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.36,y=0))]),width=400,height=120,bgcolor="green",border_radius=20)
        
        cont5 = ft.Container(ft.Row([ft.Image(src="leg-press-45.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Leg 45°",size=22,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont6 = ft.Container(ft.Row([ft.Image(src="leg press horizontal.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Leg horizontal",size=22,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.36,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        
        page.add(btn_voltar,treino_costa,braço_informacao,quantidade,cont1,cont2,cont3,cont4,cont5,cont6)
        page.update()
        
    # abdomen
    def abdomen(e):
        page.clean()
        page.scroll = ft.ScrollMode.ALWAYS
        
        treino_braço = ft.Text(value="Treinos de Abdomen:",color="white",weight="bold",size=40)
        
        btn_voltar = ft.Container((ft.Image(src="voltar.png",width=40,height=40,fit=ft.ImageFit.CONTAIN)),width=40,height=40,on_click=nav_bar,offset=ft.Offset(x=-4.5,y=0))
        
        braço_informacao = ft.Container((ft.Text(value="Treinar o abdomen, fortalece os músculos abdominais ajuda a proteger a coluna vertebral e a prevenir lesões, especialmente nas costas.",color = "white",weight="bold",size=20,text_align="center")),width=400,height=120,bgcolor="green",border_radius=20)
        
        quantidade = ft.Text(value="6 exercicios",color="white",weight="bold",size=25,offset=ft.Offset(x=-1,y=0)) 
        
        
        cont1 =  ft.Container(ft.Row([ft.Image(src="abdominal reto no solo.webp",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Abdominal .R .S",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.35,y=0))]),width=400,height=120,bgcolor="green",border_radius=20)
        
        cont2 = ft.Container(ft.Row([ft.Image(src="exercicio-de-prancha.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Prancha",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont3 = ft.Container(ft.Row([ft.Image(src="Abdominal-Reto-Sentado-na-Máquina.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Abdominal .M",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont4 = ft.Container(ft.Row([ft.Image(src="barra-fixa.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Elevação .P .BF",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont5 = ft.Container(ft.Row([ft.Image(src="abdominal-bicicleta.webp",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Abdominal .B",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.35,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont6 = ft.Container(ft.Row([ft.Image(src="Prancha lateral.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Prancha Lateral",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
     
        
        page.add(btn_voltar,treino_braço,braço_informacao,quantidade,cont1,cont2,cont3,cont4,cont5,cont6)
        page.update
        
    #costa
    def costa(e):
        page.clean()
        page.scroll = ft.ScrollMode.ALWAYS
        
        treino_costa = ft.Text(value="Treinos de Costa:",color="white",weight="bold",size=45)
        
        btn_voltar = ft.Container((ft.Image(src="voltar.png",width=40,height=40,fit=ft.ImageFit.CONTAIN)),width=40,height=40,on_click=nav_bar,offset=ft.Offset(x=-4.5,y=0))
        
        braço_informacao = ft.Container((ft.Text(value="Músculos das costas fortes são essenciais para a realização de atividades diárias que envolvem levantamento, empurrar e puxar.",color = "white",weight="bold",size=20,text_align="center")),width=400,height=120,bgcolor="green",border_radius=20)
        
        quantidade = ft.Text(value="5 exercicios",color="white",weight="bold",size=25,offset=ft.Offset(x=-1,y=0)) 
        
        
        cont1 =  ft.Container(ft.Row([ft.Image(src="Puxada aperta de costa.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Puxada Aberta",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20)
        
        cont2 = ft.Container(ft.Row([ft.Image(src="Puxada no triangulo.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Puxada No .T",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont3 = ft.Container(ft.Row([ft.Image(src="remada-curvada-.webp",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Puxada .C Barra",size=22,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont4 = ft.Container(ft.Row([ft.Image(src="remada-unilateral.png",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Remada .U Halter .S",size=22,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont5 = ft.Container(ft.Row([ft.Image(src="pull-down-tronco-curvado.webp",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Pulldown Na Polia",size=22,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.35,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        
        page.add(btn_voltar,treino_costa,braço_informacao,quantidade,cont1,cont2,cont3,cont4,cont5)
        page.update()
    
    #braço
    def braço(e):
        page.clean()
        page.scroll = ft.ScrollMode.ALWAYS
        
        treino_braço = ft.Text(value="Treinos de Braço:",color="white",weight="bold",size=45)
        
        btn_voltar = ft.Container((ft.Image(src="voltar.png",width=40,height=40,fit=ft.ImageFit.CONTAIN)),width=40,height=40,on_click=nav_bar,offset=ft.Offset(x=-4.5,y=0))
        
        braço_informacao = ft.Container((ft.Text(value="Treinar os braços ajuda a manter um equilíbrio muscular.",color = "white",weight="bold",size=26,text_align="center")),width=400,height=120,bgcolor="green",border_radius=20)
        
        quantidade = ft.Text(value="6 exercicios",color="white",weight="bold",size=25,offset=ft.Offset(x=-1,y=0)) 
        
        
        cont1 =  ft.Container(ft.Row([ft.Image(src="rosca-scott-.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Rosca Scott",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20)
        
        cont2 = ft.Container(ft.Row([ft.Image(src="Rosca alternada inclinada.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Rosca .In 45°",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont3 = ft.Container(ft.Row([ft.Image(src="Roca martelo com halter.webp",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Rosca .M Halter",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont4 = ft.Container(ft.Row([ft.Image(src="triceps corda.webp",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Triceps Corda",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont5 = ft.Container(ft.Row([ft.Image(src="Triceps frances com halter.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Triceps .F Halter",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.35,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
        
        cont6 = ft.Container(ft.Row([ft.Image(src="Triceps testa na polia.jpg",offset=ft.Offset(x=-0.3,y=0),
                                               fit=ft.ImageFit.COVER,width=260,height=120),
                                      ft.Text(value="Triceps .T polia",size=24,color="white",weight="bold",text_align="center",
                                              offset=ft.Offset(x=-0.3,y=0))]),width=400,height=120,bgcolor="green",border_radius=20) 
     
        
        page.add(btn_voltar,treino_braço,braço_informacao,quantidade,cont1,cont2,cont3,cont4,cont5,cont6)
        page.update

    #treinos
    #nav bar@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
        #nav bar@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                      
        
        
    #plano semanal
    def plano_semanal(e):
        page.clean()
      
        segunda = ft.TextField(label="Segunda",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
        terça = ft.TextField(label="Terça",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
        quarta  = ft.TextField(label="Quarta",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
        quinta = ft.TextField(label="Quinta",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
        sexta = ft.TextField(label="Sexta",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
        sabado = ft.TextField(label="Sábado",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
        domingo = ft.TextField(label="Domingo",width=300,height=45,bgcolor="white",border_radius=20,border=None) 
        
        st = ft.Stack([ft.Container(ft.Image(src="plano semanal.png",width=600,height=500,
                                         
                   fit=ft.ImageFit.COVER),width=600,height=500,border_radius=20),
                   
                   ft.Container(content=ft.Column([ft.Text("Plano semanal",color="white",size=45,weight="bold"),
                                                   
                  segunda,
                  terça,
                  quarta,
                  quinta,
                  sexta,
                  sabado,
                  domingo,

                   ft.ElevatedButton(text="Começar",width=300,height=50,bgcolor="blue",color="white",on_click=nav_bar)],
                                                  
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),
                                
                   alignment=ft.alignment.center,width=600,height=500)],width=600,height=500)
        
        page.add(st)
        page.update()
        
    #alimentacao
    def alimentacao(e):
        page.clean()
        restrição = ft.TextField(label="Possui alguma restrição alimentar?",width=300,height=50,bgcolor="white",border_radius=20,border=None)
        preferencia = ft.TextField(label="Preferencia em comida?",width=300,height=50,bgcolor="white",border_radius=20,border=None)
        vegano = ft.TextField(label="È vegano(a) ?",width=300,height=50,bgcolor="white",border_radius=20,border=None)
        doença = ft.TextField(label="Possui alguma doença alimentar?",width=300,height=50,bgcolor="white",border_radius=20,border=None)
        
        st = ft.Stack([ft.Container(ft.Image(src="alimentol.webp",width=600,height=500,
                                         
                   fit=ft.ImageFit.COVER),width=600,height=500,border_radius=20),
                   
                   ft.Container(content=ft.Column([ft.Text("Alimentação",color="white",size=45,weight="bold"),
                                                   
                  restrição,
                  preferencia,
                  vegano,
                  doença,

                   ft.ElevatedButton(text="Proximo",width=300,height=50,bgcolor="blue",color="white",on_click=plano_semanal)],
                                                  
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),
                                
                   alignment=ft.alignment.center,width=600,height=500)],width=600,height=500)
         
        page.add(st)
        page.add()
        page.update()
        
    #Suas informações
    def suas_informaçoes(e):
        page.clean()
        idade = ft.TextField(label="Digite a sua idade",width=300,height=50,bgcolor="white",border_radius=20,border=None)
        altura = ft.TextField(label="Digite a sua altura",width=300,height=50,bgcolor="white",border_radius=20,border=None)
        peso = ft.TextField(label="Digite o seu peso",width=300,height=50,bgcolor="white",border_radius=20,border=None)
        doença = ft.TextField(label="Possui alguma doença?",width=300,height=50,bgcolor="white",border_radius=20,border=None)
        
        st = ft.Stack([ft.Container(ft.Image(src="consulta-médica.jpg",width=600,height=500,
                                         
                   fit=ft.ImageFit.COVER),width=600,height=500,border_radius=20),
                   
                   ft.Container(content=ft.Column([ft.Text("Suas informações",color="white",size=45,weight="bold"),
                                                   
                  idade,
                  altura,
                  peso,
                  doença,

                   ft.ElevatedButton(text="Proximo",width=300,height=50,bgcolor="blue",color="white",on_click=alimentacao)],
                                                  
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5),
                                
                   alignment=ft.alignment.center,width=600,height=500)],width=600,height=500)
         
        page.add(st)
        page.update()
        
    #fazer_login
    def fazer_login(e):
        page.clean()
        email = ft.TextField(label="Email",width=300,height=50,bgcolor="white",border_radius=10) 
        senha =  ft.TextField(label="Senha",width=300,height=50,bgcolor="white",password=True,can_reveal_password=True,border_radius=10)
        
        st = ft.Stack([ft.Container(ft.Image(src="verde,gif.gif",width=600,height=500,
                                         
                   fit=ft.ImageFit.COVER),width=600,height=500,border_radius=20),
                   
                   ft.Container(content=ft.Column([ft.Text("Fazer login",color="white",size=45,weight="bold"),
                                                   
                  email,
                  senha,

                   ft.ElevatedButton(text="Entrar",width=300,height=50,bgcolor="blue",color="white",on_click=suas_informaçoes)],
                                                  
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=20),
                                
                   alignment=ft.alignment.center,width=600,height=500)],width=600,height=500)
        page.add(st)
        page.update()
    #cadastro  
    def cadastro(e):
        page.clean()
        
        usuario = ft.TextField(label="Nome",width=300,height=50,bgcolor="white",border_radius=10)
        email = ft.TextField(label="Email",width=300,height=50,bgcolor="white",border_radius=10) 
        senha =  ft.TextField(label="Senha",width=300,height=50,bgcolor="white",password=True,can_reveal_password=True,border_radius=10)
        ja_possui =  ft.Row([ft.Text(value="Já possui uma conta?",size=20,color="white",weight="bold"),
                           ft.Container((ft.Text(value="Fazer login",size=20,color="blue",weight="bold")),on_click=fazer_login)],alignment=ft.MainAxisAlignment.CENTER)
        #Container
        st = ft.Stack([ft.Container(ft.Image(src="teste copy.jpg",width=600,height=500,
                                         
                   fit=ft.ImageFit.COVER),width=600,height=500,border_radius=20),
                   
                   ft.Container(content=ft.Column([ft.Text("Cadastro",color="white",size=45,weight="bold"),                              
                   usuario,
                   email,
                   senha,
                   ja_possui, 
                   ft.ElevatedButton(text="Entrar",width=300,height=50,bgcolor="blue",color="white",on_click=suas_informaçoes)],
                                                  
                   alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=20),
                                
                   alignment=ft.alignment.center,width=600,height=500)],width=600,height=500)
        page.add(st)
        page.update() 
     #animação   
   
        
    container = ft.Container(content=ft.Image(src="nova_logo.png", fit=ft.ImageFit.CONTAIN),width=300,height=300,
                             bgcolor=ft.colors.TRANSPARENT,animate=ft.Animation(duration=300, curve=ft.AnimationCurve.EASE),
                             on_hover=animacao,on_click=cadastro)
    page.add(container)
    page.update()
    

ft.app(target=main)


