import unittest
# from game import FriendlyPokemon
from game import FriendlyPokemon

class UnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.friendly_pokemon = FriendlyPokemon("ditto")

    def test_health(self):
        actual = self.friendly_pokemon.health
        expected = 101
        self.assertEqual(
            actual, expected,
            "Expected health to be 101"
        )

if __name__ == "__main__":
    unittest.main()