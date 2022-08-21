# resizer-watermark

to make executable run

`pyinstaller
  --noconfirm
  --onedir
  --windowed
  --icon "<PATH>/icon.ico" 
  --add-data "<PATH>/arial.ttf;." 
  --add-data "<PATH>/log.txt;."  
"<PATH>/main.py" `
