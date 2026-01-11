print("Did you sleep well? (yes/no)")

sleep_well_response = input("Enter your response: ").strip().lower()

print("Are you hungry? (yes/no)")

hungry_response = input("Enter your response:").strip().lower()

print("Is today stressful? (yes/no)")

stressful_response = input("Enter your response:").strip().lower()

if sleep_well_response == "yes" and hungry_response == "no" and stressful_response == "no":
    print("Your mood is \"Happy\"")

elif sleep_well_response == "yes" and hungry_response == "no" and stressful_response == "yes":
    print("Your mood is \"Stressed\"")

