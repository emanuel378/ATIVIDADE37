""""Ler um vetor com 20 idades e exibir a

maior e menor.
"""
vetor_idades = []
for i in range(20):
    idade = int(input(f"Digite a idade {i + 1}: "))
    vetor_idades.append(idade)



maior = max(vetor_idades)
menor = min(vetor_idades)
print(f"A maior idade do vertor_idade e {maior} e a menor e {menor}")