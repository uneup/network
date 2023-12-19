class population:
    def __init__(self, total_population, infectivity, contact_rate_infectious, average_incub_time, duration_of_illness):
        """
        :param total_population: Население
        :param infectivity: Передача инфекции
        :param contact_rate_infectious: Контакт с больными
        :param average_incub_time: Инкубационный период
        :param duration_of_illness: Продолжительность болезни
        """
        self.size = total_population - 1
        self.latently_infected = 0
        self.infected = 1
        self.recovered = 0

        self.total_pop = total_population
        self.infectivity = infectivity
        self.contact_rate_infectious = contact_rate_infectious
        self.average_incub_time = average_incub_time
        self.duration_of_illness = duration_of_illness

    def _exposed_rate(self):
        tmp = self.infected*self.contact_rate_infectious*self.infectivity*self.size/self.total_pop
        self.latently_infected += tmp
        self.size -= tmp

    def _infectious_rate(self):
        tmp = self.latently_infected / self.average_incub_time
        self.infected += tmp
        self.latently_infected -= tmp

    def _recovered_rate(self):
        tmp = self.infected / self.duration_of_illness
        self.recovered += tmp
        self.infected -= tmp

    def next_day(self):
        self._exposed_rate()
        self._infectious_rate()
        self._recovered_rate()
        return {"size": int(self.size), "latently_infected": int(self.latently_infected), "infected": int(self.infected), "recovered": int(self.recovered)}