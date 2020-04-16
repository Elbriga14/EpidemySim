class virus():
    def __init__(self, infectionRadius, infectionChance, daysToSick, daysTillCuredInCare, daysTillCuredNoCare):
        self.InfectionRadius = infectionRadius
        self.InfectionChance = min(infectionChance, 1)
        self.daysToSick = daysToSick
        self.daysTillCuredInCare = daysTillCuredInCare
        self.daysTillCuredNoCare = daysTillCuredNoCare
    def __str__(self):
        return "[V] virus infection radius:           " + str(self.InfectionRadius) + "\n" + "[V] virus infectuosity:               " + str(self.InfectionChance)
