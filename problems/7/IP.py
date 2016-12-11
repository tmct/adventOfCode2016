class IP:
    def __init__(self, address):
        self.address = address

    @property
    def supports_tls(self):
        return False