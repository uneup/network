import population
import window

pop = population.population(10000, 0.6, 1.25, 10, 15)

for i in range(200):
    print(pop.next_day())


wn = window.window()
