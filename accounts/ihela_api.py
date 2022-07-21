from ihela_client import MerchantClient
from django.conf import settings

client_id = settings.IHELA_CLIENT_ID
client_secret = settings.IHELA_CLIENT_SECRET
prod = settings.IHELA_API_PROD

auth = MerchantClient(client_id,client_secret,prod)

# def ihela_api_auth():
# 	auth = MerchantClient(client_id,client_secret,prod)

# 	return auth

def ihela_bank_list():
	bank_list = auth.get_bank_list()
	return bank_list

def ihela_api_customer_lookup(bank_slug,customer_id):
	customer = auth.customer_lookup(bank_slug,customer_id)
	return customer

def ihela_api_bill_initiate(amount,account,description,reference,bank=None,bank_client=None,redirect_uri=None):
	bill = auth.init_bill(amount,account,description,reference,bank,bank_client,redirect_uri)

