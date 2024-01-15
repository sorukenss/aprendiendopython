# clases 

class Persona : 
    def __init__(self, name, last_name) :
        self.name = name
        self.last_name = last_name
        
    def walk(self):
        print(f"{self.name} {self.last_name} esta caminando ")
        
        
        
p = Persona('isaac','pimienta')

print(f"nombe :{p.name} Apellido: {p.last_name}")
print(p.name)
print(p.last_name)

p.walk()