import string
import sys

#------------------------------------------------------------
def make_mapping(dict, dict_ref):
    decode_map = {l:r for l, r in zip(sorted(dict,     reverse=True, key=dict.get),
                                      sorted(dict_ref, reverse=True, key=dict_ref.get))}
    return decode_map

#------------------------------------------------------------
def get_stats(text):
    stats = {c:0 for c in string.ascii_lowercase}
 
    for c in text:
        if c in stats:
            stats[c] += 1
    return stats

#------------------------------------------------------------
def decode(text, decode_map):
    decode_map_excpt = {
        'h':'n',
        'f':'y',
        # 'k':'v',
        # 'm':'w',
        # 'c':'m',
        # 'w':'c',
        # 'z':'q',
        # '{':'v'
    }

    decoded = ""
    for c in text:

        decd_ch = c
        if c in decode_map:
            decd_ch = decode_map[c]

        if decd_ch in decode_map_excpt:
            decd_ch = decode_map_excpt[decd_ch]

        decoded += decd_ch
    return decoded

#----------------------------------------------------------
def save_decode_map(decode_map):
    fd_out = open("key.map", "w")

    for k, v in decode_map.items():
        fd_out.write("{0}:{1}\n".format(k, v))
    fd_out.close()

#----------------------------------------------------------
if __name__ == "__main__":
    fd_in_ref = open(sys.argv[1])
    fd_in     = open(sys.argv[2])
    fd_out    = open(sys.argv[3], "w")

    text      = fd_in.read().lower()
    text_ref  = fd_in_ref.read().lower()

    stats     = get_stats(text)
    stats_ref = get_stats(text_ref)

    decode_map = make_mapping(stats, stats_ref)
    decoded    = decode(text, decode_map)

    print(decoded)

    fd_out.write(decoded)
    fd_out.close()

    save_decode_map(decode_map)
