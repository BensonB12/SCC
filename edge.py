from pydantic import BaseModel

class Edge(BaseModel):
  node: int
  neighbor: int
  weight: int = 1