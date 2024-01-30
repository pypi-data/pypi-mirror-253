# MWC Pay Python SDK

### Description
Python SDK for [MWC Pay](https://github.com/NicolasFlamel1/MWC-Pay).

### Installing
Run the following command to install this library.
```
pip install nicolasflamel.mwc-pay
```

### Usage
After an `MwcPay` object has been created, it can be used to create payments, query the status of payments, get the current price of MimbleWimble coin, and get info about MWC Pay's public server.

A high level overview of a payment's life cycle when using this SDK consists of the following steps:
1. The merchant creates a payment and gets the payment's URL from the response.
2. The buyer sends MimbleWimble Coin to that URL.
3. The merchant can optionally monitor the payment's status via the `getPaymentInfo` method, the `createPayment` method's `received_callback` parameter, the `createPayment` method's `confirmed_callback` parameter, and/or the `createPayment` method's `expired_callback` parameter.
4. The payment's completed callback is ran once the payment achieves the desired number of on-chain confirmations.

The following code briefly shows how to use this SDK. A more complete example with error checking is available [here](https://github.com/NicolasFlamel1/MWC-Pay-Python-SDK/tree/master/example).
```
# Require dependencies
from nicolasflamel.mwc_pay import MwcPay

# Initialize MWC Pay
mwcPay = MwcPay("http://localhost:9010")

# Create payment
payment = mwcPay.createPayment("123.456", 5, 600, "http://example.com/completed", "http://example.com/received", "http://example.com/confirmed", "http://example.com/expired")

# Get payment info
paymentInfo = mwcPay.getPaymentInfo(payment["payment_id"])

# Get price
price = mwcPay.getPrice()

# Get public server info
publicServerInfo = mwcPay.getPublicServerInfo()
```

### Functions
1. MWC Pay constructor: `constructor(privateServer: str = "http://localhost:9010") -> MwcPay`

   This constructor is used to create an `MwcPay` object and it accepts the following parameter:
   * `privateServer: str` (optional): The URL for your MWC Pay's private server. If not provided then the default value `http://localhost:9010` will be used.

   This method returns the following value:
   * `MwcPay`: An `MwcPay` object.

2. MWC Pay create payment method: `createPayment(price: str | None, requiredConfirmations: int | None, timeout: int | None, completedCallback: str, receivedCallback: str | None = None, confirmedCallback: str | None = None,  expiredCallback: str | None = None) -> dict[str, str] | bool | None`

   This method is used to create a payment and it accepts the following parameters:
   * `price: str | None`: The expected amount for the payment. If `None` then any amount will fulfill the payment.
   * `requiredConfirmations: int | None`: The required number of on-chain confirmations that the payment must have before it's considered complete. If `None` then one required confirmation will be used.
   * `timeout: int | None`: The duration in seconds that the payment can be received. If `None` then the payment will never expire.
   * `completedCallback: str`: The HTTP GET request that will be performed when the payment is complete. If the response status code to this request isn't `HTTP 200 OK`, then the same request will be made at a later time. This request can't follow redirects. This request may happen multiple times despite a previous attempt receiving an `HTTP 200 OK` response status code, so make sure to prepare for this and to respond to all requests with an `HTTP 200 OK` response status code if the request has already happened. All instances of `__id__`, `__completed__`, and `__received__` are replaced with the payment's ID, completed timestamp, and received timestamp respectively.
   * `receivedCallback: str | None` (optional): The HTTP GET request that will be performed when the payment is received. If the response status code to this request isn't `HTTP 200 OK`, then an `HTTP 500 Internal Error` response will be sent to the payment's sender when they are sending the payment. This request can't follow redirects. This request may happen multiple times despite a previous attempt receiving an `HTTP 200 OK` response status code, so make sure to prepare for this and to respond to all requests with an `HTTP 200 OK` response status code if the request has already happened. All instances of `__id__`, `__price__`, `__sender_payment_proof_address__`, `__kernel_commitment__`, and `__recipient_payment_proof_signature__` are replaced with the payment's ID, price, sender payment proof address, kernel commitment, and recipient payment proof signature respectively. If not provided or `None` then no request will be performed when the payment is received.
   * `confirmedCallback: str | None` (optional): The HTTP GET request that will be performed when the payment's number of on-chain confirmations changes and the payment isn't completed. The response status code to this request doesn't matter. This request can't follow redirects. All instances of `__id__`, and `__confirmations__` are replaced with the payment's ID and number of on-chain confirmations respectively. If not provided or `None` then no request will be performed when the payment's number of on-chain confirmations changes.
   * `expiredCallback: str | None` (optional): The HTTP GET request that will be performed when the payment is expired. If the response status code to this request isn't `HTTP 200 OK`, then the same request will be made at a later time. This request can't follow redirects. This request may happen multiple times despite a previous attempt receiving an `HTTP 200 OK` response status code, so make sure to prepare for this and to respond to all requests with an `HTTP 200 OK` response status code if the request has already happened. All instances of `__id__` are replaced with the payment's ID. If not provided or `None` then no request will be performed when the payment is expired.

   This method returns the following values:
   * `dict[str, str]`: The payment was created successfully. This object contains the `payment_id: str`, `url: str`, and `recipient_payment_proof_address: str` of the created payment.
   * `False`: An error occurred on the private server and/or communicating with the private server failed.
   * `None`: Parameters are invalid.

3. MWC Pay get payment info method: `getPaymentInfo(paymentId: str) -> dict[str, str | int | bool | None] | bool | None`

   This method is used to get the status of a payment and it accepts the following parameter:
   * `paymentId: str`: The payment's ID.

   This method returns the following values:
   * `dict[str, str | int | bool | None]`: This object contains the payment's `url: str`, `price: str | None`, `required_confirmations: int`, `received: bool`, `confirmations: int`, `time_remaining: int | None`, `status: str`, and `recipient_payment_proof_address: str`. The `status: str` can be one of the following values: `Expired`, `Not received`, `Received`, `Confirmed`, or `Completed`.
   * `False`: An error occurred on the private server and/or communicating with the private server failed.
   * `None`: Parameters are invalid and/or the payment doesn't exist.

4. MWC Pay get price method: `getPrice() -> str | bool | None`

   This method is used to get the price of MimbleWimble coin and it returns the following values:
   * `string`: The price of MimbleWimble Coin in USDT.
   * `False`: An error occurred on the private server and/or communicating with the private server failed.
   * `None`: Parameters are invalid and/or the price API is disabled on the private server.

5. MWC Pay get public server info method: `getPublicServerInfo() -> dict[str, str | None] | bool | None`

   This method is used to get info about MWC Pay's public server and it returns the following values:
   * `dict[str, str | None]`: This object contains the public server's `url: str` and `onion_service_address: str | None`.
   * `False`: An error occurred on the private server and/or communicating with the private server failed.
   * `None`: Parameters are invalid.
