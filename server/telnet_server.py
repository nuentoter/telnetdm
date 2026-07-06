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


async def shell(reader, writer, telnet_protocol=None):
    session = Session(writer)

    writer.write(WELCOME_TEXT)

    while True:
        cmd = await reader.readline()

        if not cmd:
            break
        cmd = cmd.strip()
               
        result = handle_command(session, cmd)

        if result == "quit":
            break

        writer.write("\r\n> ")

    writer.close()


async def main():
    server = await telnetlib3.create_server(
        host="0.0.0.0",
        port=8023,
        shell=shell
    )

    print("TelnetDM running on port 8023")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
