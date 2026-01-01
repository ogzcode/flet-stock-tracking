import flet as ft

from views import login_view, dashboard_view


def main(page: ft.Page):
    page.title = "Flet Stock Tracking App"
    page.window.width = 600
    page.window.height = 400

    def route_change(route):
        views_map = {
            "/login": login_view,
            "/dashboard": dashboard_view,
        }

        page.views.clear()

        if page.route in views_map:
            page.views.append(views_map[page.route](page))
        else:
            page.views.append(login_view(page))

        page.update()

    def view_pop(view):
        page.views.pop()
        page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/login")

if __name__ == "__main__":
    ft.run(main)
