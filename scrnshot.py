import pyscreenshot

def sacar_foto():
    pyscreenshot.grab_to_file("foto.png")


if __name__ == '__main__':
    sacar_foto()