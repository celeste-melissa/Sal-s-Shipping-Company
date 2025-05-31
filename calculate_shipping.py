# This program will calculate your shipping based on the weight of your package
weight = float(input("What is the weight of your package? "))

print("Listed below are your shipping options: ")

# Function that converts value to exact dollar amount - $0.00
def format_money(value):
  return f"${value:.2f}"

# Ground Shipping
if weight <= 2:
    ground_shipping_cost = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
    ground_shipping_cost = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
    ground_shipping_cost = weight * 4.00 + 20.00
elif weight > 10:
    ground_shipping_cost = weight * 4.75 + 20.00
    
print("Ground Shipping Cost: $", end="")
print(format_money(ground_shipping_cost))

# Premium Ground Shipping
premium_ground_cost = 125.00
print("Premium Ground Shipping: $" + format_money(premium_ground_cost))

# Drone Shipping
if weight <= 2:
  drone_shipping_cost = weight * 4.50
elif weight > 2 and weight <= 6:
  drone_shipping_cost = weight * 9.00
elif weight > 6 and weight <= 10:
  drone_shipping_cost = weight * 12.00
elif weight > 10:
  drone_shipping_cost = weight * 14.25
  
print("Drone Shipping Cost: $",end="")
print(format_money(drone_shipping_cost))

# Determine the cheapest shipping method by comparing all three shipping options - print the result
if ground_shipping_cost < premium_ground_cost and  ground_shipping_cost < drone_shipping_cost:
    print("Ground shipping is your cheapest option: " + format_money(ground_shipping_cost) + ".")
elif premium_ground_cost < ground_shipping_cost and premium_ground_cost < drone_shipping_cost:
  print("Premium ground shipping is your cheapest option: " + format_money(premium_ground_cost) + ".")
else:
  print("Drone shipping is your cheapest option: " + format_money(drone_shipping_cost) + ".")
