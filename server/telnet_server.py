import asyncio
import telnetlib3

from engine.session import Session
from engine.commands import handle_command

WELCOME_TEXT = (
    "=================================\r\n"
    "           TelnetDM\r\n"
    "=================================\r\n"
    "\r\n"
    "Type:\r\n"
    "  look\r\n"
    "  go north/south\r\n"
    "  quit\r\n"
    "\r\n"
    "> "
)


async def shell(reader, writer):
    session = Session(writer)

    # Display the welcome banner.
    writer.write(WELCOME_TEXT)

    while True:
        cmd = await reader.readline()

        if not cmd:
            break

        cmd = cmd.strip()

        # Echo what the user typed so it appears in clients
        # that don't perform local echo.

        result = handle_command(session, cmd)

        if result == "quit":
            writer.write("\r\nFarewell, adventurer.\r\n")
            break

        writer.write("\r\n> ")

    writer.close()


async def main():
    server = await telnetlib3.create_server(
        host="0.0.0.0",
        port=8023,
        shell=shell,
        line_mode=True,
    )

    print("TelnetDM running on port 8023")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
