from pydantic import BaseModel, Field

class Data(BaseModel):
    daerah: str = Field (example="kota-bogor")