"""
O objetivo do desafio é resolver a Torre de Hanói utilizando de recursividade.
"""

# pilar_a = [7, 5, 3] 
# pilar_b = []
# pilar_c = []

# def main(move) :
#     print(f"Pilar A {pilar_a} | Pilar B {pilar_b} | Pilar C {pilar_c}")
#     print()

#     match move:
#         case 0 :
#             pilar_c.append(pilar_a.pop())
#         case 1:
#             pilar_b.append(pilar_a.pop())
#         case 2:
#             pilar_b.append(pilar_c.pop())
#         case 3:
#             pilar_c.append(pilar_a.pop())
#         case 4:
#             pilar_a.append(pilar_b.pop())
#         case 5:
#             pilar_c.append(pilar_b.pop())
#         case 6:
#             pilar_c.append(pilar_a.pop())
#         case 7 :
#             return
        
#     main(move + 1)

def main (discs, origin, aux, destiny) :
    if discs == 1 :
        print(f"{origin} -> {destiny}")
        return

    main(discs - 1, origin, destiny, aux)
    print(f"{origin} -> {destiny}")
    main(discs - 1, destiny, aux, origin)


if __name__ == "__main__" :
    main(2, "Pilar A", "Pilar B", "Pilar C")