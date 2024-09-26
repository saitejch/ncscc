import tkinter as tk
from tkinter import messagebox, ttk
from pytube import YouTube
import threading

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Input Error", "Please enter a YouTube URL.")
        return

    try:
        yt = YouTube(url, on_progress_callback=progress_function)
        video = yt.streams.get_highest_resolution()
        
        # Start downloading in a separate thread to avoid freezing the GUI
        threading.Thread(target=video.download, args=(None,)).start()
    except Exception as e:
        messagebox.showerror("Download Error", str(e))

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = bytes_downloaded / total_size * 100
    progress_var.set(percentage)

def create_gui():
    global url_entry, progress_var

    root = tk.Tk()
    root.title("YouTube Video Downloader")
    root.geometry("400x200")
    root.configure(bg="#282c34")

    # URL Entry
    url_label = tk.Label(root, text="YouTube Video URL:", bg="#282c34", fg="#61dafb")
    url_label.pack(pady=10)

    url_entry = tk.Entry(root, width=50)
    url_entry.pack(pady=5)

    # Download Button
    download_button = tk.Button(root, text="Download Video", command=download_video, bg="#61dafb", fg="black")
    download_button.pack(pady=10)

    # Progress Bar
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
    progress_bar.pack(pady=10, fill=tk.X, padx=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
