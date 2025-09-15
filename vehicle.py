class Vehicle:
    """
    Represents a delivery vehicle with speed and weight capacity.
    """
    def __init__(self, max_speed, max_weight):
        """
        Initialize the Vehicle with speed and weight capacity.
        :param max_speed: Maximum speed of the vehicle (float)
        :param max_weight: Maximum weight the vehicle can carry (float)
        """
        self.max_speed = max_speed
        self.max_weight = max_weight
        self.available_at = 0.0
