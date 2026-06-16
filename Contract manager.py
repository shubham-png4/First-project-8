from datetime import datetime

class Contact:
    def __init__(self, name, phone, email, address, category="Personal"):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.category = category
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def __str__(self):
        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name: {self.name}
Phone: {self.phone}
Email: {self.email}
Address: {self.address}
Category: {self.category}
Added: {self.created_at}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self):
        print("\n➕ ADD NEW CONTACT")
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()
        address = input("Address: ").strip()
        category = input("Category (Personal/Business/Work): ").strip() or "Personal"
        
        contact = Contact(name, phone, email, address, category)
        self.contacts.append(contact)
        print(f"✅ Contact '{name}' added!")
    
    def search_contact(self):
        search_term = input("Search by name: ").strip().lower()
        results = [c for c in self.contacts if search_term in c.name.lower()]
        
        if results:
            print(f"\n🔍 Found {len(results)} contact(s):")
            for contact in results:
                print(contact)
        else:
            print("❌ No contacts found!")
    
    def filter_by_category(self):
        category = input("Filter by category: ").strip()
        results = [c for c in self.contacts if c.category == category]
        
        if results:
            print(f"\n📁 {len(results)} contacts in '{category}':")
            for contact in results:
                print(contact)
        else:
            print(f"❌ No contacts in category '{category}'!")
    
    def delete_contact(self):
        name = input("Enter name to delete: ").strip()
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts.pop(i)
                print(f"✅ Contact '{name}' deleted!")
                return
        print("❌ Contact not found!")
    
    def display_all(self):
        if not self.contacts:
            print("📭 No contacts yet!")
            return
        
        print(f"\n📚 TOTAL CONTACTS: {len(self.contacts)}")
        print("=" * 50)
        for contact in self.contacts:
            print(contact)
    
    def get_statistics(self):
        if not self.contacts:
            return
        
        categories = {}
        for contact in self.contacts:
            cat = contact.category
            categories[cat] = categories.get(cat, 0) + 1
        
        print("\n📊 CONTACT STATISTICS")
        print("=" * 40)
        for cat, count in categories.items():
            print(f"{cat}: {count} contacts ({count/len(self.contacts)*100:.1f}%)")
        print("=" * 40)
    
    def menu(self):
        while True:
            print("\n" + "=" * 50)
            print("📱 CONTACT MANAGEMENT SYSTEM")
            print("=" * 50)
            print("1. Add Contact")
            print("2. Search Contact")
            print("3. Filter by Category")
            print("4. Delete Contact")
            print("5. View All Contacts")
            print("6. View Statistics")
            print("7. Exit")
            print("=" * 50)
            
            choice = input("Choose: ").strip()
            
            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.search_contact()
            elif choice == "3":
                self.filter_by_category()
            elif choice == "4":
                self.delete_contact()
            elif choice == "5":
                self.display_all()
            elif choice == "6":
                self.get_statistics()
            elif choice == "7":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice!")

# Run the program
manager = ContactManager()
manager.menu()