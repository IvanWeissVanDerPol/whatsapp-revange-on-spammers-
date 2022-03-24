import pyautogui, time

time.sleep(5)

#nota para hacer andar deben hacer correr el programa y hacer click en donde quieren que escriba
#yo uso whatsapp web para hacerlo

for cont in range(100):
    pyautogui.typewrite('buenas Natalia Trinidad le pido que me saque de la lista de anuncios que me estoy cansando de recibir publicidad para la señora ana ya que mi nombre es ivan weiss y como se ve en mi imagen soy un hombre\n si esto sigue voy a colapsar sus celulares de verdad y joder sus bases de datos personalmente \n poneme en contacto con tu gefe si no podes hacer nada al respecto\n gracias por todo\n')
    pyautogui.press('enter')
    time.sleep(0.5)
