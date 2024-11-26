import re
from decimal import Decimal
from pygments.lexer import words

class MonetaUtils():

    @staticmethod
    def formmater_label_itens(name_item):
        if not words:
            return ""

        name_item = name_item.replace(':', '')
        formatter_word = re.sub(r'[/.()\-\']|R\$', ' ', name_item).split()
        first_word = formatter_word[0].lower()
        other_words = ''.join(formatter_word[1:]).lower().capitalize()
        camel_case_text = first_word + other_words

        return camel_case_text

    @staticmethod
    def formmater_value_item(value_item):
        itens = ['R$', '%', 'M']
        for i in itens:
            if i in value_item:
                value_item = value_item.replace(i, '').strip()

        if ',' in value_item:
            value_item = value_item.replace(',', '.')

        if 'a.a' in value_item:
            value_item = value_item.replace('a.a', '')

        # Formata o valor conforme o seu tipo de dado
        if not bool(re.search(r'[a-zA-Z]', value_item)):
            if not '.' in value_item:
                value_item = int(value_item)
            elif '.' in value_item and not '/' in value_item:
                if value_item.count('.') > 1:
                    value_item = Decimal(value_item.replace('.', ''))
                else:
                    value_item = float(value_item)
            else:
                value_item = value_item.strip()
        else:
            value_item = value_item.strip()

        return value_item