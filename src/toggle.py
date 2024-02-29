class ToggleManager:
    def __init__(self, toggle=True):
        # Initializes a toggle manager with a default toggle status
        self.toggle = toggle

    def get_toggle_status(self):
        # Retrieves the current toggle status
        return self.toggle

    def set_toggle_status(self, new_status):
        # Sets the toggle status to a new value
        self.toggle = new_status

# Creates an instance of ToggleManager for managing the toggle status
toggle_running = ToggleManager()
