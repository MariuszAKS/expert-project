from tkinter import Toplevel
from tkinter.ttk import Frame, Separator, Label


def show_creators(main_window):
    window = Toplevel(main_window)
    window.title('Creators')

    window.grab_set()

    frame = Frame(window, padding=(10, 10))
    frame.pack()

    Separator(frame, orient='horizontal').pack(fill='x')
    Label(frame, text='Michał Roman 205858', anchor='center', padding=(20, 5))\
        .pack(fill='x')

    Separator(frame, orient='horizontal').pack(fill='x')
    Label(frame, text='Marcin Laszczka 205839', anchor='center', padding=(20, 5))\
        .pack(fill='x')

    Separator(frame, orient='horizontal').pack(fill='x')
    Label(frame, text='Mariusz Sikora 205863', anchor='center', padding=(20, 5))\
        .pack(fill='x')

    Separator(frame, orient='horizontal').pack(fill='x')


def btn_start_pressed(year, runtime, imdb, genre):
    print('Button pressed here run logic')
    print('Selected movie:', year, runtime, imdb, genre)
