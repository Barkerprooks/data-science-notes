from unittest import TestCase, main
from hw_help import letter_count

class TestHw1(TestCase):
    
    def test_abba(self):
        self.assertEqual(
            letter_count("abba"),
            {
                "a": 2, 
                "b": 2
            }
        )
    
    def test_statistically(self):
        self.assertEqual(
            letter_count("statistically"),
            {
                "s": 2,
                "t": 3,
                "a": 2,
                "i": 2,
                "c": 1,
                "l": 2,
                "y": 1
            }
        )

if __name__ == "__main__":
    main()