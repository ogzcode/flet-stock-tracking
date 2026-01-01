import flet as ft
from components import CSnackBar


def login_view(page: ft.Page):
    user_name = ft.TextField(label="Username", width=300, hint_text="Enter your username")
    password = ft.TextField(
        label="Password",
        width=300,
        password=True,
        can_reveal_password=True,
        hint_text="Enter your password",
    )

    def login_click(e: ft.Event[ft.Button]):
        print("Login button clicked")
        if user_name.value == "admin" and password.value == "admin123":
            page.go("/dashboard")
        else:
            CSnackBar.show(page, "Invalid username or password", severity="success")
        page.update()

    login_button = ft.Button(
        content="Login",
        on_click=login_click,
        style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
    )

    return ft.View(
        route="/login",
        controls=[
            ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER,
                content=ft.Column(
                    [
                        ft.Icon(ft.Icons.LOCK, size=80, color=ft.Colors.BLUE),
                        ft.Text("Login", size=30, weight=ft.FontWeight.BOLD),
                        user_name,
                        password,
                        login_button,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
            )
        ],
    )
