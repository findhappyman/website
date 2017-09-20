class Ticket:
    normal_adult = 100
    weekend_adult = 1.2*normal_adult
    normal_child = 0.5*normal_adult
    weekend_child = 0.5*weekend_adult
a = Ticket()
print(2*a.normal_adult + a.normal_child)
