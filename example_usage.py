from client import VercelKvRedisCacherClient
client = VercelKvRedisCacherClient()
print(client.set_cache("prompt_hash_1", "Output text"))