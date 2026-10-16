# try:
#     number = int("hello")
# except ValueError as exc:
#     print("Type:", type(exc))
#     print("Error:", exc)
#     print("Agruments:", exc.args)

try:
    number = int("Hello")
except ValueError as exc:
    error = exc

print(type(error))
print(error)