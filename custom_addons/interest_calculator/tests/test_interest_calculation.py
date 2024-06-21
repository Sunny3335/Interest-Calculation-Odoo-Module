from odoo.tests.common import TransactionCase


class TestInterestCalculation(TransactionCase):

    def test_simple_interest(self):
        record = self.env["interest.calculation"].create(
            {
                "principal_amount": 1000,
                "interest_rate": 5,
                "time_period": 2,
                "interest_type": "simple",
            }
        )
        self.assertEqual(record.simple_interest, 100.0)

    def test_compound_interest(self):
        record = self.env["interest.calculation"].create(
            {
                "principal_amount": 1000,
                "interest_rate": 5,
                "time_period": 2,
                "interest_type": "compound",
            }
        )
        self.assertAlmostEqual(record.compound_interest, 102.5, places=2)
