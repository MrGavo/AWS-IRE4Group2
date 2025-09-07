#! /usr/bin/python

'''
    To use this you've got to:
                    pip install textual
    It is just an idea for a user interface for our Coffee Stain app.
    To end the app - Ctrl-q
'''

from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, ContentSwitcher, DataTable, Markdown

MARKDOWN_EXAMPLE = """# Our Range of Cakes

Our cakes are all made in **the Coffee Stain** by our bakers under the strictest
hygiene standards.

## Apple Pie

| Flavour | Known Allergens | Price |
| -- | -- | -- |
| Apple | Apple | 12.99 |

## Cinnamon Roll

| Flavour | Known Allergens | Price |
| -- | -- | -- |
| Cinnamon | Milk | 3.99 |

## Chocolate Cake

| Flavour | Known Allergens | Price |
| -- | -- | -- |
| Chocolate | Milk, Nuts | 15.49 |

## Lemon Slice

| Flavour | Known Allergens | Price |
| -- | -- | -- |
| Lemon | Milk | 4.99 |

## Raspberry Muffin

| Flavour | Known Allergens | Price |
| -- | -- | -- |
| Raspberry | Nuts | 4.99 |
"""


class ContentSwitcherApp(App[None]):
    CSS_PATH = "content_switcher.tcss"

    def compose(self) -> ComposeResult:
        with Horizontal(id="buttons"):  
            yield Button("DataTable", id="data-table")  
            yield Button("Markdown", id="markdown")  

        with ContentSwitcher(initial="data-table"):  
            yield DataTable(id="data-table")
            with VerticalScroll(id="markdown"):
                yield Markdown(MARKDOWN_EXAMPLE)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one(ContentSwitcher).current = event.button.id  

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("Drink", "Price")
        table.add_rows(
            [
                (drink.ljust(35), price)
                for drink, price in (
                    ("Americano", 11.99),
                    ("Cappucino", 14.99),
                    ("Espresso", 12.99),
                    ("Latte", 12.99),
                    ("Perrier", 8.99),
                    ("Breakfast Tea", 12.99),
                )
            ]
        )


if __name__ == "__main__":
    ContentSwitcherApp().run()
