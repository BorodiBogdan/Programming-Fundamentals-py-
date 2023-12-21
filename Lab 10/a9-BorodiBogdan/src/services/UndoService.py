from src.domain.command import *
from src.domain.UndoRedoError import UndoRedoError


class UndoService:
    def __init__(self):
        self.__undo = []
        self.__redo = []

    def register(self, oper: CascadianOperation):
        self.__undo.append(oper)

    def undo(self):
        if not self.__undo:
            raise UndoRedoError("No more undos!")

        o = self.__undo.pop()
        self.__redo.append(o)
        o.undo()

    def redo(self):
        if not self.__redo:
            raise UndoRedoError("No more redos!")

        o = self.__redo.pop()
        self.__undo.append(o)
        o.redo()