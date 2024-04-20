class Eye:
    """An eye.

    >>> Eye().draw()
    '•'
    >>> print(Eye(False).draw(), Eye(True).draw())
    • -
    """

    def __init__(self, closed=False):
        self.closed = closed

    def draw(self):
        if self.closed:
            return "-"
        else:
            return "•"


class Bear:
    """A bear.

    >>> Bear().print()
    ʕ •ᴥ•ʔ
    """

    def __init__(self):
        self.nose_and_mouth = "ᴥ"

    def next_eye(self):
        return Eye()

    def print(self):
        left, right = self.next_eye(), self.next_eye()
        print("ʕ " + left.draw() + self.nose_and_mouth + right.draw() + "ʔ")


class SleepyBear(Bear):
    """A bear with closed eyes.

    >>> SleepyBear().print()
    ʕ -ᴥ-ʔ
    """

    "*** YOUR CODE HERE ***"

    def next_eye(self):
        return Eye(True)


class WinkingBear(Bear):
    """A bear whose left eye is different from its right eye.

    >>> WinkingBear().print()
    ʕ -ᴥ•ʔ
    """

    def __init__(self):
        "*** YOUR CODE HERE ***"
        self.nose_and_mouth = "ᴥ"
        self.next_eye_times = 0

    def next_eye(self):
        "*** YOUR CODE HERE ***"
        self.next_eye_times += 1
        return Eye(True) if self.next_eye_times % 2 == 1 else Eye(False)
