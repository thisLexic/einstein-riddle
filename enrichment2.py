from constraint import *
problem = Problem()

nationality = ["Brit", "Swede", "Dane", "Norwegian", "German", "Filipino"]
pet = ["dog", "birds", "cats", "horse", "fish", "turtle"]
cigarette = ["Pall Mall", "Dunhill", "Blends", "Blue Master", "Prince", "Marlbro"]
colour = ["red", "green", "yellow", "blue", "white", "black"]
beverage = ["coffee", "milk", "beer", "water", "tea", "yakult"]

criteria = nationality + pet + cigarette + colour + beverage
problem.addVariables(criteria,[1,2,3,4,5,6])

problem.addConstraint(AllDifferentConstraint(), nationality)
problem.addConstraint(AllDifferentConstraint(), pet)
problem.addConstraint(AllDifferentConstraint(), cigarette)
problem.addConstraint(AllDifferentConstraint(), colour)
problem.addConstraint(AllDifferentConstraint(), beverage)

problem.addConstraint(lambda b, r: b == r, ["Brit","red"])
problem.addConstraint(lambda s, d: s == d, ("Swede","dog"))
problem.addConstraint(lambda d, t: d == t, ("Dane","tea"))
problem.addConstraint(lambda g, i: i-g == 1, ("green","white"))
problem.addConstraint(lambda c, g: c == g, ("coffee","green"))
problem.addConstraint(lambda p, b: p == b, ("Pall Mall","birds"))
problem.addConstraint(lambda d, y: d == y, ("Dunhill","yellow"))
problem.addConstraint(InSetConstraint([3]), ["milk"])
problem.addConstraint(InSetConstraint([1]), ["Norwegian"])
problem.addConstraint(lambda b, c: abs(b-c) == 1, ("Blends","cats"))
problem.addConstraint(lambda d, h: abs(d-h) == 1, ("Dunhill","horse"))
problem.addConstraint(lambda bl, be: bl == be, ["Blue Master","beer"])
problem.addConstraint(lambda g, p: g == p, ["German","Prince"])
problem.addConstraint(lambda n, b: abs(n-b) == 1, ("Norwegian","blue"))
problem.addConstraint(lambda b, w: abs(b-w) == 1, ("Blends","water"))

# all possible solutions
print("Number of solutions: " + str(len(problem.getSolutions())))

# one of the solutions
print("One of the solutions:")
solution = problem.getSolutions()[0]

for i in range(1,7):
    for x in solution:
        if solution[x] == i:
            print(str(i), x)
