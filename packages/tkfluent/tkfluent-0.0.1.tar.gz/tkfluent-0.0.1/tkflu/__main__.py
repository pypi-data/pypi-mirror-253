from tkflu import *
from tkinter import *
from tkinter.font import *

mode = "light"

root = FluWindow(mode=mode)
root.wincustom()
root.wm_geometry("180x320")

frame = FluFrame(mode=mode)

badge1 = FluBadge(frame, text="DBadge", width=60, mode=mode)
badge1.pack(padx=5, pady=5)

badge2 = FluBadge(frame, text="DBadge (Accent)", width=110, mode=mode, style="accent")
badge2.pack(padx=5, pady=5)

button1 = FluButton(
    frame, text="DButton", command=lambda: print("DDarkButton -> Clicked"), mode=mode
)
button1.pack(fill="x", padx=5, pady=5)

button2 = FluButton(
    frame, text="DButton (Accent)", command=lambda: print("DDarkAccentButton -> Clicked"), style="accent", mode=mode
)
button2.pack(fill="x", padx=5, pady=5)

entry1 = FluEntry(frame, mode=mode)
entry1.pack(fill="x", padx=5, pady=5)

text1 = FluText(frame, mode=mode)
text1.pack(fill="x", padx=5, pady=5)

frame.pack(fill="both", expand="yes", side="right", padx=5, pady=5)
root.mainloop()
