repeat_string = lambda string, repeats: string * repeats

string = input()
repeats = int(input())
repeated_string = repeat_string(string, repeats)

print(repeated_string)