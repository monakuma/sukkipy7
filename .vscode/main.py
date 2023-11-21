import tkinter as tk

root=tk.Tk()
root.geometry("1280x720")
label=tk.Label(root,text="テストです",font=("Arial",30))
label1=tk.Label(root,text="ファンタジー",font=("Arial",40))
label2=tk.Label(root,text="ヤマト運輸",font=("Arial",30))
label3=tk.Label(root,text="マイクロソフト",font=("Arial",30))
#label.grid(row=0,column=0) #pack(上部中央寄せ),grid(カラム=0row=0のマス目状態にして配置していく),place(座標指定)
#label1.grid(row=0,column=1) #pack(上部中央寄せ),grid(カラム=0row=0のマス目状態にして配置していく),place(座標指定)
#label2.grid(row=0,column=2) #pack(上部中央寄せ),grid(カラム=0row=0のマス目状態にして配置していく),place(座標指定)
#label3.place(x=1000,y=500) #pack(上部中央寄せ),grid(カラム=0row=0のマス目状態にして配置していく),place(座標指定)
def button_click():
   label1.pack()
button=tk.Button(root,text="ボタンだよ",font=("Arial",40),command=button_click)

button.pack()
entry=tk.Entry(root,font=("Arial",40))
entry.pack



root.mainloop()