# step 1:
Beatles = []
print(Beatles)
# step 2:
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print(Beatles)


# step 3:
for members in range(2):
    Beatles.append(input("add name here "))
print(Beatles)

# step 4:
del Beatles[-1]
del Beatles[-1]
print(Beatles)

# step 5:
Beatles.insert(0,"Ringo Starr")
print(Beatles)
#
