from tkinter.ttk import Style


color_background_dark = '#123524'
color_background_light = '#3E7B27'
color_font = '#EFE3C2'


def configure_styles():
    style = Style()

    style.configure('TFrame',
                    background=color_background_light,
                    relief='raised',
                    borderwidth=2)

    style.configure('TLabel',
                    background=color_background_light,
                    foreground=color_font,
                    font=('Arial', 12, 'bold'))

    style.configure('TRadiobutton',
                    background=color_background_light,
                    foreground=color_font,
                    font=('Arial', 8, 'normal'))

    # style.configure('TCombobox',
    #                 selectbackground=color_background_light,
    #                 fieldbackground=color_background_light,
    #                 background=color_background_light,
    #                 font=('Arial', 8, 'normal'))

    return style
