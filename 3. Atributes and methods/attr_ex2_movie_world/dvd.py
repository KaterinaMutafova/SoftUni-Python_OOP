MONTH_NUMS = {1: "January", 2: "February", 3:"March", 4: "April", 5: "May", 6: "June",
              7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

class DVD:
    def __init__(self, name: str, id_m: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_m
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        # self.is_rented = False

    def __repr__(self):
        rent_status = ""
        if self.is_rented:
            rent_status = "rented"
        else:
            rent_status = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {rent_status}"

    @classmethod
    def from_date(cls, id_m: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split('.')
        year = int(year)
        month = MONTH_NUMS[int(month)]
        return cls(name, id_m, year, month, age_restriction)





