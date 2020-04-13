class virus():
    def __init__(self, infectionRadius, infectionChance, infToDisease):
        self.InfectionRadius = infectionRadius
        self.InfectionChance = min(infectionChance, 1)
        self.infectionToDiseaseSpeed = infToDisease
    def __str__(self):
        return "[V] virus infection radius:           " + str(self.InfectionRadius) + "\n" + "[V] virus infectuosity:               " + str(self.InfectionChance)
