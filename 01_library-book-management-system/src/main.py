from services.library_service import(
	add_book,
	view_all_books,
	search_book,
	remove_last_added_book,
	total_books)

print("===== Library Book Management System =====")


# main function - starter function
def main():

	while True:
		print("1. Add Book\n2. View All Books\n3. Search Book\n4. Remove Last Added Book\n5. Show Total Books\n6. Exit")
		print("choice : ",end="")
		choice = int(input())
		print()

		match choice:
			case 1: # Add Book
				# call to add_book method of library_service
				# taking input for a book
				print("Enter Book Name : ",end="")
				book = input()
				is_book_added = add_book(book)
				if is_book_added:
					print("Book is added : ",book)
	
				print()

			case 2: #  View All Books
				# call view_all_books method of library_service
				all_books = view_all_books()
				if len(all_books) > 0:
					print("Available Books :")
					# printing all_books
					for le in range(0,len(all_books)):
						print((le+1),". ",all_books[le])
				else:
					print("No Books Found.")

				print()

			case 3: # Searching book
				# taking input of book
				print("Enter Book Name : ",end="")
				book = input()
				# call to search_book method of library_service
				book_found = search_book(book)
				# checking found book
				if book_found:
					print("Book Found : ",book)
				else:
					print("No Book Found.")

				print()

			case 4: # Remove Last Added Book
				# call to remove_last_added_book method of library_service
				is_removed,book_removed = remove_last_added_book()
				if is_removed :
					print("Book Removed : ",book_removed)
				else:
					print("No Books To Remove")
			
				print()
			
			case 5: #Show Total Books
				# call to total_books method of library_service
				count = total_books()
				print("Total Books : ",count)

				print()

			case 6: # Exit
				print("Thank you for using Library Book Management System.")
				return

# starter
if __name__ == "__main__":
	# call main()
	main()
