#program 1 - main
from event_systems import register_event, dispatch
from functions import notify_teammates, send_message


def create_player(name: str, goals: int):
    print("Player was saved", name, goals)
    dispatch('player_registered', name)

register_event('player_registered', send_message)
register_event('player_registered', notify_teammates)

create_player("Ashley", 100)
