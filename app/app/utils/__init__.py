import urllib.parse
import os


env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../.env')


def clean_url_path(path, max_legth=50):
    res = path.lower().replace(' ', '_').replace('á', 'a').replace(
        'í', 'i').replace('é', 'e').replace('ó', 'o').replace(
        'ú', 'o').replace('ü', 'u').replace('ñ', 'n').replace(
        ',', '').replace('/', '').replace('.', '').replace(
        '-', '_').replace('?', '').replace('¿', '').replace('!', '').replace('¡', '').replace('"', "").replace("'", "").replace("%", "_")

    if(len(res) > max_legth):
        res = res[:max_legth]

    res = urllib.parse.quote(res)

    res = res.replace(' ', '_').replace('á', 'a').replace(
        'í', 'i').replace('é', 'e').replace('ó', 'o').replace(
        'ú', 'o').replace('ü', 'u').replace('ñ', 'n').replace(
        ',', '').replace('/', '').replace('.', '').replace(
        '-', '_').replace('?', '').replace('¿', '').replace('!', '').replace('¡', '').replace('"', "").replace("'", "").replace("%", "_")

    return res


def fix_word(word):
    res = word
    res = res.lower().replace('  ', ' ').replace(
        ',', ' ').replace('/', ' ').replace('.', ' ').replace(
        '-', '_').replace('?', ' ').replace('¿', ' ').replace('!', ' ').replace('¡', ' ').replace('.', ' ').replace(
            '“', ' ').replace('”', ' ').replace('|', ' ').replace(';', ' ').replace('%', ' ').replace("_", " ")

    while(res.startswith(' ')):
        res = res[1:]
    res = res.replace("  ", " ")
    res = res.replace("  ", " ")
    res = res.lower().replace('  ', ' ').replace(
        ',', ' ').replace('/', ' ').replace('.', ' ').replace(
        '-', '_').replace('?', ' ').replace('¿', ' ').replace('!', ' ').replace('¡', ' ').replace('.', ' ').replace(
            '“', ' ').replace('”', ' ').replace('|', ' ').replace(';', ' ').replace('%', ' ').replace("_", " ")
    for i in range(0, 10):
        res = res.replace(str(i), '')
    return res
