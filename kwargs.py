def hola(**kwargs):
    for key, value in kwargs.items():
        print("%s = %s" % (key, value))

    return kwargs.get("num1") + kwargs.get("num2")

varg = {
    "surname": "pepe",
    "name": "Hola",
    "num1":2,
    "num2":1,
    "lista": {"hola": 1, "2": 2, "lol": [1], "lola": {}}
}

print(varg.get("lista").get("hola"))
resultado = hola(**varg)