import time


# @size the incoming size is in 'Bytes'
# @return return human understand
def convertFuckSize(size):
    m_byte = 1
    kb = m_byte * 1024
    mb = kb * 1024
    gb = mb * 1024
    tb = gb * 1024

    if size >= tb:
        return "%.1f TB" % float(size / tb)
    if size >= gb:
        return "%.1f GB" % float(size / gb)
    if size >= mb:
        return "%.1f MB" % float(size / mb)
    if size >= kb:
        return "%.1f KB" % float(size / kb)
    if size >= m_byte:
        return "%.1f B" % float(size / m_byte)


# convert date like this => '2018-11-27T13:05:32 +0800'
# and return to timestamp
def convertFuckDate(date):
    time_array = time.strptime(date, "%Y-%m-%dT%H:%M:%S +0800")
    timestamp = int(time.mktime(time_array))
    return timestamp
