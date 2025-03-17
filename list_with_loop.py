#[expression for tempvar in originaliterable]
x = [nametag.capitalize() for nametag in ["granade", "bazooka"]]
print(x)
y = [i.upper() for i in ["granade"]]
print(y)
z = [i.lower() for i in ["ROCKET LAUNCHER"]]
print(z)
