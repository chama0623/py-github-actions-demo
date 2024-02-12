def add(a:int, b:int)->int:
    """足し算を実行する

    Args:
        a (int): 整数
        b (int): 整数

    Returns:
        int: a+b
    """
    return a+b

if __name__ == "__main__":
    a, b = 3, 5
    print(f"{a}+{b}={add(a, b)}")