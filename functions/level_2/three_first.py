NOT_SET = "NOT_SET"


def first(items: list[int], default: int | None | str = NOT_SET) -> int | None | str:
    if items:
        return items[0]
    if default == NOT_SET:
        raise AttributeError
    return default
