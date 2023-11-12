import requests
from bs4 import BeautifulSoup


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


def display_tab_content(tabs, current_tab_index):
    if not tabs:
        print("No tabs to display.")
        return

    index = input("Enter the index of the tab to display its content (press Enter to display the last opened tab): ")
    if index.strip() == "":
        index = current_tab_index
    else:
        index = int(index) - 1

    if 0 <= index < len(tabs):
        url = tabs[index]['url']
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            print(f"Content of '{tabs[index]['title']}' ({url}):\n{soup.prettify()}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching content: {e}")
    else:
        print("Invalid tab index.")


def display_all_tabs(tabs):
    if not tabs:
        print("No tabs open.")
        return
    for i, tab in enumerate(tabs, start=1):
        print(i, "tab", [title])
        display_all_tabs(tab['nested_tabs'])


def open_nested_tab(tabs, current_tab_index):
    if not tabs:
        print("No current tab to nest under.")
        return tabs, current_tab_index
    parent_index = int(input("Enter the index of the parent tab to create nested tabs under: "))
    parent_index -= 1  # Adjust to 0-based index
    if 0 <= parent_index < len(tabs):
        nested_title = input("Enter the title for the nested tab:")
        nested_url = input("Enter the URL for the nested tab: ")


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
        # Prompt the user for the index of the tab to display its content
        elif choice == "3":
            display_tab_content(tabs, current_tab_index)

        # Prompt the user to print the titles of all open tabs.
        elif choice == "4":
            display_all_tabs(tabs)


