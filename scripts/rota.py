import random
import datetime
import itertools
import tabulate


def pop_random(items: list[str]) -> tuple[str, list[str]]:
    item = items.pop(random.randrange(len(items)))
    return (item, items)

def create_ordering(members: list[str]):
    m = members.copy()
    order = []

    while len(m) > 0:
        p, m = pop_random(m)
        order.append(p)

    return itertools.cycle(order)

def assemble_rota(members: list[str], starting: datetime.date, weeks_ahead: int) -> dict[datetime.date, str]:
    ordering = create_ordering(members)

    rota = []
    date = starting

    for week in range(weeks_ahead):
        rota.append((date, next(ordering)))
        date += datetime.timedelta(days=7)

    return rota

def format_rota(rota: dict[datetime.date, str]) -> str:
    data = []
    for (date, person) in rota:
        data.append([date.isoformat(), person])
    return tabulate.tabulate(data, headers=["Date", "Presenter"], tablefmt="github")

if __name__ == "__main__":
    members = [
        "Tom",
        "Teresa",
        "Matt",
        "Rhys",
        "Jiachen",
        "Gloria",
        "Belinda",
        "Anantanarayanan",
        "Fergus",
        "Andy",
    ]
    # needed a random seed so that either andy, tom or fergus was the first to
    # present
    random.seed(42 + 11)
    rota = assemble_rota(members, datetime.date(2024, 9, 17), 10)

    print(format_rota(rota))


