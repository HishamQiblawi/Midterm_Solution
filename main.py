def print_menu():  # Print the menu options
    print("Welcome to Browser Tabs!")
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Clear All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")


def create_tab(title, url):
    return {"title": title, "url": url, "nested_tabs": []}


def open_tab(tabs, current_tab_index, title, url):
    tab = create_tab(title, url)
    tabs.append(tab)
    current_tab_index = len(tabs) - 1
    print("Opened tab:", title, "with URL:", url)
    return tabs, current_tab_index


def close_tab(tabs, current_tab_index):
    if not tabs:
        print("No tabs to close.")
        return tabs, current_tab_index

    index = input("Enter the index of the tab to close")

    if index.strip() == "":
        index = current_tab_index
    else:
        index = int(index) - 1

    if 0 <= index < len(tabs):
        closed_tab = tabs.pop(index)
        current_tab_index = min(current_tab_index, len(tabs) - 1)
        print("Closed tab:", closed_tab["title"])
    else:
        print("Invalid tab index.")

    return tabs, current_tab_index


if __name__ == "__main__":
    tabs = []  # List to store open tabs
    current_tab_index = None  # Index of the currently selected tab

    # Display the menu options and prompt the user for a choice
    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            # Prompt the user for a title and open a new tab with the provided title
            title = input("Enter the title for the new tab: ")
            url = input("Enter the URL for the new tab: ")
            tabs, current_tab_index = open_tab(tabs, current_tab_index, title, url)
            print("tab has been added")


        # Prompt the user for the index of the tab to close
        elif choice == "2":
            tabs, current_tab_index = close_tab(tabs, current_tab_index)


