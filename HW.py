setx={"red", "yellow"}
sety={"yellow", "Blue"}
print("The original elements are:")
print(setx)
print(sety)
print("The common between the two sets is:")
setz1=setx.union(sety)
setz2=setx.difference(sety)
setz3=setx.symmetric_difference(sety)
setz4=sety.symmetric_difference(setx)
print(setz1)
print(setz2)
print(setz3)
print(setz4)