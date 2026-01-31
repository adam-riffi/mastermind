import random

colors = ("R", "G", "B", "Y", "W", "O")
code_length = 4



def generate_code(colors, code_length):
    code = ()
    if code_length <= 0:
        raise ValueError("code_length must be > 0")
    if not colors:
        raise ValueError("colors must be non-empty")
    return tuple(random.choice(colors) for _ in range(code_length))


def validate_code(code, colors, code_length):
    if len(code) != code_length:
        raise (f"expected length {code_length}, got {len(code)}")
    for c in code:
        if c not in colors:
            raise ValueError(f"invalid color {c}")
    return tuple(code)


if __name__ == "__main__":
    secret = generate_code(colors, code_length)
    print(secret)