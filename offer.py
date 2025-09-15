class Offer:
    """
    Represents an offer code and provides discount calculation based on package details.
    """
    def __init__(self, code):
        """
        Initialize the Offer with a specific code.
        :param code: Offer code string (e.g., 'OFR001')
        """
        self.code = code

    def get_discount(self, weight, distance, base_cost):
        """
        Calculate the discount for a package based on offer code, weight, and distance.
        :param weight: Weight of the package
        :param distance: Delivery distance
        :param base_cost: Calculated base cost for the package
        :return: Discount amount (float)
        """
        if self.code == "OFR001" and 70 <= distance <= 200 and 0 < weight <= 200:
            return 0.1 * base_cost
        elif self.code == "OFR002" and 50 <= distance <= 150 and 100 < weight <= 250:
            return 0.07 * base_cost
        elif self.code == "OFR003" and 50 <= distance <= 250 and 10 < weight <= 150:
            return 0.05 * base_cost
        return 0