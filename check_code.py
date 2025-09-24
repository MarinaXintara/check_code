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

    if not has_digit and not has_upper and not has_special:
       print("Ο κωδικός δεν είναι ισχυρός, γιατί δεν περιλαμβάνει τίποτα από τα απαραίτητα.")
    elif not has_digit and not has_upper:
       print("Ο κωδικός δεν είναι ισχυρός, γιατί δεν περιλαμβάνει ψηφία και κεφαλαία γράμματα.")
    elif not has_digit and not has_special:
       print("Ο κωδικός δεν είναι ισχυρός, γιατί δεν περιλαμβάνει ψηφία και σύμβολα.")
    elif not has_upper and not has_special:
       print("Ο κωδικός δεν είναι ισχυρός, γιατί δεν περιλαμβάνει κεφαλαία γράμματα και σύμβολα.")
    elif not has_digit:
       print("Ο κωδικός δεν είναι ισχυρός, γιατί δεν περιλαμβάνει ψηφία.")
    elif not has_upper:
       print("Ο κωδικός δεν είναι ισχυρός, γιατί δεν περιλαμβάνει κεφαλαία γράμματα.")
    elif not has_special:
       print("Ο κωδικός δεν είναι ισχυρός, γιατί δεν περιλαμβάνει σύμβολα.")
    else:
       print("Ο κωδικός είναι ισχυρός")



check(code)
