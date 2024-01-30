# Require dependencies
import urllib.request
import urllib.parse
import json
import re


# Classes

# MWC Pay class
class MwcPay:

	# Constructor
	def __init__(self, privateServer: str = "http://localhost:9010") -> None:
	
		# Check if paramaters are invalid
		if isinstance(privateServer, str) is False:
		
			# Throw error
			raise TypeError("Invalid parameters")
			
		# Set private server
		self._privateServer = privateServer
	
	# Create payment
	def createPayment(self, price: str | None, requiredConfirmations: int | None, timeout: int | None, completedCallback : str, receivedCallback: str | None = None, confirmedCallback: str | None = None, expiredCallback: str | None = None) -> dict[str, str, str] | bool | None:
	
		# Check if parameters are invalid
		if (isinstance(price, str) is False and price is not None) or (isinstance(requiredConfirmations, int) is False and requiredConfirmations is not None) or (isinstance(timeout, int) is False and timeout is not None) or isinstance(completedCallback, str) is False or (isinstance(receivedCallback, str) is False and receivedCallback is not None) or (isinstance(confirmedCallback, str) is False and confirmedCallback is not None) or (isinstance(expiredCallback, str) is False and expiredCallback is not None):
		
			# Return None
			return None
			
		# Try
		try:
		
			# Send create payment request to the private server
			with urllib.request.urlopen("{}/create_payment?{}".format(self._privateServer, urllib.parse.urlencode({key: value for key, value in {
			
				# Price
				"price": price,
				
				# Required confirmations
				"required_confirmations": requiredConfirmations,
				
				# Timeout
				"timeout": timeout,
				
				# Completed callback
				"completed_callback": completedCallback,
				
				# Received callback
				"received_callback": receivedCallback,
				
				# Confirmed callback
				"confirmed_callback": confirmedCallback,
				
				# Expired callback
				"expired_callback": expiredCallback
				
			}.items() if value is not None}))) as createPaymentResponse:
			
				# Get payment info from create payment response
				paymentInfo = json.loads(createPaymentResponse.read())
				
				# Check if payment info's payment ID, URL, or recipient payment proof address are invalid
				if isinstance(paymentInfo, dict) is False or "payment_id" not in paymentInfo or isinstance(paymentInfo["payment_id"], str) is False or paymentInfo["payment_id"] == "" or "url" not in paymentInfo or isinstance(paymentInfo["url"], str) is False or paymentInfo["url"] == "" or "recipient_payment_proof_address" not in paymentInfo or isinstance(paymentInfo["recipient_payment_proof_address"], str) is False or paymentInfo["recipient_payment_proof_address"] == "":
				
					# Return false
					return False
				
				# Return payment info's payment ID, URL, and recipient payment proof address
				return {
				
					# Payment ID
					"payment_id": paymentInfo["payment_id"],
					
					# URL
					"url": paymentInfo["url"],
					
					# Recipient payment proof address
					"recipient_payment_proof_address": paymentInfo["recipient_payment_proof_address"]
				}
		
		# Catch HTTP errors
		except urllib.error.HTTPError as error:
		
			# Check if an error occurred on the private server
			if error.code == 500:
			
				# Return false
				return False
			
			# Otherwise assume request was invalid
			else:
			
				# Return none
				return None
		
		# Catch errors
		except:
		
			# Return false
			return False
	
	# Get payment info
	def getPaymentInfo(self, paymentId: str) -> dict[str, str | None, int, bool, int, int | None, str, str] | bool | None:
	
		# Check if parameters are invalid
		if isinstance(paymentId, str) is False:
		
			# Return None
			return None
			
		# Try
		try:
		
			# Send get payment info request to the private server
			with urllib.request.urlopen("{}/get_payment_info?{}".format(self._privateServer, urllib.parse.urlencode({
			
				# Payment Id
				"payment_id": paymentId
				
			}))) as getPaymentInfoResponse:
			
				# Get payment info from get payment info response
				paymentInfo = json.loads(getPaymentInfoResponse.read())
				
				# Check if payment info's URL, price, required confirmations, received, confirmations, time remaining, status, or recipient payment proof address are invalid
				if isinstance(paymentInfo, dict) is False or "url" not in paymentInfo or isinstance(paymentInfo["url"], str) is False or paymentInfo["url"] == "" or "price" not in paymentInfo or (paymentInfo["price"] is not None and isinstance(paymentInfo["price"], str) is False) or (paymentInfo["price"] is not None and re.match("^(?:0(?:\.\d+)?|[1-9]\d*(?:\.\d+)?)$", paymentInfo["price"]) is None) or "required_confirmations" not in paymentInfo or isinstance(paymentInfo["required_confirmations"], int) is False or paymentInfo["required_confirmations"] <= 0 or "received" not in paymentInfo or isinstance(paymentInfo["received"], bool) is False or "confirmations" not in paymentInfo or isinstance(paymentInfo["confirmations"], int) is False or paymentInfo["confirmations"] < 0 or paymentInfo["confirmations"] > paymentInfo["required_confirmations"] or "time_remaining" not in paymentInfo or (paymentInfo["time_remaining"] is not None and isinstance(paymentInfo["time_remaining"], int) is False) or (paymentInfo["time_remaining"] is not None and paymentInfo["time_remaining"] < 0) or "status" not in paymentInfo or isinstance(paymentInfo["status"], str) is False or "recipient_payment_proof_address" not in paymentInfo or isinstance(paymentInfo["recipient_payment_proof_address"], str) is False or paymentInfo["recipient_payment_proof_address"] == "":
				
					# Return false
					return False
				
				# Return payment info's URL, price, required confirmations, received, confirmations, time remaining, status, and recipient payment proof address
				return {
				
					# URL
					"url": paymentInfo["url"],
					
					# Price
					"price": paymentInfo["price"],
					
					# Required confirmations
					"required_confirmations": paymentInfo["required_confirmations"],
					
					# Received
					"received": paymentInfo["received"],
					
					# Confirmations
					"confirmations": paymentInfo["confirmations"],
					
					# Time remaining
					"time_remaining": paymentInfo["time_remaining"],
					
					# Status
					"status": paymentInfo["status"],
					
					# Recipient payment proof address
					"recipient_payment_proof_address": paymentInfo["recipient_payment_proof_address"]
				}
		
		# Catch HTTP errors
		except urllib.error.HTTPError as error:
		
			# Check if an error occurred on the private server
			if error.code == 500:
			
				# Return false
				return False
			
			# Otherwise assume request was invalid
			else:
			
				# Return none
				return None
		
		# Catch errors
		except:
		
			# Return false
			return False
	
	# Get price
	def getPrice(self) -> str | bool | None:
	
		# Try
		try:
		
			# Send get price request to the private server
			with urllib.request.urlopen("{}/get_price".format(self._privateServer)) as getPriceResponse:
			
				# Get price from get price response
				price = json.loads(getPriceResponse.read())
				
				# Check if price is invalid
				if isinstance(price, dict) is False or "price" not in price or isinstance(price["price"], str) is False or re.match("^(?:0(?:\.\d+)?|[1-9]\d*(?:\.\d+)?)$", price["price"]) is None:
				
					# Return false
					return False
				
				# Return price
				return price["price"]
		
		# Catch HTTP errors
		except urllib.error.HTTPError as error:
		
			# Check if an error occurred on the private server
			if error.code == 500:
			
				# Return false
				return False
			
			# Otherwise assume request was invalid
			else:
			
				# Return none
				return None
		
		# Catch errors
		except:
		
			# Return false
			return False
	
	# Get public server info
	def getPublicServerInfo(self) -> dict[str, str | None] | bool | None:
	
		# Try
		try:
		
			# Send get public server info request to the private server
			with urllib.request.urlopen("{}/get_public_server_info".format(self._privateServer)) as getPublicServerInfoResponse:
			
				# Get public server info from get public server info response
				publicServerInfo = json.loads(getPublicServerInfoResponse.read())
				
				# Check if public server info's URL or Onion Service address are invalid
				if isinstance(publicServerInfo, dict) is False or "url" not in publicServerInfo or isinstance(publicServerInfo["url"], str) is False or publicServerInfo["url"] == "" or "onion_service_address" not in publicServerInfo or (publicServerInfo["onion_service_address"] is not None and isinstance(publicServerInfo["onion_service_address"], str) is False) or (publicServerInfo["onion_service_address"] is not None and publicServerInfo["onion_service_address"] == ""):
				
					# Return false
					return False
				
				# Return public server info's URL and Onion Service address
				return {
				
					# URL
					"url": publicServerInfo["url"],
					
					# Onion Service address
					"onion_service_address": publicServerInfo["onion_service_address"]
				}
		
		# Catch HTTP errors
		except urllib.error.HTTPError as error:
		
			# Check if an error occurred on the private server
			if error.code == 500:
			
				# Return false
				return False
			
			# Otherwise assume request was invalid
			else:
			
				# Return none
				return None
		
		# Catch errors
		except:
		
			# Return false
			return False
