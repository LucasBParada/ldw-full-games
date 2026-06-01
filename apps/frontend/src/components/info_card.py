import flet as ft


def info_card(title, subtitle):

    return ft.Card(
        elevation=5,
        content=ft.Container(
            padding=20,
            border_radius=10,
            content=ft.Column(
                [
                    ft.Text(
                        title,
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Text(subtitle)
                ]
            )
        )
    )