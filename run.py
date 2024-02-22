# -*- coding: utf-8 -*-
import os, sys, time, pyfiglet

hijau = "\033[32m"
kuning = "\033[93m"
hitamxhijau = "\033[30;42m"
reset = "\033[0m"

logo = """{}
    ┏———————————————————————————————————————————┓
    ┃    ╔╦╗╔═╗═╗ ╦╔╦╗  ╔╦╗╔═╗  ╔═╗╔═╗╔═╗╦╦     ┃
    ┃     ║ ║╣ ╔╩╦╝ ║    ║ ║ ║  ╠═╣╚═╗║  ║║     ┃
    ┃     ╩ ╚═╝╩ ╚═ ╩    ╩ ╚═╝  ╩ ╩╚═╝╚═╝╩╩     ┃
    ┗———————————————————————————————————————————┛
      • Author : Zidan IDz
      • Github : https://github.com/ZidanID17
""".format(hijau)

def text_to_ascii(text, font="standard"):
    fig = pyfiglet.Figlet(font=font)
    ascii_art = fig.renderText(text)
    return ascii_art

def main():
    time.sleep(0.5)
    os.system("clear")
    print(logo)
    text = input("  {} Enter Text {}{} ".format(hitamxhijau, reset, kuning))
    print("\n")
    
    fig = pyfiglet.Figlet()
    available_fonts = fig.getFonts()
    
    fonts_to_display = available_fonts[:160]
    for font_choice in fonts_to_display:
        ascii_art = text_to_ascii(text, font=font_choice)
        print("{}FONT : {}{}".format(kuning, font_choice, hijau))
        print(ascii_art)
        print("{}===================================={}".format(hijau, reset))

    continued = input("\n  {} Tap to Continue {}{} ".format(hitamxhijau, reset, kuning))
    
    start_index = 500
    end_index = 600
    fonts_to_display = available_fonts[start_index:end_index]
    for font_choice in fonts_to_display:
        ascii_art = text_to_ascii(text, font=font_choice)
        print("{}FONT : {}{}".format(kuning, font_choice, hijau))
        print(ascii_art)
        print("{}===================================={}".format(hijau, reset))
    
    continued = input("\n  {} Tap to Exit {}{} ".format(hitamxhijau, reset, kuning))
    print("()".format(reset))
    os.system("clear")
    os.system("login")
    sys.exit()

main()