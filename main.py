def car_selection(katalog, param, kriteriy):
    your_car = []

    for car_info in katalog:
        if car_info['Характеристики'][param] == kriteriy:
            your_car.append((car_info['Модель'], car_info['Класс']))
    print(your_car)


def create_katalog():
    katalog = []
    cars = [
    {
        "Модель": "Mercedes-Benz C-Class",
        "Класс": "D",
        "Характеристики": {
            "price": 25000,
            "двигатель": 2.0,
            "разгон до 100": 6.5,
            "выпуск": 2020,
            "страна": "Германия"
        }
    },
    {
        "Модель": "BMW 3 Series",
        "Класс": "D",
        "Характеристики": {
            "price": 27000,
            "двигатель": 2.0,
            "разгон до 100": 5.8,
            "выпуск": 2021,
            "страна": "Германия"
        }
    },
    {
        "Модель": "Audi A4",
        "Класс": "D",
        "Характеристики": {
            "price": 26000,
            "двигатель": 2.0,
            "разгон до 100": 6.0,
            "выпуск": 2019,
            "страна": "Германия"
        }
    },
    {
        "Модель": "Toyota Camry",
        "Класс": "E",
        "Характеристики": {
            "price": 24000,
            "двигатель": 2.5,
            "разгон до 100": 7.5,
            "выпуск": 2022,
            "страна": "Япония"
        }
    },
    {
        "Модель": "Honda Accord",
        "Класс": "E",
        "Характеристики": {
            "price": 23000,
            "двигатель": 2.0,
            "разгон до 100": 7.2,
            "выпуск": 2021,
            "страна": "Япония"
        }
    },
    {
        "Модель": "Ford Mustang",
        "Класс": "S",
        "Характеристики": {
            "price": 35000,
            "двигатель": 5.0,
            "разгон до 100": 4.2,
            "выпуск": 2020,
            "страна": "США"
        }
    },
    {
        "Модель": "Chevrolet Camaro",
        "Класс": "S",
        "Характеристики": {
            "price": 34000,
            "двигатель": 6.2,
            "разгон до 100": 4.0,
            "выпуск": 2021,
            "страна": "США"
        }
    },
    {
        "Модель": "Tesla Model 3",
        "Класс": "E",
        "Характеристики": {
            "price": 40000,
            "двигатель": "Электрический",
            "разгон до 100": 3.1,
            "выпуск": 2022,
            "страна": "США"
        }
    },
    {
        "Модель": "Porsche 911",
        "Класс": "S",
        "Характеристики": {
            "price": 100000,
            "двигатель": 3.0,
            "разгон до 100": 3.5,
            "выпуск": 2021,
            "страна": "Германия"
        }
    },
    {
        "Модель": "Nissan Altima",
        "Класс": "D",
        "Характеристики": {
            "price": 24000,
            "двигатель": 2.5,
            "разгон до 100": 7.8,
            "выпуск": 2020,
            "страна": "Япония"
        }
    }]

    katalog.extend(cars)
    for installment_car in katalog:
        installment_car['Характеристики']['рассрочка'] = True

    return katalog


def main():
    katalog = create_katalog()
    param = 'выпуск'
    kriteriy = 2020

    car_selection(katalog, param, kriteriy)


if __name__ == '__main__':
    main()
