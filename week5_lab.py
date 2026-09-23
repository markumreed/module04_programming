# week5_lab.py
# Author: Markum Reed
# Business domain: Tech bro buy new tech yo


product_name = "Laptop"  # str
status = "Pending"  # str
quantity = 3  # int
unit_price = 450.00  # float
is_over_limit = unit_price * quantity > 1000  # bool

print(
    type(product_name),
    type(status),
    type(unit_price),
    type(quantity),
    type(is_over_limit),
)

# Step 4

subtotal = unit_price * quantity
tax = subtotal * 0.07
total = subtotal + tax
requires_approval = total > 1000

# Step 5

print("=== Purchase Request Summary ===")
print(f"Product: {product_name}")
print(f"Qty: {quantity}")
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Tax: ${tax:,.2f}")
print(f"Total: ${total:,.2f}")
print(f"Requires Approval: {requires_approval}")

# Step 6

user_qty = int(input("Enter a new quantity: "))  # convert str to int
new_total = unit_price * user_qty * 1.07
print(f"New total for {user_qty} units: ${new_total:.2f}")
print(f"Requires approval: {new_total > 1000}")
