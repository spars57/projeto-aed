from tkinter import Tk, Frame
from tkinter.ttk import Button


class UiConstructor:
    def __init__(self, root: Tk, frame_width: int, frame_height: int):
        self.__root: Tk = root
        self.__frame: Frame = Frame(self.__root, width=frame_width, height=frame_height)
        self.__buttons: list[Button] = []

    def create_button(self, name: str, **args: Button.__class__):
        new_button = Button(self.__frame, name=name, **args)


root = Tk()

c = UiConstructor(root, frame_width=500, frame_height=500)

c.create_button(name="B1", text="")
