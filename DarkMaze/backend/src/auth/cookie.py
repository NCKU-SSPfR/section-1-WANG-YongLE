from datetime import datetime, timedelta
class CookieManager:
    @staticmethod
    def create_cookie(name: str, value: str, days: int = 1):
        """Create cookie settings format"""
        expires = datetime.utcnow() + timedelta(days=days)
        return {
            "name": name,
            "value": value,
            "expires": expires.strftime("%Y-%m-%dT%H:%M:%SZ")
        }