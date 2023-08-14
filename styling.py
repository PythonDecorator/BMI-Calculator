# from ctypes import windll, byref, sizeof, c_int

# FONTS
RESULT_FONT = ("Roboto Slab", 156, "bold")
CHANGE_UINT_FONT = ("Roboto Slab", 11, "normal")
WEIGHT_FONT = ("Roboto Slab", 28, "normal")
HEIGHT_FONT = ("Roboto Slab", 25, "normal")
PLUS_LARGE = ("Roboto Slab", 30, "normal")
PLUS_SMALL = ("Roboto Slab", 18, "normal")
MINUS_LARGE = ("Roboto Slab", 35, "normal")
MINUS_SMALL = ("Roboto Slab", 22, "normal")
BOTTOM_FONT = ("Roboto Slab", 11, "normal")
COMMENT_FONT = ("Roboto Slab", 14, "normal")

# COLORS
BG_BORDER_COLOR = "#04293A"
BG_COLOR = "#064663"
TEXT_COLOR = "#ECB365"
BOTTOM_TEXT_COLOR = "#000000"
BUTTON_HOVER_COLOR = "#057F9B"
COMMENT_COLOR = "#ED9E48"


# def change_title_bar_color(app):
#     hwnd = windll.user32.GetParent(app.winfo_id())
#     dwmwa_attribute = 35
#     color = 0x00FFFFFF
#     windll.dwmapi.DwmSetWindowAttribute(hwnd, dwmwa_attribute, byref(c_int(color)), sizeof(c_int))
