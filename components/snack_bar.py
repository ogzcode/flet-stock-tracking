import flet as ft


class CSnackBar(ft.SnackBar):
    @staticmethod
    def show(page: ft.Page, message: str, severity: str = "info"):
        config = {
            "info": {"bgcolor": ft.Colors.BLUE, "icon": ft.Icons.INFO},
            "success": {"bgcolor": ft.Colors.GREEN, "icon": ft.Icons.CHECK_CIRCLE},
            "warning": {"bgcolor": ft.Colors.ORANGE, "icon": ft.Icons.WARNING},
            "error": {"bgcolor": ft.Colors.RED, "icon": ft.Icons.ERROR},
        }

        selected = config.get(severity, config["info"])

        snack_bar = ft.SnackBar(
            content=ft.Row(
                [
                    ft.Icon(selected["icon"], color=ft.Colors.WHITE),
                    ft.Text(message, color=ft.Colors.WHITE),
                ],
                tight=True,
            ),
            bgcolor=selected["bgcolor"],
            duration=4000,
            show_close_icon=True,
            close_icon_color=ft.Colors.WHITE,
            behavior=ft.SnackBarBehavior.FLOATING,
            margin=ft.Margin.all(10),
        )

        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()