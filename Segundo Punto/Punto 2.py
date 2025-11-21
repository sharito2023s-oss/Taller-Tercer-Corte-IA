# Probabilidades iniciales
P_S = 0.30  # Probabilidad de spam
P_G_dado_S = 0.80  # Probabilidad de "gratis" dado spam
P_G_dado_no_S = 0.10  # Probabilidad de "gratis" dado no spam

# Cálculo de P(G) usando probabilidad total
P_no_S = 1 - P_S
P_G = P_G_dado_S * P_S + P_G_dado_no_S * P_no_S

# Aplicar Teorema de Bayes para P(S|G)
P_S_dado_G = (P_G_dado_S * P_S) / P_G

print(f"Probabilidad de que sea spam dado 'gratis': {P_S_dado_G:.4f} ({P_S_dado_G*100:.2f}%)")