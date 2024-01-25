from tkdeft import *
from tkinter import *
from tkinter.font import *

root = DWindow(mode="dark")
root.wincustom()
root.wm_geometry("680x320")

frame2 = DFrame(mode="dark")

badge2 = DBadge(frame2, text="DDarkBadge", width=100, mode="dark")
badge2.pack(padx=5, pady=5)

button3 = DButton(
    frame2, text="DDarkButton", command=lambda: print("DDarkButton -> Clicked"),
    style="standard", mode="dark"
)
button3.pack(fill="x", padx=5, pady=5)

button4 = DButton(
    frame2, text="DDarkAccentButton", command=lambda: print("DDarkAccentButton -> Clicked"),
    style="accent", mode="dark"
)
button4.pack(fill="x", padx=5, pady=5)

entry2 = DEntry(frame2, mode="dark")
entry2.pack(fill="x", padx=5, pady=5)

text2 = DText(frame2, mode="dark")
text2.pack(fill="x", padx=5, pady=5)

frame2.pack(fill="both", expand="yes", side="right", padx=5, pady=5)
root.mainloop()
