import flet as ft

from src.api import ApiClient


def build():

    health = ApiClient.get_health()

    return ft.Column(
        controls=[
            ft.Text(
                "Health Check",
                size=24
            ),
            ft.Text(
                f"Status: {health.get('status')}"
            ),
            ft.Text(
                f"Database: {health.get('database')}"
            )
        ]
    )