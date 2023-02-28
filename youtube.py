import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video_title = ytObject.title
        title.configure(text=video_title)

        finishLabel.configure(text="Downloading.... ", text_color="blue")

        video = ytObject.streams.get_highest_resolution()
        video.download()
        finishLabel.configure(text="Download Complite!", text_color="green")
    except:
        print("YouTube link is invalide")
        finishLabel2.configure(text="YouTube link is invalide", text_color="red")
        title.configure(text="Insert a youtube video link")
        finishLabel.configure(text="")
    #finishLabel.configure(text="Download Complite!", text_color="green")
    #print("Download Complite!")


def on_progress(stream, chunk, bytes_remaining):
    total_size =  stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    per = bytes_downloaded / total_size * 100
    per1 = str(int(per))
    progress.configure(text=per1 + '%', text_color="green")
    progress.update()
    progressbar.set(float(per)/100 )
    print(per)


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1024*720")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert a youtube video link", text_color="blue")
title.pack(padx=10, pady=10)
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(padx=30, pady=10)

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

finishLabel2 = customtkinter.CTkLabel(app, text="")
finishLabel2.pack()

progress = customtkinter.CTkLabel(app, text="")
progress.pack()

progressbar = customtkinter.CTkProgressBar(app, width=350)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

title1 = customtkinter.CTkLabel(app, text="©Azaharul Rashid Neloy")
title1.pack(padx=30, pady=10)

app.mainloop()