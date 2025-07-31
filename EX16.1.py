from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        # Layout
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Text input field
        self.text_input = TextInput(hint_text="Type something here", multiline=False, font_size=20)
        self.layout.add_widget(self.text_input)

        # Button to show the text
        submit_button = Button(text="Show Text", font_size=24)
        submit_button.bind(on_press=self.show_text)
        self.layout.add_widget(submit_button)

        # Label to display the text
        self.output_label = Label(text="", font_size=24)
        self.layout.add_widget(self.output_label)

        return self.layout

    def show_text(self, instance):
        # Get text and show in label
        typed_text = self.text_input.text
        self.output_label.text = f"You typed: {typed_text}"

# Run the app
if __name__ == '__main__':
    TextInputApp().run()
