"""This is main program."""

def add(a: int, b: int) -> int:
    """add a and b

    Args:
        a (int): number
        b (int): number

    Returns:
        int: a+b
    """
    return a + b


if __name__ == "__main__":
    x, y = 3, 5
    print(f"{x}+{y}={add(x, y)}")
