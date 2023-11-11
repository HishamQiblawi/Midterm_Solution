import json


def tab_menu():
    while True:
        print("Hello")
        print("1. open tab")
        print("2. close tab")
        print("3.switch Tab")
        print("4.display All Tabs")
        print("5.open Nested Tab")
        print("6.clear All Tabs")
        print("7.save Tabs")
        print("8.import Tabs")
        print("9.exit")
        choice = int(input("Enter a number:"))

        if choice == 1:


print(tab_menu())


def tab1(title, url):
    return {"title": title, "url": url}


def tab2(title, url):
    return {"title": title, "url": url}


def tab3(title, url):
    return {"title": title, "url": url}