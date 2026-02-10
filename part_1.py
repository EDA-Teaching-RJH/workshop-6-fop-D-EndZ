def main():
    sample_bay =  ["Basalt", "Iron", "Dust", "Silica"]
    for i in range(len(sample_bay)):
        print("Transmitting data for " + sample_bay[i])


    new_findings = []

    #for i in range(3):
    #    rock = input("Give me a rock ")
    #    new_findings.append(rock)

    #print(new_findings)
    
    if "Dust" in sample_bay:
        sample_bay.pop(sample_bay.index("Dust"))
        print("dust removed")
        print(sample_bay)
    else:
            print("dust is not in list")

main()
