from offer import Offer

class Package:
    """
    Represents a delivery package with cost and discount calculations.
    """
    def __init__(self, pkg_id, weight, distance, offer_code, base_cost):
        """
        Initialize the Package with details and calculate cost, discount, and total cost.
        :param pkg_id: Package ID (string)
        :param weight: Weight of the package (float)
        :param distance: Delivery distance (float)
        :param offer_code: Offer code (string)
        :param base_cost: Base delivery cost (float)
        """
        self.pkg_id = pkg_id
        self.weight = weight
        self.distance = distance
        self.offer_code = offer_code

        self.cost = base_cost + weight * 10 + distance * 5
        self.discount = Offer(offer_code).get_discount(weight, distance, self.cost)
        self.total_cost = int(self.cost - self.discount)
        self.delivery_time = 0.0
