from pyowm import OWM
from pyowm.utils.config import get_default_config

owm = OWM('f571499b1de8ee017956351375a45822')
mgr = owm.weather_manager()

config_dict = get_default_config()
config_dict['language'] = 'ru'

while True:
    place = input('Введите город: ')
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    status = w.detailed_status
    print('В городе', place, 'сейчас', status + '.', 'Температура воздуха составляет:', temp, 'градусов цельсия')
    x = input('Хотите продолжить? ').lower()
    if x == "да" or x == "yes":
        continue
    else:
        print('Хорошего дня, одевайтесь по погоде и спасибо, что выбрали нас! :)')
        break
