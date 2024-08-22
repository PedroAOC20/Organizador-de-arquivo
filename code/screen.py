from kivy.app import App
from kivy.lang import Builder
from plyer import filechooser
from organizador import organizarDir, msmFinal
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

GUI = Builder.load_file('Views/kview.kv')

class OrganizadorApp(App):
    def build(self):
        return GUI
    
    def abrir_seletor_diretorio(self):
        paths = filechooser.choose_dir(title='Selecione a Pasta desejada:')
        if paths:
            self.root.ids.input_diretorio.text = paths[0]
    
    def organizar_arquivos(self):
        diretorio = self.root.ids.input_diretorio.text
        if diretorio:
            try:
                resultado = organizarDir(diretorio)
                self.root.ids.label_status.text = resultado

                if resultado == msmFinal:
                    self.exibir_popup_sucesso(resultado)
            except Exception as e:
                self.root.ids.label_status.text = f"Erro: {e}"

    def exibir_popup_sucesso(self, mensagem):
        # Criar um layout que vai conter a mensagem e o botão
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=mensagem)
        
        # Criar o Popup
        popup = Popup(title='Sucesso!', content=layout, size_hint=(0.75, 0.5))
        
        # Criar o botão de "Retomar" e passar o popup como argumento
        retomar_btn = Button(
            text="Retomar", 
            size_hint_y=None, 
            height=50, 
            on_press=lambda *args: self.retomar(popup)
        )
        
        # Adicionar os widgets ao layout
        layout.add_widget(label)
        layout.add_widget(retomar_btn)
        
        popup.open()

    def retomar(self, popup):
        popup.dismiss()  # Fecha o popup
        self.root.ids.input_diretorio.text = ''  # Limpa o campo de diretório
        self.root.ids.label_status.text = 'Status:'  # Reseta o status