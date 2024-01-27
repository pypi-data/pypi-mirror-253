from time import sleep

from rich.columns import Columns
from rich.live import Live
from rich.panel import Panel
from rich.spinner import SPINNERS, Spinner
from rich.text import Text

all_spinners = Columns(
    [Spinner(spinner_name, text=Text(repr(spinner_name), style="green")) for spinner_name in sorted(SPINNERS)],
    column_first=True,
    expand=True,
)

# with Live(
#     Panel(all_spinners, title="Spinners", border_style="blue"),
#     refresh_per_second=20,
# ) as live:
#     while True:
#         sleep(0.1)

spinner = Spinner('dots3', text=Text('Testing upload'))
with Live(spinner):
    for _ in range(10):
        # spinner.update()
        sleep(0.5)
