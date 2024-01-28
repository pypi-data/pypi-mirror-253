import extraexceptions as ee


@ee.ignore_exc_decorator
def div(a, b):
    return a / b


if __name__ == "__main__":
    print(div(5, 0))
    print(div(4, 2))
