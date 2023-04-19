class Booking:
    #конструктор для создания объекта класса
    def __init__(self, idBooking, startBooking, endBooking, rate, bookingCar,  bookingStatus):
        self.idBooking = idBooking
        self.startBooking = startBooking
        self.endBooking = endBooking
        self.rate = rate
        self.bookingCar = bookingCar
        self.bookingStatus = bookingStatus

    #удаление объекта класса
    def __del__(self):
        print('Booking is deleted')

    #проверка статуса бронирования
    def checkTheBookingStatus(self):
        return self.bookingStatus

    # метод для подтверждения бронировния
    #def confirmTheReservation(self):


    #from datetime import datetime
    #def addCostEstimation (self, idBookin, startBooking, endBooking, rate):

