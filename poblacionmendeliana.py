# Generación de la poblacion
import scipy # for random numbers

def build_population(N, p):
    """La generación de la población consta de N individuos. Cada individuo tiene dos cromosomas, que contienen el alelo "A" o "a", con probabilidad p o 1-p, respectivamente. La población es una lista de tuplas."""
    population = []
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1= "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population 

# Conteo de frecuencia de alelos
def frequency_count(population):
    """Contar los genotipos. Devuelve un diccionario de frecuencias genotípicas."""
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})

# Reproduccion de la poblacion en el modulo del poblacion mendeliana
def reproduce_population(population):
    """"crear una nueva generación a través de la reproducción. Para cada uno de N nuevos descendientes:
-elegir los padres al azar.
-la descendencia recibe un cromosoma de cada uno de los padres."""
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 a N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        # if offspring == ("a", "a"):
            #next()
        new_generation.append(offspring)
    return new_generation