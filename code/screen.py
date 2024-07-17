from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from organizador import organizarDir
from organizador import msmFinal
from plyer import filechooser 

GUI = Builder.load_file('Views/kview.kv')

class OrganizadorApp(App):
    #meu construtor de tela
    def build(self):
        return GUI
    
    #Função para abrir o diretorio
    def abrir_seletor_diretorio(self):
         # Usar o seletor nativo do S.O do usuário
        paths = filechooser.choose_dir(title='Selecione a Pasta desejada:') 
        
        if paths:
            diretorio = paths[0]
            self.root.ids.input_diretorio.text = diretorio
    
    #Função de selecionar repositorio
    def selecionar_diretorio(self, instance, selection):
        if selection:
            diretorio = selection[0]
            self.root.ids.input_diretorio.text = diretorio
            instance.parent.dismiss()

    def organizar_arquivos(self):
        diretorio = self.root.ids.input_diretorio.text
        if diretorio:
            resultado = organizarDir(diretorio)
            self.root.ids.label_status.text = resultado

            if resultado == msmFinal:
                popup = Popup(
                    title = 'Sucesso!',
                    title_size= '14sp',
                    content = Label(text=resultado)
                )
                popup.open()