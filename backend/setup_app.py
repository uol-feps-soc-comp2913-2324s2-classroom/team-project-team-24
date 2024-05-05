import stripe
from app.models import *
from app.db_functions import *
import random
from datetime import date

stripe.api_key = "sk_test_51PBedsRq4UQ9omwxmLSrDcG9TL8bmhprG5G7LFiCszpoghpS2QTZjjimEO4571P4h40WQNgv8pOhiVXHvi2wuGq60093lrCCiF"

memberships = [
    {
        "name": "Weekly",
        "price": 1.99,
        "payment_regularity": "weekly",
        "interval": "week",
    },
    {
        "name": "Monthly",
        "price": 4.99,
        "payment_regularity": "monthly",
        "interval": "month",
    },
    {
        "name": "Yearly",
        "price": 49.99,
        "payment_regularity": "yearly",
        "interval": "year",
    },
]

def create_stripe_prices():
    #  ALREADY DONE DON'T RUN THIS FUNCTION AGAIN
    products = []
    prices = []
    for membership in memberships:
        product = stripe.Product.create(
            name=membership["name"],
            description=f"{membership['name']} subscription."
        )
        price = stripe.Price.create(
            unit_amount=int(membership["price"] * 100),
            currency="gbp",
            recurring={"interval": membership["interval"]},
            product=product
        )
        products.append(product)
        prices.append(price)
        
    print("Products:")
    print([x.id for x in products])
    print("\nPrice:")
    print([x.id for x in prices])
    """
    OUTPUT:
        Products:
        ['prod_Q1iJA4uFD2jflw', 'prod_Q1iJwIBnEjGzqX', 'prod_Q1iJdsq6qx59qs']

        Price:
        ['price_1PBesyRq4UQ9omwxHV4VrEwS', 'price_1PBeszRq4UQ9omwxIWKcOV2O', 'price_1PBeszRq4UQ9omwx6Gyf7T47']
    """
    
def create_db_memberships():
    stripe_data = [{
        "name":stripe.Product.retrieve(x["product"])["name"],
        "price":x["id"],
        "product":x["product"],
    } for x in stripe.Price.list()]
    for membership in memberships:
        m = MembershipPlan()
        m.name = membership["name"]
        m.cost = membership["price"]
        m.payment_regularity = membership["payment_regularity"]
        for data in stripe_data:
            if data["name"] == membership["name"]:
                m.stripe_product = data["product"]
                m.stripe_price = data["price"]
        
        db_add(m)

def create_test_members():
    users = ["Lukecb", "Raccoon", "Irishaha", "ShreyB", "Branson", "SamWilkie"]
    password = "asdfasdf"
    for user in users:
        u = User(user, password)
        u.membership = random.choice(MembershipPlan.query.all())
        u.membership_start_date = date.today()
        db.session.add(u)
    db.session.commit()

def create_owner_login():
    if not User.query.filter_by(username="admin").first():
        u = User("admin", "admin")
        u.is_owner = True
        u.membership = MembershipPlan.query.all()[0]
        db.session.add(u)
        db.session.commit()

delete_all(MembershipPlan)
delete_all(User)
create_db_memberships()
create_test_members()
create_owner_login()