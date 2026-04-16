import unittest


# 1. The function we want to test (usually imported from another file)
def calculate_discount(price, discount):
    if discount < 0 or discount > 1:
        raise ValueError("Discount must be between 0.0 and 1.0")
    return price - (price * discount)


# 2. The Test Class
# We inherit from unittest.TestCase to turn this class into a testing engine.
class TestBillingEngine(unittest.TestCase):
    # 3. The Test Methods
    # Method names MUST start with the word 'test_' to be detected by the engine.
    def test_standard_discount(self):
        # assertEqual checks if Output A matches Expected Output B
        result = calculate_discount(100, 0.20)
        self.assertEqual(result, 80.0)

    def test_zero_discount(self):
        result = calculate_discount(50, 0.0)
        self.assertEqual(result, 50.0)

    def test_invalid_discount_raises_error(self):
        # assertRaises checks if the function successfully CRASHES when given bad data
        with self.assertRaises(ValueError):
            calculate_discount(100, 1.5)


# if __name__ == "__main__":
#     unittest.main()
# unittest.main(): It terminates the program when it finishes. Under the hood, unittest.main() executes all the tests it has found so far, and then calls sys.exit() to shut down the server so it can return a pass/fail status code to the CI/CD pipeline.

# ========Another Example
import logging
import unittest

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(levelname)s: %(message)s",
    force=True,
)

logging.error("error check")


def get_user(db, user_id):
    try:
        return db[user_id]
    except KeyError:
        logging.error("User missing!")
        raise


class TestDatabase(unittest.TestCase):

    def test_missing_user(self):
        mock_db = {1: "Admin"}
        with self.assertRaises(KeyError):
            get_user(mock_db, 99)


if __name__ == "__main__":
    unittest.main()
