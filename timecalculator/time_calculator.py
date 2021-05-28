def add_time(start, duration, day=False):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    seen = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5,
            "sunday": 6}
    finalHours = 0
    finalMinutes = 0

    initTime = start.split()
    intiHour = int(initTime[0].split(":")[0])
    initMin = int(initTime[0].split(":")[1])
    meridian = initTime[1]

    addTime = duration.split(":")
    addHour = int(addTime[0])
    addMin = int(addTime[1])

    numDays = addHour // 24

    addHour -= (numDays * 24)

    finalMinutes = initMin + addMin

    if finalMinutes >= 60:
        finalHours += 1
        finalMinutes -= 60

    finalHours += intiHour + addHour

    while finalHours > 12:

        if meridian == "PM":
            numDays += 1

        finalHours -= 12
        meridian = swapMeridian(meridian)

    if finalHours == 12:
        if meridian == "PM":
            numDays += 1
        meridian = swapMeridian(meridian)

    if len(str(finalMinutes)) == 1:
        finalMinutes = "0" + str(finalMinutes)

    if day:
        days = seen[day.lower()]
        days = (days + numDays) % 7

    return f"{finalHours}:{finalMinutes} {meridian}" + (f", {weekdays[days]}" if day else "") + \
           (" (next day)" if numDays == 1 else ("" if numDays == 0 else f" ({numDays} days later)"))


def swapMeridian(meridian):
    if meridian == "AM":
        return "PM"
    else:
        return "AM"
