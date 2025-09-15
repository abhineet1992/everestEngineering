from collections import deque
from vehicle import Vehicle
from package import Package

class DeliveryManager:
    """
    Manages delivery scheduling and delivery time estimation for packages.
    """
    def __init__(self, base_cost, vehicles_count, max_speed, max_weight):
        """
        Initialize the DeliveryManager with vehicles and base cost.
        :param base_cost: Base delivery cost (float)
        :param vehicles_count: Number of vehicles (int)
        :param max_speed: Maximum speed for all vehicles (float)
        :param max_weight: Maximum weight for all vehicles (float)
        """
        self.base_cost = base_cost
        self.vehicles = [Vehicle(max_speed, max_weight) for _ in range(vehicles_count)]

    def estimate_delivery_times(self, packages):
        """
        Estimate delivery times for a list of packages using available vehicles.
        :param packages: List of Package objects
        :return: List of Package objects with updated delivery_time
        """
        packages = sorted(packages, key=lambda p: (-p.weight, p.distance))
        queue = deque(packages)
        results = []

        while queue:
            for v in self.vehicles:
                if not queue:
                    break
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
                    v.available_at += 2 * delivery_time
                    for pkg in trip:
                        pkg.delivery_time = round(v.available_at - delivery_time, 2)
                        results.append(pkg)
        results.sort(key=lambda p: int(p.pkg_id[3:]))
        return results
