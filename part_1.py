def main():
    sample_bay =  ["Basalt", "Iron", "Dust", "Silica"]
    for i in range(len(sample_bay)):
        print("Transmitting data for " + sample_bay[i])


    new_findings = []

    for i in range(3):
        rock = input("Give me a rock ")
        new_findings.append(rock)

    print(new_findings)

main()
