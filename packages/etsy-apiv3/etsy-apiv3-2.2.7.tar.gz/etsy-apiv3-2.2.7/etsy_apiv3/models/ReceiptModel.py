from dataclasses import dataclass
from typing import List, Optional
from pydantic import BaseModel
import pycountry
from .PriceModel import Price
from .TransactionModel import Transaction
from .ShipmentModel import Shipment
from .RefundModel import Refund





@dataclass(frozen=True)
class ReceiptType:
    UNSHIPPED = {"was_paid":True, "was_shipped":False}
    SHIPPED = {"was_paid":True, "was_shipped":True}
    UNPAID = {"was_paid":False}
    PAID = {"was_paid":True}
    CANCELED = {"was_canceled":True}


@dataclass(frozen=True)
class ReceiptStatus:
    CANCELED = "Canceled"
    PAID = "Paid"
    COMPLETED = "Completed"
    OPEN = "Open"
    PAYMENT_PROCESSING = "Payment Processing"
    

class Receipt(BaseModel):
    receipt_id: int
    receipt_type: int
    seller_user_id: int
    seller_email: str
    buyer_user_id: int
    buyer_email: Optional[str]
    name: str
    first_line: str
    second_line: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    status: str
    formatted_address: str
    country_iso: str
    payment_method: str
    payment_email: Optional[str]
    message_from_seller: Optional[str]
    message_from_buyer: Optional[str]
    message_from_payment: Optional[str]
    is_paid: bool
    is_shipped: bool
    create_timestamp: int
    update_timestamp: int
    is_gift: bool
    gift_message: Optional[str]
    grandtotal: Price
    subtotal: Price
    total_price: Price
    total_shipping_cost: Price
    total_tax_cost: Price
    total_vat_cost: Price
    discount_amt: Price
    gift_wrap_price: Price
    shipments: Optional[List[Shipment]]
    transactions: List[Transaction]
    refunds: List[Refund]
    
    @property
    def country_name(self):
        return pycountry.countries.get(alpha_2=self.country_iso).name

    @property
    def is_gift_wrap(self):
        if self.gift_wrap_price.amount > 0:
            return True
        return False