from package import Package

def main():
    first_line = input("Enter the base delivery cost and number of packages: ")
    base_fare, num_packages = first_line.split()
    base_fare = float(base_fare)
    num_packages = int(num_packages)
    packages = []
    for i in range(1, num_packages + 1):
        pkg_line = input(f"Enter package {i} details: ")
        pkg_id, weight, distance, offer_code = pkg_line.split()
        package = Package(
            pkg_id=pkg_id,
            weight=float(weight),
            distance=float(distance),
            offer_code=offer_code,
            base_cost=base_fare
        )
        packages.append(package)
    for package in packages:
        print(f"{package.pkg_id} {int(package.discount)} {package.total_cost}")

if __name__ == "__main__":
    main()
