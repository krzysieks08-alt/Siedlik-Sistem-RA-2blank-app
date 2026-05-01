import flet as ft
import random

def main(page: ft.Page):
    # Podstawowe ustawienia wyglądu pod telefon
    page.title = "SIEDLIK SYSTEM"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    def generate(e):
        atoms = ["MAKAN", "TIDUR", "KERJA", "BELI", "JALAN", "LIHAT"]
        osoby = ["SAYA", "KITA", "KAMI", "MEREKA"]
        res.value = f"{random.choice(osoby)} RAI {random.choice(atoms)}"
        page.update()

    # Interfejs użytkownika
    res = ft.Text(
        value="SYSTEM READY", 
        size=32, 
        color="cyan", 
        weight="bold",
        text_align=ft.TextAlign.CENTER
    )
    
    btn = ft.ElevatedButton(
        text="GENERUJ SYGNAŁ", 
        on_click=generate,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_700,
            padding=20
        )
    )

    # Dodanie elementów do strony
    page.add(
        ft.Column(
            [
                ft.Icon(ft.icons.CELL_TOWER, color="cyan", size=50),
                res,
                ft.Divider(height=20, color="transparent"),
                btn
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# TO JEST KLUCZOWE DLA ANDROIDA:
if __name__ == "__main__":
    ft.app(target=main)
