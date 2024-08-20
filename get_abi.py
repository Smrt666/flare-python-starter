import flare_python_periphery_package as fpp

# get contract abi in 3 different ways
abi1 = fpp.coston2.products.WNat.abi  # the recommended way
abi2 = fpp.coston2.name_to_abi("WNat")
abi3 = fpp.name_to_abi("WNat", "coston2")

print(f"abi1 == abi2: {abi1 == abi2}")
print(f"abi2 == abi3: {abi2 == abi3}")

print(f"abi1: {str(abi1)[:50]}...")
