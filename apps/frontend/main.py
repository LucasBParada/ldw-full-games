import flet as ft

from src.components.navbar import navbar

from src.views import (
    home_view,
    health_view,
    hosts_view,
    games_view,
    players_view
)


def main(page: ft.Page):

    page.title = "LDW Merge Skills"
    page.window_width = 1200
    page.window_height = 800
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO

    content = ft.Container(
        expand=True,
        padding=20
    )

    def change_view(index):

        if index == 0:
            content.content = home_view.build()

        elif index == 1:
            content.content = health_view.build()

        elif index == 2:
            content.content = hosts_view.build(page)

        elif index == 3:
            content.content = games_view.build(page)

        elif index == 4:
            content.content = players_view.build(page)

        page.update()

    rail = navbar(change_view)

    layout = ft.Container(
        expand=True,
        content=ft.Row(
            controls=[
                rail,
                ft.VerticalDivider(width=1),
                content
            ],
            expand=True
        )
    )

    page.add(layout)

    change_view(0)


if __name__ == "__main__":
    ft.run(main)