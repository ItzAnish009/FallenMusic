from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "26108237"))
API_HASH = getenv("API_HASH", "b69fac6842079a15c7b51b16f70cf77e")

BOT_TOKEN = getenv("BOT_TOKEN", "6571199121:AAGyGOXDBfA17LPYsTzZX9_8AoTPCbl20JI")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "1822479202"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BQGOYU0AwaXCdZipm6rM-2nndkGoFYc4pWyNMUXwfwi49sTDix798rpMSY6cfq_LfuTKyNqDDirrqqto24HqG_o6lA4eP_pgbGhzpbLzcWNL4hu3Ys4XSCN1CDKuAQKitARcV_NUyFEj_9cEGdlVuMaz-_DWGhlRKnFSeKOCbg3-oo6u3SICE87AQg1E8vbhrOnwEab572ExRowlQEaHD7T_LZTwIEFvELdCCFntO_tUkOXu_uCrNi_kMsXp5cfzWI-tbWuzsFRxpS1NqyRbHwsg6AiJKdcLYq9A0E5nDE8IyYGeOkaaok1_pzPrISxNRtqF_QNhUgQtwkeLLhCOfxLDBwo4DgAAAAGUbHYOAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT" None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL" None)

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1822479202").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
