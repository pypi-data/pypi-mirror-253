import re
import string
from typing import Literal
from functools import partial
from .emoji import EMOJI_DICT

__all__ = [
    'text_normalize'
]

std_replace_table = {
    ' ': ' ', # added at 2024-01-22
    '　': ' ',
    # '！': '!',
    '＂': '"',
    '＃': '#',
    '＄': '$',
    '％': '%',
    '＆': '&',
    '＇': "'",
    # '（': '(',
    # '）': ')',
    '＊': '*',
    '＋': '+',
    # '，': ',',
    '－': '-',
    # '．': '.',
    '／': '/',
    '０': '0',
    '１': '1',
    '２': '2',
    '３': '3',
    '４': '4',
    '５': '5',
    '６': '6',
    '７': '7',
    '８': '8',
    '９': '9',
    # '：': ':',
    # '；': ';',
    '＜': '<',
    '＝': '=',
    '＞': '>',
    # '？': '?',
    '＠': '@',
    'Ａ': 'A',
    'Ｂ': 'B',
    'Ｃ': 'C',
    'Ｄ': 'D',
    'Ｅ': 'E',
    'Ｆ': 'F',
    'Ｇ': 'G',
    'Ｈ': 'H',
    'Ｉ': 'I',
    'Ｊ': 'J',
    'Ｋ': 'K',
    'Ｌ': 'L',
    'Ｍ': 'M',
    'Ｎ': 'N',
    'Ｏ': 'O',
    'Ｐ': 'P',
    'Ｑ': 'Q',
    'Ｒ': 'R',
    'Ｓ': 'S',
    'Ｔ': 'T',
    'Ｕ': 'U',
    'Ｖ': 'V',
    'Ｗ': 'W',
    'Ｘ': 'X',
    'Ｙ': 'Y',
    'Ｚ': 'Z',
    '［': '[',
    '＼': '\\',
    '］': ']',
    '＾': '^',
    '＿': '_',
    '｀': '`',
    'ａ': 'a',
    'ｂ': 'b',
    'ｃ': 'c',
    'ｄ': 'd',
    'ｅ': 'e',
    'ｆ': 'f',
    'ｇ': 'g',
    'ｈ': 'h',
    'ｉ': 'i',
    'ｊ': 'j',
    'ｋ': 'k',
    'ｌ': 'l',
    'ｍ': 'm',
    'ｎ': 'n',
    'ｏ': 'o',
    'ｐ': 'p',
    'ｑ': 'q',
    'ｒ': 'r',
    'ｓ': 's',
    'ｔ': 't',
    'ｕ': 'u',
    'ｖ': 'v',
    'ｗ': 'w',
    'ｘ': 'x',
    'ｙ': 'y',
    'ｚ': 'z',
    '｛': '{',
    '｜': '|',
    '｝': '}',
    '～': '~',
}


full2half_table = {
    '！': '!',
    '）': ')',
    '．': '.',
    '。': '.',
    '：': ':',
    '；': ';',
    '？': '?',
    '“': '"',
    '（': '(',
    '”': '"',
    '，': ',',
}

half2full_table = {
    '!': '！',
    ')': '）',
    '.': '。',
    ':': '：',
    ';': '；',
    '?': '？',
    '(': '（',
    ',': '，',
}


right_full2half_table = {
    # '，': ',',
    # '！': '!',
    # '）': ')',
    # '。': '.',
    '：': ':',
    # '；': ';',
    # '？': '?',
    # '“': '"',
}

right_half2full_table = {
    # ',': '，',
    # '!': '！',
    # ')': '）',
    # '.': '。',
    ':': '：',
    # ';': '；',
    # '?': '？',
}

space_pattern = re.compile(r'\s+')

def _replace(ch, replace_table):
    replace = replace_table.get(ch)
    if not replace is None:
        return replace
    return ch


std_replace = partial(_replace, replace_table=std_replace_table)


def general_normalize(text):
    '''basic normalizate for all languages.'''
    text = map(lambda ch: '' if ch in EMOJI_DICT else ch, text) # remove emoji
    text = map(std_replace, text)
    text = filter(lambda ch: ch.isprintable() or ch in ('\n', '\t'), text)
    text = ''.join(text)

    text = space_pattern.sub(' ', text)

    text = text.strip()

    return text.strip()


def char_kind(ch):
    tag = ''
    if ch in string.ascii_letters or ch in string.digits:
        return 'E' # English and digit
    elif '\u4e00' <= ch <= '\u9fff':
        return 'C' # Chinese
    if ch == ' ':
        tag = 'S' # space
    elif '\uff00' <= ch <= '\uffef' or ch in ('“', '”', '。'):
        tag = 'F' # full width punctuation
    elif 33 <= ord(ch) <= 126:
        tag = 'H' # falf width punctuation
    else:
        tag = 'O' # Other
    return tag

lang2kind = {
    'en': 'E',
    'zh': 'C',
}

def char_kind_at_sides(kinds, idx, lang: Literal['en', 'zh']):
    default_kind = lang2kind[lang]

    pre_kind = default_kind
    i = idx-1
    while i>=0:
        if kinds[i] in ('E', 'C'):
            pre_kind = kinds[i]
            break
        i-=1
    
    next_kind = default_kind
    i = idx+1
    while i<len(kinds):
        if kinds[i] in ('E', 'C'):
            next_kind = kinds[i]
            break
        i+=1

    sides_kind = ''
    if pre_kind == next_kind:
        sides_kind = pre_kind
    return pre_kind, next_kind, sides_kind

def width_form_normalize(text, lang: Literal['en', 'zh']):
    chs = []
    kinds = [char_kind(ch) for ch in text]

    # 这段逻辑的基本原则是：原标点符号大部分是正确的。如果很难确定要不要改、怎么改，那就尊重原标点符号

    for idx, ch in enumerate(text):
        kind = kinds[idx]

        if kind == 'F': # full width punctuation
            pre_kind, _, sides_kind = char_kind_at_sides(kinds, idx, lang)
            if sides_kind == 'E':
                new_ch = full2half_table.get(ch)
                if new_ch:
                    ch = new_ch
                    kind = 'H'
                    kinds[idx] = kind
            elif pre_kind == 'E' and ch in right_full2half_table.keys():
                ch = right_full2half_table[ch]
                kind = 'H'
                kinds[idx] = kind
        elif kind == 'H': # half width punctuation
            pre_kind, _, sides_kind = char_kind_at_sides(kinds, idx, lang)
            if sides_kind == 'C':
                new_ch = half2full_table.get(ch)
                if new_ch:
                    ch = new_ch
                    kind = 'F'
                    kinds[idx] = kind
            elif pre_kind == 'C' and ch in right_half2full_table.keys():
                ch = right_half2full_table[ch]
                kind = 'F'
                kinds[idx] = kind
        
        chs.append(ch)
    
    half_quote_count = 0
    quote_kind_stack = []
    for idx, ch in enumerate(chs):
        if ch == '"': # half width quote
            pre_kind, _, sides_kind = char_kind_at_sides(kinds, idx, lang)
            if half_quote_count % 2 == 0:   # left
                if pre_kind == 'C': # chinese
                    ch = '“'
                    chs[idx] = ch
                    kinds[idx] = 'F'           
                quote_kind_stack.append(char_kind(ch))
            else: # right
                if quote_kind_stack:
                    left_kind = quote_kind_stack[-1]
                    quote_kind_stack = quote_kind_stack[:-1]
                    if left_kind == 'F':
                        ch = '”'
                        chs[idx] = ch
                        kinds[idx] = 'F'
            half_quote_count+=1
        elif ch == '“': # full width quote, left
            quote_kind_stack.append(char_kind(ch))
        elif ch == '”': # full width quote, right
            if quote_kind_stack:
                quote_kind_stack = quote_kind_stack[:-1]

    text = ''.join(chs)
    return text


def remove_unnecessary(text):
    # remove unnecessary `"`
    count = 0
    if text.startswith('"') or text.endswith('"'):
        for idx, ch in enumerate(text):
            if ch == '"':
                count+=1
    if count == 1:
        if text.startswith('"'):
            text = text[1:]
        if text.endswith('"'):
            text = text[:-1]

    # remove unnecessary `“` or `”`
    stack = []
    if text.startswith('“') or text.endswith('”'):
        for idx, ch in enumerate(text):
            if ch == '“':
                stack.append(ch)
            elif ch == '”':
                if stack:
                    stack = stack[:-1]
                else:
                    if idx == len(text)-1:
                        text = text[:-1]
        if stack:
            text = text[1:]
    
    return text


def text_normalize(text: str, lang: Literal['en', 'zh']):
    '''Text normalization processing. Correct common character errors in text from the internet.
    '''

    text = general_normalize(text)
    text = remove_unnecessary(text)
    text = width_form_normalize(text, lang)
    
    return text