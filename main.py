from PIL import Image, ImageDraw, ImageFont
import os
import PySimpleGUI as sg

with open("log.txt", "a") as w:
    w.write("\n")


def convert(input_folder="0orig-images", output_folder="0resized-images", src="zdroj234", output_name="image"):

    result_counter = 1

    for file in os.listdir(input_folder):

        ending = ""

        if file.endswith(".jpg") or file.endswith(".JPG"):
            ending = ".jpg"

        if file.endswith(".png") or file.endswith(".PNG"):
            ending = ".png"

        if file.endswith(".jpeg") or file.endswith(".JPEG"):
            ending = ".jpeg"

        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".JPG") or file.endswith(".JPEG") or file.endswith(".PNG"):

            new_image = Image.open(input_folder + "/" + file)

            if new_image.size[0] > 1000:
                tmp_imege = new_image
                pomer = new_image.size[0] / 1000
                new_image = tmp_imege.resize((int(new_image.size[0] / pomer), int(new_image.size[1] / pomer)))

            if new_image.size[1] > 1000:
                tmp_imege = new_image
                pomer = new_image.size[1] / 1000
                new_image = tmp_imege.resize((int(new_image.size[0] / pomer), int(new_image.size[1] / pomer)))

            # TODO velky rozdiel pomeru stran

            res_path = output_folder + "/" + output_name + ("0" if result_counter < 10 else "") + str(result_counter) + ending

            new_image.save(res_path)

            kbs = os.stat(res_path).st_size / 1024

            while kbs > 95:
                pomer = 0.95

                new_image = new_image.resize((int(new_image.size[0] * pomer), int(new_image.size[1] * pomer)))

                new_image.save(res_path)
                kbs = os.stat(res_path).st_size / 1024  # under 100

            # watermark
            draw = ImageDraw.Draw(new_image)
            txt = src
            fontsize = 20

            font = ImageFont.truetype("arial.ttf", fontsize)
            draw.text((10, new_image.size[1]-30), txt, fill=(0, 0, 0), font=font)

            new_image.save(res_path)

            result_counter +=1

            print(file + " : " + res_path + " " + str(os.stat(res_path).st_size / 1024), new_image.size[0],
                  new_image.size[1])
            with open("log.txt", "a") as w:
                w.write(file + " : " + res_path + " " + str(os.stat(res_path).st_size / 1024) + " " + str(new_image.size[0]) + " " +
                  str(new_image.size[1]) + "\n")

        else:
            print("Nepodporovaný typ súboru : " + file)
            with open("log.txt", "a") as w:
                w.write("Nepodporovaný typ súboru : " + file + "\n")


sg.theme('Topanga')
layout = \
    [
        [sg.Text('Meno súborov : ', size=(15, 1)), sg.InputText(key="-NAME-")],
        [sg.Text('Názov zdroja : ', size=(15, 1)), sg.InputText(key="-SOURCE-")],
        [sg.Button("skonvertuj", key="-SUBMIT-")],
        [sg.Text('', key='-LOG-')]
    ]

try:
    window = sg.Window('Image resizer, watermark creator', layout)
    while True:
        event, values = window.read()
        if event == "-SUBMIT-":
            with open("log.txt", "a") as w:
                w.write("\n")
            convert(src=values["-SOURCE-"], output_name=values["-NAME-"])
            window['-LOG-'].update("konverzia dokončená")
        if event == sg.WIN_CLOSED:
            break
except Exception as e:
    with open("log.txt", "a") as w:
        w.write(str(e) + "\n")

window.close()
