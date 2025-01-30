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


def btn_start_pressed(window, movies, year, runtime, imdb, genre):
    movie_titles = run_engine(year, runtime, imdb, genre)

    for i in range(len(movies)):
        movies[i].set('-')

    for i in range(min(len(movie_titles), len(movies))):
        movies[i].set(movie_titles[i])
