# from lib.account_repository import *
# from lib.account import *

# '''
# #all returns a list of all records from the seed data
# '''
# def test_all(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = AccountRepository(db_connection)
#     accounts = repository.all()

#     assert accounts == [
#         Account(1, 'George@hello.com', 'George Orwell'),
#         Account(2, 'Ben@hiya.com', 'Ben Almond')
#     ]

# '''
# #find returns a single account
# where the account matches the query condition
# '''

# def test_find(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = AccountRepository(db_connection)
#     result = repository.find(1)
#     result == Account(1, 'George@hello.com', 'George Orwell')

# '''
# #create makes a new account record entry in the accounts table
# and the new account appears in the table when #all is called
# '''

# def test_create(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = AccountRepository(db_connection)
#     account = Account(None, 'jason@hello.com', 'Jason J Jasonson')
#     repository.create(account)
    
#     assert repository.all() == [
#         Account(1, 'George@hello.com', 'George Orwell'),
#         Account(2, 'Ben@hiya.com', 'Ben Almond'),       
#         Account(3, 'jason@hello.com', 'Jason J Jasonson')
#     ]