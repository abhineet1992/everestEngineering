class Package:
    def __init__(self, pkg_id, weight, distance, offer_code, base_cost):
        self.pkg_id = pkg_id
        self.weight = weight
        self.distance = distance
        self.offer_code = offer_code

        self.cost = base_cost + weight * 10 + distance * 5
        self.discount = get_discount(weight, distance, self.cost, offer_code)
        self.total_cost = int(self.cost - self.discount)

        self.delivery_time = 0.0
