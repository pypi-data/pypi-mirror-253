from typing import Literal, TypeVar, Generic
from dataclasses import dataclass
from pydantic import BaseModel
import ramda as R

class Skip(BaseModel):
    type: Literal['skip'] = 'skip'
    idx: int
       
A = TypeVar('A')
class Insert(BaseModel, Generic[A]):
    type: Literal['insert'] = 'insert'
    idx: int
    value: A = None
    
Edit = Insert | Skip
    
@dataclass
class Inserted(Generic[A]):
    value: A