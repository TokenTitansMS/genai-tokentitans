class LoanMatcher:
    """
    A class to match borrowers with lenders based on predefined criteria.
    """

    def __init__(self, borrowers, lenders):
        """
        Initializes the LoanMatcher with borrowers and lenders.

        :param borrowers: List of borrower dictionaries with 'id', 'amount', and 'max_interest_rate'.
        :param lenders: List of lender dictionaries with 'id', 'amount', 'interest_rate', and 'status'.
        """
        self.borrowers = borrowers
        self.lenders = lenders
        self.matches = []

    def match(self):
        """
        Matches borrowers with lenders based on predefined criteria.

        :return: List of matches as dictionaries with 'borrower_id' and 'lender_id'.
        """
        for borrower in self.borrowers:
            for lender in self.lenders:
                if (
                    lender['amount'] >= borrower['amount'] and
                    lender['interest_rate'] <= borrower['max_interest_rate'] and
                    lender['status'] == 'available'
                ):
                    self.matches.append({'borrower_id': borrower['id'], 'lender_id': lender['id']})
                    lender['status'] = 'matched'  # Update lender status to prevent multiple matches
                    break  # Move to the next borrower once a match is found
        return self.matches

    def get_matches(self):
        """
        Returns the list of matches.

        :return: List of matches as dictionaries with 'borrower_id' and 'lender_id'.
        """
        return self.matches

