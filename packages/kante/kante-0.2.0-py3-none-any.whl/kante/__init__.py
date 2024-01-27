from kante.gateway import build_gateway
from pydantic import BaseModel
class Hallo(BaseModel):

    message: str


x = build_gateway("test", Hallo)


x.broadcast("fuck")