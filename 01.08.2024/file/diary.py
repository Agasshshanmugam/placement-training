def add_entry(entries, date, text):
    entries.append({'date': date, 'text': text})

def view_entries(entries):
    for entry in entries:
        print(f"Date: {entry['date']}")
        print(f"Entry: {entry['text']}")
        print("")

def main():
    entries = []
    while True:
        print("1. Add entry")
        print("2. View entries")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            text = input("Enter entry text: ")
            add_entry(entries, date, text)
        elif choice == '2':
            view_entries(entries)
        elif choice == '3':
            break

if __name__ == '__main__':
    main()
