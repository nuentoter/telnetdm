import asyncio
from server.telnet_server import main as server_main


def main():
    asyncio.run(server_main())


if __name__ == "__main__":
    main()
