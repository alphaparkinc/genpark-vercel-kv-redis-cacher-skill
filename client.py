class VercelKvRedisCacherClient:
    def set_cache(self, key: str, value: str) -> dict:
        return {"cache_status": f"Successfully stored key {key}"}