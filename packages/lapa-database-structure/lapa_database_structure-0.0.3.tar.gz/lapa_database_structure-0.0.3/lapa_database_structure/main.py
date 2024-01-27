from enum import Enum


class DatabasesEnum(str, Enum):
    file_storage = "file_storage"
    game = "game"


class TablesEnum(str, Enum):
    file = "file"
    game = "game"
    game_instance = "game_instance"
    game_instance_player = "game_instance_player"
    player = "player"


class SchemaEnum(str, Enum):
    public = "public"
