import flare_python_periphery_package as fpp

# get contract abi in 3 different ways
abi1 = fpp.coston2.abis.IWNat
abi2 = fpp.coston2.name_to_abi("IWNat")
abi3 = fpp.name_to_abi("IWNat", "coston2")

print(f"abi1 == abi2: {abi1 == abi2}")
print(f"abi2 == abi3: {abi2 == abi3}")
