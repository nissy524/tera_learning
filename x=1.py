from dataclasses import dataclass
@dataclass
class User:
    name:str
    age:int

user =User('sato',20)
print(user.name)
print(user.age)

from dataclasses import field, dataclass
@dataclass
class User:
    name:str
    age:int
    items:list[int]=field(default_factory=lambda:['note','pen'])



user=User('supu',10)
print(user.items)
#frozenはfieldを変更できない、asdictは、辞書型に変更できる(resultの後)


import dataclasses
@dataclass(frozen=True)
class User:
    name:str
    age:int

user=User('tera',26)
result=dataclasses.asdict(user)
print(result)



