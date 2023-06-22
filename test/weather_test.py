from interview import weather
import io
import sys


def test_replace_me():
    testlines = "Foster Weather Station,01/09/2016 09:00:00 PM,69.0\n"
    testlines += "Foster Weather Station,01/09/2016 08:00:00 PM,77.0\n"
    testlines += "Foster Weather Station,01/09/2016 07:00:00 PM,62.0\n"
    testlines += "Foster Weather Station,01/09/2016 06:00:00 PM,70.0\n"

    testlines += "Buoy Station,01/09/2016 09:00:00 PM,69\n"
    testlines += "Buoy Station,01/09/2016 08:00:00 PM,77\n"
    testlines += "Buoy Station,01/09/2016 07:00:00 PM,62\n"
    testlines += "Buoy Station,01/09/2016 06:00:00 PM,70\n"

    testlines += "Buoy Station,01/08/2016 08:00:00 PM,55.0\n"

    testlines += "Buoy Station,01/07/2016 08:00:00 PM,41.0\n"
    testlines += "Buoy Station,01/07/2016 07:00:00 PM,42.0\n"

    reader = io.StringIO(testlines)
    #writer = io.StringIO()
    writer = sys.stdout
    weather.process_csv(reader, writer)
    #assert writer.getvalue() == "Saw 2 lines\n"

test_replace_me()
