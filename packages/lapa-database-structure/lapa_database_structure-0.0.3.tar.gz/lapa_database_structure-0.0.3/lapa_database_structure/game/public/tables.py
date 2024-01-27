from sqlalchemy import Column, Integer, DateTime, func, ForeignKey, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

data_to_insert = []


class Game(Base):
    __tablename__ = 'game'

    game_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    game_name = Column(String, nullable=False, unique=True)


data_to_insert.extend([
    Game(game_name="truecolor")
])


class GameInstance(Base):
    __tablename__ = 'game_instance'

    game_instance_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey(Game.game_id, ondelete="RESTRICT", onupdate="RESTRICT"), index=True,
                     nullable=False)
    game_instance_date_created = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    game_instance_last_modified = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(),
                                         nullable=False)


class Player(Base):
    __tablename__ = 'player'

    player_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    player_name = Column(String, nullable=False)
    player_date_created = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class GameInstancePlayer(Base):
    __tablename__ = 'game_instance_player'

    game_instance_player_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    game_instance_id = Column(Integer,
                              ForeignKey(GameInstance.game_instance_id, ondelete="RESTRICT", onupdate="RESTRICT"),
                              index=True,
                              nullable=False)
    player_id = Column(Integer,
                       ForeignKey(Player.player_id, ondelete="RESTRICT", onupdate="RESTRICT"),
                       index=True,
                       nullable=False)
