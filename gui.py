import webbrowser
import tkinter as tk
import configparser
import gettext
import observer


def query_players():
    print('query_players')
    try:
        players = observer.check_players()
        ss = [_('list of players'), '']
        for alias, race in players:
            s = f'{alias},{_(race)}'
            ss.append(s)
        res = '\n'.join(ss)
    except Exception as e:
        res = e.args
    update_text(res)


def query_teams():
    print('query_teams')
    try:
        teams = observer.check_teams()
        ss = [_('list of teams'), '']
        for team_name, team_side, ppl in teams:
            s = f'{team_name},{_(team_side)},{_(ppl)}'
            ss.append(s)
        res = '\n'.join(ss)
    except Exception as e:
        res = e.args
    update_text(res)


def update_text(s):
    text.delete(1.0, "end")
    text.insert(1.0, s)


# load config
config = configparser.ConfigParser()
config.read('config.ini')
language = config['lang']['language']

# translate
lang = gettext.translation('gui', 'locales', languages=[
                           language], fallback=True)
_ = lang.gettext

# build window
root = tk.Tk()
root.title('COH2 DARK POWER')
root.geometry('600x400')
root.iconbitmap('./icon.ico')
root.resizable(width=False, height=False)
btn_frame = tk.Frame(root)
text_frame = tk.Frame(root)
btn_frame.pack()
text_frame.pack()

# build bottom frame
btn1 = tk.Button(btn_frame, text=_('query players'), command=query_players)
btn2 = tk.Button(btn_frame, text=_('query teams'), command=query_teams)
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)

# build text frame
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text = tk.Text(text_frame, height=25)
text.config(padx=5, pady=5)
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)
text.pack(side=tk.LEFT, fill=tk.Y)

# build data source label
label = tk.Label(root, text='data source : coh2stats.com', fg='blue')
label.pack()
label.bind("<Button>",
           lambda x: webbrowser.open_new_tab("https://coh2stats.com/"))


root.mainloop()
