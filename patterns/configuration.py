# Singleton pattern for a Configuration class
class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
            # Initialize configuration here
            cls._instance.debug_mode = False
        return cls._instance

    def get_debug_mode(self):
        return self.debug_mode

    def set_debug_mode(self, debug_mode):
        self.debug_mode = debug_mode