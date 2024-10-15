import flet

def main(page: flet.Page):

    number_text = flet.Text("0")

    def minus_click(e):
        prev_value = int(number_text.value)
        new_value = prev_value - 1
        number_text.value = str(new_value)
        number_text.update()

    def plus_click(e):
        prev_value = int(number_text.value)
        new_value = prev_value + 1
        number_text.value = str(new_value)
        number_text.update()

    row = flet.Row(
        controls=[
            flet.TextButton("-", on_click=minus_click),
            number_text,
            flet.TextButton("+", on_click=plus_click)
        ]
    )
    page.add(row)


flet.app(main)