# browser_stack.py

class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None

    def open_page(self, url):
        if self.current_page is not None:
            self.back_stack.append(self.current_page)
        self.current_page = url
        self.forward_stack.clear()
        print(f"Opened: {url}")

    def back(self):
        if not self.back_stack:
            print("No pages in back history.")
            return
        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()
        print(f"Back to: {self.current_page}")

    def forward(self):
        if not self.forward_stack:
            print("No pages in forward history.")
            return
        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(f"Forward to: {self.current_page}")

    def show_status(self):
        print("Current page:", self.current_page)
        print("Back stack:", self.back_stack)
        print("Forward stack:", self.forward_stack)


# Example usage
if __name__ == "__main__":
    b = Browser()
    b.open_page("google.com")
    b.open_page("github.com")
    b.open_page("krmu.edu.in")
    b.show_status()
    b.back()
    b.back()
    b.forward()
    b.show_status()
