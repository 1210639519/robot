from mb import command,slot,gc
def get(addr=None):
    val = command(slot(addr,10),b'get_flame_val',1)
    x = 1
    if val != 1:
        return x
    else:
        return 0
gc()