from app.models import *
from app.db_functions import *
from app import app, db

# Memberships
def memberships():
    m1 = MembershipPlan()
    m1.name = "Weekly"
    m1.cost = 3.50
    m1.payment_regularity = "weekly"
    m2 = MembershipPlan()
    m2.name = "Monthly"
    m2.cost = 10.99
    m2.payment_regularity = "monthly"
    m3 = MembershipPlan()
    m3.name = "Yearly"
    m3.cost = 99.00
    m3.payment_regularity = "yearly"
    
    db_add(m1, m2, m3)
    
memberships()