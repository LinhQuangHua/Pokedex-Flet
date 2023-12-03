import flet as ft
from flet import (
    Checkbox,
    Column,
    FloatingActionButton,
    IconButton,
    Page,
    Row,
    Tab,
    Tabs,
    TextField,
    UserControl,
    colors,
    icons,
)


def main(page: ft.Page):

    page.title = "Pokedex App"
    page.bgcolor = "white"

    txt_name = ft.Text("Hello Pokemon", text_align="center", color="red")

    page.add(txt_name)

ft.app(target=main)