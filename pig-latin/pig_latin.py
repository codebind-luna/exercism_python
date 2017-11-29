def translate(text):
    translated_text = ''
    for word in text.split(" "):
        translated_text += ' ' + applyTranlation(word)
    return translated_text.lstrip()

def applyTranlation(text_input):
    if text_input.startswith(("thr", "sch")):
        text_input = text_input[3:] + text_input[:3]
    elif text_input.startswith(("ch", "th", "rh", "qu")):
        text_input = text_input[2:] + text_input[:2]
    elif text_input.startswith(("yt", "xr")):
        text_input = text_input
    elif not text_input.startswith(('a', 'e', 'i', 'o', 'u')):
        if text_input.startswith(text_input[0] + "qu"):
            text_input = text_input[3:] + text_input[:3]
        else:
            text_input = ''.join(y if x else '' for x, y in enumerate(list(text_input))) + text_input[0]
    return text_input + 'ay'
