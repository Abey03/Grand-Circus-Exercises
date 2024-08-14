def heating_cooling(actual_temp, desired_temp):
        if actual_temp < desired_temp:
            print(f"Current Temp {actual_temp}")
            print(f"Desired Temp {desired_temp}")
            print("Run heat")
        elif actual_temp > desired_temp:
            print(f"Current Temp {actual_temp}")
            print(f"Desired Temp {desired_temp}")
            print("Run A/C")
        elif actual_temp == desired_temp:
            print(f"Current Temp {actual_temp}")
            print(f"Desired Temp {desired_temp}")
            print("Standby")

heating_cooling(actual_temp = 60, desired_temp = 70)
heating_cooling(actual_temp = 68, desired_temp = 65)
heating_cooling(actual_temp= 60, desired_temp= 60)
heating_cooling(actual_temp= int(input("Enter current temp: ")), desired_temp= int(input("Enter desired temp: ")))
