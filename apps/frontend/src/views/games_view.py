import flet as ft
from src.api import ApiClient
from src.components.info_card import info_card


def build(page: ft.Page):

    games_column = ft.Column()

    name_field = ft.TextField(label="Nome do Game")
    host_id_field = ft.TextField(label="Host ID")
    genre_field = ft.TextField(label="Gênero (FPS, RPG, etc)")

    def load_games():

        games_column.controls.clear()

        try:
            games = ApiClient.get_games()

            for game in games:
                games_column.controls.append(
                    info_card(
                        game.get("name", "Sem nome"),
                        f"Host ID: {game.get('host_id')} | Gênero: {game.get('genre')}"
                    )
                )

        except Exception as e:
            games_column.controls.append(
                ft.Text(f"Erro ao carregar games: {e}", color="red")
            )

        page.update()

    def create_game(e):

        if not name_field.value or not host_id_field.value or not genre_field.value:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos"))
            page.snack_bar.open = True
            page.update()
            return

        try:
            ApiClient.create_game({
                "name": name_field.value,
                "host_id": int(host_id_field.value),
                "genre": genre_field.value
            })

            name_field.value = ""
            host_id_field.value = ""
            genre_field.value = ""

            load_games()

        except Exception as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {ex}"))
            page.snack_bar.open = True
            page.update()

    load_games()

    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        controls=[

            ft.Text(
                "Games",
                size=30,
                weight=ft.FontWeight.BOLD
            ),

            ft.Card(
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        name_field,
                        host_id_field,
                        genre_field,

                        ft.ElevatedButton(
                            "Cadastrar Game",
                            on_click=create_game
                        )
                    ])
                )
            ),

            ft.Divider(),

            games_column
        ]
    )