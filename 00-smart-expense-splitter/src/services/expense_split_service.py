# method to calculate final bill amount
def final_bill(original_amount, discount, service_charge):
	
	# applying discount on original_amount
	discount_amount = original_amount * discount / 100
	original_amount = original_amount - discount_amount

	# adding service_charge in original_amount
	service_charge_amount = original_amount * service_charge / 100
	payable_amount = original_amount + service_charge_amount

	return payable_amount

# method to calculate amount payable to each person
def split_expense(final_amount, people):

	# now splitting final_amount equally in people
	splitted_amount = final_amount / people

	return splitted_amount


# method to display receipt
def display_receipt(trip_name, original_amount, discount, service_charge, final_amount, per_person_amount):
	print("\n----- Expense Summary -----\n")
	print("Trip/Event Name 	:",trip_name)
	print("Original Bill		: ₹",original_amount)
	print("Discount Applied	:",discount,"%")
	print("Service Charge 		:",service_charge,"%")
	print("Final Bill		: ₹",f"{final_amount:.2f}")
	print("Each Person Pays	: ₹",f"{per_person_amount:.2f}")
