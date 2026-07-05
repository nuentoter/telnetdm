import asyncio
import telnetlib3

from engine.session import Session
from engine.commands import handle_command


WELCOME_TEXT = """
=================================
           TelnetDM
=================================

Type:
  look
  go north/south
  quit

> """


async def shell(reader, writer):
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

        writer.write("\n> ")

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
