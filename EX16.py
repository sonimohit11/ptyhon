from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):
    def build(self):
        self.count = 0

        # Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Label to show count
        self.label = Label(text="0", font_size=50)
        layout.add_widget(self.label)

        # Button to increment
        btn = Button(text="Increment", font_size=30)
        btn.bind(on_press=self.increment_counter)
        layout.add_widget(btn)

        return layout

    def increment_counter(self, instance):
        self.count += 1
        self.label.text = str(self.count)

# Run the app
if __name__ == '__main__':
    CounterApp().run()