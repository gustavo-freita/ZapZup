num = int(10)

# Conversão para binário (base 2)
binario = bin(num)[2:]  # [2:] para remover o prefixo '0b'
print("Numero em binario: ", binario)

# Conversão para octal (base 8)
octal = oct(num)[2:]   # [2:] para remover o prefixo '0o'
print("Numero em octal: ", octal)

# Conversão para hexadecimal (base 16)
hexadecimal = hex(num)[2:]  # [2:] para remover o prefixo '0x'
print("Numero em hexadecimal: ", hexadecimal)
