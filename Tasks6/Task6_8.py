class Pagination:
    """Implement a Pagination class helpful to arrange text on pages and list content on given page.
     The class should take in a text and a positive integer which indicate how many symbols will be allowed per each
      page (take spaces into account as well). You need to be able to get the amount of whole symbols in text, get
       a number of pages that came out and method that accepts the page number and return quantity of symbols on this
        page. If the provided number of the page is missing print the warning message "Invalid index. Page is missing".
         If you're familliar with using of Excpetions in Python display the error message in this way. Pages indexing
         starts with 0."""

    list_with_symbols = []

    def __init__(self, content: str, symbols):
        self.content = content
        self.symbols = symbols

    def page_count(self):
        page_count = len(self.content) % self.symbols
        return page_count

    def items_count(self):
        items_count = len(self.content)
        return items_count

    def count_items_on_page(self, page):
        list_with_symbols = []
        last = self.symbols
        first = 0
        for i in range(0, len(self.content) % self.symbols - 1, 1):
            list_with_symbols.append(self.content[first:last])
            first += self.symbols
            last += self.symbols
        list_with_symbols.append(self.content[last-self.symbols:])
        try:
            return len(list_with_symbols[page])
        except:
            raise Exception("Invalid index. Page is missing.")

    def find_page(self, text):
        pages_with_text = set()
        next_word = 0

        if self.content.count(text) == 0:
            raise Exception(f"'{text}' is missing on the pages")

        else:
            for i in range(0, self.content.count(text), 1):
                from_page_number = self.content.find(text, next_word) // self.symbols
                pages_with_text.add(from_page_number)
                end_page_number = (self.content.find(text) + len(text)) // self.symbols
                pages_with_text.add(end_page_number)
                next_word = self.content.find(text) + len(text)
            return list(pages_with_text)

    def display_page(self, page):
        list_with_symbols = []
        last = self.symbols
        first = 0
        for i in range(0, len(self.content) % self.symbols - 1, 1):
            list_with_symbols.append(self.content[first:last])
            first += self.symbols
            last += self.symbols
        list_with_symbols.append(self.content[last - self.symbols:])
        try:
            return f"'{list_with_symbols[page]}'"
        except:
            raise Exception("Invalid index. Page is missing.")

pages = Pagination("Your beautiful text", 5)
print(pages.page_count()) # 4
print(pages.items_count()) # 19
print(pages.count_items_on_page(0)) # 5
print(pages.count_items_on_page(3)) # 4
#print(pages.count_items_on_page(4)) #Exception: Invalid index. Page is missing.

print(pages.find_page('Your')) # [0]
print(pages.find_page('e')) # [1, 3]
print(pages.find_page('beautiful')) # [1, 2]
#print(pages.find_page("great")) # Exception: 'great' is missing on the pages
print(pages.display_page(0)) # 'Your '

