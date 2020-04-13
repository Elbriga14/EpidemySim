class virus():
    def __init__(self, infectionRadius, infectionChance):
        self.InfectionRadius = infectionRadius
        self.InfectionChance = min(infectionChance, 1)
    def __str__(self):
        return "[V] virus infection radius:           " + str(self.InfectionRadius) + "\n" + "[V] virus infectuosity:               " + str(self.InfectionChance)
