from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from plyer import filechooser
from organizador import organizarDir, msmFinal

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
        layout = BoxLayout(
            orientation='vertical',
            padding=10, 
            spacing=10
        )
        
        label = Label(text=mensagem)
        popup = Popup(
            title='Sucesso!', 
            title_size='14sp', 
            content=layout, 
            size_hint=(0.75, 0.5)
        )
        
        retomar_btn = Button(
            text="Retomar", 
            size_hint_y=None, 
            height=50, 
            on_press=popup.dismiss
        )
        
        layout.add_widget(label)
        layout.add_widget(retomar_btn)
        
        popup.open()
