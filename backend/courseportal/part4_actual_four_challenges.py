
"""
DTI412 - Part 4: Four Assigned ORM Challenges

Run:
python manage.py shell < part4_actual_four_challenges.py

Required Product fields:
category, price, status, warehouse, stock_quantity,
reorder_level, is_promotional, max_allowed_price,
total_sold, total_revenue.

Category must have a `name` field.
Warehouse must have a `country` field.
"""

from decimal import Decimal

from django.db import transaction
from django.db.models import (
    Case,
    DecimalField,
    F,
    Q,
    Value,
    When,
)
from django.db.models.lookups import GreaterThan

from core.models import Product


# ============================================================
# CHALLENGE 1: ADVANCED CONDITIONAL SEARCH (Q OBJECTS)
# ============================================================

def challenge_1():

    products = Product.objects.filter(
        (
            Q(category__name="Electronics")
            & Q(price__gt=Decimal("10000"))
        )
        |
        (
            Q(status="DISCOUNTED")
            & ~Q(warehouse__country="China")
        )
    )

    print("\nChallenge 1: Advanced Conditional Search")

    for product in products:
        print(product)

    return products


# ============================================================
# CHALLENGE 2: DYNAMIC STOCK THRESHOLD ALERT
# ============================================================

def challenge_2():

    products = Product.objects.filter(
        Q(stock_quantity__lte=F("reorder_level"))
        |
        (
            Q(is_promotional=True)
            & Q(stock_quantity__lt=F("reorder_level") * 2)
        )
    )

    print("\nChallenge 2: Dynamic Stock Alert")

    for product in products:
        print(product)

    return products


# ============================================================
# CHALLENGE 3: ATOMIC PRICE INCREASE WITH SAFETY CEILING
# ============================================================

def challenge_3():

    increased_price = F("price") * Value(Decimal("1.15"))

    exceeds_ceiling = GreaterThan(
        increased_price,
        F("max_allowed_price"),
    )

    updated_count = Product.objects.filter(
        category__name="Gadgets"
    ).update(
        price=Case(
            When(
                condition=exceeds_ceiling,
                then=F("max_allowed_price"),
            ),
            default=increased_price,
            output_field=DecimalField(
                max_digits=12,
                decimal_places=2,
            ),
        )
    )

    print("\nChallenge 3: Atomic Price Increase")
    print(f"Updated {updated_count} product(s).")

    return updated_count


# ============================================================
# CHALLENGE 4: ATOMIC PURCHASE GUARD
# ============================================================

def challenge_4(product_id, quantity):

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    with transaction.atomic():

        updated_count = Product.objects.filter(
            pk=product_id,
            stock_quantity__gte=quantity,
        ).update(
            stock_quantity=F("stock_quantity") - quantity,
            total_sold=F("total_sold") + quantity,
            total_revenue=(
                F("total_revenue") + F("price") * quantity
            ),
        )

    if updated_count == 1:
        print("\nChallenge 4: Purchase successful.")
        return True

    print("\nChallenge 4: Purchase failed. Insufficient stock.")
    return False


# ============================================================
# MAIN
# ============================================================

def main():

    print("\nStarting the four Part 4 challenges...")

    # These two challenges only retrieve data.
    challenge_1()
    challenge_2()

    # These two challenges modify database records.
    # Run them manually after checking your test data.

    print("\nChallenge 3 is not executed automatically.")
    print("Run: challenge_3()")

    print("\nChallenge 4 is not executed automatically.")
    print("Example: challenge_4(product_id=1, quantity=2)")

    print("\nFour challenge functions are ready.")


main()
