# coding: utf-8
from __future__ import unicode_literals

import pytest
from spacy.util import get_lang_class


<<<<<<< Updated upstream
def pytest_addoption(parser):
    parser.addoption("--slow", action="store_true", help="include slow tests")
=======

# These languages are used for generic tokenizer tests – only add a language
# here if it's using spaCy's tokenizer (not a different library)
# TODO: re-implement generic tokenizer tests
_languages = ['bn', 'ca', 'da', 'de', 'el', 'en', 'es', 'fi', 'fr', 'ga', 'he', 'hu', 'id',
              'it', 'nb', 'nl', 'pl', 'pt', 'ro', 'ru', 'sv', 'tr', 'ar', 'ur', 'tt', 'uk',
              'xx']

_models = {'en': ['en_core_web_sm'],
           'de': ['de_core_news_sm'],
           'fr': ['fr_core_news_sm'],
           'xx': ['xx_ent_web_sm'],
           'en_core_web_md': ['en_core_web_md'],
           'es_core_news_md': ['es_core_news_md']}


# only used for tests that require loading the models
# in all other cases, use specific instances

@pytest.fixture(params=_models['en'])
def EN(request):
    return load_test_model(request.param)


@pytest.fixture(params=_models['de'])
def DE(request):
    return load_test_model(request.param)


@pytest.fixture(params=_models['fr'])
def FR(request):
    return load_test_model(request.param)


@pytest.fixture()
def RU(request):
    pymorphy = pytest.importorskip('pymorphy2')
    return util.get_lang_class('ru')()

@pytest.fixture()
def JA(request):
    mecab = pytest.importorskip("MeCab")
    return util.get_lang_class('ja')()


#@pytest.fixture(params=_languages)
#def tokenizer(request):
#lang = util.get_lang_class(request.param)
#return lang.Defaults.create_tokenizer()
>>>>>>> Stashed changes


@pytest.fixture(scope="module")
def tokenizer():
    return get_lang_class("xx").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def en_tokenizer():
    return get_lang_class("en").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def en_vocab():
    return get_lang_class("en").Defaults.create_vocab()


@pytest.fixture(scope="session")
def en_parser(en_vocab):
    nlp = get_lang_class("en")(en_vocab)
    return nlp.create_pipe("parser")


@pytest.fixture(scope="session")
def es_tokenizer():
    return get_lang_class("es").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def de_tokenizer():
    return get_lang_class("de").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def fr_tokenizer():
    return get_lang_class("fr").Defaults.create_tokenizer()


@pytest.fixture
def hu_tokenizer():
    return get_lang_class("hu").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def fi_tokenizer():
    return get_lang_class("fi").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def ro_tokenizer():
    return get_lang_class("ro").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def id_tokenizer():
    return get_lang_class("id").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def sv_tokenizer():
    return get_lang_class("sv").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def bn_tokenizer():
    return get_lang_class("bn").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def ga_tokenizer():
    return get_lang_class("ga").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def he_tokenizer():
    return get_lang_class("he").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def nb_tokenizer():
    return get_lang_class("nb").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def da_tokenizer():
    return get_lang_class("da").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def ja_tokenizer():
    pytest.importorskip("MeCab")
    return get_lang_class("ja").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def th_tokenizer():
    pytest.importorskip("pythainlp")
    return get_lang_class("th").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def tr_tokenizer():
    return get_lang_class("tr").Defaults.create_tokenizer()


<<<<<<< Updated upstream
@pytest.fixture(scope="session")
=======
@pytest.fixture(scope='session')
def uk_tokenizer():
    pymorphy = pytest.importorskip('pymorphy2')
    return util.get_lang_class('uk').Defaults.create_tokenizer()

@pytest.fixture(scope='session')
>>>>>>> Stashed changes
def ca_tokenizer():
    return get_lang_class("ca").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def tt_tokenizer():
    return get_lang_class("tt").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def el_tokenizer():
    return get_lang_class("el").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def ar_tokenizer():
    return get_lang_class("ar").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def ur_tokenizer():
    return get_lang_class("ur").Defaults.create_tokenizer()


@pytest.fixture(scope="session")
def ru_tokenizer():
    pytest.importorskip("pymorphy2")
    return get_lang_class("ru").Defaults.create_tokenizer()


def pytest_runtest_setup(item):
    def getopt(opt):
        # When using 'pytest --pyargs spacy' to test an installed copy of
        # spacy, pytest skips running our pytest_addoption() hook. Later, when
        # we call getoption(), pytest raises an error, because it doesn't
        # recognize the option we're asking about. To avoid this, we need to
        # pass a default value. We default to False, i.e., we act like all the
        # options weren't given.
        return item.config.getoption("--%s" % opt, False)

    for opt in ["slow"]:
        if opt in item.keywords and not getopt(opt):
            pytest.skip("need --%s option to run" % opt)
