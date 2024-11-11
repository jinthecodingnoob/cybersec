m = 25
p = 83
g = 39
x = 66
r = 28

y = pow(g, x, p)

c1 = pow(g,r,p)
c2 = (m*pow(y,r,p)) % p

print(f"Ciphertext: (c1 = {c1}, c2 ={c2})")

k = pow(c1, x, p)
k_inv = pow(k, p-2, p)
m_decrypted = (c2 * k_inv) % p

print(f"Decrypted Message : ({m_decrypted})")