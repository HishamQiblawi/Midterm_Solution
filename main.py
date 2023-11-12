import json  # Import json module for parsing JSON files
import requests  # Import requests module for making HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup module for parsing HTML files


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


def create_tab(title, url):  # Create a new tab
    return {"title": title, "url": url, "nested_tabs": []}  # Return a new tab object


def open_tab(tabs, current_tab_index, title, url):  # Open a new tab
    tab = create_tab(title, url)  # Create a new tab
    tabs.append(tab)
    current_tab_index = len(tabs) - 1
    print("Opened tab:", title, "with URL:", url)
    return tabs, current_tab_index


def close_tab(tabs, current_tab_index):  # Close the current tab
    if not tabs:
        print("No tabs to close.")
        return tabs, current_tab_index  # Close and update current tabs indices(none)

    index = int(input("Enter the index of the tab to close"))

    if index.strip() == "":  # If the user enters an empty string, close the current tab
        index = current_tab_index  # index for the tab we want to close
    else:
        index = int(index) - 1  # Subtract 1 from the user input to get the correct index

    if 0 <= index < len(tabs):  # Check if the index is valid (in the list)
        closed_tab = tabs.pop(index)  # Pop the tab at the specified index from the list
        current_tab_index = min(current_tab_index, len(tabs) - 1)  # Update the current tab index
        print("Tab has been closed successfully")
    else:
        print("Invalid tab index.")

    return tabs, current_tab_index  # Return the updated list and current tab index


def display_tab_content(tabs, current_tab_index):  # Display the content of the current tab
    if not tabs:  # If there are no tabs, display an error message
        print("No tabs to display.")
        return

    index = input("Enter the index of the tab to display its content (press Enter to display the last opened tab): ")
    if index.strip() == "":  # If the user enters an empty string, display the last opened tab
        index = current_tab_index  # index for the tab we want to display
    else:
        index = int(index) - 1  # Subtract 1 from the user input to get the correct index

    if 0 <= index < len(tabs):  # Check if the index is valid (in the list)
        url = tabs[index]['url']  # Display the content of the tab at the specified index
        try:  # Try to open the URL
            response = requests.get(url)  # Display the content of the tab at the specified index
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            print(f"Content of '{tabs[index]['title']}' ({url}):\n{soup.prettify()}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching content: {e}")
    else:
        print("Invalid tab index.")


def display_all_tabs(tabs):  # Display all tabs
    if not tabs:
        print("No tabs open.")
        return

    tab_number = 1
    for tab in tabs:
        title = tab.get('title', 'Untitled Tab')  # Assuming the title is stored in the 'title' key
        print(tab_number, "tab:", title)
        tab_number += 1  # tab_number is moving up by 1 each time
        display_all_tabs(tab.get('nested_tabs', []))  # dsiplaying all tabs and nested tabs


def open_nested_tab(tabs, current_tab_index):  # Open a new nested tab
    if not tabs:  # If there are no tabs, display an error message
        print("No current tab to nest under.")
        return tabs, current_tab_index

    parent_index = int(input("Enter the index of the parent tab to create nested tabs under: "))
    parent_index -= 1  # Adjust to 0-based index
    if 0 <= parent_index < len(tabs):  # Check if the parent index is valid (in the list)
        nested_title = input("Enter the title for the nested tab:")
        nested_url = input("Enter the URL for the nested tab: ")
        nested_tab = create_tab(nested_title, nested_url)  # create a nested tab
        tabs[parent_index]['nested_tabs'].append(nested_tab)  # add the nested tab to the parent tab's nested tabs list
        print("Opened nested tab: ", nested_title, " under", tabs[parent_index][title])

    else:
        print("Invalid parent tab index.")

    return tabs, current_tab_index


def clear_all_tabs():  # Clear all tabs
    tabs = []
    current_tab_index = None
    print("All tabs cleared.")
    return tabs, current_tab_index


def save_tabs(tabs, file_path):  # Save tabs to a file in json format
    try:
        with open(file_path, "w") as file:
            tabs_data = tabs.copy()  # Creating a copy to avoid modifying the original list
            json.dump(tabs_data, file, indent=2)  # Saving the tabs data to the file
        print(f"Tabs saved successfully to '{file_path}'.")
    except Exception as e:  # If there is an error saving the tabs, display an error message
        print(f"Error saving tabs: {e}")


def import_tabs(file_path):  # Import tabs from a file in json format
    try:
        with open(file_path, "r") as file:  # Reading the tabs data from the file
            tabs_data = json.load(file)  # Loading the tabs data from the file
            tabs = tabs_data.copy()  # Creating a copy to avoid modifying the original list
            current_tab_index = None  # Initializing the current tab index
        print(f"Tabs imported successfully from '{file_path}'.")
    except FileNotFoundError:  # If the file is not found, display an error message
        print("No saved tabs found.")
        tabs = []
        current_tab_index = None
    except Exception as e:  # If there is an error importing the tabs, display an error message
        print(f"Error importing tabs: {e}")
        tabs = []
        current_tab_index = None

    return tabs, current_tab_index  # Return the tabs and current tab index


def update_current_tab_index(tabs, current_tab_index):  # Update the current tab index
    if tabs:
        current_tab_index = min(current_tab_index, len(tabs) - 1)
    else:
        current_tab_index = None

    return current_tab_index


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
            print("tab has been openned succesfully")


        # Prompt the user for the index of the tab to close
        elif choice == "2":
            tabs, current_tab_index = close_tab(tabs, current_tab_index)
        # Prompt the user for the index of the tab to display its content
        elif choice == "3":
            display_tab_content(tabs, current_tab_index)

        # Prompt the user to print the titles of all open tabs.
        elif choice == "4":
            display_all_tabs(tabs)
        elif choice == '5':  # Prompt the user for a title and open a new nested tab with the provided title
            tabs, current_tab_index = open_nested_tab(tabs, current_tab_index)
        elif choice == '6':  # clear all tabs
            tabs, current_tab_index = clear_all_tabs()
        elif choice == '7':  # Save tabs to a file in json format
            file_path = input("Enter the file path to save tabs (e.g., 'tabs.json'): ")
            save_tabs(tabs, file_path)

        elif choice == '8':  # Import tabs from a file in json format
            file_path = input("Enter the file path to import tabs from: ")
            tabs, current_tab_index = import_tabs(file_path)

        elif choice == '9':  # Exit the program
            print("Exiting Browser Tabs. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

        current_tab_index = update_current_tab_index(tabs, current_tab_index)  # Update the current tab index

# REF:
# close_tabe(): https://stackoverflow.com/questions/36249367/stripping-a-string-and-getting-start-index-and-end-index
#https://www.w3schools.com/python/python_json.asp
#https://www.w3schools.com/python/module_requests.asp
#https://medium.com/@kimdang229/python-and-beautifulsoup-web-scraping-tutorial-1d47e7a38fab
#https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/