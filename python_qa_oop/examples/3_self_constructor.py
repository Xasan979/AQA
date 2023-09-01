class Page:
    class_attribute = "CLASS_ATTR"

    def __init__(self, name):
        self.name = name
        self.new_attr = "NEW_ATTR"

    def open(self):
        print("Opened: " + self.name)

    def show(self):
        print(self.class_attribute)


main_page = Page(name="MainPage")
login_page = Page(name="LoginPage")

print(main_page.new_attr)

main_page.show()
login_page.show()
