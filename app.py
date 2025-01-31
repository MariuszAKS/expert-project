import tkinter
from tkinter import Tk, StringVar  # Menu
from tkinter.ttk import Frame, Separator, Label, Radiobutton, Button, Combobox

import commands as com
from styles import configure_styles, color_background_dark


class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Expert Project - Movie Recommendation')
        self.configure(background=color_background_dark)

        configure_styles()

        self.grid_columnconfigure(0, weight=1, uniform='equal')
        self.grid_columnconfigure(1, weight=1, uniform='equal')
        self.grid_columnconfigure(2, weight=1, uniform='equal')

        options_year = ['new', 'old']
        options_runtime = ['long', 'average', 'short']
        options_imdb = ['good', 'average', 'poor']
        options_genre = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Drama', 'Family',
                         'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance',
                         'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']

        year = StringVar(value=options_year[0])
        runtime = StringVar(value=options_runtime[0])
        imdb = StringVar(value=options_imdb[0])

        titles = [StringVar(value='-'), StringVar(value='-'), StringVar(value='-')]
        runtimes = [StringVar(value='-'), StringVar(value='-'), StringVar(value='-')]
        years = [StringVar(value='-'), StringVar(value='-'), StringVar(value='-')]

        menu_frame = Frame(self)
        menu_frame.grid(row=0, columnspan=3, sticky='nsew')

        Button(menu_frame, text='Creators', command=lambda: com.show_creators(self)).pack(side='left',
                                                                                          padx=(4, 0),
                                                                                          pady=4)
        # Can add more buttons - simply copy above and change text and command

        # Frames
        year_frame = Frame(self, padding=(10, 10))
        year_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        runtime_frame = Frame(self, padding=(10, 10))
        runtime_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

        imdb_frame = Frame(self, padding=(10, 10))
        imdb_frame.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

        genre_frame = Frame(self, padding=(10, 10))
        genre_frame.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

        result_frame = Frame(self, padding=(10, 10))
        result_frame.grid(row=4, columnspan=3, padx=10, pady=10, sticky='nsew')

        result_frame.grid_columnconfigure(0, weight=30, uniform='equal')
        result_frame.grid_columnconfigure(1, weight=1, uniform='equal')
        result_frame.grid_columnconfigure(2, weight=9, uniform='equal')
        result_frame.grid_columnconfigure(3, weight=1, uniform='equal')
        result_frame.grid_columnconfigure(4, weight=9, uniform='equal')

        result_title_frame = Frame(result_frame, style='Borderless.TFrame')
        result_title_frame.grid(row=0, column=0, sticky='ew')

        Separator(result_frame, orient='vertical').grid(row=0, column=1, sticky='ns')

        result_year_frame = Frame(result_frame, style='Borderless.TFrame')
        result_year_frame.grid(row=0, column=2, sticky='ew')

        Separator(result_frame, orient='vertical').grid(row=0, column=3, sticky='ns')

        result_runtime_frame = Frame(result_frame, style='Borderless.TFrame')
        result_runtime_frame.grid(row=0, column=4, sticky='ew')

        # Section Labels
        Label(year_frame, text='Release Year').pack(anchor='n')
        Separator(year_frame, orient='horizontal').pack(anchor='nw', fill='x', pady=10)

        Label(runtime_frame, text='Runtime').pack(anchor='n')
        Separator(runtime_frame, orient='horizontal').pack(anchor='nw', fill='x', pady=10)

        Label(imdb_frame, text='Imdb rating').pack(anchor='n')
        Separator(imdb_frame, orient='horizontal').pack(anchor='nw', fill='x', pady=10)

        # Section RadioButtons
        for opt in options_year:
            Radiobutton(year_frame, text=opt.capitalize(), variable=year, value=opt).pack(anchor='nw')
        for opt in options_runtime:
            Radiobutton(runtime_frame, text=opt.capitalize(), variable=runtime, value=opt).pack(anchor='nw')
        for opt in options_imdb:
            Radiobutton(imdb_frame, text=opt.capitalize(), variable=imdb, value=opt).pack(anchor='nw')

        # Genre selection
        Label(genre_frame, text='Genre').pack(anchor='n')
        Separator(genre_frame, orient='horizontal').pack(anchor='nw', fill='x', pady=10)

        genre_combo = Combobox(genre_frame, state='readonly', values=options_genre)
        genre_combo.pack(anchor='n')
        genre_combo.set(options_genre[0])

        # Recommendation Button
        Button(self, text='Recommend movies',
               command=lambda: com.btn_start_pressed(
                   runtimes, titles, years, year.get(), runtime.get(), imdb.get(), genre_combo.get())
               ).grid(row=3, column=1)

        # Result display
        Label(result_title_frame, text='Movie Title').pack()
        Label(result_year_frame, text='Release Year').pack()
        Label(result_runtime_frame, text='Runtime [min]').pack()

        Separator(result_title_frame, orient='horizontal').pack(fill='x')
        Separator(result_year_frame, orient='horizontal').pack(fill='x')
        Separator(result_runtime_frame, orient='horizontal').pack(fill='x')

        for i in range(3):
            Label(result_title_frame, textvariable=titles[i]).pack(anchor='nw')
            Label(result_year_frame, textvariable=years[i]).pack()
            Label(result_runtime_frame, textvariable=runtimes[i]).pack()
