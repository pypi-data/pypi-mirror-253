from enum import Enum


class DatabasesEnum(str, Enum):
    file_storage = "file_storage"
    game = "game"
    authentication = "authentication"


class TablesEnum(str, Enum):
    file = "file"
    game = "game"
    game_instance = "game_instance"
    game_instance_player = "game_instance_player"
    player = "player"
    user_validation_status = "user_validation_status"
    user_registration = "user_registration"
    hashing_algorithm = "hashing_algorithm"
    user = "user"


class SchemaEnum(str, Enum):
    public = "public"