# Delivery Cost Estimation with Offers
# Only one coupon offer can be applied for any given package
# Packages should meet the required mentioned offer criterias.
# If offer code is not valid/found, discounted mount will be equal to zero.

class input_for_delivery_cost:
    def __init__(self):
        self.first_line = None

    def read_lines(self):
        self.first_line = input("Enter the base delivery cost and number of packages:")
        return self.first_line

    def input_line_parser(self):
        if self.first_line is None:
            raise ValueError("No Input found")
        try:
            base_fare, no_of_packages = self.first_line.split()
        except:
            raise ValueError("Invalid value")
        return base_fare, no_of_packages

    def check_offer_criteria(self, package):
        if package['offer_code'] == 'OFR001':
            if (package['base_distance'] < 200) & (70 < package['pkg_weight'] < 200):
                return True
        elif package['offer_code'] == 'OFR002':
            if (50 < package['base_distance'] < 150) & (100 < package['pkg_weight'] < 250):
                return True
        elif package['offer_code'] == 'OFR003':
            if (50 < package['base_distance'] < 250) & (10 < package['pkg_weight'] < 150):
                return True
        return False

    def get_delivery_cost_per_package(self):
        base_fare = self,input_for_delivery_cost()[0]
        num_packages = self.input_line_parser()[1]
        self.packages = []
        for i in range(1, int(num_packages) + 1):
            pkg_line = input(f"Enter package {i} details")
            line_splits = pkg_line.split()
            package = {}
            package['pkg_id'] = str(line_splits[0])
            package['pkg_weight'] = float(line_splits[1])
            package['base_distance'] = float(line_splits[2])
            package['offer_code'] = str(line_splits[3])
            self.packages.append(package)
        # return self.packages

        # delivery_cost = 0
        for package in self.packages:
            if(self.check_offer_criteria(package)):
                if package['offer_code'] == 'OFR001':
                    delivery_cost = 0.9*(base_fare + package['pkg_weight']*10 + package['base_distance']*5)
                elif package['offer_code'] == 'OFR002':
                    delivery_cost = 0.93*(base_fare + package['pkg_weight']*10 + package['base_distance']*5)
                elif package['offer_code'] == 'OFR003':
                    delivery_cost = 0.95*(base_fare + package['pkg_weight']*10 + package['base_distance']*5)
            delivery_cost = (base_fare + package['pkg_weight']*10 + package['base_distance']*5)
            print(f"Delivery cost of package {self.packages['pkg_id']}- {delivery_cost}")
        # return delivery_cost

inp = input_for_delivery_cost
# inp.get_delivery_cost_per_package()
print(inp.get_delivery_cost_per_package())

# def get_total_delivery_cost()