# This program will calculate your shipping based on the weight of your package
weight = float(input("What is the weight of your package? "))

print("Listed below are your shipping options: ")

# Ground Shipping
if weight <= 2:
    ground_shipping = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
    ground_shipping = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
    ground_shipping = weight * 4.00 + 20.00
elif weight > 10:
    ground_shipping = weight * 4.75 + 20.00
    
print("Ground Shipping Cost: $", end="")
print(ground_shipping)

# Premium Ground Shipping
premium_ground = weight + 125.00
# Drone Shipping
if weight <= 2:
  drone_shipping = weight * 4.50
elif weight > 2 and weight <= 6:
  drone_shipping = weight * 9.00
elif weight > 6 and weight <= 10:
  drone_shipping = weight * 12.00
elif weight > 10:
  drone_shipping = weight * 14.25
  
print("Drone Shipping Cost: $",end="")
print(round(drone_shipping,2))
