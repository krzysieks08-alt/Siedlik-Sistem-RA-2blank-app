import flet as ft

def main(page: ft.Page):
    page.title = "SIEDLIK SYSTEM"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0A0A0A"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_click(e):
        btn.text = "SYGNAŁ WYSŁANY"
        btn.bgcolor = ft.colors.GREEN_700
        page.update()

    icon = ft.Icon(ft.icons.WIFI_TETHERING_ROUNDED, size=100, color=ft.colors.BLUE_600)
    status = ft.Text("SYSTEM GOTOWY", size=18, color=ft.colors.GREY_500)
    
    btn = ft.ElevatedButton(
        text="GENERUJ SYGNAŁ",
        width=250,
        height=60,
        on_click=handle_click
    )

    page.add(
        icon,
        ft.Text("SIEDLIK SYSTEM", size=28, weight="bold"),
        status,
        ft.Divider(height=20, color="transparent"),
        btn
    )

# TO JEST NAJWAŻNIEJSZA LINIA DLA VERCELA:
app = ft.app(target=main, view=ft.AppView.WEB_BROWSER)
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
