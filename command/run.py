from button import Button
from receptor import Receptor
from commands import ButtonCommand

recep = Receptor()
butt = Button()

butt.set_comand(ButtonCommand(recep,{"Olá":'mundo'}))
butt.action()







