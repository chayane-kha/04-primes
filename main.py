"""import de la fonction sqrt du module math"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Retourne True si p est premier sinon retourne False

    """
    # votre code ici
    if p == 1:
        return False
    for i in range(2,(int)(sqrt(p)+1)):
        if p%i == 0:
            return False
    return True

#### Fonction principale


def main():
    """
    Programme principal
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
