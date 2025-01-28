from tkinter import Tk, Menu, StringVar
from tkinter.ttk import Frame, Separator, Label, Radiobutton, Button, Combobox

import commands as fc
from styles import configure_styles, color_background_dark


window = Tk()
window.title('Expert Project - Movie Recommendation')
window.configure(background=color_background_dark)

styles = configure_styles()

window.grid_columnconfigure(0, weight=1, uniform='equal')
window.grid_columnconfigure(1, weight=1, uniform='equal')
window.grid_columnconfigure(2, weight=1, uniform='equal')


options_year = ['new', 'old']
options_runtime = ['long', 'average', 'short']
options_imdb = ['good', 'average', 'poor']
options_genre = ['Action', 'Crime', 'Drama']

year = StringVar(value=options_year[0])
runtime = StringVar(value=options_runtime[0])
imdb = StringVar(value=options_imdb[0])


# menu_ = Menu(window)
# help_ = Menu(menu_, tearoff=0)
# menu_.add_cascade(label='Help', menu=help_)
# help_.add_command(label='Creators', command=fc.show_creators)
#
# window.configure(menu=menu_)


menu_frame = Frame(window)
menu_frame.grid(row=0, columnspan=3, sticky='nsew')


Button(menu_frame, text='Creators', command=lambda: fc.show_creators(window)).pack(side='left', padx=(4, 0), pady=4)
# Can add more buttons - simply copy above and change text and command


year_frame = Frame(window, padding=(10, 10))
year_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

runtime_frame = Frame(window, padding=(10, 10))
runtime_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

imdb_frame = Frame(window, padding=(10, 10))
imdb_frame.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

genre_frame = Frame(window, padding=(10, 10))
genre_frame.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

result_frame = Frame(window, padding=(10, 10))
result_frame.grid(row=4, columnspan=3, padx=10, pady=10, sticky='nsew')


Label(year_frame, text='Release Year').pack(anchor='n')
Separator(year_frame, orient='horizontal').pack(anchor='nw', fill='x', pady=10)

Label(runtime_frame, text='Runtime').pack(anchor='n')
Separator(runtime_frame, orient='horizontal').pack(anchor='nw', fill='x', pady=10)

Label(imdb_frame, text='Imdb rating').pack(anchor='n')
Separator(imdb_frame, orient='horizontal').pack(anchor='nw', fill='x', pady=10)


for opt in options_year:
    Radiobutton(year_frame, text=opt.capitalize(), variable=year, value=opt).pack(anchor='nw')
for opt in options_runtime:
    Radiobutton(runtime_frame, text=opt.capitalize(), variable=runtime, value=opt).pack(anchor='nw')
for opt in options_imdb:
    Radiobutton(imdb_frame, text=opt.capitalize(), variable=imdb, value=opt).pack(anchor='nw')


Label(genre_frame, text='Genre').pack(anchor='n')
Separator(genre_frame, orient='horizontal').pack(anchor='nw', fill='x', pady=10)

genre_combo = Combobox(genre_frame, state='readonly', values=options_genre)
genre_combo.pack(anchor='nw')
genre_combo.set(options_genre[0])


Button(window, text='Recommend a movie',
       command=lambda: fc.btn_start_pressed(year.get(), runtime.get(), imdb.get(), genre_combo.get())
       ).grid(row=3, column=1)


Label(result_frame, text='The title of Movie no.1').pack(anchor='w')
Label(result_frame, text='The title of Movie no.2').pack(anchor='w')
Label(result_frame, text='The title of Movie no.3').pack(anchor='w')


window.mainloop()
