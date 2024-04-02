from command import (
    GUIWindow,
    SaveCommand,
    CloseCommand,
    MinimizeCommand,
    KeyboardShortcut,
    Button
)

window = GUIWindow("Example")

close_combination = KeyboardShortcut(CloseCommand(window), ["Ctrl", "Q"])
minimize_combination = KeyboardShortcut(MinimizeCommand(window), ["Super", "H"])
save_combination = KeyboardShortcut(SaveCommand(window), ["Ctrl", "S"])

close_button = Button(CloseCommand(window))
minimize_button = Button(MinimizeCommand(window))

print("\nMinimize window:")
minimize_combination.press(["Super", "H"])
print(window)

print("\nAgain:")
minimize_button.click()
print(window)

print("\nSave window:")
save_combination.press(["Ctrl", "S"])
print(window)

print("\nWrong combination not closing:")
close_combination.press(["Wrong", "Combo"])
print(window)

print("\nClose window:")
close_combination.press(["Ctrl", "Q"])
print(window)
