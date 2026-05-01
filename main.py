import flet as ft

def main(page: ft.Page):
    # Ustawienia wizualne
    page.title = "SIEDLIK SYSTEM"
    page.theme_mode = ft.ThemeMode.DARK  # Zmieńmy na Dark, żeby wyglądało bardziej "pro"
    page.bgcolor = "#1A1A1A"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Funkcja przycisku
    def on_generate_click(e):
        btn.text = "SYGNAŁ WYSŁANY"
        btn.bgcolor = ft.colors.GREEN_600
        status_text.value = "STATUS: AKTYWNY"
        status_text.color = ft.colors.GREEN_400
        page.update()

    # Elementy interfejsu
    status_text = ft.Text("STATUS: OCZEKIWANIE", size=20, color=ft.colors.AMBER_400)
    
    btn = ft.ElevatedButton(
        text="GENERUJ SYGNAŁ",
        width=250,
        height=60,
        on_click=on_generate_click,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE_800,
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12),
        )
    )

    # Budowanie widoku
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.icons.CELL_TOWER_ROUNDED, size=100, color=ft.colors.BLUE_500),
                    ft.Text("SIEDLIK SYSTEM", size=32, weight="bold"),
                    ft.Divider(height=40, color="transparent"),
                    status_text,
                    ft.Divider(height=20, color="transparent"),
                    btn,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=40
        )
    )

# Start aplikacji
if __name__ == "__main__":
    ft.app(target=main)
