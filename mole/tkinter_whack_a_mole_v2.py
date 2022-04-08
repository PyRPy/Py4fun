# https://runestone.academy/ns/books/published/thinkcspy/GUIandEventDrivenProgramming/11_gui_program_example.html
"""
Implement the basic layout of a Whack-a-mole game.
STEP 2 : create moles in a 'matrix'
"""
# =====================================================================
import tkinter as tk
from tkinter import PhotoImage 

def main():
    # Create the GUI program
    program = WhackAMole()

    # Start the GUI event loop
    program.window.mainloop()

class WhackAMole:
    NUM_MOLES_ACROSS = 4

    def __init__(self):
        self.window = tk.Tk()
        self.mole_frame, self.status_frame = self.create_frames()
        self.mole_photo = PhotoImage(file="images/mole.png")
        self.mole_buttons = self.create_moles()

    def create_frames(self):
        mole_frame = tk.Frame(self.window, bg='red')
        mole_frame.grid(row=1, column=1)

        status_frame = tk.Frame(self.window, bg='green', width=100)
        status_frame.grid(row=1, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        return mole_frame, status_frame

    def create_moles(self):
        mole_buttons = [] 
        for r in range(WhackAMole.NUM_MOLES_ACROSS):
            row_of_buttons = [] 
            for c in range(WhackAMole.NUM_MOLES_ACROSS):
                mole_button = tk.Button(self.mole_frame, image=self.mole_photo)
                mole_button.grid(row=r, column=c, padx=8, pady=8)

                row_of_buttons.append(mole_button)
            mole_buttons.append(row_of_buttons) 
        return mole_buttons


if __name__ == "__main__":
    main()