phone= int(input("Phone: "))
digits_mapping={
    "1" ="one"
    "2" ="Two"
    "3"="Three"
    "4" = "Four"
}

for ch in phone:
   output +=digits_mapping.get(ch, "!")
   print (output)
