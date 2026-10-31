class Pet:
    attribute1="mammal"
    attribute2="dog"
    attribute3="mix pom-pom"
    def mypet(self):
        print("my pet is a", self.attribute1)
        print("he is a", self.attribute2)
        print("his breed is", self.attribute3)
    def about(self, color):
        print("the color of my", self.attribute2, "is", color)

Chicko= Pet()
Chicko.mypet()
Chicko.about(color="brown")
print (Chicko.attribute1)
Chicko.attribute3="pom-pom"
Chicko.mypet()