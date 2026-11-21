"""
Part 4 — Django ORM Lab Practice
Run from the backend project root:

    python manage.py shell < part4_practice.py

This script covers Q objects, F expressions, SQL inspection,
select_related(), prefetch_related(), lazy evaluation, and query logging.
"""

from decimal import Decimal

from django.db import connection, reset_queries
from django.db.models import F, Q

from core.models import Employee, Course


print("\n" + "=" * 65)
print("PART 4 — DJANGO ORM PRACTICE")
print("=" * 65)


# ------------------------------------------------------------
# Task 4.1 — Q Objects: OR, AND, and NOT
# ------------------------------------------------------------

print("\nTASK 4.1 — Q OBJECTS")

# OR: employees in IT OR employees earning more than 70,000
it_or_high_salary = Employee.objects.filter(
    Q(department__code="IT") | Q(salary__gt=70000)
)

print("\nIT department OR salary > 70,000:")
for employee in it_or_high_salary:
    print(employee.first_name, employee.last_name, employee.salary)

# AND + NOT: first name is John AND department is NOT HR
john_not_hr = Employee.objects.filter(
    Q(first_name="John") & ~Q(department__code="HR")
)

print("\nFirst name is John AND department is NOT HR:")
for employee in john_not_hr:
    print(employee.first_name, employee.last_name, employee.department.name)


# ------------------------------------------------------------
# Task 4.2 — F Expressions
# ------------------------------------------------------------

print("\nTASK 4.2 — F EXPRESSIONS")

print(
    "The 10% salary update was already executed during the interactive "
    "exercise."
)
print("Current IT salaries:")
for employee in Employee.objects.filter(department__code="IT"):
    print(employee.first_name, employee.salary)

# IMPORTANT:
# Do not uncomment and run this update again unless you intentionally
# want to increase the current IT salaries by another 10%.
#
# Employee.objects.filter(department__code="IT").update(
#     salary=F("salary") * Decimal("1.10")
# )


# ------------------------------------------------------------
# SQL inspection — QuerySet.query
# ------------------------------------------------------------

print("\nSQL INSPECTION — QUERYSET.QUERY")

qs = Employee.objects.filter(
    Q(department__code="IT") | Q(salary__gt=70000)
)

print(qs.query)


# ------------------------------------------------------------
# Task 4.3 — select_related()
# ------------------------------------------------------------

print("\nTASK 4.3 — select_related()")

reset_queries()

employees_without_join = Employee.objects.all()
for employee in employees_without_join:
    print(employee.first_name, employee.department.name)
