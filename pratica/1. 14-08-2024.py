class Person :
  def __init__ (self, name: str, weight: float, height: float) :
    self.name = name
    self.weight = weight
    self.height = height

  def calculate_imc (self) :
    return self.weight / self.height ** 2
  

def main() :
  people = []

  while True :
    try :
      p = {}

      print("\nCadastrando uma pessoa [Ctrl+C para sair]: ")

      p["name"] = input("Nome da pessoa: ")
      p["weight"] = float(input(f"Peso de {p['name']} (Kg): "))
      p["height"] = float(input(f"Altura de {p['name']} (m): "))

      person = Person(p["name"], p["weight"], p["height"])

      people.append(person)

      print(f"Seu IMC é {person.calculate_imc():.2f}")

    except KeyboardInterrupt :
      break

  
  higher = { "imc": 0 }
  lower = { "imc": 9999 }

  for p in people:
    if p.calculate_imc() > higher["imc"] :
      higher["imc"] = p.calculate_imc()
      higher["name"] = p.name

    if p.calculate_imc() < lower["imc"] :
      lower["imc"] = p.calculate_imc()
      lower["name"] = p.name
  
  print(f"\nForam cadastradas {len(people)} pessoa(s), o maior IMC é {higher['imc']:.2f} ({higher['name']}) e o menor é {lower['imc']:.2f} ({lower['name']})")

if __name__ == "__main__" :
  main()