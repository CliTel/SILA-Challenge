def apply_dark_theme(app):
    app.root.configure(bg="#1e1e1e")
    app.display.configure(bg="#2d2d2d", fg="white", insertbackground="white")
    app.history.configure(bg="#2d2d2d", fg="white")


def apply_light_theme(app):
    app.root.configure(bg="white")
    app.display.configure(bg="white", fg="black", insertbackground="black")
    app.history.configure(bg="white", fg="black")