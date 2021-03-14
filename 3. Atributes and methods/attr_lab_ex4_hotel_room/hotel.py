from attr_lab_ex4_hotel_room.room import Room

class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(self, stars_count):
        return Hotel(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        the_room = [r for r in self.rooms if room_number == r.number][0]
        new_guests = the_room.take_room(people)
        if isinstance(new_guests, int):
            self.guests += new_guests

    def free_room(self, room_number):
        the_room = [r for r in self.rooms if room_number == r.number][0]
        people_in_room = the_room.guests
        message = the_room.free_room()
        if not message:
            self.guests -= people_in_room

    def print_status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms =[str(r.number) for r in self.rooms if r.is_taken]
        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join(free_rooms)}")
        print(f"Taken rooms: {', '.join(taken_rooms)}")







