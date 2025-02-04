from defaults import Index


class Statistics:
    def __init__(self, male_population, female_population, **kwargs):
        self.fitness_index = kwargs.get('fitness_index') or Index.FITNESS
        self.male_population = male_population
        self.female_population = female_population
        self.population = zip(self.male_population, self.female_population)
    
    def _calculate_fitness_percent(self, population):
        counter = 0
        for individual in population:
            if individual.fitness >= Index.FITNESS:
                counter += 1
        return counter / len(population) * 100

    def calculate_total_fit_percent(self):
        return self._calculate_fitness_percent(self.population)
    
    def calculate_total_fit_male_percent(self):
        return self._calculate_fitness_percent(self.male_population)
    
    def calculate_total_fit_female_percent(self):
        return self._calculate_fitness_percent(self.female_population)
