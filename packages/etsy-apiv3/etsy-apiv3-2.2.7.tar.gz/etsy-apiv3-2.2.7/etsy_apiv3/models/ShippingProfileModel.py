from pydantic import BaseModel
from typing import List, Optional
from .ShippingProfileUpgradeModel import ShippingProfileUpgrade
from .ShippingProfileDestinationModel import ShippingProfileDestination


class ShippingProfile(BaseModel):
    shipping_profile_id: int
    title: str
    user_id: int
    min_processing_days: Optional[int]
    max_processing_days: Optional[int]
    processing_days_display_label: str
    origin_country_iso: str
    is_deleted: bool
    shipping_profile_destinations: List[ShippingProfileDestination]
    shipping_profile_upgrades: List[ShippingProfileUpgrade]
    origin_postal_code: Optional[str]
    profile_type: str
    domestic_handling_fee: int
    international_handling_fee: int