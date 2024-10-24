class Smartphone:
    def __init__(self, model):
        self.__model = model
        self.__schedule = None

    def get_model(self):
        return self.__model

    def set_schedule(self, schedule):
        self.__schedule = schedule
        schedule.set_smartphone(self)

    def get_schedule(self):
        return self.__schedule
