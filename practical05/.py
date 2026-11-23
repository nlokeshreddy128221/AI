
# Rule-Based Expert System for Computer Diagnosis

print("Computer Diagnosis Expert System")
print("Answer with yes or no.\n")

internet = input("Is the internet not working? ").lower()
wifi = input("Is Wi-Fi connected? ").lower()
restart = input("Have you restarted the router? ").lower()

# Rules for diagnosis
if internet == "yes" and wifi == "no":
    print("Advice: Connect to the Wi-Fi network.")

elif internet == "yes" and wifi == "yes" and restart == "no":
    print("Advice: Restart the router.")

elif internet == "yes" and wifi == "yes" and restart == "yes":
    print("Advice: Contact your internet service provider.")

else:
    print("Diagnosis: Internet connection is working.")

print("Diagnosis completed.")
