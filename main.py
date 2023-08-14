import customtkinter as ctk
from styling import *
import os
import sys


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=BG_BORDER_COLOR)
        self.title(" Bmi Calculator")
        self.geometry("450x450+1500+300")
        self.resizable(False, False)
        self.iconbitmap(self.resource_path("files/images/logo/Logo_ico.ico"))

        # VARIABLES
        self.height_var = ctk.StringVar()
        self.slider_var = ctk.IntVar(value=198)
        self.weight_var = ctk.DoubleVar(value=60.0)
        self.unit_var = ctk.StringVar(value="Metric")

        # LAYOUT DESIGN
        # MAIN BG FRAME
        self.frame = ctk.CTkFrame(self, fg_color=BG_COLOR, corner_radius=10)
        self.frame.pack(fill="both", expand=True, pady=15, padx=15)

        # CHANGE UNIT FRAME
        ChangeUnitFrame(self)

        # RESULT FRAME
        self.result = ResultFrame(self)

        # WEIGHT FRAME
        self.weight = WeightFrame(self)

        # HEIGHT FRAME
        self.height = HeightFrame(self)

        # Comment FRAME
        self.comment = CommentFrame(self)

        # BOTTOM FRAME
        BottomFrame(self)

        self.slider_var.trace_add("write", self.calculate_bmi)
        self.weight_var.trace_add("write", self.calculate_bmi)
        self.unit_var.trace_add("write", self.calculate_bmi)

    def calculate_bmi(self, *args):
        weight = self.weight_var.get()
        height = self.slider_var.get()
        if self.unit_var.get() == "Metric":
            bmi = round(weight / (height/100) ** 2, 1)

            self.result.result_text.configure(text=str(bmi))
            meters = str(round(height / 100, 2))
            self.weight.weight_text.configure(text=f"{round(weight, 1)}kg")
            self.height.height_label.configure(text=f"{meters}m")
        else:
            weight = weight * 2.205
            height = height / 2.54
            bmi = round((weight / (height ** 2)) * 703, 1)

            self.result.result_text.configure(text=str(bmi))

            foot = str(round(height / 12, 1)).split('.')
            self.weight.weight_text.configure(text=f"{round(weight, 1)} lbs")
            self.height.height_label.configure(text=f"{foot[0]}\'{foot[1]}\"")

        self.result.result_text.configure(text=str(bmi))

        if bmi < 18.5:
            self.comment.comment_text.configure(text="Underweight")
        elif 18.5 <= bmi <= 24.9:
            self.comment.comment_text.configure(text="Healthy Weight")
        elif 25.0 <= bmi <= 29.9:
            self.comment.comment_text.configure(text="Overweight")
        else:
            self.comment.comment_text.configure(text="Obesity")

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)


class WeightFrame(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(master=parent.frame, fg_color=BG_BORDER_COLOR)
        self.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.15)
        self.parent = parent

        self.columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="c")
        self.rowconfigure(0, weight=1, uniform="c")

        # LARGE MINUS BUTTON
        self.large_minus_btn = ctk.CTkButton(self, text="-", text_color=TEXT_COLOR, font=MINUS_LARGE, fg_color=BG_COLOR,
                                             hover_color=BUTTON_HOVER_COLOR,
                                             command=lambda value=-1: self.update_weight(value=value))
        self.large_minus_btn.grid(column=0, row=0, pady=5, padx=5, sticky="news")

        # SMALL MINUS BUTTON
        self.small_minus_btn = ctk.CTkButton(self, text="-", text_color=TEXT_COLOR, font=MINUS_SMALL, fg_color=BG_COLOR,
                                             hover_color=BUTTON_HOVER_COLOR,
                                             command=lambda value=-0.1: self.update_weight(value=value))
        self.small_minus_btn.grid(column=1, row=0, pady=5, padx=5, sticky="we")

        # LARGE PLUS BUTTON
        self.large_plus_btn = ctk.CTkButton(self, text="+", text_color=TEXT_COLOR, font=MINUS_LARGE, fg_color=BG_COLOR,
                                            hover_color=BUTTON_HOVER_COLOR,
                                            command=lambda value=1: self.update_weight(value=value))
        self.large_plus_btn.grid(column=5, row=0, pady=5, padx=5, sticky="news")

        # SMALL PLUS BUTTON
        self.small_plus_btn = ctk.CTkButton(self, text="+", text_color=TEXT_COLOR, font=MINUS_SMALL, fg_color=BG_COLOR,
                                            hover_color=BUTTON_HOVER_COLOR,
                                            command=lambda value=0.1: self.update_weight(value=value))
        self.small_plus_btn.grid(column=4, row=0, pady=5, padx=5, sticky="we")

        # WEIGHT TEXT
        self.weight_text = ctk.CTkLabel(self, text="60.0kg", text_color=TEXT_COLOR, font=WEIGHT_FONT, fg_color=BG_COLOR)
        self.weight_text.grid(column=2, columnspan=2, row=0, pady=5, padx=5, sticky="news")

    def update_weight(self, value):
        weight = self.parent.weight_var.get() + value
        self.parent.weight_var.set(weight)


class HeightFrame(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(master=parent.frame, fg_color=BG_BORDER_COLOR)
        self.place(relx=0.05, rely=0.72, relwidth=0.9, relheight=0.15)
        self.parent = parent

        self.height_label = ctk.CTkLabel(self, text="1.98m", font=HEIGHT_FONT, text_color=TEXT_COLOR)
        self.height_label.pack(side="right", padx=5, pady=5)

        self.height_slider = ctk.CTkSlider(self, width=300, progress_color=TEXT_COLOR, fg_color=BG_COLOR,
                                           button_color=TEXT_COLOR, button_hover_color=BUTTON_HOVER_COLOR,
                                           from_=100, to=280, command=self.update_height,
                                           variable=self.parent.slider_var)
        self.height_slider.pack(side="left", padx=5, pady=5)

    def update_height(self, *args):
        slider_value = str(self.parent.slider_var.get())
        height = f"{slider_value[0]}.{slider_value[1:3]}m"
        self.parent.height_var.set(value=height)


class ResultFrame(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(master=parent.frame, fg_color=BG_COLOR)
        self.place(relx=0.05, rely=0.12, relwidth=0.9, relheight=0.4)

        self.result_text = ctk.CTkLabel(self, text="15.3", font=RESULT_FONT, text_color=TEXT_COLOR)
        self.result_text.pack(padx=2, pady=2)


class CommentFrame(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(master=parent.frame, fg_color=BG_COLOR)
        self.place(relx=0.05, rely=0.889, relwidth=0.9, relheight=0.05)

        self.comment_text = ctk.CTkLabel(self, text="Underweight", font=COMMENT_FONT, text_color=TEXT_COLOR)
        self.comment_text.pack(padx=2, pady=2)


class BottomFrame(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(master=parent.frame, fg_color=BG_COLOR)
        self.place(relx=0.05, rely=0.95, relwidth=0.9, relheight=0.05)

        self.bottom_text = ctk.CTkLabel(self, text="Designed by Amos @PythonDecorator",
                                        font=BOTTOM_FONT, text_color=BOTTOM_TEXT_COLOR)
        self.bottom_text.pack(padx=2, pady=2)


class ChangeUnitFrame(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(master=parent.frame, fg_color=BG_COLOR)
        self.place(relx=0.05, rely=0.03, relwidth=0.9, relheight=0.05)

        self.parent = parent

        self.change_unit_menu = ctk.CTkOptionMenu(self, width=50, values=["Metric", "Imperial"],
                                                  bg_color=BG_COLOR, fg_color=BG_COLOR,
                                                  dropdown_hover_color=BUTTON_HOVER_COLOR, font=CHANGE_UINT_FONT,
                                                  dropdown_fg_color=BG_BORDER_COLOR, dropdown_font=CHANGE_UINT_FONT,
                                                  text_color=TEXT_COLOR, dropdown_text_color=TEXT_COLOR,
                                                  variable=self.parent.unit_var,
                                                  button_hover_color=BUTTON_HOVER_COLOR)
        self.change_unit_menu.pack(side="right", padx=2, pady=2)


if __name__ == "__main__":
    app = App()
    app.mainloop()
