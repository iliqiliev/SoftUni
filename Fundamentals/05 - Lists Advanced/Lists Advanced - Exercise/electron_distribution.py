electrons = int(input())
atom = list()

electron_layer = 1
while electrons > 0:

    layer_capacity = 2 * (electron_layer ** 2)
    electron_layer += 1

    # avoids adding more electrons than can fit
    layer_electrons = min(layer_capacity, electrons)
    electrons -= layer_electrons

    atom.append(layer_electrons)

print(atom)