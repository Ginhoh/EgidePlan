import customtkinter as ctk

# ── Tema ────────────────────────────────────────────────────────────────────
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# ── Paleta EgidePlan ────────────────────────────────────────────────────────
C = {
    "sidebar_bg":    "#0C447C",
    "sidebar_hover": "#185FA5",
    "sidebar_active":"#185FA5",
    "accent":        "#185FA5",
    "accent_light":  "#378ADD",
    "blue_bg":       "#E6F1FB",
    "blue_text":     "#0C447C",
    "green_bg":      "#EAF3DE",
    "green_text":    "#27500A",
    "amber_bg":      "#FAEEDA",
    "amber_text":    "#633806",
    "red_text":      "#A32D2D",
    "red_border":    "#F09595",
    "surface":       "#F5F5F5",
    "card":          "#FFFFFF",
    "border":        "#D8D8D8",
    "text":          "#1A1A1A",
    "text_muted":    "#6B6B6B",
    "text_hint":     "#9A9A9A",
}

GASTOS = [
    {"nome": "Cabelo",   "data": "03/04/2026", "categoria": "Auto Cuidado",        "valor": 38.00,  "cor": "blue",  "fixo": False},
    {"nome": "Netflix",  "data": "01/04/2026", "categoria": "Streaming",           "valor": 39.90,  "cor": "green", "fixo": True},
    {"nome": "Internet", "data": "01/04/2026", "categoria": "Internet & Telefone", "valor": 109.99, "cor": "amber", "fixo": True},
]

MESES = ["Abril 2026", "Março 2026", "Fevereiro 2026", "Janeiro 2026"]

NAV_ITEMS = [
    ("Home",          "⊞"),
    ("Dashboard",     "〰"),
    ("Gastos",        "≡"),
    ("Contato",       "◯"),
    ("Configurações", "✦"),
]


# ── App ──────────────────────────────────────────────────────────────────────
class EgidePlanApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EgidePlan — Controle de Gastos")
        self.geometry("860x560")
        self.minsize(760, 480)
        self.configure(fg_color=C["surface"])

        self.gastos = [g.copy() for g in GASTOS]
        self.mes_var = ctk.StringVar(value=MESES[0])
        self.nav_active = "Gastos"

        self._build()

    # ── Layout raiz ─────────────────────────────────────────────────────────
    def _build(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._build_sidebar()
        self._build_main()

    # ── Sidebar ──────────────────────────────────────────────────────────────
    def _build_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=190, corner_radius=0, fg_color=C["sidebar_bg"])
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        self.sidebar.grid_rowconfigure(6, weight=1)

        # Logo
        logo_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        logo_frame.grid(row=0, column=0, padx=16, pady=(20, 12), sticky="w")

        mark = ctk.CTkFrame(logo_frame, width=30, height=30, corner_radius=6, fg_color=C["accent_light"])
        mark.grid(row=0, column=0, sticky="w")
        mark.grid_propagate(False)
        ctk.CTkLabel(mark, text="EP", font=ctk.CTkFont(size=11, weight="bold"), text_color="white").place(relx=.5, rely=.5, anchor="center")

        ctk.CTkLabel(logo_frame, text="EgidePlan", font=ctk.CTkFont(size=14, weight="bold"),
                     text_color="white").grid(row=1, column=0, sticky="w", pady=(6, 0))
        ctk.CTkLabel(logo_frame, text="Controle de gastos", font=ctk.CTkFont(size=10),
                     text_color=C["accent_light"]).grid(row=2, column=0, sticky="w")

        sep = ctk.CTkFrame(self.sidebar, height=1, fg_color="white", corner_radius=0)
        sep.grid(row=1, column=0, sticky="ew", padx=0, pady=0)
        sep.configure(fg_color="#1a5c9a")

        # Nav items
        self.nav_buttons = {}
        for i, (label, icon) in enumerate(NAV_ITEMS[:-1], start=2):
            btn = self._nav_btn(label, icon)
            btn.grid(row=i, column=0, padx=8, pady=2, sticky="ew")
            self.nav_buttons[label] = btn

        # Footer nav
        sep2 = ctk.CTkFrame(self.sidebar, height=1, fg_color="#1a5c9a", corner_radius=0)
        sep2.grid(row=7, column=0, sticky="ew", padx=0, pady=4)

        cfg_btn = self._nav_btn("Configurações", "✦")
        cfg_btn.grid(row=8, column=0, padx=8, pady=(0, 12), sticky="ew")
        self.nav_buttons["Configurações"] = cfg_btn

        self._set_active(self.nav_active)

    def _nav_btn(self, label, icon):
        btn = ctk.CTkButton(
            self.sidebar,
            text=f"  {icon}   {label}",
            anchor="w",
            height=36,
            corner_radius=8,
            font=ctk.CTkFont(size=13),
            fg_color="transparent",
            hover_color=C["sidebar_hover"],
            text_color=C["accent_light"],
            command=lambda l=label: self._set_active(l),
        )
        return btn

    def _set_active(self, label):
        self.nav_active = label
        for name, btn in self.nav_buttons.items():
            if name == label:
                btn.configure(fg_color=C["sidebar_active"], text_color="white")
            else:
                btn.configure(fg_color="transparent", text_color=C["accent_light"])

    # ── Área principal ───────────────────────────────────────────────────────
    def _build_main(self):
        self.main = ctk.CTkFrame(self, corner_radius=0, fg_color=C["card"])
        self.main.grid(row=0, column=1, sticky="nsew")
        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid_rowconfigure(1, weight=1)

        self._build_topbar()
        self._build_content()
        self._build_actionbar()

    # ── Topbar ───────────────────────────────────────────────────────────────
    def _build_topbar(self):
        bar = ctk.CTkFrame(self.main, height=52, corner_radius=0, fg_color=C["card"],
                           border_width=1, border_color=C["border"])
        bar.grid(row=0, column=0, sticky="ew")
        bar.grid_propagate(False)
        bar.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(bar, text="Meus gastos", font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=C["text"]).grid(row=0, column=0, padx=20, pady=14, sticky="w")

        right = ctk.CTkFrame(bar, fg_color="transparent")
        right.grid(row=0, column=2, padx=16, pady=8, sticky="e")

        ctk.CTkOptionMenu(right, values=MESES, variable=self.mes_var, width=130, height=30,
                          corner_radius=8, font=ctk.CTkFont(size=12),
                          fg_color=C["surface"], button_color=C["border"],
                          button_hover_color=C["border"], text_color=C["text"],
                          dropdown_fg_color=C["card"], dropdown_text_color=C["text"],
                          command=lambda _: None).pack(side="left", padx=(0, 8))

        ctk.CTkButton(right, text="+ Adicionar", height=30, width=110, corner_radius=8,
                      font=ctk.CTkFont(size=12, weight="bold"),
                      fg_color=C["accent"], hover_color=C["sidebar_active"], text_color="white",
                      command=self._dialog_adicionar).pack(side="left")

    # ── Conteúdo central ─────────────────────────────────────────────────────
    def _build_content(self):
        self.content_frame = ctk.CTkScrollableFrame(self.main, corner_radius=0,
                                                     fg_color=C["surface"])
        self.content_frame.grid(row=1, column=0, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)

        self._build_metrics()
        self._build_expense_list()

    def _build_metrics(self):
        if hasattr(self, "_metrics_frame"):
            self._metrics_frame.destroy()

        self._metrics_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self._metrics_frame.grid(row=0, column=0, padx=16, pady=(14, 8), sticky="ew")
        self._metrics_frame.grid_columnconfigure((0, 1, 2), weight=1)

        total = sum(g["valor"] for g in self.gastos)
        fixos = sum(g["valor"] for g in self.gastos if g["fixo"])
        qtd   = len(self.gastos)

        self._metric_card(self._metrics_frame, 0, "Total do mês",       f"R$ {total:,.2f}".replace(",", "."), C["accent"])
        self._metric_card(self._metrics_frame, 1, "Gastos fixos",        f"R$ {fixos:,.2f}".replace(",", "."), C["amber_text"])
        self._metric_card(self._metrics_frame, 2, "Lançamentos",         str(qtd),                             C["text"])

    def _metric_card(self, parent, col, label, value, value_color):
        card = ctk.CTkFrame(parent, corner_radius=8, fg_color=C["card"],
                            border_width=1, border_color=C["border"])
        card.grid(row=0, column=col, padx=(0 if col == 0 else 6, 0), sticky="ew")
        card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(card, text=label.upper(), font=ctk.CTkFont(size=10),
                     text_color=C["text_hint"]).grid(row=0, column=0, padx=14, pady=(10, 2), sticky="w")
        ctk.CTkLabel(card, text=value, font=ctk.CTkFont(size=19, weight="bold"),
                     text_color=value_color).grid(row=1, column=0, padx=14, pady=(0, 10), sticky="w")

    def _build_expense_list(self):
        if hasattr(self, "_list_frame"):
            self._list_frame.destroy()

        self._list_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self._list_frame.grid(row=1, column=0, padx=16, pady=(4, 16), sticky="ew")
        self._list_frame.grid_columnconfigure(0, weight=1)

        # Header
        hdr = ctk.CTkFrame(self._list_frame, fg_color="transparent")
        hdr.grid(row=0, column=0, sticky="ew", pady=(0, 6))
        ctk.CTkLabel(hdr, text=f"Lançamentos — {self.mes_var.get()}",
                     font=ctk.CTkFont(size=12, weight="bold"),
                     text_color=C["text"]).pack(side="left")

        # Rows
        for i, g in enumerate(self.gastos):
            self._expense_row(self._list_frame, i + 1, g)

        if not self.gastos:
            ctk.CTkLabel(self._list_frame, text="Nenhum gasto registrado.",
                         font=ctk.CTkFont(size=13), text_color=C["text_hint"]).grid(
                row=1, column=0, pady=30)

    def _expense_row(self, parent, row_idx, gasto):
        dot_colors = {"blue": C["accent_light"], "green": "#639922", "amber": "#BA7517"}
        badge_cfg = {
            "blue":  (C["blue_bg"],  C["blue_text"]),
            "green": (C["green_bg"], C["green_text"]),
            "amber": (C["amber_bg"], C["amber_text"]),
        }

        card = ctk.CTkFrame(parent, corner_radius=8, fg_color=C["card"],
                            border_width=1, border_color=C["border"])
        card.grid(row=row_idx, column=0, sticky="ew", pady=(0, 6))
        card.grid_columnconfigure(2, weight=1)

        # Dot
        dot = ctk.CTkFrame(card, width=8, height=8, corner_radius=4,
                           fg_color=dot_colors.get(gasto["cor"], C["accent_light"]))
        dot.grid(row=0, column=0, padx=(14, 10), pady=14)
        dot.grid_propagate(False)

        # Info
        info = ctk.CTkFrame(card, fg_color="transparent")
        info.grid(row=0, column=1, pady=10, sticky="w")
        ctk.CTkLabel(info, text=gasto["nome"], font=ctk.CTkFont(size=13, weight="bold"),
                     text_color=C["text"]).pack(anchor="w")
        meta = gasto["data"] + (" · Gasto fixo" if gasto["fixo"] else "")
        ctk.CTkLabel(info, text=meta, font=ctk.CTkFont(size=10),
                     text_color=C["text_hint"]).pack(anchor="w")

        # Badge
        bg, fg = badge_cfg.get(gasto["cor"], (C["surface"], C["text"]))
        badge = ctk.CTkLabel(card, text=gasto["categoria"],
                             font=ctk.CTkFont(size=11),
                             fg_color=bg, text_color=fg,
                             corner_radius=20, padx=10, pady=3)
        badge.grid(row=0, column=2, padx=8)

        # Valor
        ctk.CTkLabel(card, text=f"R$ {gasto['valor']:,.2f}".replace(",", "."),
                     font=ctk.CTkFont(size=13, weight="bold"),
                     text_color=C["text"]).grid(row=0, column=3, padx=12)

        # Remover
        ctk.CTkButton(card, text="Remover", width=80, height=28, corner_radius=6,
                      font=ctk.CTkFont(size=11),
                      fg_color="transparent", border_width=1,
                      border_color=C["red_border"],
                      text_color=C["red_text"],
                      hover_color="#FEF0F0",
                      command=lambda g=gasto: self._remover(g)).grid(row=0, column=4, padx=(0, 12))

    # ── Action bar ───────────────────────────────────────────────────────────
    def _build_actionbar(self):
        bar = ctk.CTkFrame(self.main, height=50, corner_radius=0, fg_color=C["card"],
                           border_width=1, border_color=C["border"])
        bar.grid(row=2, column=0, sticky="ew")
        bar.grid_propagate(False)

        inner = ctk.CTkFrame(bar, fg_color="transparent")
        inner.place(relx=0, rely=0.5, anchor="w", x=16)

        ctk.CTkButton(inner, text="+ Criar gasto fixo", height=30, corner_radius=8,
                      font=ctk.CTkFont(size=12),
                      fg_color="transparent", border_width=1,
                      border_color=C["border"], text_color=C["text_muted"],
                      hover_color=C["surface"],
                      command=self._dialog_fixo).pack(side="left", padx=(0, 8))

        ctk.CTkButton(inner, text="✕  Remover gasto fixo", height=30, corner_radius=8,
                      font=ctk.CTkFont(size=12),
                      fg_color="transparent", border_width=1,
                      border_color=C["red_border"], text_color=C["red_text"],
                      hover_color="#FEF0F0",
                      command=self._remover_fixos).pack(side="left")

    # ── Ações ────────────────────────────────────────────────────────────────
    def _refresh(self):
        self._build_metrics()
        self._build_expense_list()

    def _remover(self, gasto):
        if gasto in self.gastos:
            self.gastos.remove(gasto)
        self._refresh()

    def _remover_fixos(self):
        self.gastos = [g for g in self.gastos if not g["fixo"]]
        self._refresh()

    def _dialog_adicionar(self):
        dlg = ctk.CTkToplevel(self)
        dlg.title("Adicionar gasto")
        dlg.geometry("360x340")
        dlg.resizable(False, False)
        dlg.grab_set()
        dlg.configure(fg_color=C["card"])

        ctk.CTkLabel(dlg, text="Novo gasto", font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=C["text"]).pack(padx=24, pady=(20, 4), anchor="w")

        def field(label, placeholder):
            ctk.CTkLabel(dlg, text=label, font=ctk.CTkFont(size=11),
                         text_color=C["text_hint"]).pack(padx=24, anchor="w", pady=(10, 2))
            e = ctk.CTkEntry(dlg, height=36, corner_radius=8, placeholder_text=placeholder,
                             border_color=C["border"], fg_color=C["surface"],
                             text_color=C["text"])
            e.pack(padx=24, fill="x")
            return e

        nome_e  = field("Título", "Ex: Conta de luz")
        valor_e = field("Valor (R$)", "0,00")

        ctk.CTkLabel(dlg, text="Categoria", font=ctk.CTkFont(size=11),
                     text_color=C["text_hint"]).pack(padx=24, anchor="w", pady=(10, 2))
        cat_var = ctk.StringVar(value="Auto Cuidado")
        ctk.CTkOptionMenu(dlg, values=["Auto Cuidado", "Streaming", "Internet & Telefone",
                                        "Alimentação", "Transporte", "Outro"],
                          variable=cat_var, height=36, corner_radius=8,
                          fg_color=C["surface"], button_color=C["border"],
                          button_hover_color=C["accent"], text_color=C["text"],
                          dropdown_fg_color=C["card"], dropdown_text_color=C["text"]
                          ).pack(padx=24, fill="x")

        fixo_var = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(dlg, text="Gasto fixo", variable=fixo_var,
                        font=ctk.CTkFont(size=12), text_color=C["text"],
                        fg_color=C["accent"], hover_color=C["accent_light"]).pack(padx=24, pady=(12, 0), anchor="w")

        def confirmar():
            nome  = nome_e.get().strip()
            valor_str = valor_e.get().strip().replace(",", ".")
            try:
                valor = float(valor_str)
            except ValueError:
                valor = 0.0
            if not nome:
                return
            cores = {"Auto Cuidado": "blue", "Streaming": "green",
                     "Internet & Telefone": "amber"}
            self.gastos.append({
                "nome": nome, "data": "07/04/2026",
                "categoria": cat_var.get(),
                "valor": valor,
                "cor": cores.get(cat_var.get(), "blue"),
                "fixo": fixo_var.get(),
            })
            self._refresh()
            dlg.destroy()

        ctk.CTkButton(dlg, text="Adicionar gasto", height=36, corner_radius=8,
                      font=ctk.CTkFont(size=13, weight="bold"),
                      fg_color=C["accent"], hover_color=C["sidebar_active"],
                      text_color="white", command=confirmar).pack(padx=24, pady=16, fill="x")

    def _dialog_fixo(self):
        dlg = ctk.CTkToplevel(self)
        dlg.title("Criar gasto fixo")
        dlg.geometry("360x280")
        dlg.resizable(False, False)
        dlg.grab_set()
        dlg.configure(fg_color=C["card"])

        ctk.CTkLabel(dlg, text="Novo gasto fixo", font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=C["text"]).pack(padx=24, pady=(20, 4), anchor="w")

        def field(label, placeholder):
            ctk.CTkLabel(dlg, text=label, font=ctk.CTkFont(size=11),
                         text_color=C["text_hint"]).pack(padx=24, anchor="w", pady=(10, 2))
            e = ctk.CTkEntry(dlg, height=36, corner_radius=8, placeholder_text=placeholder,
                             border_color=C["border"], fg_color=C["surface"],
                             text_color=C["text"])
            e.pack(padx=24, fill="x")
            return e

        nome_e  = field("Título", "Ex: Netflix")
        valor_e = field("Valor (R$)", "0,00")

        cat_var = ctk.StringVar(value="Streaming")
        ctk.CTkLabel(dlg, text="Categoria", font=ctk.CTkFont(size=11),
                     text_color=C["text_hint"]).pack(padx=24, anchor="w", pady=(10, 2))
        ctk.CTkOptionMenu(dlg, values=["Streaming", "Internet & Telefone", "Assinatura", "Outro"],
                          variable=cat_var, height=36, corner_radius=8,
                          fg_color=C["surface"], button_color=C["border"],
                          button_hover_color=C["accent"], text_color=C["text"],
                          dropdown_fg_color=C["card"], dropdown_text_color=C["text"]
                          ).pack(padx=24, fill="x")

        def confirmar():
            nome = nome_e.get().strip()
            try:
                valor = float(valor_e.get().strip().replace(",", "."))
            except ValueError:
                valor = 0.0
            if not nome:
                return
            cores = {"Streaming": "green", "Internet & Telefone": "amber"}
            self.gastos.append({
                "nome": nome, "data": "01/04/2026",
                "categoria": cat_var.get(), "valor": valor,
                "cor": cores.get(cat_var.get(), "blue"), "fixo": True,
            })
            self._refresh()
            dlg.destroy()

        ctk.CTkButton(dlg, text="Criar gasto fixo", height=36, corner_radius=8,
                      font=ctk.CTkFont(size=13, weight="bold"),
                      fg_color=C["accent"], hover_color=C["sidebar_active"],
                      text_color="white", command=confirmar).pack(padx=24, pady=16, fill="x")


# ── Entry point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = EgidePlanApp()
    app.mainloop()
