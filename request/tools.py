def covertFukeSize(size):
    mByte = 1
    kb = mByte * 1024
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
    if size >= mByte:
        return "%.1f B" % float(size / mByte)
