def main():
    tabs = [
        {
            "title": "youtube",
            "url": "https://www.youtube.com"
        },
        {
            "title": "google",
            "url": "https://www.google.com"
        },

        {"title": "facebook",
         "url": "https://www.facebook.com"
         }
    ]

    def menu():
        while True:
            print("Hello")
            print("1.open tab")
            print("2.close tab")
            print("3.switch Tab")
            print("4.display All Tabs")
            print("5.open Nested Tab")
            print("6.clear All Tabs")
            print("7.save Tabs")
            print("8.import Tabs")
            print("9.exit")
            choice = int(input("Enter a number:"))

            if choice == "1":
                title = input("Enter a title: ")
                url = input("Enter url: ")
                open_tab(title, url)

            if choice == 2:
                close = int(input("Enter a number"))
                close_tab()

    def open_tab(title, url):
        tabs.append({"title": title, "url": url})

    def close_tab():
        for close in range(0, (len(tabs) - 1)):
            if close == (len(tabs) - 1):
                tabs.pop()
            tabs[close]

    print(menu())


if __name__ == "__main__":
    main()


