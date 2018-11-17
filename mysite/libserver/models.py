from django.db import models

# class User_details(models.Model):
# ''' 
# 	id
# 	username
# 	roll no.
# 	dob
# 	fine || fine history
# 	books issued   
# 	books_holded   -----> create a json data // at max 4 books can be holded// store only book id
# 	user history	
# 	searched books
	
# 	def __str__():
# 		retunr id
# 	def holded_books():
# 		L = []
# 		for i in books_holded:  ----> not so effective way to do it.
# 			L.append(i)
# 		return L
# 	def books_issued():
# 		L = list()
# 		for i in books_issued:  ----> not so effective way to do it.
# 			L.append(i)
# 		return L
# 	def 	

#  '''

# class Book_details(models.Model):
# '''
# 	book id
# 	book name
# 	author name
# 	publication name
# 	book jouner
# 	book descrpton
# 	no. of issued
# 	past issuers

# 	actual no. of books 
# 	now , how many are left
# '''

# class Loan_info(models.Model):
# '''
# 	issuer_id ---->
# 	book_id ----->
# 	date_issued 
# 	date_to_be_returned

# '''	
# '''
# if book returned:
# 	If book_returned.date() < date_to_be_returned :
# 		no fine,

# 	else 
# 		add fine according to that	
# 	increment "now, how many left"
# 	remove user from Loan_info : schema be  // select * from Loan_info where book_id = "" and user_id = " "	
# 	r
# 	if(todays.date() < date_to_be_returned):
# 		fine += 0
# 	else 
# 		fine += accordingly
# 	delete * from Loan_info
# else:
# 	details will be avlble on Loan_info 
# 	if(today.date() - book_to_be_returned is equal to 1):
# 		inform user to return book;
			
# '''

# '''
#  trending books : the book which has more no. of issues 
#  Efficient search bar

# '''

# '''
#  when user entered into the main page
#  	@logged in
#  	def show_following_things():
#  		// users have right for to edit their profile
#  		// past views
#  		// trending books
#  		// machine learning - see the time 
#  		// u r selling ur books _ so u need to think in that way
# 	def holding_process():
# 		if book is holded implies 
# 			reduce size of book_avlble by 1
# 			if(book checked_out in 32 hours) okay
# 			otherwise
# 				increase it by 1 
# 		add book_id into books_holded

				


# '''
# ''' 
# 	book jouner , book info 
# 	create a new jouner or add it into the previous , can add many jouner to same book.
# 	if new_jouner_created():
# 		add details of this in main page that ya new jouner is created in left sub head with a very
# 		classic view.
# 	else
# 		add it on 	
# '''
# '''
# 	nuggets.life
# 	help me endaveour the basics of everything....
# 	// real time chat application ...
# 	// apps should have some motive ...
# 	// must be run by sometihng ... // on the top of block chain 

	 	
# '''