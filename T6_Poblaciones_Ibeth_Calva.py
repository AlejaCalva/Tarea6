#!/usr/bin/env python
# coding: utf-8

# # BIOINFORMÁTICA
# - Nombre: Ibeth Calva
# - Grupo: 1
# - Fecha: 18/07/2022

# In[1]:


import poblacionmendeliana


# In[2]:


poblacionmendeliana.build_population(25, 0.43)


# In[5]:


my_pop = poblacionmendeliana.build_population(500, 0.21)


# In[11]:


import numpy as np
np.random.seed(seed=123)
my_pop = poblacionmendeliana.build_population(500, 0.21)


# In[12]:


fmy_pop = poblacionmendeliana.frequency_count(my_pop)
print(fmy_pop)


# In[14]:


fmy_pop = poblacionmendeliana.frequency_count(my_pop)
print(fmy_pop)
print((500-fmy_pop["aa"])/500)


# In[17]:


print(poblacionmendeliana.frequency_count(my_pop))
new_pop = poblacionmendeliana.reproduce_population(my_pop)
new_pop2 = poblacionmendeliana.reproduce_population(new_pop)
print(poblacionmendeliana.frequency_count(new_pop))
print(poblacionmendeliana.frequency_count(new_pop2))


# In[20]:


# import poblaciones as pbc\n",

pop0 = poblacionmendeliana.build_population(10, 0.35)
allele_pop0 = poblacionmendeliana.frequency_count(pop0)
pop1 = poblacionmendeliana.reproduce_population(pop0)
allele_pop1 = poblacionmendeliana.frequency_count(pop1)

print(pop0)
print(allele_pop0)
print(pop1)
print(allele_pop1)


# In[21]:


def simulate_drift(N, p):
    # initialize the population
    my_pop = poblacionmendeliana.build_population(N, p)
    fixation = False # condiciòn incial de fijacion
    num_generations = 0 # población parental
    while fixation == False:
        # compute genotype counts
        genotype_counts = poblacionmendeliana.frequency_count(my_pop)
        # if one allele went to fixation, end
        if (genotype_counts["AA"] == N or genotype_counts["aa"] == N):
            print("An allele reached fixation at generation", num_generations)
            print("The genotype counts are")
            print(genotype_counts)
            fixation == True
            break
        # if not, reproduce
        my_pop = poblacionmendeliana.reproduce_population(my_pop)
        num_generations += 1
    return num_generations, genotype_counts


# In[22]:


sim1 = simulate_drift(500, 0.5 ) #simulacion de generacion
sim1


# In[27]:


Generacion500 = poblacionmendeliana.build_population(500,0.5) #genero 500 individuos con una probabilidad de 50% 
print(Generacion500) # ver generacion 500
Conteo = poblacionmendeliana.frequency_count(Generacion500) # contar el numero de alelos en generacion 500
print(Conteo) #imprimo este conteo
len(Generacion500) # para saber el numero de individuos que tengo en la generacion

