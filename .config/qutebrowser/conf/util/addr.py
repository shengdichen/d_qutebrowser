class Addr:
    @staticmethod
    def make_https(addr: str) -> str:
        start = "https://"
        if not addr.startswith(start):
            return start + addr
