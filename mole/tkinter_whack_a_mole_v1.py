# https://runestone.academy/ns/books/published/thinkcspy/GUIandEventDrivenProgramming/11_gui_program_example.html
"""
Implement the basic layout of a Whack-a-mole game.
STEP 1 : just show two frames
"""
# =====================================================================
import tkinter as tk

class WhackAMole:

    def __init__(self):
        self.window = tk.Tk()
        self.mole_frame, self.status_frame = self.create_frames()

    def create_frames(self):
        mole_frame = tk.Frame(self.window, bg='red', width=300, height=300)
        mole_frame.grid(row=1, column=1)

        status_frame = tk.Frame(self.window, bg='green', width=100, height=300)
        status_frame.grid(row=1, column=2)

        return mole_frame, status_frame

def main():
    # Create the GUI program
    program = WhackAMole()

    # Start the GUI event loop
    program.window.mainloop()

if __name__ == "__main__":
    main()