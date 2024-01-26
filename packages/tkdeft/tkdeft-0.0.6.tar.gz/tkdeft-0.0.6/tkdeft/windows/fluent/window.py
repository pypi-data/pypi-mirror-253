from tkinter import Tk
from ...object import DObject


class DWindow(Tk, DObject):
    def __init__(self, *args, className="tkdeft", mode="light", **kwargs):

        self._init(mode)

        self.custom = False

        super().__init__(*args, className=className, **kwargs)

        self.bind("<Configure>", self._event_configure)

    def _event_configure(self, event=None):
        self.configure(background=self.attributes.back_color)
        if self.custom:
            if hasattr(self, "titlebar"):
                self.titlebar.configure(background=self.attributes.back_color)
            if hasattr(self, "titlelabel"):
                self.titlelabel.dconfigure(text_color=self.attributes.text_color)
            if hasattr(self, "closebutton"):
                self.closebutton.dconfigure(
                    rest={
                        "back_color": self.titlebar.cget("background"),
                        "border_color": "#f0f0f0",
                        "border_color2": "#d6d6d6",
                        "border_width": 0,
                        "radius": 0,
                        "text_color": self.attributes.closebutton.text_color,
                    },
                    hover={
                        "back_color": self.attributes.closebutton.back_color,
                        "border_color": "#f0f0f0",
                        "border_color2": "#d6d6d6",
                        "border_width": 0,
                        "radius": 0,
                        "text_color": self.attributes.closebutton.text_hover_color,
                    },
                    pressed={
                        "back_color": self.attributes.closebutton.back_color,
                        "border_color": "#f0f0f0",
                        "border_color2": "#f0f0f0",
                        "border_width": 0,
                        "radius": 0,
                        "text_color": self.attributes.closebutton.text_hover_color,
                    }
                )

    def _init(self, mode):
        from easydict import EasyDict
        self.attributes = EasyDict(
            {
                "back_color": None,
                "text_color": None,
                "closebutton": {
                    "back_color": None,
                    "text_color": None,
                    "text_hover_color": None
                }
            }
        )

        self.theme(mode)

    def theme(self, mode: str):
        if mode.lower() == "dark":
            self._dark()
        else:
            self._light()

    def _light(self):
        self.dconfigure(
            back_color="#ffffff",
            text_color="#000000",
            closebutton={
                "back_color": "red",
                "text_color": "#000000",
                "text_hover_color": "#ffffff"
            }
        )

    def _dark(self):
        self.dconfigure(
            back_color="#202020",
            text_color="#ffffff",
            closebutton={
                "back_color": "red",
                "text_color": "#ffffff",
                "text_hover_color": "#000000"
            }
        )

    def wincustom(self, wait=200):
        from .button import DButton
        from .label import DLabel
        from tkinter import Frame
        self.titlebar = Frame(self, width=180, height=35)
        self.titlelabel = DLabel(self.titlebar, text=self.title(), width=50)
        self.titlelabel.pack(fill="y", side="left")
        self.closebutton = DButton(self.titlebar, text="", width=32, height=32, command=lambda: self.quit())
        self.closebutton.pack(fill="y", side="right")
        self.titlebar.pack(fill="x", side="top")

        from .customwindow import CustomWindow
        self.customwindow = CustomWindow(self, wait=wait)
        self.customwindow.bind_drag(self.titlebar)
        self.customwindow.bind_drag(self.titlelabel)
        self.custom = True
