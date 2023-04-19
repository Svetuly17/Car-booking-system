class Car:
    #конструктор создания автомобиля
    def __init__(self, idCar, statusCar, carLocation):
        self.idCar = idCar
        self.statusCar = statusCar
        self.carLocation = carLocation

    #получение статуса автомобиля
    def gerCarStatus(self):
        return self.statusCar

    # определение ближайшего автомобиля

