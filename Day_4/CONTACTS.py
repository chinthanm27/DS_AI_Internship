
contacts = {
    "Alice": "123-456-7890",
    "Bob": "555-123-4567",
    "Charlie": "987-654-3210"
}
contacts["Diana"] = "222-333-4444"        
contacts["Bob"] = "555-000-1111"          

existing = contacts.get("Alice")
non_existing = contacts.get("Eve", "Contact not found")
print("Contact List:")
for name, number in contacts.items():
    print(f"Contact: {name} | Phone: {number}")

print("\nSafe Lookup Results:")
print(f"Alice: {existing}")
print(f"Eve: {non_existing}")