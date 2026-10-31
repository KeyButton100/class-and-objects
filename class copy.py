class Pet:
    def __init__(self, attribute1, attribute2, attribute3):
        self.attribute1=attribute1
        self.attribute2=attribute2
        self.attribute3=attribute3
    def mypet(self):
        print("my pet is a", self.attribute1)
        print("he is a", self.attribute2)
        print("his breed is", self.attribute3)
    def about(self, color):
        print("the color of my", self.attribute2, "is", color)

Chicko= Pet("mammal", "dog", "mixed pom-pom")
Chicko.mypet()
Chicko.about(color="brown")
print (Chicko.attribute1)
Chicko.attribute3="pom-pom"
Chicko.mypet()
Butter= Pet("avian", "bird", "parrot")
Butter.mypet()