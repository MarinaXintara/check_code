import random
import string

def δημιούργησε_κωδικό(μήκος):
    χαρακτήρες = string.ascii_letters + string.digits + string.punctuation
    κωδικός = ''.join(random.choice(χαρακτήρες) for _ in range(μήκος))
    return κωδικός

μήκος = int(input("Μήκος κωδικού; "))
print("Ισχυρός κωδικός:", δημιούργησε_κωδικό(μήκος))
