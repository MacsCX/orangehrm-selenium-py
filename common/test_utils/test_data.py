from common.utils import draw_tree

TEST_ENV_MAIN_URL = "https://opensource-demo.orangehrmlive.com/"


class BuzzPostsData:
    TREE = (
        f"Sprzedam choinkę zapachową Wunderbaum 'Wyciąg z Konta' (o zapachu piniondza). "
        f"Wisi, pachnie, wygląda. Cena priv. Zdjęcie poglądowe:\n"
        f"{draw_tree(5)}"
    )

    XIAOMI = (
        "Guys, I flashed my Xiaomi vacuum cleaner, using the following software. "
        'Now, it\'s kidnapping my cat and screaming "Hasta la vista, baby". Can someone help?!\n\n'
        "https://github.com/Hypfer/Valetudo\n\n#XiaomiLepsze #AleKradnieKoty"
    )

    SULTAN = "`Maciek, do odważnych wszechświat należy. Po co testować, skoro domyślasz się, że powinno działać.` ~Sultan Kosmitów"


class LoginData:
    PROPER_USERNAME = "Admin"
    PROPER_PASSWORD = "admin123"

    WRONG_CREDENTIALS_DATA_SET = [
        ("wrongusername", "wrongpassword"),
        (PROPER_USERNAME, "wrongpassword"),
        (PROPER_USERNAME + " ", "wrongpassword"),
        ("wrongusername", PROPER_PASSWORD),
        ("wrongusername", PROPER_PASSWORD + " "),
    ]

    MISSING_CREDENTIALS_DATA_SET = [(PROPER_USERNAME, ""), ("", PROPER_PASSWORD), ("", "")]
