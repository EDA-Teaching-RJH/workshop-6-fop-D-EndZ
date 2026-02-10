def main():
    rover_status = {
    "Battery":100,
    "Heater":"Off",
    "Camera":"Standby"
    }

    print(rover_status)

    rover_status.update({"Battery":85, "Speed":5})
    print(rover_status)


main()

