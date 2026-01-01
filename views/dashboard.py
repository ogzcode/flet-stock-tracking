import flet as ft

def dashboard_view(page: ft.Page):
    return ft.View(
        route="/dashboard",
        controls=[
            ft.Column(
                [
                    ft.Text("Welcome to the Dashboard!", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text("This is your main dashboard view.", size=20),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        ],
    )