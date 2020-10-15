class Bicycle(object):
    def __init__(self, brand, color, gear, speed, brakes, tyres):
        self.brand = brand
        self.tyres = tyres
        self.brakes = brakes
        self.speed = speed
        self.gear = gear
        self.color = color

    def speed_up(self, increment_speed):
        self.speed += increment_speed
        print('Your bike speed is: {} mph'.format(self.speed))

    def brake(self, decrease_speed):
        if decrease_speed <= self.speed:
            self.speed -= decrease_speed
        else:
            self.speed = 0
        print('Your bike speed is: {} mph'.format(self.speed))

    def __str__(self):
        return 'brand: {}, color: {}, gear: {}, brakes: {}, tyres: {}, speed: {}'.format(
            self.brand, self.color, self.gear, self.brakes, self.tyres, self.speed
        )


class MountainBike(Bicycle):
    def __init__(self, brand, color, gear, speed, brakes, tyres, suspensions, is_full_suspension, mtb_style):
        super(MountainBike, self).__init__(brand, color, gear, speed, brakes, tyres)
        self.suspensions = suspensions
        self.is_full_suspension = is_full_suspension
        self.mtb_style = mtb_style

    def __str__(self):
        return super(MountainBike, self).__str__() + ' suspensions: {}, is full suspension: {}, mtb style: {}'.format(
            self.suspensions, self.is_full_suspension, self.mtb_style)


new_bike = Bicycle('Cube', 'grey', 12, 0, 'Shimano', '14 inch')
print(new_bike)
new_mountain_bike = MountainBike('Cannondale', 'blue', 21, 0, 'Gucci_brakes', '12 inch', 'MTB suspension', True,
                                 'Downhill')
print(new_mountain_bike)
new_mountain_bike.speed_up(12)
new_mountain_bike.brake(8)



