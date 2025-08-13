# Quran/Hadith Generator by Aaron Mairel

# NOT DONE | NOT DEBUGGED

import random
import webbrowser
import time

confirmation_list = ["yes", "true", "sure", "mhm", "okay", "yea", "y"]

quran_suwar = {
    1: "الفاتحة / Al-Fatiha",
    2: "البقرة / Al-Baqarah",
    3: "آل عمران / Al-Imran",
    4: "النساء / An-Nisa",
    5: "المائدة / Al-Ma'idah",
    6: "الأنعام / Al-An'am",
    7: "الأعراف / Al-A'raf",
    8: "الأنفال / Al-Anfal",
    9: "التوبة / At-Tawbah",
    10: "يونس / Yunus",
    11: "هود / Hud",
    12: "يوسف / Yusuf",
    13: "الرعد / Ar-Ra'd",
    14: "إبراهيم / Ibrahim",
    15: "الحجر / Al-Hijr",
    16: "النحل / An-Nahl",
    17: "الإسراء / Al-Isra",
    18: "الكهف / Al-Kahf",
    19: "مريم / Maryam",
    20: "طه / Ta-Ha",
    21: "الأنبياء / Al-Anbiya",
    22: "الحج / Al-Hajj",
    23: "المؤمنون / Al-Mu'minun",
    24: "النور / An-Nur",
    25: "الفرقان / Al-Furqan",
    26: "الشعراء / Ash-Shu'ara",
    27: "النمل / An-Naml",
    28: "القصص / Al-Qasas",
    29: "العنكبوت / Al-Ankabut",
    30: "الروم / Ar-Rum",
    31: "لقمان / Luqman",
    32: "السجدة / As-Sajda",
    33: "الأحزاب / Al-Ahzab",
    34: "سبإ / Saba",
    35: "فاطر / Fatir",
    36: "يس / Ya-Sin",
    37: "الصافات / As-Saffat",
    38: "ص / Sad",
    39: "الزمر / Az-Zumar",
    40: "غافر / Ghafir",
    41: "فصلت / Fussilat",
    42: "الشورى / Ash-Shura",
    43: "الزخرف / Az-Zukhruf",
    44: "الدخان / Ad-Dukhan",
    45: "الجاثية / Al-Jathiya",
    46: "الأحقاف / Al-Ahqaf",
    47: "محمد / Muhammad",
    48: "الفتح / Al-Fath",
    49: "الحجرات / Al-Hujurat",
    50: "ق / Qaf",
    51: "الذاريات / Adh-Dhariyat",
    52: "الطور / At-Tur",
    53: "النجم / An-Najm",
    54: "القمر / Al-Qamar",
    55: "الرحمن / Ar-Rahman",
    56: "الواقعة / Al-Waqia",
    57: "الحديد / Al-Hadid",
    58: "المجادلة / Al-Mujadila",
    59: "الحشر / Al-Hashr",
    60: "الممتحنة / Al-Mumtahina",
    61: "الصف / As-Saff",
    62: "الجمعة / Al-Jumu'a",
    63: "المنافقون / Al-Munafiqun",
    64: "التغابن / At-Taghabun",
    65: "الطلاق / At-Talaq",
    66: "التحريم / At-Tahrim",
    67: "الملك / Al-Mulk",
    68: "القلم / Al-Qalam",
    69: "الحاقة / Al-Haqqa",
    70: "المعارج / Al-Ma'arij",
    71: "نوح / Nuh",
    72: "الجن / Al-Jinn",
    73: "المزّمّل / Al-Muzzammil",
    74: "المدّثر / Al-Muddaththir",
    75: "القيامة / Al-Qiyama",
    76: "الإنسان / Al-Insan",
    77: "المرسلات / Al-Mursalat",
    78: "النبأ / An-Naba",
    79: "النازعات / An-Nazi'at",
    80: "عبس / Abasa",
    81: "التكوير / At-Takwir",
    82: "الإنفطار / Al-Infitar",
    83: "المطفّفين / Al-Mutaffifin",
    84: "الإنشقاق / Al-Inshiqaq",
    85: "البروج / Al-Buruj",
    86: "الطارق / At-Tariq",
    87: "الأعلى / Al-A'la",
    88: "الغاشية / Al-Ghashiya",
    89: "الفجر / Al-Fajr",
    90: "البلد / Al-Balad",
    91: "الشمس / Ash-Shams",
    92: "الليل / Al-Lail",
    93: "الضحى / Ad-Duha",
    94: "الشرح / Ash-Sharh",
    95: "التين / At-Tin",
    96: "العلق / Al-'Alaq",
    97: "القدر / Al-Qadr",
    98: "البينة / Al-Bayyina",
    99: "الزلزلة / Az-Zalzala",
    100: "العاديات / Al-Adiyat",
    101: "القارعة / Al-Qaria",
    102: "التكاثر / At-Takathur",
    103: "العصر / Al-Asr",
    104: "الهمزة / Al-Humaza",
    105: "الفيل / Al-Fil",
    106: "قريش / Quraish",
    107: "الماعون / Al-Ma'un",
    108: "الكوثر / Al-Kawthar",
    109: "الكافرون / Al-Kafirun",
    110: "النصر / An-Nasr",
    111: "المسد / Al-Masad",
    112: "الإخلاص / Al-Ikhlas",
    113: "الفلق / Al-Falaq",
    114: "الناس / An-Nas"
}

sunan_links = {1 : "bukhari", 2 : "muslim", 3 : "nasai", 4 : "abudawud", 5 : "tirmidhi", 6 : "ibnmajah", 7 : "malik", 8 : "ahmad"}

sunan = {
    1: "Sahih Al-Bukhari",
    2: "Sahih Muslim",
    3: "Sunan an-Nasa'i",
    4: "Sunan Abi Dawud",
    5: "Jami' al-Tirmidhi",
    6: "Sunan Ibn Majah",
    7: "Muwatta Malik",
    8: "Musnad Ahmad"
}

def main():
    print("█████████████████████████████████████████████████\n"
          "█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n"
          "█░░░░░░░░░░░░░░░░░░░█▀▀▀░█░░░░░░░░█░░░█░█░░░░░░░█\n"
          "█░░░░░░░░░░░█░░░█░░░▀▀▀█░█░░░█▀█░░█░░░█░█░░░░░░░█\n"
          "█░░░░░░░░░░░█▀▀▀▀▀▀▀▀▀▀▀░▀░░░▀▀▀▀▀▀▀▀▀▀░▀░░░░░░░█\n"
          "█░░░░░░░▀▀▀▀▀░░░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n"
          "█████████████████████████████████████████████████\n")
    time.sleep(0.5)
    randomornot = input("Quran Verse Generator/Finder\n"
                        "\n"
                        "Would you like to generate a ?"
                        "\n"
                        "\n"
                        "1 | Random ayah from the Quran\n"
                        "              OR\n"
                        "2 | Random hadith from the authentic sunan.")

    if randomornot == "1":
        surah = random.randint(0, 114)
        ayah = random.randint(0, 15)

        if surah >= 100:
            ayah = random.randint(0, 3)
        elif 1 < surah <= 20:
            ayah = random.randint(0, 100)

        url = f"https://quran.com/{surah}/{ayah}"

        print("Surah: {}, Verse : {}".format(quran_suwar[surah], ayah))

        time.sleep(0.5)
        print("Opening.")
        time.sleep(0.3)
        print("Opening..")
        time.sleep(0.3)
        print("Opening..")
        time.sleep(0.3)

        webbrowser.open(url)

        return
    elif randomornot == "2":
        book = random.randint(0, 8)
        hadith = random.randint(0, 1500)

        if book <= 4:
            hadith = random.randint(0, 2000)
        elif book <= 3:
            hadith = random.randint(0, 3000)

        url = f"https://sunnah.com/{sunan_links[book]}:{hadith}"

        print("{}, Hadith : #{}".format(sunan[book], hadith))

        time.sleep(0.5)
        print("Opening.")
        time.sleep(0.3)
        print("Opening..")
        time.sleep(0.3)
        print("Opening..")
        time.sleep(0.3)

        webbrowser.open(url)

        return
    else:
        print("\nThat is not one of the two options\n")
        time.sleep(1)
        return main()
main()