from requests import get


class Traduzir:

    @staticmethod
    def traduzir(frase, idioma='pt'):
        url = 'http://api.mymemory.translated.net/get?q={frase}&key=' \
              'd90375dbc687e6e7b3c6&langpair=''en|{idioma}'.format(frase=frase, idioma=idioma)
        return dict(get(url).json())['responseData']['translatedText']
