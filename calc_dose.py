
def dose_boron(f4,area,flag:int,cf:float)->float:
    flux_n = 10**9 # neutron flux [count/sec]
    density = 1.00 # tissue density[g/cc]
    Q = 2.31 # energy by boron-neutron reaction [MeV]

    # CBE - Compound biological effective factor by BPA
    # tumor:1 brain tissue:2 skin:3
    if flag == 1:
        CBE = 3.8
        C = 3.5
    elif flag == 2:
        CBE = 1.35
        C = 1
    elif flag == 3:
        CBE = 2.5
        C = 1
    else:
        raise Exception('Choose the type of tissue : tumor:1 brain tissue:2 skin:3')
        exit(1)
            
    energy = Q*(10**6)*1.6*(10**-19) #[J]
    
    total = f4/density*energy*1000 #[J/kg/source] = [Gy/source]
    total = total*flux_n*area # [Gy/sec]
    total = total*3600*CBE*C #[Gy-eq/h]
    total *= cf #C/F ratio
    return total

def dose_nitro(f4,area,cf) -> float:
    flux_n = 10**9 # neutron flux   - 
    density = 1.00  # tissue density[g/cc]
    CBE = 3.0 
    Q = 2.31 # energy by boron-neutron reaction
    energy = 2.31*(10**6)*1.6*(10**-19) #[J]
    
    total = f4/density*energy*1000 #[J/kg/source] = [Gy/source]
    total = total*flux_n*area # [Gy/sec]
    total = total*3600*CBE #[Gy-eq/h]
    total *= cf #C/F ratio
    return total  


def dose_gamma(f6,area,cf) -> float:
    # f6 [MeV/g/source]
    flux_n = 10**9
    RBE = 1
    
    total = f6*(10**6)*1.6*(10**-19)*1000 # [J/kg/source] = [Gy/source]
    total = total*flux_n*area # [Gy/sec]
    total = total*3600*RBE # [Gy-eq/h]
    total *= cf
    return total
    
# !! Calculate input file excluding Nitrogen !! 
# H2 Dose
def dose_neutron(f6,area,cf) -> float:
    # f6 [MeV/g/source]
    flux_n = 10**9
    RBE = 3.0
    
    total = f6*(10**6)*1.6*(10**-19)*1000 # [J/kg/source] = [Gy/source]
    total = total*flux_n*area # [Gy/sec]
    total = total*3600*RBE # [Gy-eq/h]
    total *= cf
    return total


    
    