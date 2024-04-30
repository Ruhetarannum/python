class DynamicScaler:
    def __init__(self, initial_instances=1, max_instances=10):
        self.instances = initial_instances
        self.max_instances = max_instances

    def scale_up(self, num_instances=1):
        if self.instances + num_instances <= self.max_instances:
            self.instances += num_instances
            print(f"Scaled up to {self.instances} instances.")
        else:
            print("Cannot scale up, maximum instances reached.")

    def scale_down(self, num_instances=1):
        if self.instances - num_instances >= 1:
            self.instances -= num_instances
            print(f"Scaled down to {self.instances} instances.")
        else:
            print("Cannot scale down further, at minimum instances.")

    def current_instances(self):
        return self.instances


# Example usage
if __name__ == "__main__":
    scaler = DynamicScaler(initial_instances=3, max_instances=5)
    print("Current instances:", scaler.current_instances())

    # Scaling up
    scaler.scale_up(2)
    print("Current instances:", scaler.current_instances())

    # Attempting to scale up beyond max_instances
    scaler.scale_up(3)
    print("Current instances:", scaler.current_instances())

    # Scaling down
    scaler.scale_down(1)
    print("Current instances:", scaler.current_instances())

    # Attempting to scale down below 1 instance
    scaler.scale_down(3)
    print("Current instances:", scaler.current_instances())
