from frota import Carro

if __name__ == '__main__':
    c1 = Carro("Volkswagen","Lamborguini", 50.0, 13.3, mot=True)
    c2 = Carro("BMW", "Bmw i4", 75, 9.5)

    try:
        c1.ligar()
        c2.ligar()

        while c1.odometro < 600 and c2.odometro < 600 and c1.tanque > 0 and c2.tanque > 0:
            c1.acelerar(60, 1) # 60km/h por 1h
            c2.acelerar(100,1) # 100km/h por 1h

            print(f"{c1.modelo}: {c1.odometro} km\n")
            print(f"{c2.modelo}: {c2.odometro} km\n")
        
        if c1.odometro > c2.odometro:
            print(f"{c1.modelo} ganhou!")
        elif c2.odometro > c1.odometro:
            print(f"{c2.modelo} ganhou!")
        else:
            print("Os carros empataram!")

    except Exception as e:
        print(e)