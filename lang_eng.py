def dict_data():
	return {
    "ru":
        {
            "repoopen.title":"Добавление репозитория..."
        },
    "en":
        {
            "repoopen.title":"Repo adding..."
        },
    "list_lang":
        {
            "ru":"Русский",
            "en":"English"
        }
    }


def get(lang_key, key):
    return dict_data()[lang_key][key]

def list(lang_key, key):
    return dict_data()["list_lang"]