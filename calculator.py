
import tkinter as tk
from tkinter import ttk
import math
from datetime import datetime, date

# ─────────────────────────────────────────────────────────────────────────────
#  THEME PALETTES
# ─────────────────────────────────────────────────────────────────────────────
THEMES = {
    "light": {
        "root_bg":           "#f3f3f3",
        "header_bg":         "#f3f3f3",
        "header_fg":         "#000000",
        "header_btn_bg":     "#f3f3f3",
        "header_btn_fg":     "#000000",
        "header_btn_active": "#e0e0e0",
        "display_bg":        "#f3f3f3",
        "history_fg":        "#666666",
        "result_fg":         "#000000",
        "btn_num_bg":        "#ffffff",
        "btn_op_bg":         "#f0f0f0",
        "btn_eq_bg":         "#85b7e2",
        "btn_eq_fg":         "#ffffff",
        "btn_fg":            "#000000",
        "btn_active":        "#dcdcdc",
        "btn_sci_bg":        "#e8e8e8",
        "sidebar_bg":        "#fafafa",
        "sidebar_fg":        "#000000",
        "sidebar_hdr_fg":    "#777777",
        "sidebar_hover":     "#e8e8e8",
        "sidebar_active":    "#d0e8ff",
        "divider":           "#dddddd",
        "toggle_on":         "#85b7e2",
        "toggle_off":        "#bbbbbb",
        "input_bg":          "#ffffff",
        "input_fg":          "#000000",
        "input_border":      "#cccccc",
        "view_bg":           "#f3f3f3",
        "view_fg":           "#000000",
        "view_secondary_fg": "#555555",
        "history_panel_bg":  "#fafafa",
    },
    "dark": {
        "root_bg":           "#1e1e1e",
        "header_bg":         "#2b2b2b",
        "header_fg":         "#ffffff",
        "header_btn_bg":     "#2b2b2b",
        "header_btn_fg":     "#ffffff",
        "header_btn_active": "#3a3a3a",
        "display_bg":        "#1e1e1e",
        "history_fg":        "#aaaaaa",
        "result_fg":         "#ffffff",
        "btn_num_bg":        "#333333",
        "btn_op_bg":         "#2d2d2d",
        "btn_eq_bg":         "#1a6aad",
        "btn_eq_fg":         "#ffffff",
        "btn_fg":            "#ffffff",
        "btn_active":        "#484848",
        "btn_sci_bg":        "#383838",
        "sidebar_bg":        "#252525",
        "sidebar_fg":        "#eeeeee",
        "sidebar_hdr_fg":    "#888888",
        "sidebar_hover":     "#333333",
        "sidebar_active":    "#1a3a5c",
        "divider":           "#3a3a3a",
        "toggle_on":         "#1a6aad",
        "toggle_off":        "#555555",
        "input_bg":          "#2d2d2d",
        "input_fg":          "#ffffff",
        "input_border":      "#555555",
        "view_bg":           "#1e1e1e",
        "view_fg":           "#ffffff",
        "view_secondary_fg": "#aaaaaa",
        "history_panel_bg":  "#252525",
    },
}

# ─────────────────────────────────────────────────────────────────────────────
#  CONVERTER DATA
# ─────────────────────────────────────────────────────────────────────────────
CONVERTER_UNITS = {
    "Currency":        ["USD","EUR","GBP","JPY","INR","CAD","AUD","CHF","CNY"],
    "Volume":          ["Liter","Milliliter","Gallon (US)","Quart","Pint","Cup","Fluid Ounce","Cubic Meter","Cubic Inch"],
    "Length":          ["Meter","Kilometer","Centimeter","Millimeter","Mile","Yard","Foot","Inch","Nautical Mile"],
    "Weight and Mass": ["Kilogram","Gram","Milligram","Pound","Ounce","Ton (metric)","Stone"],
    "Temperature":     ["Celsius","Fahrenheit","Kelvin"],
    "Energy":          ["Joule","Kilojoule","Calorie","Kilocalorie","Watt-hour","Kilowatt-hour","BTU","Electronvolt"],
    "Area":            ["Square Meter","Square Kilometer","Square Mile","Square Yard","Square Foot","Square Inch","Hectare","Acre"],
    "Speed":           ["m/s","km/h","mph","knot","ft/s"],
    "Time":            ["Second","Minute","Hour","Day","Week","Month","Year"],
    "Power":           ["Watt","Kilowatt","Megawatt","Horsepower","BTU/hour"],
    "Data":            ["Bit","Byte","Kilobyte","Megabyte","Gigabyte","Terabyte","Petabyte"],
    "Pressure":        ["Pascal","Kilopascal","Bar","PSI","Atmosphere","mmHg","Torr"],
    "Angle":           ["Degree","Radian","Gradian","Minute of arc","Second of arc"],
}

CONVERTER_FACTORS = {
    "Volume":     {"Liter":1,"Milliliter":0.001,"Gallon (US)":3.78541,"Quart":0.946353,"Pint":0.473176,
                   "Cup":0.24,"Fluid Ounce":0.0295735,"Cubic Meter":1000,"Cubic Inch":0.0163871},
    "Length":     {"Meter":1,"Kilometer":1000,"Centimeter":0.01,"Millimeter":0.001,"Mile":1609.34,
                   "Yard":0.9144,"Foot":0.3048,"Inch":0.0254,"Nautical Mile":1852},
    "Weight and Mass": {"Kilogram":1,"Gram":0.001,"Milligram":0.000001,"Pound":0.453592,
                        "Ounce":0.0283495,"Ton (metric)":1000,"Stone":6.35029},
    "Energy":     {"Joule":1,"Kilojoule":1000,"Calorie":4.184,"Kilocalorie":4184,
                   "Watt-hour":3600,"Kilowatt-hour":3600000,"BTU":1055.06,"Electronvolt":1.602e-19},
    "Area":       {"Square Meter":1,"Square Kilometer":1e6,"Square Mile":2.59e6,"Square Yard":0.836127,
                   "Square Foot":0.092903,"Square Inch":0.00064516,"Hectare":10000,"Acre":4046.86},
    "Speed":      {"m/s":1,"km/h":0.277778,"mph":0.44704,"knot":0.514444,"ft/s":0.3048},
    "Time":       {"Second":1,"Minute":60,"Hour":3600,"Day":86400,"Week":604800,
                   "Month":2629800,"Year":31557600},
    "Power":      {"Watt":1,"Kilowatt":1000,"Megawatt":1e6,"Horsepower":745.7,"BTU/hour":0.29307},
    "Data":       {"Bit":1,"Byte":8,"Kilobyte":8000,"Megabyte":8e6,"Gigabyte":8e9,
                   "Terabyte":8e12,"Petabyte":8e15},
    "Pressure":   {"Pascal":1,"Kilopascal":1000,"Bar":100000,"PSI":6894.76,
                   "Atmosphere":101325,"mmHg":133.322,"Torr":133.322},
    "Angle":      {"Degree":1,"Radian":57.2958,"Gradian":0.9,"Minute of arc":1/60,"Second of arc":1/3600},
}
CURRENCY_RATES = {"USD":1,"EUR":0.92,"GBP":0.79,"JPY":149.5,"INR":83.1,
                  "CAD":1.36,"AUD":1.53,"CHF":0.89,"CNY":7.24}


def convert_value(category, from_unit, to_unit, value):
    try:
        val = float(value)
    except ValueError:
        return "Invalid"
    if category == "Temperature":
        if from_unit == to_unit:
            return f"{val:.6g}"
        to_c   = {"Celsius":lambda x:x, "Fahrenheit":lambda x:(x-32)*5/9, "Kelvin":lambda x:x-273.15}
        from_c = {"Celsius":lambda x:x, "Fahrenheit":lambda x:x*9/5+32,   "Kelvin":lambda x:x+273.15}
        return f"{from_c[to_unit](to_c[from_unit](val)):.6g}"
    if category == "Currency":
        return f"{(val / CURRENCY_RATES[from_unit]) * CURRENCY_RATES[to_unit]:.4f}"
    factors = CONVERTER_FACTORS.get(category, {})
    if from_unit not in factors or to_unit not in factors:
        return "N/A"
    return f"{val * factors[from_unit] / factors[to_unit]:.6g}"


def draw_rounded_rect(canvas, x1, y1, x2, y2, r, **kw):
    for ax, ay, start in [(x1,y1,90),(x2-2*r,y1,0),(x1,y2-2*r,180),(x2-2*r,y2-2*r,270)]:
        canvas.create_arc(ax, ay, ax+2*r, ay+2*r, start=start, extent=90, style="pieslice", **kw)
    canvas.create_rectangle(x1+r, y1,   x2-r, y2,   **kw)
    canvas.create_rectangle(x1,   y1+r, x2,   y2-r, **kw)


# ─────────────────────────────────────────────────────────────────────────────
#  MAIN APP
# ─────────────────────────────────────────────────────────────────────────────
class CalculatorApp:
    SIDEBAR_W = 255

    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("360x600")
        self.root.minsize(320, 520)

        self.theme        = "light"
        self.sidebar_open = False
        self.history_open = False
        self.history_list = []
        self.active_view  = "Standard"
        self.std_expr     = ""
        self._sci_expr    = ""
        self._prog_val    = 0
        self._prog_op     = None
        self._prog_first  = 0
        self._prog_new    = True

        self._build_skeleton()
        self._build_sidebar()
        self._build_history_panel()
        self._build_all_views()
        self._switch_view("Standard", apply_theme=False)
        self._apply_theme()

        # FIX: only respond to root-window resize, not every child Configure
        self.root.bind("<Configure>", self._on_root_configure)
        self._last_root_size = (0, 0)

    # ══════════════════════════════════════════════════════════════════════
    #  SKELETON
    # ══════════════════════════════════════════════════════════════════════
    def _build_skeleton(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # Header
        self.header = tk.Frame(self.root, height=46)
        self.header.grid(row=0, column=0, sticky="ew")
        self.header.columnconfigure(1, weight=1)
        self.header.grid_propagate(False)

        self.btn_hamburger = tk.Button(
            self.header, text="☰", font=("Segoe UI", 17),
            relief="flat", bd=0, cursor="hand2", width=3,
            command=self._toggle_sidebar)
        self.btn_hamburger.grid(row=0, column=0, sticky="ns", padx=4)

        self.lbl_mode = tk.Label(
            self.header, text="Standard",
            font=("Segoe UI", 13, "bold"), anchor="w")
        self.lbl_mode.grid(row=0, column=1, sticky="ew", padx=6)

        self.btn_history = tk.Button(
            self.header, text="📜", font=("Segoe UI", 15),
            relief="flat", bd=0, cursor="hand2", width=3,
            command=self._toggle_history)
        self.btn_history.grid(row=0, column=2, sticky="ns", padx=4)

        # Content area — all views live here
        self.content = tk.Frame(self.root)
        self.content.grid(row=1, column=0, sticky="nsew")
        self.content.columnconfigure(0, weight=1)
        self.content.rowconfigure(0, weight=1)

        # ── FIX: overlay is a transparent click-catcher, NOT black ────────
        # We use a 1×1 invisible frame; visibility is handled by place()
        # Its only job is to intercept clicks outside the sidebar.
        # We deliberately do NOT set bg here — it will be set to the current
        # root_bg in _apply_theme so it is always invisible.
        self.overlay = tk.Frame(self.root)
        self.overlay.place_forget()
        self.overlay.bind("<Button-1>", lambda e: self._close_all_panels())

        # Sidebar and history shells (children of root, placed on top)
        self.sidebar    = tk.Frame(self.root, width=self.SIDEBAR_W)
        self.hist_panel = tk.Frame(self.root, width=self.SIDEBAR_W)
        self.sidebar.place_forget()
        self.hist_panel.place_forget()
        self.sidebar.pack_propagate(False)
        self.hist_panel.pack_propagate(False)

    # ══════════════════════════════════════════════════════════════════════
    #  SCROLLABLE SIDEBAR
    # ══════════════════════════════════════════════════════════════════════
    def _build_sidebar(self):
        sb = self.sidebar

        # Fixed header
        self.sb_header = tk.Frame(sb)
        self.sb_header.pack(side="top", fill="x")

        self.sb_title = tk.Label(
            self.sb_header, text="Calculator",
            font=("Segoe UI", 14, "bold"), anchor="w", padx=14, pady=12)
        self.sb_title.pack(side="left", fill="x", expand=True)

        self.sb_close_btn = tk.Button(
            self.sb_header, text="✕", font=("Segoe UI", 11),
            relief="flat", bd=0, cursor="hand2",
            command=self._close_all_panels)
        self.sb_close_btn.pack(side="right", padx=8)

        # Fixed footer (packed to bottom BEFORE scrollable area)
        self.sb_footer = tk.Frame(sb)
        self.sb_footer.pack(side="bottom", fill="x")

        self.sb_footer_divider = tk.Frame(self.sb_footer, height=1)
        self.sb_footer_divider.pack(fill="x", padx=10, pady=3)

        self.sb_footer_row = tk.Frame(self.sb_footer, padx=14, pady=10)
        self.sb_footer_row.pack(fill="x")

        self.sb_theme_lbl = tk.Label(
            self.sb_footer_row, text="Dark Mode",
            font=("Segoe UI", 11), anchor="w")
        self.sb_theme_lbl.pack(side="left")

        self.toggle_canvas = tk.Canvas(
            self.sb_footer_row, width=48, height=26,
            bd=0, highlightthickness=0, cursor="hand2")
        self.toggle_canvas.pack(side="right")
        self.toggle_canvas.bind("<Button-1>", lambda e: self._toggle_theme())

        # Scrollable middle (between header and footer)
        scroll_outer = tk.Frame(sb)
        scroll_outer.pack(side="top", fill="both", expand=True)

        self.sb_scrollbar = tk.Scrollbar(scroll_outer, orient="vertical")
        self.sb_scrollbar.pack(side="right", fill="y")

        self.sb_canvas = tk.Canvas(
            scroll_outer, highlightthickness=0, bd=0,
            yscrollcommand=self.sb_scrollbar.set)
        self.sb_canvas.pack(side="left", fill="both", expand=True)
        self.sb_scrollbar.config(command=self.sb_canvas.yview)

        self.sb_inner = tk.Frame(self.sb_canvas)
        self.sb_canvas_window = self.sb_canvas.create_window(
            (0, 0), window=self.sb_inner, anchor="nw")

        self.sb_inner.bind("<Configure>", self._on_sb_inner_configure)
        self.sb_canvas.bind("<Configure>", self._on_sb_canvas_configure)
        # Mousewheel — only scroll when sidebar is actually open
        self.root.bind("<MouseWheel>", self._on_mousewheel)
        self.root.bind("<Button-4>",   self._on_mousewheel)
        self.root.bind("<Button-5>",   self._on_mousewheel)

        # Populate menu items
        self.sb_item_widgets  = []
        self.sb_section_labels = []
        self.sb_dividers       = []

        def section(text):
            lbl = tk.Label(self.sb_inner, text=text.upper(),
                           font=("Segoe UI", 8, "bold"), anchor="w",
                           padx=14, pady=6)
            lbl.pack(fill="x")
            self.sb_section_labels.append(lbl)

        def item(icon, label, cmd):
            row = tk.Frame(self.sb_inner, cursor="hand2")
            row.pack(fill="x")
            lbl = tk.Label(row, text=f"  {icon}  {label}",
                           font=("Segoe UI", 11), anchor="w",
                           padx=8, pady=8)
            lbl.pack(fill="x")
            for w in (row, lbl):
                w.bind("<Button-1>", lambda e, c=cmd: c())
                w.bind("<Enter>",    lambda e, r=row: self._sb_hover(r, True))
                w.bind("<Leave>",    lambda e, r=row: self._sb_hover(r, False))
            self.sb_item_widgets.append((row, lbl))

        def div():
            d = tk.Frame(self.sb_inner, height=1)
            d.pack(fill="x", padx=10, pady=3)
            self.sb_dividers.append(d)

        section("Calculator")
        for icon, name in [("🖩","Standard"),("📐","Scientific"),
                            ("📈","Graphing"),("💻","Programmer"),
                            ("📅","Date Calculation")]:
            item(icon, name, lambda n=name: self._select_mode(n))
        div()
        section("Converter")
        conv_icons = {
            "Currency":"💱","Volume":"🧪","Length":"📏",
            "Weight and Mass":"⚖️","Temperature":"🌡️","Energy":"⚡",
            "Area":"🗺️","Speed":"🚀","Time":"⏱️","Power":"🔌",
            "Data":"💾","Pressure":"🔵","Angle":"📐",
        }
        for name, icon in conv_icons.items():
            item(icon, name, lambda n=name: self._select_mode(n))

    def _on_sb_inner_configure(self, event=None):
        self.sb_canvas.configure(scrollregion=self.sb_canvas.bbox("all"))

    def _on_sb_canvas_configure(self, event=None):
        self.sb_canvas.itemconfig(self.sb_canvas_window, width=event.width)

    def _on_mousewheel(self, event):
        if not self.sidebar_open:
            return
        if event.num == 4:
            self.sb_canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.sb_canvas.yview_scroll(1, "units")
        else:
            self.sb_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _sb_hover(self, row, on):
        t = THEMES[self.theme]
        col = t["sidebar_hover"] if on else t["sidebar_bg"]
        row.configure(bg=col)
        for c in row.winfo_children():
            try:
                c.configure(bg=col)
            except Exception:
                pass

    # ══════════════════════════════════════════════════════════════════════
    #  HISTORY PANEL
    # ══════════════════════════════════════════════════════════════════════
    def _build_history_panel(self):
        hp = self.hist_panel

        hdr = tk.Frame(hp)
        hdr.pack(fill="x", padx=10, pady=8)
        self.hist_title = tk.Label(
            hdr, text="History", font=("Segoe UI", 14, "bold"), anchor="w")
        self.hist_title.pack(side="left")
        self.hist_close_btn = tk.Button(
            hdr, text="✕", font=("Segoe UI", 12),
            relief="flat", bd=0, cursor="hand2",
            command=self._close_all_panels)
        self.hist_close_btn.pack(side="right")

        scroll_frame = tk.Frame(hp)
        scroll_frame.pack(fill="both", expand=True, padx=6)

        self.hist_sb_widget = tk.Scrollbar(scroll_frame, orient="vertical")
        self.hist_sb_widget.pack(side="right", fill="y")

        self.hist_canvas = tk.Canvas(
            scroll_frame, highlightthickness=0, bd=0,
            yscrollcommand=self.hist_sb_widget.set)
        self.hist_canvas.pack(side="left", fill="both", expand=True)
        self.hist_sb_widget.config(command=self.hist_canvas.yview)

        self.hist_inner = tk.Frame(self.hist_canvas)
        self._hist_win = self.hist_canvas.create_window(
            (0, 0), window=self.hist_inner, anchor="nw")
        self.hist_inner.bind("<Configure>",
            lambda e: self.hist_canvas.configure(
                scrollregion=self.hist_canvas.bbox("all")))
        self.hist_canvas.bind("<Configure>",
            lambda e: self.hist_canvas.itemconfig(self._hist_win, width=e.width))

    def _refresh_history(self):
        t = THEMES[self.theme]
        for w in self.hist_inner.winfo_children():
            w.destroy()
        bg = t["history_panel_bg"]
        self.hist_inner.configure(bg=bg)
        self.hist_canvas.configure(bg=bg)
        if not self.history_list:
            tk.Label(self.hist_inner, text="No history yet.",
                     font=("Segoe UI", 11),
                     fg=t["sidebar_hdr_fg"], bg=bg).pack(pady=20)
            return
        for expr, result in reversed(self.history_list[-40:]):
            f = tk.Frame(self.hist_inner, bg=bg)
            f.pack(fill="x", pady=2, padx=4)
            tk.Label(f, text=expr, font=("Segoe UI", 9),
                     fg=t["sidebar_hdr_fg"], bg=bg,
                     anchor="e", wraplength=220).pack(fill="x")
            tk.Label(f, text=result, font=("Segoe UI", 15, "bold"),
                     fg=t["sidebar_fg"], bg=bg, anchor="e").pack(fill="x")
            tk.Frame(f, height=1, bg=t["divider"]).pack(fill="x", pady=2)

    # ══════════════════════════════════════════════════════════════════════
    #  VIEW MANAGER
    # ══════════════════════════════════════════════════════════════════════
    def _build_all_views(self):
        self.views = {}
        self._build_standard_view()
        self._build_scientific_view()
        self._build_graphing_view()
        self._build_programmer_view()
        self._build_date_view()
        for name in CONVERTER_UNITS:
            self._build_converter_view(name)

    def _switch_view(self, name, apply_theme=True):
        for v in self.views.values():
            v["frame"].grid_remove()
        self.views[name]["frame"].grid(row=0, column=0, sticky="nsew")
        self.active_view = name
        self.lbl_mode.config(text=name)
        # FIX: don't call _apply_theme() here — it causes black-flash.
        # Theme is already applied globally; just repaint this view's buttons.
        if apply_theme:
            self._repaint_view(name)

    def _select_mode(self, name):
        self._switch_view(name)
        self._close_all_panels()

    # ══════════════════════════════════════════════════════════════════════
    #  PANEL SHOW / HIDE
    # ══════════════════════════════════════════════════════════════════════
    def _toggle_sidebar(self):
        if self.sidebar_open:
            self._close_all_panels()
        else:
            self._open_sidebar()

    def _toggle_history(self):
        if self.history_open:
            self._close_all_panels()
        else:
            self._open_history()

    def _open_sidebar(self):
        self.history_open = False
        self.hist_panel.place_forget()
        self.sidebar_open = True
        self._place_panels()

    def _open_history(self):
        self.sidebar_open = False
        self.sidebar.place_forget()
        self.history_open = True
        self._refresh_history()
        self._place_panels()

    def _place_panels(self):
        """Position overlay + sidebar/history on top of the content area."""
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()

        # FIX: overlay matches the current theme background so it looks like
        # a very slight dim — NOT solid black. It sits above content but
        # below the sidebar, acting only as a click-catcher.
        t = THEMES[self.theme]
        self.overlay.configure(bg=t["root_bg"])
        self.overlay.place(x=0, y=0, width=w, height=h)

        if self.sidebar_open:
            self.sidebar.place(x=0, y=0, width=self.SIDEBAR_W, height=h)

        if self.history_open:
            self.hist_panel.place(
                x=max(0, w - self.SIDEBAR_W), y=0,
                width=self.SIDEBAR_W, height=h)

        # Stacking order: overlay above content, panel above overlay
        self.overlay.lift()
        if self.sidebar_open:
            self.sidebar.lift()
        if self.history_open:
            self.hist_panel.lift()

    def _close_all_panels(self):
        self.sidebar_open = False
        self.history_open = False
        self.sidebar.place_forget()
        self.hist_panel.place_forget()
        self.overlay.place_forget()

    # FIX: filter <Configure> to root window size changes only
    def _on_root_configure(self, event):
        if event.widget is not self.root:
            return
        new_size = (event.width, event.height)
        if new_size == self._last_root_size:
            return
        self._last_root_size = new_size
        if self.sidebar_open or self.history_open:
            self._place_panels()

    # ══════════════════════════════════════════════════════════════════════
    #  STANDARD VIEW
    # ══════════════════════════════════════════════════════════════════════
    def _build_standard_view(self):
        frame = tk.Frame(self.content)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=2)

        disp = tk.Frame(frame, padx=14, pady=6)
        disp.grid(row=0, column=0, sticky="nsew")
        disp.columnconfigure(0, weight=1)
        disp.rowconfigure(0, weight=1)
        disp.rowconfigure(1, weight=1)

        hist_lbl = tk.Label(disp, text="", anchor="e", font=("Segoe UI", 11))
        hist_lbl.grid(row=0, column=0, sticky="nsew")
        res_lbl = tk.Label(disp, text="0", anchor="e",
                           font=("Segoe UI Semibold", 34))
        res_lbl.grid(row=1, column=0, sticky="nsew")

        btn_frame = tk.Frame(frame, padx=3, pady=3)
        btn_frame.grid(row=1, column=0, sticky="nsew")
        for i in range(4): btn_frame.columnconfigure(i, weight=1)
        for i in range(6): btn_frame.rowconfigure(i, weight=1)

        layout = [
            ('%',0,0,"op"),('CE',0,1,"op"),('C',0,2,"op"),('⌫',0,3,"op"),
            ('1/x',1,0,"op"),('x²',1,1,"op"),('√x',1,2,"op"),('÷',1,3,"op"),
            ('7',2,0,"num"),('8',2,1,"num"),('9',2,2,"num"),('×',2,3,"op"),
            ('4',3,0,"num"),('5',3,1,"num"),('6',3,2,"num"),('-',3,3,"op"),
            ('1',4,0,"num"),('2',4,1,"num"),('3',4,2,"num"),('+',4,3,"op"),
            ('+/-',5,0,"num"),('0',5,1,"num"),('.',5,2,"num"),('=',5,3,"eq"),
        ]
        btns = {}
        for text, row, col, kind in layout:
            b = tk.Button(btn_frame, text=text, font=("Segoe UI", 11),
                          relief="flat",
                          command=lambda t=text: self._std_click(t))
            b.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            btns[text] = (b, kind)

        self.views["Standard"] = {
            "frame": frame, "disp": disp,
            "hist_lbl": hist_lbl, "res_lbl": res_lbl,
            "btn_frame": btn_frame, "btns": btns,
        }

    def _std_click(self, char):
        v   = self.views["Standard"]
        rl  = v["res_lbl"]
        hl  = v["hist_lbl"]
        cur = rl.cget("text")
        if char.isdigit():
            rl.config(text=char if cur in ("0","Error") else cur+char)
        elif char == ".":
            if "." not in cur and cur != "Error": rl.config(text=cur+".")
        elif char == "⌫":
            if cur != "Error": rl.config(text=cur[:-1] if len(cur)>1 else "0")
        elif char in ("CE","C"):
            rl.config(text="0")
            if char == "C": hl.config(text=""); self.std_expr=""
        elif char in ("+","-","×","÷"):
            if cur != "Error":
                op = char.replace("×","*").replace("÷","/")
                self.std_expr = f"{cur} {op} "
                hl.config(text=f"{cur} {char}"); rl.config(text="0")
        elif char in ("x²","√x","1/x","%"):
            try:
                val = float(cur)
                res = (val**2 if char=="x²" else val**0.5 if char=="√x"
                       else 1/val if char=="1/x" else val/100)
                rl.config(text=f"{res:.6g}" if not float(res).is_integer() else str(int(res)))
            except: rl.config(text="Error")
        elif char == "+/-":
            if cur != "0": rl.config(text=cur[1:] if cur.startswith("-") else "-"+cur)
        elif char == "=":
            try:
                res = eval(self.std_expr + cur)
                expr_txt = f"{hl.cget('text')} {cur} ="
                hl.config(text=expr_txt)
                rs = f"{res:.8g}" if not float(res).is_integer() else str(int(res))
                rl.config(text=rs)
                self.history_list.append((expr_txt, rs))
                self.std_expr = ""
            except: rl.config(text="Error")

    # ══════════════════════════════════════════════════════════════════════
    #  SCIENTIFIC VIEW
    # ══════════════════════════════════════════════════════════════════════
    def _build_scientific_view(self):
        frame = tk.Frame(self.content)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=3)

        disp = tk.Frame(frame, padx=14, pady=4)
        disp.grid(row=0, column=0, sticky="nsew")
        disp.columnconfigure(0, weight=1)
        hist_lbl = tk.Label(disp, text="", anchor="e", font=("Segoe UI", 10))
        hist_lbl.pack(fill="x")
        res_lbl = tk.Label(disp, text="0", anchor="e",
                           font=("Segoe UI Semibold", 28))
        res_lbl.pack(fill="x")

        btn_frame = tk.Frame(frame, padx=2, pady=2)
        btn_frame.grid(row=1, column=0, sticky="nsew")
        for i in range(5): btn_frame.columnconfigure(i, weight=1)
        for i in range(8): btn_frame.rowconfigure(i, weight=1)

        sci_layout = [
            ("sin",0,0,"sci"),("cos",0,1,"sci"),("tan",0,2,"sci"),("log",0,3,"sci"),("ln",0,4,"sci"),
            ("x²",1,0,"sci"),("x³",1,1,"sci"),("xʸ",1,2,"sci"),("√x",1,3,"sci"),("∛x",1,4,"sci"),
            ("π",2,0,"sci"),("e",2,1,"sci"),("n!",2,2,"sci"),("1/x",2,3,"sci"),("%",2,4,"op"),
            ("CE",3,0,"op"),("C",3,1,"op"),("⌫",3,2,"op"),("(",3,3,"op"),(")",3,4,"op"),
            ("7",4,0,"num"),("8",4,1,"num"),("9",4,2,"num"),("÷",4,3,"op"),("±",4,4,"op"),
            ("4",5,0,"num"),("5",5,1,"num"),("6",5,2,"num"),("×",5,3,"op"),("·10ˣ",5,4,"sci"),
            ("1",6,0,"num"),("2",6,1,"num"),("3",6,2,"num"),("-",6,3,"op"),("+",6,4,"op"),
            ("0",7,0,"num"),(".",7,1,"num"),("+/-",7,2,"num"),("=",7,3,"eq"),
        ]
        sci_btns = {}
        for text, row, col, kind in sci_layout:
            cs = 2 if text == "=" and col == 3 else 1
            b = tk.Button(btn_frame, text=text, font=("Segoe UI", 10),
                          relief="flat",
                          command=lambda t=text: self._sci_click(t))
            b.grid(row=row, column=col, columnspan=cs, sticky="nsew", padx=1, pady=1)
            sci_btns[f"{row},{col}"] = (b, kind, text)

        self.views["Scientific"] = {
            "frame": frame, "disp": disp,
            "hist_lbl": hist_lbl, "res_lbl": res_lbl,
            "btn_frame": btn_frame, "btns": sci_btns,
        }

    def _sci_click(self, char):
        v   = self.views["Scientific"]
        rl  = v["res_lbl"]
        hl  = v["hist_lbl"]
        cur = rl.cget("text")
        if char.isdigit():
            rl.config(text=char if cur in ("0","Error") else cur+char)
        elif char == ".":
            if "." not in cur and cur != "Error": rl.config(text=cur+".")
        elif char == "⌫":
            if cur != "Error": rl.config(text=cur[:-1] if len(cur)>1 else "0")
        elif char in ("CE","C"):
            rl.config(text="0"); hl.config(text=""); self._sci_expr=""
        elif char in ("+","-","×","÷"):
            op = char.replace("×","*").replace("÷","/")
            self._sci_expr = f"{cur} {op} "
            hl.config(text=f"{cur} {char}"); rl.config(text="0")
        elif char == "(":
            self._sci_expr += "("; hl.config(text=self._sci_expr)
        elif char == ")":
            self._sci_expr += cur+")"; hl.config(text=self._sci_expr); rl.config(text="0")
        elif char in ("±","+/-"):
            if cur != "0": rl.config(text=cur[1:] if cur.startswith("-") else "-"+cur)
        elif char in ("sin","cos","tan","log","ln"):
            try:
                val = float(cur)
                fns = {"sin":math.sin,"cos":math.cos,"tan":math.tan,
                       "log":math.log10,"ln":math.log}
                if char in ("sin","cos","tan"): val = math.radians(val)
                res = fns[char](val)
                hl.config(text=f"{char}({cur})")
                rl.config(text=f"{res:.8g}")
            except: rl.config(text="Error")
        elif char == "x²":
            try:
                res=float(cur)**2; hl.config(text=f"sqr({cur})")
                rl.config(text=f"{res:.8g}" if not float(res).is_integer() else str(int(res)))
            except: rl.config(text="Error")
        elif char == "x³":
            try:
                res=float(cur)**3; hl.config(text=f"cube({cur})")
                rl.config(text=f"{res:.8g}" if not float(res).is_integer() else str(int(res)))
            except: rl.config(text="Error")
        elif char == "xʸ":
            self._sci_expr = f"{cur} ** "; hl.config(text=f"{cur} ^"); rl.config(text="0")
        elif char == "√x":
            try:
                res=math.sqrt(float(cur)); hl.config(text=f"√({cur})")
                rl.config(text=f"{res:.8g}" if not float(res).is_integer() else str(int(res)))
            except: rl.config(text="Error")
        elif char == "∛x":
            try:
                res=float(cur)**(1/3); hl.config(text=f"∛({cur})")
                rl.config(text=f"{res:.8g}" if not float(res).is_integer() else str(int(res)))
            except: rl.config(text="Error")
        elif char == "π":  rl.config(text=str(math.pi))
        elif char == "e":  rl.config(text=str(math.e))
        elif char == "n!":
            try:
                res=math.factorial(int(float(cur)))
                hl.config(text=f"{cur}!"); rl.config(text=str(res))
            except: rl.config(text="Error")
        elif char == "1/x":
            try: rl.config(text=f"{1/float(cur):.8g}")
            except: rl.config(text="Error")
        elif char == "%":
            try: rl.config(text=f"{float(cur)/100:.8g}")
            except: rl.config(text="Error")
        elif char == "·10ˣ":
            self._sci_expr = f"{cur} * 10 ** "
            hl.config(text=f"{cur}×10^"); rl.config(text="0")
        elif char == "=":
            try:
                res = eval(self._sci_expr + cur)
                expr_txt = f"{hl.cget('text')} {cur} ="
                hl.config(text=expr_txt)
                rs = f"{res:.8g}" if not float(res).is_integer() else str(int(res))
                rl.config(text=rs)
                self.history_list.append((expr_txt, rs))
                self._sci_expr = ""
            except: rl.config(text="Error")

    # ══════════════════════════════════════════════════════════════════════
    #  GRAPHING VIEW
    # ══════════════════════════════════════════════════════════════════════
    def _build_graphing_view(self):
        frame = tk.Frame(self.content)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)

        tk.Label(frame, text="Graphing Calculator",
                 font=("Segoe UI", 13, "bold"), anchor="w",
                 padx=14, pady=10).grid(row=0, column=0, sticky="ew")

        inner = tk.Frame(frame, padx=14, pady=8)
        inner.grid(row=1, column=0, sticky="nsew")
        inner.columnconfigure(0, weight=1)
        inner.rowconfigure(2, weight=1)

        tk.Label(inner, text="Enter function  f(x) =",
                 font=("Segoe UI", 11), anchor="w").grid(row=0, column=0, sticky="ew")
        entry = tk.Entry(inner, font=("Segoe UI", 12), relief="flat", bd=2)
        entry.insert(0, "x**2")
        entry.grid(row=1, column=0, sticky="ew", pady=6)

        canvas = tk.Canvas(inner, highlightthickness=1,
                           highlightbackground="#cccccc")
        canvas.grid(row=2, column=0, sticky="nsew")

        def plot(*_):
            canvas.delete("all")
            w = canvas.winfo_width() or 300
            h = canvas.winfo_height() or 200
            cx, cy = w//2, h//2
            t = THEMES[self.theme]
            canvas.configure(bg=t["input_bg"])
            canvas.create_line(0,cy,w,cy, fill=t["sidebar_hdr_fg"], width=1)
            canvas.create_line(cx,0,cx,h, fill=t["sidebar_hdr_fg"], width=1)
            expr = entry.get()
            scale = 20
            pts = []
            for px in range(w):
                x = (px - cx) / scale
                try:
                    y = eval(expr, {"x":x,"math":math,
                                    "sin":math.sin,"cos":math.cos,"tan":math.tan,
                                    "sqrt":math.sqrt,"pi":math.pi,"e":math.e})
                    py = cy - y * scale
                    if -h < py < 2*h:
                        pts.append((px, py))
                except: pass
            for i in range(1, len(pts)):
                if abs(pts[i][1]-pts[i-1][1]) < h:
                    canvas.create_line(pts[i-1], pts[i], fill="#1a7abf", width=2)

        tk.Button(inner, text="Plot", font=("Segoe UI", 11),
                  relief="flat", padx=16, pady=4,
                  command=plot).grid(row=3, column=0, pady=6)
        canvas.bind("<Configure>", plot)

        self.views["Graphing"] = {"frame": frame, "btns": {}, "plot_canvas": canvas}

    # ══════════════════════════════════════════════════════════════════════
    #  PROGRAMMER VIEW
    # ══════════════════════════════════════════════════════════════════════
    def _build_programmer_view(self):
        frame = tk.Frame(self.content)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(2, weight=3)

        disp = tk.Frame(frame, padx=14, pady=8)
        disp.grid(row=0, column=0, sticky="nsew")
        disp.columnconfigure(1, weight=1)

        self._prog_base = tk.StringVar(value="DEC")
        self._prog_displays = {}
        for i, key in enumerate(["HEX","DEC","OCT","BIN"]):
            tk.Label(disp, text=key, font=("Segoe UI", 9, "bold"),
                     width=5, anchor="w").grid(row=i, column=0, sticky="w", pady=1)
            lbl = tk.Label(disp, text="0", font=("Segoe UI", 11), anchor="e")
            lbl.grid(row=i, column=1, sticky="ew", padx=4)
            self._prog_displays[key] = lbl

        base_frame = tk.Frame(frame)
        base_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=4)
        for base in ["HEX","DEC","OCT","BIN"]:
            tk.Radiobutton(base_frame, text=base, variable=self._prog_base,
                           value=base, font=("Segoe UI", 10),
                           command=self._prog_update).pack(side="left", padx=6)

        btn_frame = tk.Frame(frame, padx=3, pady=2)
        btn_frame.grid(row=2, column=0, sticky="nsew")
        for i in range(4): btn_frame.columnconfigure(i, weight=1)
        for i in range(6): btn_frame.rowconfigure(i, weight=1)

        prog_layout = [
            ("A",0,0,"hex"),("B",0,1,"hex"),("C",0,2,"hex"),("D",0,3,"hex"),
            ("E",1,0,"hex"),("F",1,1,"hex"),("AND",1,2,"op2"),("OR",1,3,"op2"),
            ("7",2,0,"num"),("8",2,1,"num"),("9",2,2,"num"),("XOR",2,3,"op2"),
            ("4",3,0,"num"),("5",3,1,"num"),("6",3,2,"num"),("NOT",3,3,"op2"),
            ("1",4,0,"num"),("2",4,1,"num"),("3",4,2,"num"),("⌫",4,3,"op"),
            ("CLR",5,0,"op"),("0",5,1,"num"),("<<",5,2,"op2"),("=",5,3,"eq"),
        ]
        prog_btns = {}
        for text, row, col, kind in prog_layout:
            b = tk.Button(btn_frame, text=text, font=("Segoe UI", 10),
                          relief="flat",
                          command=lambda t=text: self._prog_click(t))
            b.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            prog_btns[f"{text}{row}{col}"] = (b, kind)

        self.views["Programmer"] = {
            "frame": frame, "disp": disp,
            "btn_frame": btn_frame, "btns": prog_btns,
        }

    def _prog_update(self):
        val = self._prog_val
        self._prog_displays["DEC"].config(text=str(val))
        h = hex(val)[2:].upper() if val >= 0 else "-"+hex(val)[3:].upper()
        o = oct(val)[2:]         if val >= 0 else "-"+oct(val)[3:]
        b = bin(val)[2:]         if val >= 0 else "-"+bin(val)[3:]
        self._prog_displays["HEX"].config(text=h)
        self._prog_displays["OCT"].config(text=o)
        self._prog_displays["BIN"].config(text=b)

    def _prog_click(self, char):
        base  = self._prog_base.get()
        radix = {"HEX":16,"DEC":10,"OCT":8,"BIN":2}[base]
        if char in "0123456789ABCDEF":
            if self._prog_new:
                try: self._prog_val = int(char, radix); self._prog_new = False
                except: pass
            else:
                cur = self._prog_displays[base].cget("text").lstrip("-")
                try: self._prog_val = int(cur + char, radix)
                except: pass
        elif char == "⌫":
            cur = self._prog_displays[base].cget("text")
            self._prog_val = int(cur[:-1], radix) if len(cur) > 1 else 0
        elif char == "CLR":
            self._prog_val = 0; self._prog_op = None; self._prog_new = True
        elif char in ("AND","OR","XOR","<<",">>"):
            self._prog_op = char; self._prog_first = self._prog_val; self._prog_new = True
        elif char == "NOT":
            self._prog_val = ~self._prog_val
        elif char == "=":
            if self._prog_op:
                a, b2 = self._prog_first, self._prog_val
                res = {"AND":a&b2,"OR":a|b2,"XOR":a^b2,"<<":a<<b2,">>":a>>b2}.get(self._prog_op, b2)
                self._prog_val = res; self._prog_op = None
            self._prog_new = True
        self._prog_update()

    # ══════════════════════════════════════════════════════════════════════
    #  DATE VIEW
    # ══════════════════════════════════════════════════════════════════════
    def _build_date_view(self):
        frame = tk.Frame(self.content)
        frame.columnconfigure(0, weight=1)

        tk.Label(frame, text="Date Calculation",
                 font=("Segoe UI", 13, "bold"), anchor="w",
                 padx=14, pady=10).pack(fill="x")

        inner = tk.Frame(frame, padx=20, pady=10)
        inner.pack(fill="both", expand=True)
        inner.columnconfigure(1, weight=1)

        def date_row(label, row):
            tk.Label(inner, text=label, font=("Segoe UI", 11),
                     anchor="w").grid(row=row, column=0, sticky="w", pady=6, padx=4)
            e = tk.Entry(inner, font=("Segoe UI", 12), relief="flat", bd=2, width=16)
            e.insert(0, date.today().strftime("%Y-%m-%d"))
            e.grid(row=row, column=1, sticky="ew", padx=8, pady=6)
            return e

        e1 = date_row("From (YYYY-MM-DD):", 0)
        e2 = date_row("To   (YYYY-MM-DD):", 1)

        result_var = tk.StringVar(value="")
        result_lbl = tk.Label(inner, textvariable=result_var,
                              font=("Segoe UI", 12), anchor="w",
                              wraplength=280, justify="left")
        result_lbl.grid(row=3, column=0, columnspan=2, sticky="ew", padx=4, pady=10)

        def calculate():
            try:
                d1 = datetime.strptime(e1.get().strip(), "%Y-%m-%d").date()
                d2 = datetime.strptime(e2.get().strip(), "%Y-%m-%d").date()
                delta = abs((d2 - d1).days)
                yrs, rem = divmod(delta, 365)
                mos, days = divmod(rem, 30)
                result_var.set(f"Difference:  {delta} day(s)\n≈ {yrs} yr  {mos} mo  {days} d")
            except ValueError:
                result_var.set("⚠  Invalid date — use YYYY-MM-DD")

        tk.Button(inner, text="Calculate Difference",
                  font=("Segoe UI", 11), relief="flat", padx=14, pady=6,
                  command=calculate).grid(row=2, column=0, columnspan=2,
                                          sticky="ew", padx=4, pady=8)

        self.views["Date Calculation"] = {
            "frame": frame, "btns": {}, "entries": (e1, e2), "result_lbl": result_lbl,
        }

    # ══════════════════════════════════════════════════════════════════════
    #  CONVERTER VIEWS
    # ══════════════════════════════════════════════════════════════════════
    def _build_converter_view(self, name):
        frame = tk.Frame(self.content)
        frame.columnconfigure(0, weight=1)

        tk.Label(frame, text=name,
                 font=("Segoe UI", 13, "bold"), anchor="w",
                 padx=14, pady=10).pack(fill="x")

        units = CONVERTER_UNITS[name]
        inner = tk.Frame(frame, padx=20, pady=10)
        inner.pack(fill="both", expand=True)
        inner.columnconfigure(0, weight=1)
        inner.columnconfigure(1, weight=1)

        tk.Label(inner, text="From", font=("Segoe UI", 10),
                 anchor="w").grid(row=0, column=0, sticky="ew", pady=2)
        from_var = tk.StringVar(value=units[0])
        from_drop = ttk.Combobox(inner, textvariable=from_var,
                                 values=units, state="readonly",
                                 font=("Segoe UI", 11))
        from_drop.grid(row=1, column=0, sticky="ew", padx=4, pady=4)

        tk.Label(inner, text="To", font=("Segoe UI", 10),
                 anchor="w").grid(row=0, column=1, sticky="ew", pady=2, padx=8)
        to_var = tk.StringVar(value=units[1] if len(units) > 1 else units[0])
        to_drop = ttk.Combobox(inner, textvariable=to_var,
                               values=units, state="readonly",
                               font=("Segoe UI", 11))
        to_drop.grid(row=1, column=1, sticky="ew", padx=4, pady=4)

        tk.Label(inner, text="Value", font=("Segoe UI", 10),
                 anchor="w").grid(row=2, column=0, sticky="ew", pady=6, padx=4)
        input_entry = tk.Entry(inner, font=("Segoe UI", 14),
                               relief="flat", bd=2, justify="right")
        input_entry.insert(0, "1")
        input_entry.grid(row=3, column=0, columnspan=2, sticky="ew", padx=4, pady=2)

        result_var = tk.StringVar(value="")
        tk.Label(inner, text="Result", font=("Segoe UI", 10),
                 anchor="w").grid(row=4, column=0, sticky="ew", pady=6, padx=4)
        result_lbl = tk.Label(inner, textvariable=result_var,
                              font=("Segoe UI", 18, "bold"), anchor="e",
                              relief="flat", padx=6)
        result_lbl.grid(row=5, column=0, columnspan=2, sticky="ew", padx=4)

        unit_lbl = tk.Label(inner,
                            text=units[1] if len(units) > 1 else units[0],
                            font=("Segoe UI", 11), anchor="w", padx=4)
        unit_lbl.grid(row=6, column=0, columnspan=2, sticky="ew")

        def do_convert(*_):
            res = convert_value(name, from_var.get(), to_var.get(), input_entry.get())
            result_var.set(res)
            unit_lbl.config(text=to_var.get())

        input_entry.bind("<KeyRelease>", do_convert)
        from_drop.bind("<<ComboboxSelected>>", do_convert)
        to_drop.bind("<<ComboboxSelected>>", do_convert)
        do_convert()

        def swap():
            f, t2 = from_var.get(), to_var.get()
            from_var.set(t2); to_var.set(f); do_convert()

        tk.Button(inner, text="⇄  Swap", font=("Segoe UI", 11),
                  relief="flat", padx=12, pady=6,
                  command=swap).grid(row=7, column=0, columnspan=2,
                                     sticky="ew", padx=4, pady=12)

        self.views[name] = {
            "frame": frame, "btns": {},
            "input": input_entry, "result_var": result_var,
        }

    # ══════════════════════════════════════════════════════════════════════
    #  THEME ENGINE
    # ══════════════════════════════════════════════════════════════════════
    def _toggle_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"
        self._apply_theme()

    def _draw_toggle(self):
        c = self.toggle_canvas
        c.delete("all")
        t = THEMES[self.theme]
        dark = (self.theme == "dark")
        c.configure(bg=t["sidebar_bg"])
        draw_rounded_rect(c, 2, 2, 46, 24, 11,
                          fill=t["toggle_on"] if dark else t["toggle_off"],
                          outline="")
        x = 34 if dark else 14
        c.create_oval(x-9, 4, x+9, 22, fill="white", outline="")

    def _apply_theme(self):
        t = THEMES[self.theme]

        # Root and structural frames
        self.root.configure(bg=t["root_bg"])
        self.content.configure(bg=t["root_bg"])

        # Header
        self.header.configure(bg=t["header_bg"])
        self.lbl_mode.configure(bg=t["header_bg"], fg=t["header_fg"])
        for b in (self.btn_hamburger, self.btn_history):
            b.configure(bg=t["header_btn_bg"], fg=t["header_btn_fg"],
                        activebackground=t["header_btn_active"],
                        activeforeground=t["header_btn_fg"])

        # FIX: overlay always matches root background — never black
        self.overlay.configure(bg=t["root_bg"])

        # Sidebar
        self._theme_tree(self.sidebar, t, "sidebar")
        self._draw_toggle()

        # History panel
        self._theme_tree(self.hist_panel, t, "sidebar")
        self.hist_canvas.configure(bg=t["history_panel_bg"])
        self.hist_inner.configure(bg=t["history_panel_bg"])

        # All views
        self._theme_all_views(t)

        # ttk combobox style
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TCombobox",
                        fieldbackground=t["input_bg"],
                        background=t["input_bg"],
                        foreground=t["input_fg"],
                        selectbackground=t["sidebar_active"],
                        selectforeground=t["input_fg"])

    def _repaint_view(self, name):
        """Re-apply theme colors to a single view (used by _switch_view)."""
        t = THEMES[self.theme]
        v = self.views[name]
        self._theme_view_widgets(v["frame"], t)
        self._theme_view_buttons(v, t)

    def _theme_all_views(self, t):
        for name, v in self.views.items():
            self._theme_view_widgets(v["frame"], t)
            self._theme_view_buttons(v, t)

    def _theme_view_buttons(self, v, t):
        """Paint calculator buttons with their correct kind-based color."""
        for key, val in v.get("btns", {}).items():
            if not (isinstance(val, tuple) and len(val) >= 2):
                continue
            btn, kind = val[0], val[1]
            if kind == "eq":
                btn.configure(bg=t["btn_eq_bg"], fg=t["btn_eq_fg"],
                              activebackground=t["btn_eq_bg"],
                              activeforeground=t["btn_eq_fg"])
            elif kind == "num":
                btn.configure(bg=t["btn_num_bg"], fg=t["btn_fg"],
                              activebackground=t["btn_active"],
                              activeforeground=t["btn_fg"])
            elif kind in ("sci", "hex"):
                btn.configure(bg=t["btn_sci_bg"], fg=t["btn_fg"],
                              activebackground=t["btn_active"],
                              activeforeground=t["btn_fg"])
            else:  # op, op2
                btn.configure(bg=t["btn_op_bg"], fg=t["btn_fg"],
                              activebackground=t["btn_active"],
                              activeforeground=t["btn_fg"])
        # Display labels stored separately
        for lkey in ("hist_lbl", "res_lbl"):
            if lkey in v:
                fg = t["history_fg"] if lkey == "hist_lbl" else t["result_fg"]
                try: v[lkey].configure(bg=t["display_bg"], fg=fg)
                except Exception: pass
        if "disp" in v:
            try: v["disp"].configure(bg=t["display_bg"])
            except Exception: pass
        if "btn_frame" in v:
            try: v["btn_frame"].configure(bg=t["root_bg"])
            except Exception: pass

    def _theme_tree(self, widget, t, mode="view"):
        """Recursively paint a widget subtree.
        mode='sidebar' uses sidebar palette; mode='view' uses view palette."""
        bg = t["sidebar_bg"]   if mode == "sidebar" else t["view_bg"]
        fg = t["sidebar_fg"]   if mode == "sidebar" else t["view_fg"]
        hover = t["sidebar_hover"] if mode == "sidebar" else t["btn_active"]
        cls = widget.winfo_class()
        try:
            if cls in ("Frame", "Labelframe"):
                widget.configure(bg=bg)
            elif cls == "Label":
                widget.configure(bg=bg, fg=fg)
            elif cls == "Button":
                widget.configure(bg=bg, fg=fg,
                                 activebackground=hover,
                                 activeforeground=fg)
            elif cls == "Canvas":
                widget.configure(bg=bg)
            elif cls == "Scrollbar":
                pass  # leave system default
        except Exception:
            pass
        for child in widget.winfo_children():
            self._theme_tree(child, t, mode)

    def _theme_view_widgets(self, widget, t):
        """Paint a view frame tree with view-palette colors."""
        cls = widget.winfo_class()
        try:
            if cls == "Frame":
                widget.configure(bg=t["view_bg"])
            elif cls == "Label":
                widget.configure(bg=t["view_bg"], fg=t["view_fg"])
            elif cls == "Entry":
                widget.configure(
                    bg=t["input_bg"], fg=t["input_fg"],
                    insertbackground=t["input_fg"],
                    highlightbackground=t["input_border"],
                    highlightcolor=t["btn_eq_bg"],
                    highlightthickness=1)
            elif cls == "Button":
                widget.configure(bg=t["btn_op_bg"], fg=t["btn_fg"],
                                 activebackground=t["btn_active"],
                                 activeforeground=t["btn_fg"])
            elif cls == "Radiobutton":
                widget.configure(bg=t["view_bg"], fg=t["view_fg"],
                                 activebackground=t["view_bg"],
                                 selectcolor=t["btn_eq_bg"])
            elif cls == "Canvas":
                widget.configure(bg=t["input_bg"])
        except Exception:
            pass
        for child in widget.winfo_children():
            self._theme_view_widgets(child, t)


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
