from classes import * 

if __name__ == '__main__':

    interclasse = Maratona(2025)

    juiz = Juiz("Clark Kent", "clark@unisantos.br")

    gabriel = Aluno("Gabriel", 1, "M")
    diogo = Aluno("Diogo", 2, "M")
    bianca = Aluno("Bianca", 3, "M")

    eduardo = Aluno("Eduardo", 4, "M")
    heloisa = Aluno("Heloisa", 5, "M")
    giovana = Aluno("Giovana", 6, "P")

    time1 = Time("SI the best", [gabriel, diogo, bianca])
    time2 = Time("CC the worse", [eduardo, heloisa, giovana])

    interclasse.add_time(time1)
    interclasse.add_time(time2)
    interclasse.juiz = j

    if interclasse.get_ano() == 2025:
        print("Maratona deste ano")

    print("Lista dos alunos com camiseta tamanho M:")
    for time in interclasse:
        alunos = time.get_alunos()
        for a in alunos:
            if a.tamanho_camisa == "M":
                print(a)
            print(interclasse)
    







