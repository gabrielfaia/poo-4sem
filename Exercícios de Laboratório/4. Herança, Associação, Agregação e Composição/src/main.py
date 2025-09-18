if __name__ == '__main__':

    interclasse = Maratona(2025)

    juiz = Juiz("Clark Kent", "clark@unisantos.br")

    gabriel = Aluno("Gabriel Conrado", 1, "M")
    diogo = Aluno("Diogo Dantas", 2, "M")
    bianca = Aluno("Bianca Franco", 3, "M")

    eduardo = Aluno("Eduardo Flam", 4, "M")
    heloisa = Aluno("Heloisa Nunes", 5, "M")
    giovana = Aluno("Giovana Machado", 6, "P")

    time1 = Time("SI the best", [gabriel, diogo, bianca])
    time2 = Time("CC the worst", [eduardo, heloisa, giovana])

    interclasse.add_time(time1)
    interclasse.add_time(time2)
    interclasse.juiz = j

    if interclasse.get_ano() == 2025:
        print("Maratona deste ano")

    print("Lista dos launos com camiseta tamanho M:")
    for time in interclasse:
        alunos = time.get_alunos()
        for a in alunos:
            if a.tamanho_camisa == "M":
                print(a)
            print(interclasse)
    







