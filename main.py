from package import Package
from delivery_manager import DeliveryManager

def main():
    # Console input section
    base_cost = float(input("Enter base delivery cost: "))
    num_packages = int(input("Enter number of packages: "))
    packages_data = []
    for i in range(1, num_packages + 1):
        pkg_line = input(f"Enter package {i} details (id weight distance offer_code): ")
        pkg_id, weight, distance, offer_code = pkg_line.split()
        packages_data.append((pkg_id, float(weight), float(distance), offer_code))
    vehicles_count = int(input("Enter number of vehicles: "))
    max_speed = float(input("Enter max speed of vehicles: "))
    max_weight = float(input("Enter max weight per vehicle: "))

    packages = [Package(pid, w, d, oc, base_cost) for pid, w, d, oc in packages_data]
    manager = DeliveryManager(base_cost, vehicles_count, max_speed, max_weight)
    results = manager.estimate_delivery_times(packages)

    for p in results:
        print(f"{p.pkg_id} {int(p.discount)} {p.total_cost} {p.delivery_time}")

if __name__ == "__main__":
    main()

    # --- For testing only, uncomment to use hardcoded data ---
    # base_cost = 100
    # packages_data = [
    #     ("PKG1", 50, 30, "OFR001"),
    #     ("PKG2", 75, 125, "OFR008"),
    #     ("PKG3", 175, 100, "OFR003"),
    #     ("PKG4", 110, 60, "OFR002"),
    #     ("PKG5", 155, 95, "NA")
    # ]
    # vehicles_count, max_speed, max_weight = 2, 70, 200
    # packages = [Package(pid, w, d, oc, base_cost) for pid, w, d, oc in packages_data]
    # manager = DeliveryManager(base_cost, vehicles_count, max_speed, max_weight)
    # results = manager.estimate_delivery_times(packages)
    # for p in results:
    #     print(f"{p.pkg_id} {int(p.discount)} {p.total_cost} {p.delivery_time}")
