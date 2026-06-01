import flet as ft


def navbar(change_view):

    return ft.Container(
        width=250,
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text(
                    "LDW Merge Skills",
                    size=24,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Divider(),

                ft.ElevatedButton(
                    "🏠 Home",
                    width=200,
                    on_click=lambda _: change_view(0)
                ),

                ft.ElevatedButton(
                    "❤️ Health",
                    width=200,
                    on_click=lambda _: change_view(1)
                ),

                ft.ElevatedButton(
                    "🖥️ Hosts",
                    width=200,
                    on_click=lambda _: change_view(2)
                ),

                ft.ElevatedButton(
                    "🎮 Games",
                    width=200,
                    on_click=lambda _: change_view(3)
                ),

                ft.ElevatedButton(
                    "👤 Players",
                    width=200,
                    on_click=lambda _: change_view(4)
                ),
            ]
        )
    )