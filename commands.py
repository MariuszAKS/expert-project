from tkinter import Toplevel
from tkinter.ttk import Frame, Separator, Label
from expert_system import run_engine


def show_creators(main_window):
    window = Toplevel(main_window)
    window.title('Creators')

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

    window.grab_set()


def btn_start_pressed(runtimes, titles, years, year, runtime, imdb, genre):
    movie_runtimes, movie_titles, movie_years = run_engine(year, runtime, imdb, genre)

    for i in range(3):
        runtimes[i].set('-')
        titles[i].set('-')
        years[i].set('-')

    for i in range(min(len(movie_titles), len(movie_titles))):
        runtimes[i].set(movie_runtimes[i])
        titles[i].set(movie_titles[i])
        years[i].set(movie_years[i])
