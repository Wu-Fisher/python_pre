# custmor={
#     "name":"John Smith",
#     "age":30,
#     "is_verified":True
# }
# custmor["name"]="Jack Smith"
# print(custmor.get("birthday","jan,1"))
# print(custmor["name"])

# execrise
phone= input("PHONE:")

map={
    "1":"One",
    "2":"Two",
    "3":"Three"
}
p=""
for ch in phone:
    p+=map.get(ch,"!")
    p+=" "
print(p)