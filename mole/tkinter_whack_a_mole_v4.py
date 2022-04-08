# https://runestone.academy/ns/books/published/thinkcspy/GUIandEventDrivenProgramming/11_gui_program_example.html
"""
Implement the basic layout of a Whack-a-mole game.
STEP 3: add status frame
STEP 4: add callback function
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
    STATUS_BACKGROUND = "white"

    def __init__(self):
        self.window = tk.Tk()
        self.mole_frame, self.status_frame = self.create_frames()
        self.mole_photo = PhotoImage(file="images/mole.png")
        self.mole_buttons = self.create_moles()

        self.hit_counter, self.miss_counter, self.start_button, self.quit_button \
            = self.create_status_widgets()

        self.set_callbacks() 

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

    def create_status_widgets(self):
        spacer = tk.Label(self.status_frame, text = "", bg=WhackAMole.STATUS_BACKGROUND)
        spacer.pack(side="top", fill=tk.Y, expand=True)

        hit_label = tk.Label(self.status_frame, text="Number of Hits", bg=WhackAMole.STATUS_BACKGROUND)
        hit_label.pack(side="top", fill=tk.Y, expand=True)

        hit_counter = tk.Label(self.status_frame, text="0", bg=WhackAMole.STATUS_BACKGROUND)
        hit_counter.pack(side="top", fill=tk.Y, expand=True)

        spacer = tk.Label(self.status_frame, text="", bg=WhackAMole.STATUS_BACKGROUND)
        spacer.pack(side="top", fill=tk.Y, expand=True)

        miss_label = tk.Label(self.status_frame, text="Number of Misses", bg=WhackAMole.STATUS_BACKGROUND)
        miss_label.pack(side="top", fill=tk.Y, expand=True)

        miss_counter = tk.Label(self.status_frame, text="0", bg=WhackAMole.STATUS_BACKGROUND)
        miss_counter.pack(side="top", fill=tk.Y, expand=True)

        spacer = tk.Label(self.status_frame, text="", bg=WhackAMole.STATUS_BACKGROUND)
        spacer.pack(side="top", fill=tk.Y, expand=True)

        start_button = tk.Button(self.status_frame, text="Start")
        start_button.pack(side="top", fill=tk.Y, expand=True, ipadx=10)

        spacer = tk.Label(self.status_frame, text="", bg=WhackAMole.STATUS_BACKGROUND)
        spacer.pack(side="top", fill=tk.Y, expand=True)

        quit_button = tk.Button(self.status_frame, text="Quit")
        quit_button.pack(side="top", fill=tk.Y, expand=True, ipadx=10)

        spacer = tk.Label(self.status_frame, text="", bg=WhackAMole.STATUS_BACKGROUND)
        spacer.pack(side="top", fill=tk.Y, expand=True)

        return hit_counter, miss_counter, start_button, quit_button

    def set_callbacks(self):
        # for each mole button 
        for r in range(WhackAMole.NUM_MOLES_ACROSS):
            for c in range(WhackAMole.NUM_MOLES_ACROSS):
                self.mole_buttons[r][c]['command'] = self.mole_hit 
        self.start_button['command'] = self.start 
        self.quit_button['command'] = self.quit 

    def mole_hit(self):
        print("mole button hit")

    def start(self):
        print("start button hit")

    def quit(self):
        print("quit button hit")

if __name__ == "__main__":
    main()