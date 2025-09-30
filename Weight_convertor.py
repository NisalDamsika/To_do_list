#procProcedural Programing

def weight_convertor(weight,unit):
    if unit=="K":
        print(f"\n-->>Your weight is {weight:.3f} Kg")
    elif unit=="G":
        g_weight=weight/1000
        print(f"\n-->>Your weight is {g_weight:.3f} Kg")
    elif unit=="L":
        L_weight=weight*2.204
        print(f"\n-->>Your weight is {L_weight:.3f} Kg")
    else:
        print("Enter you correct unit")
    
    
    
def main():
    print("============Weight convertor=================")
    try:   
        weight=float(input("Enter your weight:"))
        unit=input("what is your unit Kg(K),gram(G),lab(L):").upper()
        cal=weight_convertor(weight,unit)
    except:
        print("Enter corect values")
    print("\n============Program ended!=================")        
    

main()
    































