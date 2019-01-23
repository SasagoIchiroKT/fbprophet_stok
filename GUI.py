import os,sys

from tkinter import *
import tkinter.ttk as ttk

from tkinter import filedialog

import subprocess

# 参照ボタンのイベント
# button1クリック時の処理
def button1_clicked():
    fTyp = [("","*.csv")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    path.set(filepath)

# button2クリック時の処理
def button2_clicked():
    cmd = "python Prophet.py "+path.get()
    subprocess.call(cmd)
def button3_clicked():
    sys.exit()

if __name__ == '__main__':
    # rootの作成
    root = Tk()
    root.title('SpPs menu')
    root.resizable(False, False)

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # 参照ボタンの作成
    button1 = ttk.Button(root, text=u'参照', command=button1_clicked)
    button1.grid(row=0, column=3)

    # ラベルの作成
    # 「ファイル」ラベルの作成
    s = StringVar()
    s.set('ファイル>>')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # 参照ファイルパス表示ラベルの作成
    path = StringVar()
    path_entry = ttk.Entry(frame1, textvariable=path, width=50)
    path_entry.grid(row=0, column=2)

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=(0,5))
    frame2.grid(row=1)

    button2 = ttk.Button(frame2,text = "実行",command=button2_clicked)
    button2.pack(side="left")

    button3 = ttk.Button(frame2,text = "終了", command=button3_clicked)
    button3.pack(side="left")

    root.mainloop()

