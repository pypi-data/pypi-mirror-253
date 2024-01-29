class ApiResponseException(Exception):
    """Exception raised when api response is not 200 Ok

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class MissingArgumentException(Exception):
    """Exception raised when obligatory argument is not provided

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
