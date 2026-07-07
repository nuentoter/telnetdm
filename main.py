import asyncio

from server.telnet_server import main as server_main


def main():
    try:
        asyncio.run(server_main())
    except KeyboardInterrupt:
        print("\n")
        print("=================================")
        print("Stopping TelnetDM...")
        print("Goodbye!")
        print("=================================")


if __name__ == "__main__":
    main()
