import flet as ft
import flet.fastapi as flet_fastapi

def main(page: ft.Page):
    page.title = "SIEDLIK SYSTEM"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Icon(ft.icons.CELL_TOWER, size=100, color="blue"),
        ft.Text("SIEDLIK SYSTEM", size=30, weight="bold"),
        ft.ElevatedButton("GENERUJ SYGNAŁ", on_click=lambda _: print("OK"))
    )

# To jest klucz pod Vercela:
app = flet_fastapi.app(main)
