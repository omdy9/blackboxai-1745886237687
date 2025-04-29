from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from database import get_user_by_username

class LoginScreen(Screen):
    def login(self, username, password):
        if username == "admin" and password == "admin":
            self.manager.current = "admin_dashboard"
            return

        user = get_user_by_username(username)
        if user and user.get("password") == password:
            role = user.get("role")
            if role == "Student":
                self.manager.current = "student_dashboard"
            elif role == "Professor":
                self.manager.current = "professor_dashboard"
            else:
                self.show_error_dialog("Unknown user role.")
        else:
            self.show_error_dialog("Invalid username or password.")

    def show_error_dialog(self, message):
        if not hasattr(self, 'dialog'):
            self.dialog = MDDialog(
                text=message,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=lambda x: self.dialog.dismiss()
                    )
                ],
            )
        else:
            self.dialog.text = message
        self.dialog.open()
