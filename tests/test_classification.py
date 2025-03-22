import unittest
from src.classification.classifier import classify_email

class TestEmailClassification(unittest.TestCase):
    def test_fund_transfer_classification(self):
        email_text = "I need to transfer $10,000 to account 987654321."
        result = classify_email(email_text)
        self.assertEqual(result['request_type'], "Money Movement")
        self.assertEqual(result['sub_request_type'], "Fund Transfer")

    def test_disputed_transaction_classification(self):
        email_text = "There is an incorrect charge of $500 on my credit card ending in 1234."
        result = classify_email(email_text)
        self.assertEqual(result['request_type'], "Adjustments & Reconciliation")
        self.assertEqual(result['sub_request_type'], "Disputed Transaction")

if __name__ == '__main__':
    unittest.main()
