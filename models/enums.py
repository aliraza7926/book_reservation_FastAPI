import enum

class UserRole(enum.Enum):
    SYSTEM_ADMIN = "system_admin"
    CUSTOMER = "customer"
    AUTHOR = "author"

class SubscriptionTier(enum.Enum):
    FREE = "free"
    PLUS = "plus"
    PREMIUM = "premium"
