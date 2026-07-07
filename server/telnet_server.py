import asyncio
import telnetlib3

from engine.game import Game
from engine.session import Session
from engine.player_storage import save_player, load_player


WELCOME_TEXT = (
    "=================================\r\n"
    "           TelnetDM\r\n"
    "=================================\r\n"
    "\r\n"
    "Type:\r\n"
    "  look\r\n"
    "  go north/south\r\n"
    "  inventory\r\n"
    "  quit\r\n"
    "\r\n"
    "> "
)


GAME = Game()



async def shell(reader, writer):

    session = Session(writer)


    saved_player = load_player()


    if saved_player:

        session.player.room = saved_player.get(
            "room",
            "start_room"
        )


        session.player.inventory = saved_player.get(
            "inventory",
            []
        )


    GAME.connect(session)


    writer.write(
        WELCOME_TEXT
    )


    while True:

        cmd = await reader.readline()


        if not cmd:

            break


        cmd = cmd.strip()


        result = GAME.process_command(
            session,
            cmd
        )


        if result == "quit":

            writer.write(
                "\r\nFarewell, adventurer.\r\n"
            )

            break


        if result:

            writer.write(
                "\r\n" + result + "\r\n"
            )


        writer.write(
            "\r\n> "
        )


    save_player(
        session.player
    )


    GAME.disconnect(session)


    writer.close()



async def main():

    server = await telnetlib3.create_server(
        host="0.0.0.0",
        port=8023,
        shell=shell,
        line_mode=True,
    )


    print(
        "TelnetDM running on port 8023"
    )


    await server.wait_closed()



if __name__ == "__main__":

    asyncio.run(main())
