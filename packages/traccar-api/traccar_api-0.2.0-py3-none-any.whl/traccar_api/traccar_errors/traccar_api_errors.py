class TraccarApiError(Exception):

    def __init__(self, message, status_code=None, response_body=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_body = response_body

    def __str__(self):
        if self.status_code:
            return f"{self.message} (Status Code: {self.status_code}, Response: {self.response_body})"
        else:
            return self.message


class TraccarApiAuthenticationError(TraccarApiError):

    def __init__(self, message, status_code=None, response_body=None, details=None):
        super().__init__(message, status_code, response_body)
        self.details = details

    def __str__(self):
        base_str = super().__str__()
        if self.details:
            return f"{base_str} (Details: {self.details})"
        else:
            return base_str
