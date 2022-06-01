class FiguriGeom:
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def Arie(self):
        print(self.lungime * self.latime)

    def Perimetru(self):
        print(2*self.lungime + 2*self.latime)


patrat = FiguriGeom(5, 5)
patrat.Arie()
patrat.Perimetru()

dreptunghi = FiguriGeom(7, 3)
dreptunghi.Arie()
dreptunghi.Perimetru()

num = int(input("Enter a number: "))
mod = num % 2
if mod != 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")
