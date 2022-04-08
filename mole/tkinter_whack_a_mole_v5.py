# https://runestone.academy/ns/books/published/thinkcspy/GUIandEventDrivenProgramming/11_gui_program_example.html
"""
Implement the basic layout of a Whack-a-mole game.
STEP 3: add status frame
STEP 4: add callback function
STEP 5: add functionality to callbacks
"""
# =====================================================================
import tkinter as tk
from tkinter import PhotoImage 
from tkinter import messagebox 
from random import randint 

def main():
    # Create the GUI program
    program = WhackAMole()

    # Start the GUI event loop
    program.window.mainloop()

class WhackAMole:
    NUM_MOLES_ACROSS = 4
    STATUS_BACKGROUND = "white"
    MIN_TIME_DOWN = 1000
    MAX_TIME_DOWN = 5000
    MIN_TIME_UP = 1000
    MAX_TIME_UP = 3000

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Whack-a-mole")

        self.mole_frame, self.status_frame = self.create_frames()
        self.mole_photo = PhotoImage(file="images/mole.png")
        self.mole_cover_photo = PhotoImage(file="images/no_mole.png")
        self.label_timers = {}

        self.mole_labels = self.create_moles()

        self.hit_counter, self.miss_counter, self.start_button, self.quit_button \
            = self.create_status_widgets()

        self.set_callbacks() 
        self.game_is_running = False 

    def create_frames(self):
        mole_frame = tk.Frame(self.window, bg='red')
        mole_frame.grid(row=1, column=1)

        status_frame = tk.Frame(self.window, bg='green', width=100)
        status_frame.grid(row=1, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        return mole_frame, status_frame

    def create_moles(self):
        mole_labels = [] 
        for r in range(WhackAMole.NUM_MOLES_ACROSS):
            row_of_labels = [] 
            for c in range(WhackAMole.NUM_MOLES_ACROSS):
                mole_label = tk.Button(self.mole_frame, image=self.mole_photo)
                mole_label.grid(row=r, column=c, sticky=tk.E + tk.W + tk.N + tk.S)
                self.label_timers[id(mole_label)] = None 

                row_of_labels.append(mole_label)
            mole_labels.append(row_of_labels) 
        return mole_labels

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
                self.mole_labels[r][c].bind("<ButtonPress-1>", self.mole_hit)
        self.start_button['command'] = self.start 
        self.quit_button['command'] = self.quit 

    def mole_hit(self, event):
        if self.game_is_running:
            hit_label = event.widget 
            # missed, update miss counter
            if hit_label['image'] == self.mole_cover_photo.name:
                self.miss_counter['text'] = str(int(self.miss_counter['text']) + 1)
            else:
                # hit, update hit counter
                self.hit_counter['text'] = str(int(self.hit_counter['text']) + 1)
                # remove the mole, don't update miss counter
                self.put_down_mole(hit_label, False)

    def start(self):
        if self.start_button['text'] == 'Start':
            for r in range(WhackAMole.NUM_MOLES_ACROSS):
                for c in range(WhackAMole.NUM_MOLES_ACROSS):
                    the_label = self.mole_labels[r][c]
                    the_label['image'] = self.mole_cover_photo
                    time_down = randint(WhackAMole.MIN_TIME_DOWN, WhackAMole.MAX_TIME_DOWN)
                    timer_object = the_label.after(time_down, self.pop_up_mole, the_label)
                    self.label_timers[id(the_label)] = timer_object
            self.game_is_running = True 
            self.start_button['text'] = "Stop" 

            self.hit_counter['text'] = "0"
            self.miss_counter['text'] = "0"
        # stop the game and reset everyting
        else: 
            for r in range(WhackAMole.NUM_MOLES_ACROSS):
                for c in range(WhackAMole.NUM_MOLES_ACROSS):
                    the_label = self.mole_labels[r][c]
                    # Show the mole
                    the_label['image'] = self.mole_photo   
                    the_label.after_cancel(self.label_timers[id(the_label)])
            self.game_is_running = False 
            self.start_button['text'] = "Start"         

    def put_down_mole(self, the_label, timer_expired):
        if self.game_is_running:
            if timer_expired:
                self.miss_counter['text'] = str(int(self.miss_counter['text']) + 1)
            else:
                the_label.after_cancel(self.label_timers[id(the_label)])
            the_label['image'] = self.mole_cover_photo

            time_down = randint(WhackAMole.MIN_TIME_DOWN, WhackAMole.MAX_TIME_DOWN)
            timer_object = the_label.after(time_down, self.pop_up_mole, the_label)
            self.label_timers[id(the_label)] = timer_object

    def pop_up_mole(self, the_label):

        the_label['image'] = self.mole_photo 
        if self.game_is_running:
            time_up = randint(WhackAMole.MIN_TIME_UP, WhackAMole.MAX_TIME_UP)
            timer_object = the_label.after(time_up, self.put_down_mole, the_label, True)
            self.label_timers[id(the_label)] = timer_object


    def quit(self):
        really_quit = messagebox.askyesno("Quiting?", "Do you really want to quit?")
        if really_quit:
            self.window.destroy()

if __name__ == "__main__":
    main()