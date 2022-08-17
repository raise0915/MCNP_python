
# area: pi*(10**2) -> brain area

# Boron dose
def dose_boron(f4,area,flag:int,cf):
    flux_n = 10**9 # neutron flux [count/sec]
    density = 1.00 # tissue density[g/cc]
    Q = 2.31 # energy by boron-neutron reaction [MeV]

    # CBE - Compound biological effective factor by BPA
    # C - T\N ratio
    # 1:tumor 2:brain tissue 3:skin
    if flag == 1:
        CBE = 3.8
        C = 1
    elif flag == 2:
        CBE = 1.35
        C = 1/3.5
    elif flag == 3:
        CBE = 2.5
        C = 1/3.5
    else:
        raise Exception('Choose the type of tissue : tumor:1 brain tissue:2 skin:3')
        exit(1)
            
    energy = Q*(10**6)*1.6*(10**-19) #[J]
    I = area*flux_n
    
    total = f4/density*energy*1000 #[J/kg/source] = [Gy/source]
    total = total*I # [Gy/sec]
    total = total*3600*CBE*C #[Gy-eq/h]
    total = total*cf #C/F ratio
    return total

# Nitrogen dose
def dose_nitro(f4,area,cf) -> float:
    flux_n = 10**9 # neutron flux   - 
    density = 1.00  # tissue density[g/cc]
    CBE = 3.0 
    Q = 0.626 # energy produced by reaction
    energy = Q*(10**6)*1.6*(10**-19) #[J]
    I = area*flux_n
    
    total = f4/density*energy*1000 #[J/kg/source] = [Gy/source]
    total = total*I # [Gy/sec]
    total = total*3600*CBE #[Gy-eq/h]
    total = total*cf #C/F ratio
    return total  

# Gamma dose
def dose_gamma(f6,area,cf) -> float:
    # f6 [MeV/g/source]
    flux_n = 10**9
    RBE = 1
    energy = (10**6)*1.6*(10**-19)
    I = area*flux_n
    
    total = f6*energy*1000 # [J/kg/source] = [Gy/source]
    total = total*I # [Gy/sec]
    total = total*3600*RBE # [Gy-eq/h]
    total = total*cf
    return total
    
# !! Calculate input file excluding Nitrogen !! 
# Neutron (Hydrogen) Dose
def dose_neutron(f6,area,cf) -> float:
    # f6 [MeV/g/source]
    flux_n = 10**9
    RBE = 3.0
    energy = (10**6)*1.6*(10**-19)
    I = area*flux_n
    
    total = f6*energy*1000 # [J/kg/source] = [Gy/source]
    total = total*I # [Gy/sec]
    total = total*3600*RBE # [Gy-eq/h]
    total = total*cf
    return total


    
    