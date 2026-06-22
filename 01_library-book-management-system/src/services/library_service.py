# taking empty list to store books
books = list()

# method to add new book in library
def add_book(new_book):
	# need to add new_book in books
	books.append(new_book)

	# returning updated list of books
	return True

# method to view all books in library
def view_all_books():
	return books;# returning list of books

# method to search book
def search_book(book):
	# tarversing book
	for le in range(0,len(books)):
		if book==books[le]:
			return True
	
	return False

# method to remove last added book
def remove_last_added_book():
	if len(books) == 0:
		return False,None

	# removing last book
	removed_book = books.pop()

	return True,removed_book

# method to return total books count
def total_books():
	return len(books)