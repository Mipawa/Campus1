from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.boxlayout import MDBoxLayout
import plyer
from kivy.lang import Builder

kv='''
MDBoxLayout:
    Button:
        text:'Click me'
        on_release:
            app.show_notification()
            t1.text='Clicked, notified'
    MDLabel:
        text:'Not clicked, no notification'
        id:t1

'''

class PushNotificationApp(MDApp):
    def build(self):
        return Builder.load_string(kv)
    def show_notification(self):
        plyer.notification.notify(title='test', message="Notification using plyer")

app = PushNotificationApp()
app.run()


