import tkinter as tk
from tkinter import ttk


BOTOES = [
    ['C', '±', '%', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '−'],
    ['1', '2', '3', '+'],
    ['0', '.', '⌫', '='],
]

COR_FUNDO      = '#000000'
COR_DISPLAY    = '#0a0a0a'
COR_OPERADOR   = '#ff9f0a'
COR_ESPECIAL   = '#1e1e1e'
COR_NUMERO     = '#141414'
COR_TEXTO      = '#ffffff'
COR_TEXTO_OP   = '#000000'
COR_HOVER_NUM  = '#2a2a2a'
COR_HOVER_OP   = '#ffb340'
COR_PAINEL     = '#0d0d0d'
COR_ITEM_HOVER = '#1e1e1e'


class PainelHistorico(tk.Toplevel):
    def __init__(self, parent, historico, callback_usar):
        super().__init__(parent)
        self.title('Histórico')
        self.configure(bg=COR_FUNDO)
        self.resizable(False, False)
        self.transient(parent)

        # posiciona ao lado da janela principal
        x = parent.winfo_x() + parent.winfo_width() + 8
        y = parent.winfo_y()
        self.geometry(f'260x400+{x}+{y}')

        self._construir(historico, callback_usar)

    def _construir(self, historico, callback_usar):
        tk.Label(self, text='Histórico', font=('SF Pro Display', 14, 'bold'),
                 bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=(12, 4), padx=12, anchor='w')

        frame_scroll = tk.Frame(self, bg=COR_FUNDO)
        frame_scroll.pack(fill='both', expand=True, padx=8, pady=4)

        canvas = tk.Canvas(frame_scroll, bg=COR_FUNDO, highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame_scroll, orient='vertical', command=canvas.yview)
        self.frame_itens = tk.Frame(canvas, bg=COR_FUNDO)

        self.frame_itens.bind('<Configure>',
            lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        canvas.create_window((0, 0), window=self.frame_itens, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        if not historico:
            tk.Label(self.frame_itens, text='Nenhum cálculo ainda.',
                     font=('SF Pro Display', 12), bg=COR_FUNDO, fg='#8e8e93',
                     wraplength=220).pack(pady=20)
        else:
            for expressao, resultado in reversed(historico):
                self._adicionar_item(expressao, resultado, callback_usar)

        # botão limpar histórico
        tk.Button(self, text='Limpar histórico',
                  font=('SF Pro Display', 12), bg=COR_ESPECIAL, fg=COR_TEXTO,
                  relief='flat', bd=0, cursor='hand2',
                  command=lambda: [callback_usar(None), self.destroy()]
                  ).pack(fill='x', padx=12, pady=10)

    def _adicionar_item(self, expressao, resultado, callback_usar):
        frame = tk.Frame(self.frame_itens, bg=COR_PAINEL, padx=10, pady=6,
                         cursor='hand2')
        frame.pack(fill='x', pady=2, padx=4)

        tk.Label(frame, text=expressao, font=('SF Pro Display', 11),
                 bg=COR_PAINEL, fg='#8e8e93', anchor='e').pack(fill='x')
        tk.Label(frame, text=f'= {resultado}', font=('SF Pro Display', 15, 'bold'),
                 bg=COR_PAINEL, fg=COR_TEXTO, anchor='e').pack(fill='x')

        for w in (frame, *frame.winfo_children()):
            w.bind('<Enter>', lambda e, f=frame: f.configure(bg=COR_ITEM_HOVER))
            w.bind('<Leave>', lambda e, f=frame: f.configure(bg=COR_PAINEL))
            w.bind('<Button-1>', lambda e, r=resultado: callback_usar(r))


class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title('Calculadora')
        self.root.resizable(False, False)
        self.root.configure(bg=COR_FUNDO)

        self.expressao = ''
        self.novo_numero = True
        self.resultado_exibido = False
        self.historico = []
        self._painel_historico = None

        self._construir_display()
        self._construir_botoes()
        self.root.bind('<Key>', self._teclado)

    def _construir_display(self):
        frame_topo = tk.Frame(self.root, bg=COR_FUNDO)
        frame_topo.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=8, pady=(8, 0))

        btn_hist = tk.Button(frame_topo, text='🕐 Histórico',
                             font=('SF Pro Display', 11), bg=COR_ESPECIAL, fg=COR_TEXTO,
                             relief='flat', bd=0, cursor='hand2',
                             command=self._abrir_historico)
        btn_hist.pack(anchor='e', padx=4, pady=4)
        btn_hist.bind('<Enter>', lambda e: btn_hist.configure(bg='#7c7c80'))
        btn_hist.bind('<Leave>', lambda e: btn_hist.configure(bg=COR_ESPECIAL))

        frame_display = tk.Frame(self.root, bg=COR_DISPLAY, padx=16, pady=12)
        frame_display.grid(row=1, column=0, columnspan=4, sticky='nsew', padx=8, pady=(0, 4))

        self.var_expr    = tk.StringVar()
        self.var_display = tk.StringVar(value='0')

        tk.Label(frame_display, textvariable=self.var_expr, font=('SF Pro Display', 13),
                 bg=COR_DISPLAY, fg='#8e8e93', anchor='e').pack(fill='x')
        tk.Label(frame_display, textvariable=self.var_display, font=('SF Pro Display', 36, 'bold'),
                 bg=COR_DISPLAY, fg=COR_TEXTO, anchor='e').pack(fill='x')

    def _construir_botoes(self):
        operadores = {'÷', '×', '−', '+', '='}
        especiais   = {'C', '±', '%', '⌫'}

        for r, linha in enumerate(BOTOES, start=2):
            for c, label in enumerate(linha):
                if label in operadores:
                    bg, fg, hover = COR_OPERADOR, COR_TEXTO_OP, COR_HOVER_OP
                elif label in especiais:
                    bg, fg, hover = COR_ESPECIAL, COR_TEXTO, '#7c7c80'
                else:
                    bg, fg, hover = COR_NUMERO, COR_TEXTO, COR_HOVER_NUM

                btn = tk.Button(
                    self.root, text=label,
                    font=('SF Pro Display', 18, 'bold'),
                    bg=bg, fg=fg, activebackground=hover, activeforeground=fg,
                    relief='flat', bd=0, cursor='hand2',
                    command=lambda l=label: self._clique(l),
                )
                btn.grid(row=r, column=c, padx=4, pady=4, ipadx=12, ipady=18, sticky='nsew')
                btn.bind('<Enter>', lambda e, b=btn, h=hover: b.configure(bg=h))
                btn.bind('<Leave>', lambda e, b=btn, orig=bg: b.configure(bg=orig))

        for i in range(4):
            self.root.columnconfigure(i, weight=1)

    # --- logica dos botoes ---

    def _clique(self, label):
        display = self.var_display.get()

        if label.isdigit() or label == '.':
            if self.novo_numero or display == '0' or self.resultado_exibido:
                display = label
                self.resultado_exibido = False
            else:
                if label == '.' and '.' in display:
                    return
                display += label
            self.novo_numero = False
            self.var_display.set(display)

        elif label in {'÷', '×', '−', '+'}:
            op_map = {'÷': '/', '×': '*', '−': '-'}
            op = op_map.get(label, label)
            self.expressao = display + op
            self.var_expr.set(display + ' ' + label)
            self.novo_numero = True
            self.resultado_exibido = False

        elif label == '=':
            try:
                expr_eval  = self.expressao + display
                resultado  = eval(expr_eval)
                if isinstance(resultado, float) and resultado.is_integer():
                    resultado = int(resultado)

                expr_legivel = expr_eval.replace('/', '÷').replace('*', '×').replace('-', '−')
                self.var_expr.set(expr_legivel + ' =')
                self.var_display.set(str(resultado))

                self.historico.append((expr_legivel, str(resultado)))

                self.expressao = ''
                self.resultado_exibido = True
                self.novo_numero = True
            except ZeroDivisionError:
                self.var_display.set('Erro: div/0')
                self.expressao = ''
                self.novo_numero = True
            except Exception:
                self.var_display.set('Erro')
                self.expressao = ''
                self.novo_numero = True

        elif label == 'C':
            self.var_display.set('0')
            self.var_expr.set('')
            self.expressao = ''
            self.novo_numero = True
            self.resultado_exibido = False

        elif label == '⌫':
            if not self.resultado_exibido:
                self.var_display.set(display[:-1] or '0')

        elif label == '±':
            try:
                val = float(display) * -1
                self.var_display.set(int(val) if val == int(val) else val)
            except ValueError:
                pass

        elif label == '%':
            try:
                val = float(display) / 100
                self.var_display.set(int(val) if val == int(val) else val)
            except ValueError:
                pass

    def _teclado(self, event):
        char = event.char
        if char in '0123456789.':
            self._clique(char)
        elif char in '/*-+':
            self._clique({'/' : '÷', '*': '×', '-': '−'}.get(char, char))
        elif event.keysym in ('Return', 'KP_Enter'):
            self._clique('=')
        elif event.keysym == 'BackSpace':
            self._clique('⌫')
        elif event.keysym == 'Escape':
            self._clique('C')

    # --- painel de historico ---

    def _abrir_historico(self):
        if self._painel_historico and self._painel_historico.winfo_exists():
            self._painel_historico.destroy()
            self._painel_historico = None
            return

        self._painel_historico = PainelHistorico(
            self.root,
            self.historico,
            self._usar_resultado_historico,
        )

    def _usar_resultado_historico(self, valor):
        if valor is None:
            self.historico.clear()
        else:
            self.var_display.set(valor)
            self.expressao = ''
            self.novo_numero = True
            self.resultado_exibido = True

        if self._painel_historico and self._painel_historico.winfo_exists():
            self._painel_historico.destroy()
            self._painel_historico = None


if __name__ == '__main__':
    root = tk.Tk()
    Calculadora(root)
    root.mainloop()
