import asyncio
import telnetlib3


WELCOME_TEXT = """
=================================
           TelnetDM
     AI Dungeon Master v0.1
=================================

You feel reality stabilize around you...

Type anything to begin.

> """


async def shell(reader, writer):
    writer.write(WELCOME_TEXT)

    while True:
        try:
            cmd = await reader.read(1024)

            if not cmd:
                break

            cmd = cmd.strip()

            if cmd.lower() in ("quit", "exit"):
                writer.write("\nFarewell, adventurer.\n")
                break

            response = f"\nYou said: {cmd}\n> "
            writer.write(response)

        except Exception as e:
            writer.write(f"\nError: {e}\n")
            break

    writer.close()


async def main():
    server = await telnetlib3.create_server(
        host="0.0.0.0",
        port=8023,
        shell=shell
    )

    print("TelnetDM server running on port 8023")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
