
def dose_boron(f4,area,flag:int,cf)->float:
    flux_n = 8.22e13 
    density = 1.03 # density[g/cc]
    Q = 2.31 # energy by boron-neutron reaction [MeV]

    # 1 - tumor 2 - normal brain
    if flag == 1:
        CBE = 3.8
        C = 3.5
    elif flag == 2:
        CBE = 1.3
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
    flux_n = 8.22e13 # neutron flux   - 
    density = 1.03 # density[g/cc]
    CBE = 3.0 
    Q = 0.626 # energy by boron-neutron reaction
    energy = 0.626*(10**6)*1.6*(10**-19) #[J]
    
    total = f4/density*energy*1000 #[J/kg/source] = [Gy/source]
    total = total*flux_n*area # [Gy/sec]
    total = total*3600*CBE #[Gy-eq/h]
    total *= cf #C/F ratio
    return total  


def dose_gamma(f6,area,cf) -> float:
    # f6 [MeV/g/source]
    flux_n = 8.22e13
    RBE = 1.0
    
    total = f6*(10**6)*1.6*(10**-19)*1000 # [J/kg/source] = [Gy/source]
    total = total*flux_n*area # [Gy/sec]
    total = total*3600*RBE # [Gy-eq/h]
    total *= cf
    return total
    
    
# !! Calculate input file excluding Nitrogen !! 
# H2 Dose
def dose_neutron(f6,area,cf) -> float:
    # f6 [MeV/g/source]
    flux_n = 8.22e13
    RBE = 3.2
    
    total = f6*(10**6)*1.6*(10**-19)*1000 # [J/kg/source] = [Gy/source]
    total = total*flux_n*area # [Gy/sec]
    total = total*3600*RBE # [Gy-eq/h]
    total *= cf
    return total
