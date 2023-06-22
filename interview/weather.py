
def process_csv(reader, writer):
    k = 1
    stations_dict = {}

    writer.write("Station Name,Date,Min Temp,Max Temp,First Temp,Last Temp\n")

    for line in reader:
        if k == 1:
            k+=1
            continue
        k+=1 

        fields = line.split(",") 
        st = fields[0]
        
        timefields = fields[1].split()
        dt = timefields[0]
        hour = timefields[1]
        ampm = timefields[2]

        temp = float(fields[2])
        st_day = st + "," + dt

        if stations_dict.get(st) != None:
            
            if stations_dict[st]["day"] != dt:
                statline = ",".join([st, stations_dict[st]["day"], str(stations_dict[st]["low"]), str(stations_dict[st]["high"]), str(stations_dict[st]["start"]), str(stations_dict[st]["end"])])
                writer.write(statline + "\n")

                stations_dict[st]["day"] = dt
                stations_dict[st]["end"] = temp
                stations_dict[st]["start"] = temp
                stations_dict[st]["high"] = temp
                stations_dict[st]["low"] = temp

            else:
                stations_dict[st]["start"] = temp
                if temp > stations_dict[st]["high"]:
                    stations_dict[st]["high"] = temp
                if temp < stations_dict[st]["low"]:
                    stations_dict[st]["low"] = temp
                
        else:
            stations_dict[st] = {}

            stations_dict[st]["day"] = dt
            stations_dict[st]["end"] = temp
            stations_dict[st]["start"] = temp
            stations_dict[st]["high"] = temp
            stations_dict[st]["low"] = temp

    for st in stations_dict.keys():
        statline = ",".join([st, stations_dict[st]["day"], str(stations_dict[st]["low"]), str(stations_dict[st]["high"]), str(stations_dict[st]["start"]), str(stations_dict[st]["end"])])
        writer.write(statline + "\n")        

    #Foster Weather Station,01/01/2016 11:00:00 PM,69.0        
    #writer.write(f"Saw {len(reader.readlines())} lines" + "\n")
