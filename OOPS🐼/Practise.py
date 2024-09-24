
# ! Practise Questions :-

class Students:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total_sum = sum(self.marks)
        avg = total_sum/len(self.marks)

        return avg


S1 = Students("Ashutosh Kumar Rao", [62, 64, 67])

print("The Average", S1.get_avg())
