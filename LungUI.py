import os
import tkinter as tk
from tkinter import filedialog
import LungProcessing as lungProcessor

root = tk.Tk()
root.title('CellSeeUs')

selectedFolder = tk.StringVar()
outputFileName = tk.StringVar()
processButton = tk.Button()


def disable(x):
    x.config(state=tk.DISABLED)


def enable(x):
    x.config(state=tk.NORMAL)


def browse_button_selected():
    set_selected_folder(filedialog.askdirectory())


def set_selected_folder(folder):
    global selectedFolder
    selectedFolder.set(folder)


def outputFileName_changed(var1, var2, var3):
    if len(outputFileName.get()) > 0 and len(selectedFolder.get()) > 0:
        enable(processButton)
    else:
        disable(processButton)


def process_button_selected():
    outputFullFileName = outputFileName.get() + ".csv"

    #Check if output file exists. Offer options to Overwrite, Append or Cancel
    #TODO

    #Begin Processing
    processButton.active = False
    processButton.text = "Processing..."
    lungProcessor.process_folder(selectedFolder.get(), outputFullFileName)
    processButton.text = "Process Files"
    processButton.active = True

    #Show output
    os.startfile(outputFullFileName)


outputFileName.trace_add("write", outputFileName_changed)

contentFrame = tk.Frame()
contentFrame.pack(padx=5, pady=10)

selectFolderLabel = tk.Entry(contentFrame, textvariable=selectedFolder, width=50)
selectFolderButton = tk.Button(contentFrame, text="Select Folder", command=browse_button_selected, width=10)

outputNameLabel = tk.Label(contentFrame, text="Output File Name")
outputNameEntry = tk.Entry(contentFrame, textvariable=outputFileName, width=50)

processButton = tk.Button(contentFrame, text="Process Files", state=tk.DISABLED, command=process_button_selected, width=10)


selectFolderLabel.grid(row=0, column=0)
selectFolderButton.grid(row=0, column=4, padx=5)
outputNameLabel.grid(row=1, column=0, sticky="W")
outputNameEntry.grid(row=2, column=0)
processButton.grid(row=2, column=4, padx=5)


root.mainloop()
