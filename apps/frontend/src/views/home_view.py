import flet as ft


def build():

    return ft.Column(
        controls=[
            ft.Text(
                "LDW Merge Skills",
                size=32,
                weight=ft.FontWeight.BOLD
            ),
            ft.Text(
                "Frontend Flet consumindo API Flask"
            )
        ]
    )