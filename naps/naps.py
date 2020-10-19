"""Main module."""
import anyio

from contextlib import suppress

opened = []

async def check_port(host, port, timeout, semaphore):
    async with semaphore:
        async with anyio.move_on_after(timeout):
            with suppress(OSError):
                async with await anyio.connect_tcp(host, port) as client:
                    await client.send(b'.\n')
                    banner = await client.receive()
                    if banner:
                        opened.append((host, port))
                        print(f"[+] Port {port} open at {host}")


async def schedule(network, port_range_start, port_range_end, timeout=10, concurrency=1024):
    semaphore = anyio.create_semaphore(concurrency)
    async with anyio.create_task_group() as tg:
        for host in network:
            for port in range(port_range_start, port_range_end):
                await tg.spawn(check_port, host, port, timeout, semaphore)
    print(f"Checked {port_range_end - port_range_start} ports across {network.num_addresses} host(s) and found {len(opened)} open port(s)!")
