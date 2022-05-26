class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name;
        self.age = age;
        self.tracks = tracks;
        self.score = score;
    
    def change_name(self, name):
        return name;
    def change_age(self, age):
        return int(age);
    def add_track(self, tracks):
        return tracks;
    def get_score(self):
        return self.score;

Bob = Student(name = "Bob", age=26, tracks=["FE","BE"],score=20.90)

# Outputing the initialized parameters
print(Bob.name);
print(Bob.age);
print(Bob.tracks);
print(Bob.score);

print("\n");

# Changing the initialized parameters except the score.
y = Bob.change_name("Peter")
x = Bob.change_age(34)
z = Bob.add_track("UI/UX")
u = Bob.get_score()

print(y);
print(x);
print(z);
print(u);






