from game import start as start
from story import game as go

player, characters, items = start()
go(player, characters, items)