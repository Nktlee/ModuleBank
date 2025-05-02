import random
import time
import asyncio
import aiohttp
from aiohttp.client_exceptions import ClientConnectorError

USERS = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Frank",
    "Grace",
    "Heidi",
    "Ivan",
    "Judy",
]
SERVER_URL = "http://localhost:8000/messages"
REQUEST_COUNT_PER_COROUTINE = 100
NUM_COROUTINES = 50


async def make_request(session, server_url):
    sender = random.choice(USERS)
    data = {"sender_name": sender, "text": f"{sender}'s message"}
    start_time = time.time()
    try:
        async with session.post(server_url, json=data) as response:
            await response.json()
            end_time = time.time()
            return True, end_time - start_time
    except ClientConnectorError:
        return False, None


async def worker_task(worker_id, session):
    requests_made = 0
    total_latency = 0
    while requests_made < REQUEST_COUNT_PER_COROUTINE:
        server_url = SERVER_URL
        success, latency = await make_request(session, server_url)
        if success and latency is not None:
            total_latency += latency
        requests_made += 1
    return total_latency / REQUEST_COUNT_PER_COROUTINE


async def main():
    tasks = []
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        for i in range(NUM_COROUTINES):
            task = asyncio.create_task(worker_task(i, session))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
    avg_latencies = sum(results) / len(results)
    elapsed_time = time.time() - start_time
    throughput = NUM_COROUTINES * REQUEST_COUNT_PER_COROUTINE / elapsed_time

    print(f"Total Requests: {NUM_COROUTINES * REQUEST_COUNT_PER_COROUTINE}")
    print(f"Elapsed Time: {elapsed_time:.2f}s")
    print(f"Average Latency per Request: {avg_latencies:.4f}s")
    print(f"Throughput: {throughput:.2f} req/sec")


if __name__ == "__main__":
    asyncio.run(main())
