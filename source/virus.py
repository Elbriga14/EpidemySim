class virus():
    def __init__(self, infectionRadius, infectionChance):
        self.InfectionRadius = infectionRadius
        self.InfectionChance = min(infectionChance, 1)