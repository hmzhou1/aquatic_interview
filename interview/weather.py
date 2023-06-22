
def process_csv(reader, writer):
    high = 200
    low = -200
    start = -200
    end = -200

    station = ""
    day = ""
    station_day = ""

    writer.write("Station Name,Date,Min Temp,Max Temp,First Temp,Last Temp\n")

    for line in reader:
        fields = line.split(",") 
        st = fields[0]
        
        timefields = fields[1].split()
        dt = timefields[0]
        hour = timefields[1]
        ampm = timefields[2]

        temp = float(fields[2])
        st_day = st + "," + dt

        if station_day != st_day:
            if end > -200:
                statline = ",".join([station, day, str(low), str(high), str(start), str(end)])
                writer.write(statline + "\n")

            station = st
            day = dt
            station_day = st_day

            end = temp
            start = temp
            high = temp
            low = temp

        else:
            start = temp
            if temp > high:
                high = temp
            if temp < low:
                low = temp

    if end > -200:
        statline = ",".join([station, day, str(low), str(high), str(start), str(end)])
        writer.write(statline + "\n")        

    #Foster Weather Station,01/01/2016 11:00:00 PM,69.0        
    #writer.write(f"Saw {len(reader.readlines())} lines" + "\n")
