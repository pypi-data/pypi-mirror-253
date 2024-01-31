class GrpcCoteaException(Exception):
    def __init__(self, message):
        self.message = f"grpc cotea internal exception: {message}"
        super().__init__(self.message)