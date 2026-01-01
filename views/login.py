import flet as ft


def login_view(page: ft.Page):
    return ft.View(
        route="/login",
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.LOCK, size=80, color=ft.Colors.BLUE),
                    ft.Text("Login", size=30, weight=ft.FontWeight.BOLD),
                    ft.TextField(
                        label="Username", width=300, hint_text="Enter your username"
                    ),
                    ft.TextField(
                        label="Password",
                        width=300,
                        password=True,
                        can_reveal_password=True,
                        hint_text="Enter your password",
                    ),
                    ft.Button(
                        content="Login",
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        ],
    )
