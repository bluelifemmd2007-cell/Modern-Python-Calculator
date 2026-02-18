import tkinter as tk
from app.operations import Calculator


def run_gui():
    calc = Calculator()

    window = tk.Tk()
    window.title("Calculator")
    window.geometry("330x420")
    window.resizable(False, False)

    # رنگ‌ها
    bg = "#1e1e1e"
    fg = "#ffffff"
    accent = "#4fc3f7"
    btn_bg = "#2e2e2e"
    btn_hover = "#3c3c3c"
    entry_bg = "#2b2b2b"

    window.configure(bg=bg)

    # قاب اصلی
    main_frame = tk.Frame(window, bg=bg)
    main_frame.pack(fill="both", expand=True)

    # ورودی‌ها
    tk.Label(main_frame, text="Number A:", fg=fg, bg=bg, font=("Segoe UI", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_a = tk.Entry(main_frame, font=("Segoe UI", 14), bg=entry_bg, fg=fg, insertbackground=fg, relief="flat")
    entry_a.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(main_frame, text="Number B:", fg=fg, bg=bg, font=("Segoe UI", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_b = tk.Entry(main_frame, font=("Segoe UI", 14), bg=entry_bg, fg=fg, insertbackground=fg, relief="flat")
    entry_b.grid(row=1, column=1, padx=10, pady=10)

    # نتیجه
    result_label = tk.Label(main_frame, text="Result:", fg=accent, bg=bg, font=("Segoe UI", 14, "bold"))
    result_label.grid(row=2, column=0, columnspan=2, pady=20)

    def show_result(value):
        result_label.config(text=f"Result: {value}")

    def get_values():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            return a, b
        except ValueError:
            show_result("Invalid input")
            return None, None

    def do_add():
        a, b = get_values()
        if a is not None:
            show_result(calc.add(a, b))

    def do_sub():
        a, b = get_values()
        if a is not None:
            show_result(calc.subtract(a, b))

    def do_mul():
        a, b = get_values()
        if a is not None:
            show_result(calc.multiply(a, b))

    def do_div():
        a, b = get_values()
        if a is not None:
            try:
                show_result(calc.divide(a, b))
            except ValueError:
                show_result("Cannot divide by zero")

    # تابع ساخت دکمه با رنگ واقعی
    def make_button(text, command, row, col):
        btn = tk.Label(main_frame, text=text, bg=btn_bg, fg=fg,
                       font=("Segoe UI", 12), width=12, height=2, bd=0)
        btn.grid(row=row, column=col, padx=10, pady=10)

        # هاور
        btn.bind("<Enter>", lambda e: btn.config(bg=btn_hover))
        btn.bind("<Leave>", lambda e: btn.config(bg=btn_bg))

        # کلیک
        btn.bind("<Button-1>", lambda e: command())

    make_button("Add", do_add, 3, 0)
    make_button("Subtract", do_sub, 3, 1)
    make_button("Multiply", do_mul, 4, 0)
    make_button("Divide", do_div, 4, 1)

    window.mainloop()
