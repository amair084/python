# Arabic Transliteration Name Generator :)

import random

ism = [
    "Ahmad", "Fatimah", "Khalid", "Aisha", "Yusuf", "Layla", "Zayd", "Hind", "Salim", "Mariam",
    "Bilal", "Sumayyah", "Umar", "Rania", "Tariq", "Laya", "Ibrahim", "Sara", "Hassan", "Lina", "Nabil",
    "Samira", "Rashid", "Najwa", "Adnan", "Amatullah"
]
# first name
nasab = [
    "Abdullah", "Muhammad", "Ilyas", "Ali", "Saeed", "Mahmud", "Hussein", "Tahir", "Nasser", "Salman",
    "Harun", "Omar", "Suleiman", "Kamal", "Fahd", "Karim", "Basim", "Zaki", "Jamil", "Anwar",
    "Nasir", "Zuhair", "Hamid", "Ghassan", "Yahya"
]
# lineage
nisbah = [
    "al-Baghdadi", "al-Misri", "al-Qurashi", "al-Andalusi", "al-Makki", "al-Yamani", "al-Farisi", "al-Tamimi", "al-Khurasani", "al-Dimashqi",
    "al-Maghribi", "al-Hanafi", "al-Shafi‘i", "al-Tunisi", "al-Sudani", "al-Rumi", "al-Harbi", "al-Kufi", "al-Isfahani", "al-Basri",
    "al-Qazwini", "al-Najdi", "al-Marwazi", "al-Ansari", "al-Hijazi"
]
# title
kunya = [
    "Qasim", "Hurayrah", "Layth", "Salih", "Ali", "Sawsan", "Ruqayyah", "Hamzah", "Hafsah",
    "Aminah", "Fadl", "Khadijah", "Rayyan", "Lubabah", "Anas", "Nafi‘", "Munir",
    "Barrah", "Talhah", "Uthman", "Sa’id", "Marwan"
]
# children

confirmation_list = ["yes", "true", "sure", "mhm", "okay", "yea", "y"]

name_equation = ""

# Gender/Sex
sex_kunya = ""
sex_nasab = ""
sex = random.randint(0, 1)

if sex == 1:
    sex_kunya = "Abu"
    sex_nasab = "bin"
else:
    sex_nasab = "bint"
    sex_kunya = "Umm"

#Random Generation
random_nasab = random.randint(0, 25)
random_nisbah = random.randint(0, 24)
random_kunya = random.randint(0, 21)

random_ism_index = random.choice(range(0, len(ism) - 1, 2))
actual_ism = ism[random_ism_index + (0 if sex else 1)]

actual_nasab = nasab[random_nasab]
actual_nisbah = nisbah[random_nisbah]
actual_kunya = kunya[random_kunya]

# Parent or not
if random.randint(0,10) >= 5:
    actual_kunya = kunya[random_kunya]
else:
    sex_kunya = ""
    actual_kunya = ""

# Actual Print Statement
print("Your name is: ", (sex_kunya.strip() + " " + actual_kunya + " " + actual_ism + " " + sex_nasab + " " + actual_nasab + " " + actual_nisbah))

q = input("Would you like an english translation?")
if q.strip().lower() in confirmation_list:
    print("")
else:
    print("No worries, enjoy your generated arabic full name.")




