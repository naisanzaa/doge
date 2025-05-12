import unittest

from api.client import EcfrClient


class MyTestCase(unittest.TestCase):
    def test_something(self):
        client = EcfrClient()
        client.get_agencies()

        date = '2025-01-01'
        # titles = range(1, len(client.agencies))
        titles = range(1, 6)

        for title in titles:
            client.get_versioner_full(
                date=date,
                title=title,
            )
        pass


if __name__ == '__main__':
    unittest.main()
