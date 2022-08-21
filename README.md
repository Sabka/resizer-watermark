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

then create folders 

`0orig-images` and `0resized-images` 

in output subfolder which contains exe

finally, copy images to `0orig-images`

run executable and convert via button
