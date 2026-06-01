import flet as ft

from src.api import ApiClient
from src.components.info_card import info_card


def build(page: ft.Page):

    hosts_column = ft.Column()

    name_field = ft.TextField(label="Nome da Empresa")
    country_field = ft.TextField(label="País")

    def load_hosts():

        hosts_column.controls.clear()

        for host in ApiClient.get_hosts():

            hosts_column.controls.append(
                info_card(
                    host["name"],
                    f"País: {host['country']}"
                )
            )

        page.update()

    def create_host(e):

        ApiClient.create_host({
            "name": name_field.value,
            "country": country_field.value
        })

        name_field.value = ""
        country_field.value = ""

        load_hosts()

    load_hosts()

    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Text("Hosts", size=30, weight=ft.FontWeight.BOLD),

            ft.Card(
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        name_field,
                        country_field,
                        ft.ElevatedButton(
                            "Cadastrar Host",
                            on_click=create_host
                        )
                    ])
                )
            ),

            hosts_column
        ]
    )