VN_abbreviation = set(
    [
        "M.City",
        "V.I.P",
        "PGS.Ts",
        "MRS.",
        "Mrs.",
        "Man.United",
        "Mr.",
        "SHB.ĐN",
        "Gs.Bs",
        "U.S.A",
        "TMN.CSG",
        "Kts.Ts",
        "R.Madrid",
        "Tp.",
        "T.Ư",
        "D.C",
        "Gs.Tskh",
        "PGS.KTS",
        "GS.BS",
        "KTS.TS",
        "PGS-TS",
        "Co.",
        "S.H.E",
        "Ths.Bs",
        "T&T.HN",
        "MR.",
        "Ms.",
        "T.T.P",
        "TT.",
        "TP.",
        "ĐH.QGHN",
        "Gs.Kts",
        "Man.Utd",
        "GD-ĐT",
        "T.W",
        "Corp.",
        "ĐT.LA",
        "Dr.",
        "T&T",
        "HN.ACB",
        "GS.KTS",
        "MS.",
        "Prof.",
        "GS.TS",
        "PGs.Ts",
        "PGS.BS",
        "BT.",
        "Ltd.",
        "ThS.BS",
        "Gs.Ts",
        "SL.NA",
        "Th.S",
        "Gs.Vs",
        "PGs.Bs",
        "T.O.P",
        "PGS.TS",
        "HN.T&T",
        "SG.XT",
        "O.T.C",
        "TS.BS",
        "Yahoo!",
        "Man.City",
        "MISS.",
        "HA.GL",
        "GS.Ts",
        "TBT.",
        "GS.VS",
        "GS.TSKH",
        "Ts.Bs",
        "M.U",
        "Gs.TSKH",
        "U.S",
        "Miss.",
        "GD.ĐT",
        "PGs.Kts",
        "St.",
        "Ng.",
        "Inc.",
        "Th.",
        "N.O.V.A",
    ]
)
VN_exception = set(
    [
        "Wi-fi",
        "17+",
        "km/h",
        "M7",
        "M8",
        "21+",
        "G3",
        "M9",
        "G4",
        "km3",
        "m/s",
        "km2",
        "5g",
        "4G",
        "8K",
        "3g",
        "E9",
        "U21",
        "4K",
        "U23",
        "Z1",
        "Z2",
        "Z3",
        "Z4",
        "Z5",
        "Jong-un",
        "u19",
        "5s",
        "wi-fi",
        "18+",
        "Wi-Fi",
        "m2",
        "16+",
        "m3",
        "V-League",
        "Geun-hye",
        "5G",
        "4g",
        "Z3+",
        "3G",
        "km/s",
        "6+",
        "u21",
        "WI-FI",
        "u23",
        "U19",
        "6s",
        "4s",
    ]
)


def is_alphabetic(s):
    for c in s:
        if not c.isalpha():
            return False
    return True


class StringUtils:
    @staticmethod
    def has_punctuation(s):
        for i in range(len(s)):
            if not s[i].isalpha():
                return True
        return False

    @staticmethod
    def isBrace(string):
        if string == "”" or string == "�" or string == "'" or string == ")" or string == "}" or string == "]":
            return True
        return False
