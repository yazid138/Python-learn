#!/bin/python3

# file: operator_pembanding.py
a = int(input("Inputkan nilai a: "))
b = int(input("Inputkan nilai b: "))

# apakah a sama dengan b?
c = a == b
print ("Apakah %d == %d: %r" % (a,b,c))

# apakah a < b?
c = a < b
print ("Apakah %d < %d: %r" % (a,b,c))

# apakah a > b?
c = a > b
print ("Apakah %d > %d: %r" % (a,b,c))

# apakah a <= b?
c = a <= b
print ("Apakah %d <= %d: %r" % (a,b,c))

# apakah a >= b?
c = a >= b
print ("Apakah %d >= %d: %r" % (a,b,c))

# apakah a != b?
c = a != b
print ("Apakah %d != %d: %r" % (a,b,c))

a = True
b = False

# Logika AND
c = a and b
print ("%r and %r = %r" % (a,b,c))

# Logika OR
c = a or b
print ("%r or %r = %r" % (a,b,c))

# Logika Not
c = not a
print ("not %r  = %r" % (a,c))

a = int(input("Masukan nilai a: "))
b = int(input("Masukan nilai b: "))

# Operasi AND
c = a & b
print ("a & b = %s" % c)

# Operasi OR
c = a | b
print ("a | b = %s" % c)

# Operasi XOR
c = a ^ b
print ("a ^ b = %s" % c)

# Operasi Not
c = ~a
print ("~a = %s" % c)

# Operasi shift left (tukar posisi biner)
c = a << b
print ("a << b = %s" % c)

# Operasi shift right (tukar posisi biner)
c = a >> b 
print ("a >> b = %s" % c)
