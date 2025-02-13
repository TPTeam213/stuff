'''
Program that takes two parent genotypes, either mono or di hybrid,
and calculates either the expected genotypes and phenotypic ratios or a chi squared value
with provided observed values. Cannot handle linked genes, only indpendently assorting genes

Greatest list indexer to ever do it
'''

# Function to rearrange the genotype of the offspring so that the capital letter is first
def mono_caps_first(offspring):
    for i in range(2):
        if offspring[i].isupper():
            place_holder = offspring[i]
            offspring.remove(offspring[i])
            offspring.insert(0, place_holder)

# Function to rearrange the genotype of the offspring so that the capital letter is first for each allele pair 
def di_caps_first(offspring):
    for i in range(2):
        if offspring[i].isupper():
            place_holder = offspring[i]
            offspring.remove(offspring[i])
            offspring.insert(0, place_holder)
    for index in range(2, 4):
        if offspring[index].isupper():
            place_holder = offspring[index]
            offspring.remove(offspring[index])
            offspring.insert(2, place_holder)

# Function to determine the possible genotypes of the offspring for a monohybrid cross
def mono_hybrid(p1_geno, p2_geno, skip=False):
    p1_geno = list(p1_geno)
    p2_geno = list(p2_geno)
    global mono_offspring_list
    mono_offspring_list = []
    num = 1
    for i in range(2):
        for index in range (2):
            offspring = p1_geno[i] + p2_geno[index]
            offspring = list(offspring)
            mono_caps_first(offspring)
            offspring = ''.join(offspring)
            mono_offspring_list.append(offspring)
            if not skip:
                print(f'offspring {num} genotype: {offspring}')
                num += 1

# Function to calculate the phenotypic ratio of the offspring for a monohybrid cross 
def mono_calc_ratios(mono_offspring_list, skip=False):
    global counter
    global recess_ratio
    counter = sum(x[0].isupper() for x in mono_offspring_list)
    recess_ratio = 4 - counter
    if not skip:
        print(f'Phenotypic ratio: {counter}:{recess_ratio}')


dom_dom_counter = 0
dom_recess_counter = 0
recess_dom_counter = 0
recess_recess_counter = 0

# Function to parse each genotype created from a dihybrid cross, determine its phenotype, and adjust the counter accordingly 
def get_pheno_numbers(offspring):
    global dom_dom_counter
    global dom_recess_counter
    global recess_dom_counter
    global recess_recess_counter
    if any(offspring[i].isupper() for i in [0, 1]) and any(offspring[index].isupper() for index in [2, 3]):
        dom_dom_counter += 1
    elif any(offspring[i].isupper() for i in [0, 1]):
        dom_recess_counter += 1
    elif any(offspring[i].isupper() for i in [2, 3]):
        recess_dom_counter +=1
    else:
        recess_recess_counter += 1

# Function to take the genotype list from the dihybrid cross function and print them in a 4x4 grid, formatted like it was a punnet square
def print_dihybrid_cross():
    x = 0
    place = 0
    for i in range(4):
        for f in range(4):
            print(di_offspring_list[place], end=' ')
            place += 4
        print()
        x +=  1
        place = x
       
# Function to determine the possible genotypes of the offspring for a dihybrid cross
def di_hybrid(p1_geno, p2_geno, skip=False):
    p1_geno = list(p1_geno)
    p2_geno = list(p2_geno)
    global di_offspring_list
    di_offspring_list = []
    p1_gamete_list = []
    p2_gamete_list = []
    num = 1
    for i in range(2):
        for index in range(2, 4):
            p1_gamete_list.append(p1_geno[i] + p1_geno[index])
            p2_gamete_list.append(p2_geno[i] + p2_geno[index])
    for i in range(4):
        for index in range(4):
            offspring = p1_gamete_list[i][0] + p2_gamete_list[index][0] + p1_gamete_list[i][1] + p2_gamete_list[index][1]
            offspring = list(offspring)
            di_caps_first(offspring)
            get_pheno_numbers(offspring)
            offspring = ''.join(offspring)
            di_offspring_list.append(offspring)
    if not skip:
        print_dihybrid_cross()
        print(f'Phenotype ratios: {dom_dom_counter}:{dom_recess_counter}:{recess_dom_counter}:{recess_recess_counter}')

# Function to take inputted observed values and parental genotypes and calculate the chi squared value 
def chi_square():
    if len(p1_geno) == 4 and len(p2_geno) == 4:
        obs_wt = int(input('Enter the observed amount of wild type offspring: '))
        obs_dr = int(input('Enter the observed amount of dominant/recessive offspring: '))
        obs_rd = int(input('Enter the observed amount of recessive/dominant offspring: '))
        obs_rr = int(input('Enter the observed amount of recessive/recessive offspring: '))
        total_offspring = obs_wt + obs_dr + obs_rd + obs_rr
        di_hybrid(p1_geno, p2_geno, skip=True)
        exp_wt = (total_offspring * dom_dom_counter) / 16
        exp_dr = (total_offspring * dom_recess_counter) / 16
        exp_rd = (total_offspring * recess_dom_counter) / 16
        exp_rr = (total_offspring * recess_recess_counter) / 16
        w = ((obs_wt - exp_wt) ** 2) / exp_wt
        x = ((obs_dr - exp_dr) ** 2) / exp_dr
        y = ((obs_rd - exp_rd) ** 2) / exp_rd
        z = ((obs_rr - exp_rr) ** 2) / exp_rr
        chi = w + x + y + z
        print(f'Chi Square = {chi:.5} with 3 degrees of freedom')
    if len(p1_geno) == 2 and len(p2_geno) == 2:
        obs_wt = int(input('Enter the observed amount of wild type offspring: '))
        obs_r = int(input('Enter the observed amount of recessive type offspring: '))
        total_offspring = obs_wt + obs_r
        mono_hybrid(p1_geno, p2_geno, skip=True)
        mono_calc_ratios(mono_offspring_list, skip=True)
        exp_wt = (counter * total_offspring) / 4
        exp_r = (recess_ratio * total_offspring) / 4
        y = ((obs_wt - exp_wt) ** 2) / exp_wt
        z = ((obs_r - exp_r) ** 2) / exp_r
        chi = y + z
        print(f'Chi Square = {chi:.5} with 1 degree of freedom')
    else:
        print('Something is wrong with your genotypes. This program can handle mono or dihybrid crosses only.')

if __name__ == '__main__':
    p1_geno = input("Enter the genotype of parent 1: ")
    p2_geno = input("Enter the genotype of parent 2: ")
    choice = input('Chi Square or Punnet Square?')

    if choice == 'chi square' or choice == 'Chi Square':
        chi_square()
    elif choice == 'punnet square' or choice == 'Punnet Square':
        if len(p1_geno) == 2 and len(p2_geno) == 2:
            mono_hybrid(p1_geno, p2_geno)
            mono_calc_ratios(mono_offspring_list)
        elif len(p1_geno) == 4 and len(p2_geno) == 4:
            di_hybrid(p1_geno, p2_geno)
        else:
            print('Something is wrong with your genotypes. This program can handle mono or dihybrid crosses only.')
    else:   
        print('That\'s not a choice. Check your spelling (use all lower case)')
