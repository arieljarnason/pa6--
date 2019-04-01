from enum import Enum

class OpType(Enum):
    """Undo operations: ADD, DELETE, UPDATE"""
    ADD_MEMBER = 1
    ADD_SPORT = 2
    ADD_GROUP = 3
    DELETE_MEMBER = 4
    DELETE_SPORT = 5
    DELETE_GROUP = 6
    UPDATE_NAME = 7
    UPDATE_PHONE = 8
    UPDATE_EMAIL = 9
    UPDATE_YEAR = 10
    

class OpInfo:
    """object takes in type of undo and all
    data to complete the action"""
    def __init__(self, op_type=None, data=None, extra=None):
        self.op_type = op_type
        self.data = data
        self.extra = extra