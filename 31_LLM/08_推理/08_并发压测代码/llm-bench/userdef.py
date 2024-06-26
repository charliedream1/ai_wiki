import asyncio

class UserDef:
    BASE_URL = ""

    @classmethod
    def ping_url(cls):
        return f"{cls.BASE_URL}/healthz"

    @staticmethod
    async def rest():
        import asyncio

        await asyncio.sleep(0.01)