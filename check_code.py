code = input("Δώσε κωδικό:")

def check(code):
    if len(code) < 8:
        print("Ο κωδικός είναι πολύ μικρός.")
        return

    has_digit = False
    has_upper = False
    has_special = False
    special_chars = "!@#%?&^~"

    for char in code:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char in special_chars:
            has_special = True

    if has_digit and has_upper and has_special:
        print("Ο κωδικός είναι ισχυρός.")
    else:
        print("Ο κωδικός δεν είναι ισχυρός.")

check(code)
