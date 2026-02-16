import unittest
from typing import List

# Constante définissant le seuil minimal de lettres
MINIMUM_LETTERS_THRESHOLD: int = 7

def count_names_longer_than_threshold(first_names: List[str]) -> int:
    """
    Compte le nombre de prénoms dont la longueur
    est strictement supérieure au seuil défini.
    """

    count: int = 0

    for first_name in first_names:

        # Vérifie si le prénom dépasse le seuil
        if len(first_name) > MINIMUM_LETTERS_THRESHOLD:
            count += 1

    return count


class TestCountNamesLongerThanThreshold(unittest.TestCase):

    def test_should_count_names_with_more_than_seven_letters(self) -> None:   
        """
        Vérifie que la fonction retourne bien
        le nombre attendu de prénoms > 7 lettres.
        """

        first_names: List[str] = [
            "Guillaume",
            "Gilles",
            "Juliette",
            "Antoine",
            "François",
            "Cassandre"
        ]

        result: int = count_names_longer_than_threshold(first_names)

        # Vérification du résultat attendu
        self.assertEqual(result, 4)         #4 car Guillaume ; Juliette ; François ; Cassandre

if __name__ == '__main__':
    unittest.main()
