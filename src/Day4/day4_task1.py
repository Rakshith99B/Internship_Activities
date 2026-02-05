contacts = {"Rakshith":"9901115216",
            "Jeevan":"8088379126",
            "Srujan":"7353617184"
                }
contacts["Shamanth"] = "6361567684"
contacts["Bob"] = "6787564632"

print("Contacts:")
for name, phone in contacts.items():
        print(f"Contact: {name} | Phone: {phone}")

print("\nLookups:")
print("Havyas ->", contacts.get("Havyas", "Contact not found"))
print("Dhanush   ->", contacts.get("Dhanush", "Contact not found"))
