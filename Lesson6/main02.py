from pydantic import BaseModel, Field #Функция Field позволяет задавать различные параметры для поля, такие как тип данных, значение по умолчанию, ограничения на значения и т.д

class Item(BaseModel):
    name: str = Field(max_length=10)

class User(BaseModel):
    age: int = Field(default=0)