import unittest

import orders
import logging


class TestOrderRepository(unittest.TestCase):

    def setUp(self):
        self.reset()
        """
        we're going to reset the database and
        ensure there's nothing in it.
        """
        self.repo = orders.OrderRepository()
        count = self.reset()
        logging.info('deleted', count, 'rows')
        self.assertEqual(self.repo.count(), 0)

    def test_insert(self):
        self.assertEqual(0, self.repo.count())
        order = self.repo.insert(name='Kimly')
        self.assertIsNotNone(order.id)
        self.assertEqual(order.name, 'Kimly')
        self.assertEqual(1, self.repo.count())

    def reset(self):
        return self.repo.delete_all()

    def test_all(self):
        self.reset()
        self.repo.insert(name='Tammie')
        self.repo.insert(name='Kimly')
        self.assertEqual(self.repo.count(), 2)


if __name__ == '__main__':
    unittest.main()
