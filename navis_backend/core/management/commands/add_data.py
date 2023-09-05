from django.core.management.base import BaseCommand, CommandError
from ...models import Location, Driver, Truck, Client


class Command(BaseCommand):
    help = "Updates the database with location names"

    counties_kenya = [
        "Nairobi", "Mombasa", "Kwale", "Kilifi", "Tana River", "Lamu",
        "Taita-Taveta", "Garissa", "Wajir", "Mandera", "Marsabit", "Isiolo",
        "Meru", "Tharaka-Nithi", "Embu", "Kitui", "Machakos", "Makueni",
        "Nyandarua", "Nyeri", "Kirinyaga", "Murang'a", "Kiambu", "Turkana",
        "West Pokot", "Samburu", "Trans-Nzoia", "Uasin Gishu", "Elgeyo-Marakwet",
        "Nandi", "Baringo", "Laikipia", "Nakuru", "Narok", "Kajiado", "Kericho",
        "Bomet", "Kakamega", "Vihiga", "Bungoma", "Busia", "Siaya", "Kisumu",
        "Homa Bay", "Migori", "Kisii", "Nyamira"
        ]
    
    client_data = []

    truck_data = [
    {
        "manufacturer": "Isuzu",
        "model": "FAW",
        "chassis_number": "KTR346543",
        "carry_weight": "2000.00",
        "registration_number": "KCP 765R",
        "engine_size": "3000 CC",
        "engine_power": "548 HP",
        "yom": "2014-02-24"
    },
    {
        "manufacturer": "Ford",
        "model": "F-150",
        "chassis_number": "LJK987654",
        "carry_weight": "2500.00",
        "registration_number": "XYZ 123A",
        "engine_size": "3500 CC",
        "engine_power": "450 HP",
        "yom": "2015-05-15"
    },
    {
        "manufacturer": "Toyota",
        "model": "Hilux",
        "chassis_number": "HJG456789",
        "carry_weight": "1800.00",
        "registration_number": "LMN 456B",
        "engine_size": "2700 CC",
        "engine_power": "400 HP",
        "yom": "2016-11-30"
    },
    {
        "manufacturer": "Chevrolet",
        "model": "Silverado",
        "chassis_number": "PQR123456",
        "carry_weight": "2200.00",
        "registration_number": "JKL 789C",
        "engine_size": "3200 CC",
        "engine_power": "500 HP",
        "yom": "2017-08-10"
    },
    {
        "manufacturer": "Nissan",
        "model": "Frontier",
        "chassis_number": "MNO789012",
        "carry_weight": "2100.00",
        "registration_number": "GHI 234D",
        "engine_size": "2900 CC",
        "engine_power": "450 HP",
        "yom": "2018-04-20"
    },
    {
        "manufacturer": "Honda",
        "model": "Ridgeline",
        "chassis_number": "STU234567",
        "carry_weight": "2400.00",
        "registration_number": "OPQ 567E",
        "engine_size": "3600 CC",
        "engine_power": "480 HP",
        "yom": "2019-12-05"
    },
    {
        "manufacturer": "GMC",
        "model": "Sierra",
        "chassis_number": "VWX345678",
        "carry_weight": "2300.00",
        "registration_number": "RST 890F",
        "engine_size": "3300 CC",
        "engine_power": "550 HP",
        "yom": "2020-07-15"
    },
    {
        "manufacturer": "Ram",
        "model": "1500",
        "chassis_number": "YZA456789",
        "carry_weight": "2600.00",
        "registration_number": "UVW 123G",
        "engine_size": "3700 CC",
        "engine_power": "520 HP",
        "yom": "2021-03-25"
    },
    {
        "manufacturer": "Mitsubishi",
        "model": "L200",
        "chassis_number": "BCD567890",
        "carry_weight": "1900.00",
        "registration_number": "CDE 456H",
        "engine_size": "2800 CC",
        "engine_power": "420 HP",
        "yom": "2022-10-08"
    },
    {
        "manufacturer": "Subaru",
        "model": "Baja",
        "chassis_number": "EFG678901",
        "carry_weight": "2000.00",
        "registration_number": "FGH 234I",
        "engine_size": "3100 CC",
        "engine_power": "460 HP",
        "yom": "2023-06-15"
    },
    {
        "manufacturer": "Volvo",
        "model": "VNL",
        "chassis_number": "IJK789012",
        "carry_weight": "2700.00",
        "registration_number": "IJK 789X",
        "engine_size": "3800 CC",
        "engine_power": "600 HP",
        "yom": "2014-03-12"
    },
    {
        "manufacturer": "Kenworth",
        "model": "W900",
        "chassis_number": "UVW123456",
        "carry_weight": "2800.00",
        "registration_number": "XYZ 987Y",
        "engine_size": "3900 CC",
        "engine_power": "650 HP",
        "yom": "2015-06-20"
    },
    {
        "manufacturer": "Peterbilt",
        "model": "389",
        "chassis_number": "XYZ234567",
        "carry_weight": "2900.00",
        "registration_number": "LMN 123Z",
        "engine_size": "4000 CC",
        "engine_power": "700 HP",
        "yom": "2016-11-05"
    },
    {
        "manufacturer": "Freightliner",
        "model": "Cascadia",
        "chassis_number": "LMN345678",
        "carry_weight": "3000.00",
        "registration_number": "JKL 567W",
        "engine_size": "4100 CC",
        "engine_power": "750 HP",
        "yom": "2017-09-30"
    },
    {
        "manufacturer": "Western Star",
        "model": "4900",
        "chassis_number": "OPQ456789",
        "carry_weight": "3100.00",
        "registration_number": "GHI 234U",
        "engine_size": "4200 CC",
        "engine_power": "800 HP",
        "yom": "2018-05-25"
    },
    {
        "manufacturer": "Mack",
        "model": "Anthem",
        "chassis_number": "JKL567890",
        "carry_weight": "3200.00",
        "registration_number": "RST 890L",
        "engine_size": "4300 CC",
        "engine_power": "850 HP",
        "yom": "2019-12-18"
    },
    {
        "manufacturer": "International",
        "model": "Lonestar",
        "chassis_number": "CDE678901",
        "carry_weight": "3300.00",
        "registration_number": "PQR 123M",
        "engine_size": "4400 CC",
        "engine_power": "900 HP",
        "yom": "2020-08-10"
    },
    {
        "manufacturer": "Freightliner",
        "model": "Argosy",
        "chassis_number": "RST789012",
        "carry_weight": "3400.00",
        "registration_number": "EFG 234N",
        "engine_size": "4500 CC",
        "engine_power": "950 HP",
        "yom": "2021-04-02"
    },
    {
        "manufacturer": "Volvo",
        "model": "VNR",
        "chassis_number": "PQR901234",
        "carry_weight": "3500.00",
        "registration_number": "STU 567K",
        "engine_size": "4600 CC",
        "engine_power": "1000 HP",
        "yom": "2022-11-15"
    }
]

    driver_data = [
    {
        "first_name": "Nicky",
        "last_name": "Adams",
        "email": "nicky.adams@navis.com",
        "phone_number": "0783990636",
        "licence_number": "14567532",
        "identity_number": "22886544",
        "kra_pin": "A02543876L"
    },
    {
        "first_name": "Alice",
        "last_name": "Johnson",
        "email": "alice.johnson@navis.com",
        "phone_number": "1234567890",
        "licence_number": "98765432",
        "identity_number": "34567890",
        "kra_pin": "B04561234M"
    },
    {
        "first_name": "John",
        "last_name": "Smith",
        "email": "john.smith@navis.com",
        "phone_number": "555-123-4567",
        "licence_number": "24681357",
        "identity_number": "45678901",
        "kra_pin": "C07894561N"
    },
    {
        "first_name": "Emily",
        "last_name": "Davis",
        "email": "emily.davis@navis.com",
        "phone_number": "9876543210",
        "licence_number": "13579246",
        "identity_number": "56789012",
        "kra_pin": "D06543210K"
    },
    {
        "first_name": "Michael",
        "last_name": "Wilson",
        "email": "michael.wilson@navis.com",
        "phone_number": "999-555-1234",
        "licence_number": "86420973",
        "identity_number": "67890123",
        "kra_pin": "E09876123T"
    },
    {
        "first_name": "Sophia",
        "last_name": "Brown",
        "email": "sophia.brown@navis.com",
        "phone_number": "333-222-1111",
        "licence_number": "74639210",
        "identity_number": "78901234",
        "kra_pin": "F04561234U"
    },
    {
        "first_name": "Daniel",
        "last_name": "Lee",
        "email": "daniel.lee@navis.com",
        "phone_number": "777-888-9999",
        "licence_number": "38271694",
        "identity_number": "89012345",
        "kra_pin": "G06789012V"
    },
    {
        "first_name": "Olivia",
        "last_name": "Garcia",
        "email": "olivia.garcia@navis.com",
        "phone_number": "111-222-3333",
        "licence_number": "56789012",
        "identity_number": "90123456",
        "kra_pin": "H07890123W"
    },
    {
        "first_name": "William",
        "last_name": "Martinez",
        "email": "william.martinez@navis.com",
        "phone_number": "444-555-6666",
        "licence_number": "12345677",
        "identity_number": "23456789",
        "kra_pin": "I04561234X"
    },
    {
        "first_name": "Ava",
        "last_name": "Taylor",
        "email": "ava.taylor@navis.com",
        "phone_number": "888-777-6666",
        "licence_number": "98765433",
        "identity_number": "34567891",
        "kra_pin": "J07894561Y"
    },
    {
        "first_name": "Liam",
        "last_name": "Miller",
        "email": "liam.miller@navis.com",
        "phone_number": "555-999-8888",
        "licence_number": "76543212",
        "identity_number": "45678902",
        "kra_pin": "K01234567Z"
    },
    {
        "first_name": "Emma",
        "last_name": "Harris",
        "email": "emma.harris@navis.com",
        "phone_number": "111-333-5555",
        "licence_number": "98765434",
        "identity_number": "12345679",
        "kra_pin": "L04561234A"
    },
    {
        "first_name": "James",
        "last_name": "Moore",
        "email": "james.moore@navis.com",
        "phone_number": "333-111-9999",
        "licence_number": "55555558",
        "identity_number": "23456790",
        "kra_pin": "M07894561B"
    },
    {
        "first_name": "Olivia",
        "last_name": "Jones",
        "email": "olivia.jones@navis.com",
        "phone_number": "666-444-2222",
        "licence_number": "44444445",
        "identity_number": "34567893",
        "kra_pin": "N01234567C"
    },
    {
        "first_name": "Benjamin",
        "last_name": "Davis",
        "email": "benjamin.davis@navis.com",
        "phone_number": "123-321-1111",
        "licence_number": "12345678",
        "identity_number": "45678904",
        "kra_pin": "O04561234D"
    },
    {
        "first_name": "Mia",
        "last_name": "Anderson",
        "email": "mia.anderson@navis.com",
        "phone_number": "555-123-9999",
        "licence_number": "98765435",
        "identity_number": "56789014",
        "kra_pin": "P06543210E"
    },
    {
        "first_name": "Ethan",
        "last_name": "Wilson",
        "email": "ethan.wilson@navis.com",
        "phone_number": "888-111-5555",
        "licence_number": "76543213",
        "identity_number": "67890124",
        "kra_pin": "Q09876123F"
    },
    {
        "first_name": "Ava",
        "last_name": "Smith",
        "email": "ava.smith@navis.com",
        "phone_number": "111-555-8888",
        "licence_number": "55555556",
        "identity_number": "78901234",
        "kra_pin": "R04561234G"
    }
]





    def handle(self, *args, **options):
        # for county in self.counties_kenya:
        #     try:
        #         Location.objects.create(name=county)
        #     except Exception as e:
        #         raise CommandError(f"{e} error encountered")
        
        # for driver in self.driver_data:
        #     Driver.objects.create(
        #         first_name = driver["first_name"],
        #         last_name = driver["last_name"],
        #         email = driver["email"],
        #         phone_number = driver["phone_number"],
        #         licence_number = driver["licence_number"],
        #         identity_number = driver["identity_number"],
        #         kra_pin = driver["kra_pin"],
        #     )
        
        # for truck in self.truck_data:
        #     Truck.objects.create(
        #         manufacturer = truck["manufacturer"],
        #         model = truck["model"],
        #         chasis_number = truck["chassis_number"],
        #         carry_weight = truck["carry_weight"],
        #         registration_number = truck["registration_number"],
        #         engine_size = truck["engine_size"],
        #         engine_power = truck["engine_power"],
        #         yom = truck["yom"]
        #     )

        for client in self.client_data:
            Client.objects.create(
                first_name = client["first_name"],
               last_name = client["last_name"],
                email = client["email"],
                phone_number = client["phone_number"],
               identity_number = client["identity_number"]
            )
            
        self.stdout.write(
            self.style.SUCCESS("Successfully loaded data")
        )
