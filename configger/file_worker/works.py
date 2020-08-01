"""Common functions and provisions for handlers of different types of files"""


def worker(worker_function: callable):
    """Wrapper function for handlers of different file types"""
    def wrapped(config: object, filename: str):
        """Populates config with values ​​from files, waiting returns dict."""
        try:
            with open(filename) as file:
                fields = worker_function(file)
                config.config_data = fields
        except FileNotFoundError as exc:
            raise Exception("Config file not found.")
    return wrapped
