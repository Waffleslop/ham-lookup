import tkinter as tk
import webbrowser
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def lookup_callsign():
    callsign = callsign_entry.get().strip().upper()
    if callsign:
        webbrowser.open(f"https://www.qrz.com/db/{callsign}")
        callsign_entry.delete(0, tk.END)


def lookup_grid():
    grid = grid_entry.get().strip().upper()
    if grid:
        webbrowser.open(f"https://k7fry.com/grid/?qth={grid}")
        grid_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Ham Lookup")
root.iconbitmap(os.path.join(SCRIPT_DIR, "radio.ico"))
root.resizable(False, False)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Callsign row
callsign_frame = tk.Frame(frame)
callsign_frame.pack(fill=tk.X, pady=(0, 5))

tk.Label(callsign_frame, text="Callsign:", width=10, anchor=tk.W).pack(side=tk.LEFT)
callsign_entry = tk.Entry(callsign_frame, width=12, font=("Consolas", 12))
callsign_entry.pack(side=tk.LEFT, padx=(5, 5))
callsign_entry.bind("<Return>", lambda e: lookup_callsign())
tk.Button(callsign_frame, text="QRZ", width=6, command=lookup_callsign).pack(side=tk.LEFT)

# Grid row
grid_frame = tk.Frame(frame)
grid_frame.pack(fill=tk.X)

tk.Label(grid_frame, text="Grid:", width=10, anchor=tk.W).pack(side=tk.LEFT)
grid_entry = tk.Entry(grid_frame, width=12, font=("Consolas", 12))
grid_entry.pack(side=tk.LEFT, padx=(5, 5))
grid_entry.bind("<Return>", lambda e: lookup_grid())
tk.Button(grid_frame, text="Map", width=6, command=lookup_grid).pack(side=tk.LEFT)

callsign_entry.focus_set()
root.mainloop()
