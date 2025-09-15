# Delivery Cost Estimation with Offers
# Only one coupon offer can be applied for any given package
# Packages should meet the required mentioned offer criterias.
# If offer code is not valid/found, discounted mount will be equal to zero.

class Package:
    """
    Represents a single delivery package and handles cost and discount calculation.
    """
    def __init__(self, pkg_id, weight, distance, offer_code, base_fare):
        self.pkg_id = pkg_id
        self.weight = weight
        self.distance = distance
        self.offer_code = offer_code
        self.base_fare = base_fare
        self.discount = 0.0
        self.total_cost = 0.0

    def is_offer_applicable(self):
        """
        Checks if the offer code is valid for this package.
        """
        if self.offer_code == 'OFR001':
            return 70 < self.weight <= 200 and 0 < self.distance <= 200
        elif self.offer_code == 'OFR002':
            return 100 < self.weight <= 250 and 50 < self.distance <= 150
        elif self.offer_code == 'OFR003':
            return 10 < self.weight <= 150 and 50 < self.distance <= 250
        return False

    def calculate_cost(self):
        """
        Calculates the delivery cost and discount for the package.
        """
        base_cost = self.base_fare + self.weight * 10 + self.distance * 5
        if self.is_offer_applicable():
            if self.offer_code == 'OFR001':
                self.discount = 0.1 * base_cost
            elif self.offer_code == 'OFR002':
                self.discount = 0.07 * base_cost
            elif self.offer_code == 'OFR003':
                self.discount = 0.05 * base_cost
        self.total_cost = base_cost - self.discount

    def __str__(self):
        return f"{self.pkg_id} {int(self.discount)} {int(self.total_cost)}"


class DeliverySession:
    """
    Handles input, parsing, and delivery cost calculation for multiple packages.
    """
    def __init__(self):
        self.base_fare = 0
        self.num_packages = 0
        self.packages = []

    def read_input(self):
        """
        Reads and parses the base fare and number of packages.
        """
        first_line = input("Enter the base delivery cost and number of packages: ")
        try:
            base_fare, num_packages = first_line.split()
            self.base_fare = float(base_fare)
            self.num_packages = int(num_packages)
        except Exception:
            raise ValueError("Invalid input for base fare and number of packages.")

    def read_packages(self):
        """
        Reads and parses package details from user input.
        """
        for i in range(1, self.num_packages + 1):
            pkg_line = input(f"Enter package {i} details: ")
            try:
                pkg_id, weight, distance, offer_code = pkg_line.split()
                package = Package(
                    pkg_id=pkg_id,
                    weight=float(weight),
                    distance=float(distance),
                    offer_code=offer_code,
                    base_fare=self.base_fare
                )
                self.packages.append(package)
            except Exception:
                raise ValueError(f"Invalid input for package {i}.")

    def process_packages(self):
        """
        Calculates cost and discount for all packages.
        """
        for package in self.packages:
            package.calculate_cost()

    def print_results(self):
        """
        Prints the delivery cost and discount for each package.
        """
        for package in self.packages:
            print(package)

    def run(self):
        """
        Runs the full delivery session: input, calculation, and output.
        """
        self.read_input()
        self.read_packages()
        self.process_packages()
        self.print_results()


if __name__ == "__main__":
    session = DeliverySession()
    session.run()
