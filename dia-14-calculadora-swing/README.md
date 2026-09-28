# Dia 14: Calculadora com janela (Swing)

> Original em Python: [`original.py`](original.py) (do meus projetos locais de Python)

## Missão

Recriar a calculadora do Tkinter em **Swing**, a biblioteca de janelas que já vem no Java. Esse é o projeto mais longo da trilha e **pode levar 2 ou 3 dias**. Faça um commit no fim de cada dia com o que estiver pronto.

Ordem sugerida:

1. Janela preta, display e grade 5×4 de botões (sem funcionar)
2. Números e operações funcionando
3. Cores e hover
4. (bônus) Painel de histórico

## O que muda no Java

| Tkinter | Swing |
|---|---|
| `tk.Tk()` | `JFrame janela = new JFrame("Calculadora");` |
| `tk.Button(..., command=f)` | `JButton b = new JButton("7"); b.addActionListener(e -> f());` |
| `tk.Label` / `Entry` | `JLabel` / `JTextField` |
| `.grid(row, column)` | `new JPanel(new GridLayout(5, 4, 8, 8))` |
| `bg='#ff9f0a'` | `b.setBackground(Color.decode("#ff9f0a"));` |
| `root.mainloop()` | `janela.setVisible(true);` |

Imports: `import javax.swing.*;` e `import java.awt.*;`

💡 `e -> f()` é uma **lambda**, o mesmo `lambda` do Python com outra sintaxe.

## Checklist

- [ ] janela abre com a grade de botões
- [ ] `7 × 8 =` dá 56
- [ ] `C` e `⌫` funcionam
- [ ] marquei ✅ na tabela do README principal
- [ ] commit e push

## Rodar

```
cd dia-14-calculadora-swing
java CalculadoraSwing.java
```
