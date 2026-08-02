import os


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    term_width = os.get_terminal_size().columns

    bar_width = term_width - 40
    if bar_width < 10:
        bar_width = 10

    for i, elem in enumerate(lst, start=1):
        percent = i * 100 / total
        filled = int(bar_width * i / total)

        if filled == 0:
            bar = " " * bar_width
        elif filled == bar_width:
            bar = "=" * bar_width
        else:
            bar = "=" * (filled - 1) + ">" + " " * (bar_width - filled)

        print(
            f"\r{percent:3.0f}%|{bar}| {i}/{total} [00:00<00:00, ?it/s]",
            end="",
            flush=True,
        )

        yield elem

    print()   

def main():
    """This is the main function"""
    try:
        for i in ft_tqdm(range(333)):
            continue
    except AssertionError as error:
        print("Assertion error:", error)

if __name__ == "__main__":
    main()