import flet as ft
import random

def main(page: ft.Page):
    page.title = "SIEDLIK SYSTEM"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def generate(e):
        atoms = ["MAKAN", "TIDUR", "KERJA", "BELI", "JALAN", "LIHAT"]
        osoby = ["SAYA", "KITA", "KAMI", "MEREKA"]
        wynik = f"{random.choice(osoby)} RAI {random.choice(atoms)}"
        res.value = wynik
        page.update()

    res = ft.Text("SYSTEM READY", size=30, color="cyan", weight="bold")
    btn = ft.ElevatedButton("GENERUJ SYGNAŁ", on_click=generate, height=50)

    page.add(
        ft.Center(
            ft.Column([res, btn], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
