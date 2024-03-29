def cascade(n):
    """_summary_

    Args:
        n (_type_): _description_
    >>> cascade(2024)
    2024
    202
    20
    2
    20
    202
    2024
    """
    print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)


cascade(2024)
