# Delivery time estimation
# each vehicle has  a limit (L) on max weight
# All vehicles run at same speed and in same route
# Delivery time estimation
# Delivery Criteria - Shipment should contain max packages vehicle can carry in a trip
# Prefer heavier packages when there are multiple shipments with the same no. of packages
# If the weights are same, preferences should be given to shipments which can be delivered first

import math
from collections import deque

# ---- Offer Codes Logic ----
def get_discount(weight, distance, base_cost, offer_code):
    discount = 0
    if offer_code == "OFR001" and 70 <= distance <= 200 and 0 < weight <= 200:
        discount = 0.1 * base_cost
    elif offer_code == "OFR002" and 50 <= distance <= 150 and 100 < weight <= 250:
        discount = 0.07 * base_cost
    elif offer_code == "OFR003" and 50 <= distance <= 250 and 10 < weight <= 150:
        discount = 0.05 * base_cost
    return discount


# ---- Package Class ----
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


# ---- Vehicle Class ----
class Vehicle:
    def __init__(self, max_speed, max_weight):
        self.max_speed = max_speed
        self.max_weight = max_weight
        self.available_at = 0.0


# ---- Main Logic ----
def delivery_time_estimation(base_cost, packages, vehicles_count, max_speed, max_weight):
    packages = sorted(packages, key=lambda p: (-p.weight, p.distance))

    vehicles = [Vehicle(max_speed, max_weight) for _ in range(vehicles_count)]
    queue = deque(packages)

    results = []

    while queue:
        for v in vehicles:
            if not queue:
                break

            # pick packages for this vehicle
            current_weight = 0
            trip = []

            for pkg in list(queue):
                if current_weight + pkg.weight <= v.max_weight:
                    trip.append(pkg)
                    current_weight += pkg.weight
                    queue.remove(pkg)

            if trip:
                max_distance = max(p.distance for p in trip)
                delivery_time = max_distance / v.max_speed
                v.available_at += 2 * delivery_time  # round trip

                for pkg in trip:
                    pkg.delivery_time = round(v.available_at - delivery_time, 2)
                    results.append(pkg)

    # sort back in original input order
    results.sort(key=lambda p: int(p.pkg_id[3:]))
    return results


# ---- Example Execution ----
if __name__ == "__main__":
    # Input Example
    base_cost = 100
    packages_data = [
        ("PKG1", 50, 30, "OFR001"),
        ("PKG2", 75, 125, "OFR008"),
        ("PKG3", 175, 100, "OFR003"),
        ("PKG4", 110, 60, "OFR002"),
        ("PKG5", 155, 95, "NA")
    ]
    vehicles_count, max_speed, max_weight = 2, 70, 200

    packages = [Package(pid, w, d, oc, base_cost) for pid, w, d, oc in packages_data]
    results = delivery_time_estimation(base_cost, packages, vehicles_count, max_speed, max_weight)

    # Output
    for p in results:
        print(f"{p.pkg_id} {int(p.discount)} {p.total_cost} {p.delivery_time}")
