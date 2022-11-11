from Pages.AccountPage import AccountPage
from Pages.ManagerPage import ManagerPage

def test_as_harry(driver):
    
    HP_account = AccountPage(driver)
    HP_account.login("Harry Potter")
    
    assert 'Failed' in HP_account.make_withdrawl(100)
    
    assert 'Successful' in HP_account.make_deposit(100)
    
    assert len(HP_account.get_transactions()) < 2
    
    HP_account.logout()
    
def test_login_as_manager(driver):
    
    new_customer = ["first_name", "last_name", "post_code"]
    
    manager_account = ManagerPage(driver)
    manager_account.login()
    result_message = manager_account.add_customer(*new_customer)
    assert 'successfully' in result_message
    
    customers = manager_account.get_customers()
    customers = [customer[:3] for customer in customers]
    print(customers)
    
    assert new_customer in customers
    
    
def test_as_ron(driver):
    RW_account = AccountPage(driver)
    RW_account.login("Ron Weasly")
    RW_account.logout()
    RW_account.login("Ron Weasly")
    RW_account.make_deposit(100)
    transactions = RW_account.get_transactions()
    assert transactions[0][1] == '100'