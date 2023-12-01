import re


barcode_pattern = re.compile(r"@#+[A-Z]([A-Za-z\d]{4,})[A-Z]@#+")

for _ in range(int(input())):
    valid_barcode = barcode_pattern.fullmatch(input())

    if valid_barcode:
        product_group = "".join(filter(str.isdigit, valid_barcode.group(1)))
        print(f"Product group: {product_group if product_group else '00'}")

    else:
        print("Invalid barcode")
