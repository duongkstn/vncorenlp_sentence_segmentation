class Vocabulary:
    VN_DICT = [x.strip() for x in open("vi-vocab", "r").readlines()]
    COUNTRY_L_NAME = set([
        "na uy",
        "san marino",
        "phần lan",
        "bồ đào nha",
        "ca-ri-bê hà lan",
        "quần đảo bắc mariana",
        "ả rập xê-út",
        "tây ban nha",
        "quần đảo virgin",
        "đảo somoa thuộc mỹ",
        "đông timor",
        "hoa kỳ",
        "quần đảo pitcairn",
        "samoa thuộc mỹ",
        "hàn quốc",
        "đảo ascension",
        "thuỵ sĩ",
        "ai cập",
        "burkina faso",
        "mông cổ",
        "polynesia thuộc pháp",
        "turks và caicos",
        "thổ nhĩ kỳ",
        "liên bang micronesia",
        "đảo man",
        "saint helena",
        "ả rập saudi",
        "ba lan",
        "são tomé và príncipe",
        "đảo norfolk",
        "chdcnd triều tiên",
        "quần đảo canary",
        "guiana thuộc pháp",
        "antigua và barbuda",
        "saint pierre và miquelon",
        "sri lanka",
        "ceuta và melilla",
        "việt nam",
        "bờ biển ngà",
        "thuỵ điển",
        "el salvador",
        "svalbard và jan mayen",
        "saint lucia",
        "diego garcia",
        "ấn độ",
        "tây sahara",
        "quần đảo cook",
        "guinea xích đạo",
        "trung quốc",
        "chdc congo",
        "cộng hoà dominica",
        "cape verde",
        "hà lan",
        "puerto rico",
        "đài loan",
        "cộng hoà séc",
        "costa rica",
        "saint kitts và nevis",
        "nhật bản",
        "quần đảo faroe",
        "đan mạch",
        "turk và caicos",
        "cabo verde",
        "nam sudan",
        "cộng hoà trung phi",
        "trung phi",
        "saint vincent và grenadines",
        "quần đảo cocos",
        "thành vatican",
        "saint barthélemy",
        "nam cực",
        "trinidad và tobago",
        "cộng hoà congo",
        "quần đảo cayman",
        "saint martin",
        "tristan da cunha",
        "bosnia và herzegovina",
        "thái lan",
        "new zealand",
        "hồng kông",
        "wallis và futuna",
        "sierra leone",
        "sint maarten",
        "quần đảo solomon",
        "nam phi",
        "bosna và hercegovina",
        "vương quốc anh",
        "papua new guinea",
        "hy lạp",
        "đảo giáng sinh",
        "triều tiên",
        "quần đảo falkland",
        "miến điện",
        "quần đảo marshall",
        "new caledonia",
    ])

    COUNTRY_S_NAME = set([
        "mỹ",
        "belarus",
        "guinée",
        "gambia",
        "cô-oét",
        "guinea",
        "estonia",
        "philippines",
        "cuba",
        "mauritius",
        "mali",
        "armenia",
        "aruba",
        "méxico",
        "ukraina",
        "bénin",
        "congo",
        "monaco",
        "séc",
        "kenya",
        "hungary",
        "greenland",
        "li-băng",
        "paraguay",
        "palau",
        "vanuatu",
        "colombia",
        "azerbaijan",
        "syria",
        "rwanda",
        "libya",
        "guernsey",
        "afghanistan",
        "guiné-bissau",
        "hungari",
        "kiribati",
        "dominica",
        "bulgaria",
        "brasil",
        "bahrain",
        "guatemala",
        "ghana",
        "somalia",
        "jamaica",
        "togo",
        "liechtenstein",
        "serbia",
        "ma-rốc",
        "bỉ",
        "úc",
        "senegal",
        "montserrat",
        "zambia",
        "namibia",
        "comoros",
        "curaçao",
        "palestine",
        "canada",
        "li-bi",
        "honduras",
        "réunion",
        "maldives",
        "chile",
        "algérie",
        "oman",
        "timor-leste",
        "brazil",
        "lesotho",
        "guyana",
        "peru",
        "malaysia",
        "jersey",
        "síp",
        "belize",
        "nauru",
        "campuchia",
        "kuwait",
        "slovenia",
        "somali",
        "haiti",
        "zimbabwe",
        "macedonia",
        "micronesia",
        "philippin",
        "bolivia",
        "brunei",
        "israel",
        "lào",
        "bangladesh",
        "ý",
        "ireland",
        "albania",
        "botswana",
        "venezuela",
        "andorra",
        "malawi",
        "moldova",
        "madagascar",
        "turkmenistan",
        "iran",
        "iraq",
        "seychelles",
        "indonesia",
        "tchad",
        "nicaragua",
        "gibraltar",
        "ethiopia",
        "ecuador",
        "guinea-bissau",
        "mauritania",
        "albani",
        "algeria",
        "mozambique",
        "cameroon",
        "vatican",
        "liban",
        "panama",
        "uae",
        "luxembourg",
        "nigeria",
        "sudan",
        "benin",
        "chad",
        "liberia",
        "djibouti",
        "đức",
        "tajikistan",
        "fiji",
        "singapore",
        "mexico",
        "samoa",
        "tunisia",
        "bahamas",
        "bhutan",
        "uganda",
        "uruguay",
        "gabon",
        "bungari",
        "niger",
        "kyrgyzstan",
        "pakistan",
        "martinique",
        "macao",
        "kosovo",
        "mayotte",
        "yemen",
        "georgia",
        "pháp",
        "ai-len",
        "argentina",
        "jordan",
        "anguilla",
        "swaziland",
        "burundi",
        "slovakia",
        "uzbekistan",
        "maroc",
        "tanzania",
        "litva",
        "grenada",
        "gruzia",
        "lít-va",
        "guam",
        "eritrea",
        "áo",
        "croatia",
        "niue",
        "nepal",
        "tokelau",
        "bermuda",
        "i-rắc",
        "suriname",
        "guadeloupe",
        "nga",
        "romania",
        "angola",
        "latvia",
        "kazakhstan",
        "malta",
        "myanmar",
        "iceland",
        "românia",
        "montenegro",
        "macau",
        "tuvalu",
        "qatar",
        "tonga",
        "barbados",
    ])
    WORLD_COMPANY = set([
        "verizon",
        "prada",
        "hp",
        "walmart",
        "adidas",
        "mastercard",
        "digg",
        "canon",
        "ikea",
        "sony",
        "twitter",
        "lego",
        "toshiba",
        "nokia",
        "bbc",
        "vmware",
        "mercedes-benz",
        "google",
        "intel",
        "iphone",
        "rbc",
        "fedex",
        "mercedes",
        "gillette",
        "ups",
        "carrefour",
        "lenovo",
        "loreal",
        "mcdonald",
        "coca-cola",
        "guardian",
        "cisco",
        "paypal",
        "cvs",
        "acer",
        "cnn",
        "nike",
        "facebook",
        "spotify",
        "adobe",
        "kfc",
        "westpac",
        "subway",
        "ibm",
        "panasonic",
        "visa",
        "motorola",
        "nissan",
        "citibank",
        "baidu",
        "ford",
        "microsoft",
        "bmw",
        "foxconn",
        "yahoo",
        "hermes",
        "oracle",
        "mcdonalds",
        "tencent",
        "mtv",
        "zara",
        "amazon",
        "toyota",
        "gucci",
        "ebay",
        "kodak",
        "youtube",
        "android",
        "linkedin",
        "myspace",
        "t-mobile",
        "apple",
        "samsung",
        "aldi",
        "colgate",
        "starbucks",
        "pepsi",
        "honda",
        "dell",
        "hitachi",
        "blackberry",
        "disney",
        "siemens",
        "vodafone",
    ])
    VN_LOCATIONS = set([
        "mỹ tho",
        "tập cận bình",
        "nam đông",
        "kiên lương",
        "lương sơn",
        "gò vấp",
        "quang bình",
        "ia pa",
        "lạc sơn",
        "chí linh",
        "ninh hải",
        "sơn dương",
        "quan sơn",
        "ứng hoà",
        "krông pắk",
        "tân hưng",
        "nghệ an",
        "tân thạnh",
        "yên định",
        "mường nhé",
        "ngô quyền",
        "hàm thuận bắc",
        "phú tân",
        "tân hồng",
        "trà ôn",
        "từ liêm",
        "bình thuận",
        "an phú",
        "duy xuyên",
        "nam trực",
        "phù cừ",
        "mai sơn",
        "thạnh phú",
        "lộc bình",
        "kim thành",
        "cái bè",
        "hà quảng",
        "long thành",
        "đồng phù",
        "bảo yên",
        "chiêm hoá",
        "gia nghĩa",
        "an dương",
        "phú quý",
        "quảng trạch",
        "trường sa",
        "hoàn kiếm",
        "thủ thừa",
        "hải lăng",
        "pleiku",
        "thanh hoá",
        "bạch thông",
        "vĩnh phúc",
        "vãn lãng",
        "bình gia",
        "sa thầy",
        "triệu sơn",
        "yên thuỷ",
        "văn giang",
        "hồ chí minh",
        "nga sơn",
        "gia lâm",
        "vị thanh",
        "cái răng",
        "cao bằng",
        "hoài ân",
        "vĩnh long",
        "kim động",
        "ngân sơn",
        "lấp vò",
        "sông công",
        "hoài nhơn",
        "kim bôi",
        "bắc ninh",
        "thái nguyên",
        "đơn dương",
        "định quán",
        "gò công",
        "hà giang",
        "hoà bình",
        "mèo vạc",
        "mộc châu",
        "quảng ngãi",
        "cẩm giàng",
        "sông hinh",
        "thới bình",
        "phụng hiệp",
        "ninh hoà",
        "hậu giang",
        "cái nước",
        "ô môn",
        "gia lai",
        "phổ yên",
        "quế sơn",
        "yên thành",
        "tiên du",
        "an minh",
        "chợ lách",
        "phú ninh",
        "tủa chùa",
        "hương trà",
        "thăng bình",
        "vĩnh thuận",
        "hà tĩnh",
        "lâm đồng",
        "phú quốc",
        "long mỹ",
        "long an",
        "bình lục",
        "vĩnh thạnh",
        "đống đa",
        "hạ long",
        "kỳ sơn",
        "đăk song",
        "lai vung",
        "ý yên",
        "xuyên mộc",
        "vị xuyên",
        "duy tiên",
        "khánh sơn",
        "bỉm sơn",
        "hiệp đức",
        "kim sơn",
        "xín mần",
        "hương thuỷ",
        "tuy hoà",
        "u minh",
        "thiệu hoá",
        "bù đốp",
        "yên sơn",
        "quảng xương",
        "cần đước",
        "thuỷ nguyên",
        "yên dũng",
        "yên hưng",
        "bắc mê",
        "thọ xuân",
        "móng cái",
        "lạc dương",
        "cẩm xuyên",
        "lâm thao",
        "bình tân",
        "phúc yên",
        "sơn tây",
        "vĩnh châu",
        "na hang",
        "chương mỹ",
        "bảo lộc",
        "nghi xuân",
        "lương tài",
        "thoại sơn",
        "cửa lò",
        "đông hưng",
        "lập thạch",
        "nam định",
        "quảng nam",
        "kiên hải",
        "đồng xuân",
        "phú xuyên",
        "tiểu cần",
        "phúc thọ",
        "đông giang",
        "gò dầu",
        "giá rai",
        "tây sơn",
        "phú hoà",
        "việt yên",
        "đak đoa",
        "mường la",
        "hồng ngự",
        "bắc bình",
        "phủ lý",
        "gio linh",
        "cồn cỏ",
        "đức linh",
        "củ chi",
        "hương sơn",
        "tịnh biên",
        "bình thuỷ",
        "nhà bè",
        "yên thế",
        "vĩnh tường",
        "kế sách",
        "sóc sơn",
        "chợ đồn",
        "châu phú",
        "kiến an",
        "sốp cộp",
        "lệ thuỷ",
        "sơn tịnh",
        "càng long",
        "vị thuỷ",
        "ea súp",
        "quảng điền",
        "nghĩa lộ",
        "đồ sơn",
        "krông pa",
        "việt trì",
        "tân thành",
        "nghĩa hưng",
        "bạc liêu",
        "hưng yên",
        "hoàng mai",
        "diên khánh",
        "lăk",
        "bắc trà my",
        "tân châu",
        "tân phú",
        "bình long",
        "đông hà",
        "kon plông",
        "sa đéc",
        "an lão",
        "như xuân",
        "bến lức",
        "thanh khê",
        "long xuyên",
        "chợ gạo",
        "lục nam",
        "hoà thành",
        "vũng liêm",
        "bình định",
        "cẩm mỹ",
        "mộc hoá",
        "tánh linh",
        "đất đỏ",
        "quế võ",
        "trấn yên",
        "cầu ngang",
        "lai châu",
        "gò công tây",
        "lý nhân",
        "bà rịa-vũng tàu",
        "bình giang",
        "mường khương",
        "gò quao",
        "bình đại",
        "điện bàn",
        "hải châu",
        "bắc giang",
        "văn lâm",
        "ninh thuận",
        "cô tô",
        "quảng uyên",
        "đông hải",
        "phan thiết",
        "tĩnh gia",
        "bạch long vĩ",
        "hoài đức",
        "la gi",
        "ngọc hồi",
        "bình sơn",
        "dương minh châu",
        "can lộc",
        "hồng bàng",
        "thanh miện",
        "trảng bàng",
        "thái bình",
        "hải dương",
        "hà tây",
        "krông nô",
        "tam đường",
        "nguyên bình",
        "thủ dầu một",
        "vĩnh lộc",
        "đăk r'lấp",
        "hai bà trưng",
        "long khánh",
        "bình liêu",
        "đồng hỷ",
        "võ nhai",
        "lạc thuỷ",
        "quỳnh phụ",
        "diễn châu",
        "cầu giấy",
        "sơn la",
        "sông mã",
        "kinh môn",
        "thạch thành",
        "ea kar",
        "krông búk",
        "gò công đông",
        "phù ninh",
        "sơn hà",
        "đạ tẻh",
        "mộ đức",
        "cờ đỏ",
        "hương khê",
        "phú lương",
        "di linh",
        "phú vang",
        "lạng giang",
        "yên mô",
        "giao thuỷ",
        "quốc oai",
        "tuyên quang",
        "bát xát",
        "bắc hà",
        "đắk lắk",
        "tiên phước",
        "lê chân",
        "tiên yên",
        "bến cát",
        "tây giang",
        "đà nẵng",
        "ia grai",
        "tam bình",
        "thường tín",
        "vĩnh bảo",
        "hướng hoá",
        "sơn trà",
        "tân uyên",
        "m'đrăk",
        "quản bạ",
        "liên chiểu",
        "tri tôn",
        "tiên lãng",
        "biên hoà",
        "hải hậu",
        "tây ninh",
        "quỳnh nhai",
        "thạch hà",
        "đồng nai",
        "tuyên hoá",
        "mai châu",
        "yên bái",
        "duyên hải",
        "tháp mười",
        "phú nhuận",
        "ân thi",
        "khoái châu",
        "hòn đất",
        "thống nhất",
        "nghĩa đàn",
        "quế phong",
        "thủ đức",
        "hạ lang",
        "vĩnh linh",
        "yên lạc",
        "triệu phong",
        "lâm hà",
        "bảo lâm",
        "hải phòng",
        "vũ quang",
        "cao lộc",
        "nhơn trạch",
        "quảng trị",
        "thạch thất",
        "chơn thành",
        "tân yên",
        "thanh hà",
        "thạnh hoá",
        "si ma cai",
        "bác ái",
        "đăk hà",
        "yên minh",
        "tân bình",
        "đại từ",
        "phục hoà",
        "ninh sơn",
        "long phú",
        "hà tiên",
        "thanh bình",
        "mỏ cày",
        "thạnh trị",
        "trà vinh",
        "dầu tiếng",
        "bắc kạn",
        "chư sê",
        "thanh trì",
        "ngọc lạc",
        "từ sơn",
        "gia bình",
        "pác nặm",
        "thốt nốt",
        "trà bồng",
        "thừa thiên-huế",
        "phước long",
        "cẩm phả",
        "kon rẫy",
        "long biên",
        "cư m'gar",
        "cao lãnh",
        "buôn đôn",
        "đắk nông",
        "lý sơn",
        "sóc trăng",
        "hoằng hoá",
        "quận 10",
        "krông ana",
        "quận 11",
        "quận 12",
        "phan rang-tháp chàm",
        "tân kỳ",
        "tương dương",
        "đan phượng",
        "anh sơn",
        "quận 2",
        "quận 1",
        "qui nhơn",
        "tư nghĩa",
        "bố trạch",
        "quận 9",
        "thạch an",
        "bảo thắng",
        "quận 8",
        "quận 7",
        "nghĩa hành",
        "quận 6",
        "quận 5",
        "hội an",
        "quận 4",
        "quận 3",
        "phong điền",
        "xuân lộc",
        "côn đảo",
        "nha trang",
        "tân lạc",
        "hạ hoà",
        "gia viễn",
        "đồng tháp",
        "hoành bồ",
        "bắc quang",
        "na rì",
        "sông cầu",
        "mường tè",
        "yên phong",
        "tứ kỳ",
        "vũ thư",
        "mỹ hào",
        "chư prông",
        "hóc môn",
        "châu đốc",
        "đô lương",
        "mang thít",
        "tràng định",
        "cam ranh",
        "mang yang",
        "hàm thuận nam",
        "hưng nguyên",
        "kiến xương",
        "ninh phước",
        "phong thổ",
        "đức thọ",
        "hồng lĩnh",
        "khánh vĩnh",
        "mỹ lộc",
        "ngọc hiển",
        "phước sơn",
        "hà đông",
        "lào cai",
        "vĩnh yên",
        "quỳ châu",
        "sơn động",
        "bến cầu",
        "đông anh",
        "kông chro",
        "trảng bom",
        "đông triều",
        "ba tơ",
        "cù lao dung",
        "mỹ xuyên",
        "quảng hà",
        "tân biên",
        "bá thước",
        "cà mau",
        "chi lăng",
        "yên bình",
        "bình minh",
        "bình dương",
        "an nhơn",
        "chư păh",
        "việt nam",
        "giồng riềng",
        "cát tiên",
        "thuận an",
        "ngã năm",
        "cẩm thuỷ",
        "minh long",
        "nam đàn",
        "tân hiệp",
        "thanh sơn",
        "dĩ an",
        "thuận thành",
        "điện biên phủ",
        "vạn ninh",
        "hưng yê",
        "thái thuỵ",
        "thanh xuân",
        "cần giờ",
        "ngũ hành sơn",
        "ba tri",
        "hồng dân",
        "ninh giang",
        "phan rang tháp chàm",
        "than uyên",
        "phú lộc",
        "thanh chương",
        "lục ngạn",
        "năm căn",
        "điện biên đông",
        "hữu lũng",
        "hoàng su phì",
        "tây hồ",
        "bắc yên",
        "sài gòn",
        "vĩnh cửu",
        "bình phước",
        "nam sách",
        "hưng hà",
        "bình chánh",
        "uông bí",
        "ea h'leo",
        "tam điệp",
        "nam giang",
        "trùng khánh",
        "gia lộc",
        "tam dương",
        "hoà an",
        "thừa thiên huế",
        "nông cống",
        "tam kỳ",
        "đak pơ",
        "bình thạnh",
        "hà nội",
        "châu thành",
        "tiên lữ",
        "cầu kè",
        "ninh kiều",
        "buôn ma thuột",
        "an khê",
        "đức huệ",
        "tiền hải",
        "tuy phước",
        "bà rịa",
        "đa krông",
        "đồng xoài",
        "ba vì",
        "quảng ninh",
        "điện biên",
        "hà trung",
        "thanh oai",
        "trà cú",
        "văn yên",
        "bình xuyên",
        "hoà vang",
        "trà lĩnh",
        "yên khánh",
        "kbang",
        "hoàng sa",
        "văn quan",
        "ba chẽ",
        "nho quan",
        "khánh hoà",
        "đăk mil",
        "kiến thuỵ",
        "đầm hà",
        "hàm tân",
        "phù cát",
        "kim bảng",
        "vũng tầu",
        "kiên giang",
        "long hồ",
        "mường chà",
        "thanh ba",
        "đại lộc",
        "mê linh",
        "mường lát",
        "đạ huoai",
        "huế",
        "cần thơ",
        "vụ bản",
        "thanh liêm",
        "đoan hùng",
        "hiệp hoà",
        "bắc sơn",
        "tân trụ",
        "cần giuộc",
        "đăk glong",
        "hậu lộc",
        "kỳ anh",
        "cai lậy",
        "krông bông",
        "yên lập",
        "mù căng chải",
        "mỹ tú",
        "trạm tấu",
        "cư jút",
        "quỳ hợp",
        "tân phước",
        "vĩnh lợi",
        "đồng văn",
        "đông sơn",
        "tây trà",
        "lộc ninh",
        "sầm sơn",
        "lạng sơn",
        "sa pa",
        "hàm yên",
        "vân đồn",
        "đà bắc",
        "vân canh",
        "sơn hoà",
        "thuận bắc",
        "châu đức",
        "thường xuân",
        "định hoá",
        "giồng trôm",
        "núi thành",
        "rạch giá",
        "con cuông",
        "ninh bình",
        "đồng hới",
        "tân an",
        "trực ninh",
        "thuận châu",
        "vinh",
        "trần văn thời",
        "minh hoá",
        "yên mỹ",
        "quan hoá",
        "văn bàn",
        "cam lộ",
        "lang chánh",
        "phù yên",
        "đăk tô",
        "hoa lư",
        "lục yên",
        "đức phổ",
        "hà nam",
        "tuy an",
        "an giang",
        "ba bể",
        "xuân trường",
        "cát hải",
        "kon tum",
        "bù đăng",
        "krông năng",
        "an biên",
        "yên châu",
        "phú thọ",
        "tam nông",
        "quỳnh lưu",
        "đình lập",
        "nghi lộc",
        "chợ mới",
        "đức trọng",
        "đầm dơi",
        "long đất",
        "mường lay",
        "tiền giang",
        "thông nông",
        "phú yên",
        "quảng bình",
        "sìn hồ",
        "tuy phong",
        "ba đình",
        "phù mỹ",
        "đức hoà",
        "bảo lạc",
        "đăk glei",
        "bến tre",
        "như thanh",
        "thanh thuỷ",
        "đà lạt",
        "đức cơ",
        "văn chấn",
        "bà rịa vũng tàu",
        "vĩnh hưng",
        "cao phong",
        "nam trà my",
        "phú giáo",
        "phú bình",
        "ayun pa",
        "mỹ đức",
        "tuần giáo",
    ])
    VN_FIRST_SENT_WORDS = set([
        "được",
        "cty",
        "mẹ",
        "trừ",
        "lên",
        "trưởng",
        "là",
        "chàng",
        "theo",
        "tên",
        "giờ",
        "biết",
        "già",
        "những",
        "thấy",
        "thương",
        "lang",
        "gái",
        "mà",
        "xóm",
        "má",
        "cầu",
        "khách",
        "nhánh",
        "hôm",
        "nhớ",
        "hạng",
        "huyện",
        "vậy",
        "nhà",
        "ấp",
        "sông",
        "thằng",
        "nài",
        "ngành",
        "nếu",
        "trời",
        "đảng",
        "vào",
        "thầy",
        "hai",
        "vùng",
        "chuyện",
        "nhìn",
        "tim",
        "cha",
        "sang",
        "bên",
        "đường",
        "cho",
        "bảng",
        "khi",
        "quận",
        "biển",
        "cu",
        "metro",
        "vốn",
        "đến",
        "năm",
        "khu",
        "đài",
        "miền",
        "việc",
        "do",
        "lập",
        "nghe",
        "mắt",
        "viện",
        "cả",
        "em",
        "rừng",
        "liệu",
        "bố",
        "bộ",
        "cháu",
        "riêng",
        "bà",
        "số",
        "chị",
        "người",
        "bé",
        "tàu",
        "làng",
        "cảng",
        "sở",
        "chiếc",
        "tết",
        "cậu",
        "luật",
        "chờ",
        "rời",
        "chắc",
        "hội",
        "chợ",
        "viên",
        "cụ",
        "nay",
        "thuốc",
        "bọn",
        "tờ",
        "phía",
        "chữ",
        "xe",
        "cò",
        "có",
        "cô",
        "dân",
        "nhóm",
        "song",
        "chú",
        "từ",
        "như",
        "ngày",
        "phim",
        "chính",
        "tân",
        "gặp",
        "các",
        "quê",
        "dì",
        "bởi",
        "quí",
        "về",
        "trại",
        "tại",
        "lão",
        "đảo",
        "nguyên",
        "còn",
        "tiếng",
        "dòng",
        "và",
        "hiện",
        "vợ",
        "thuyền",
        "vụ",
        "đoàn",
        "thành",
        "giới",
        "bến",
        "vì",
        "đi",
        "sân",
        "sâm",
        "con",
        "bác",
        "cùng",
        "báo",
        "chồng",
        "hàng",
        "đất",
        "mỗi",
        "núi",
        "phòng",
        "xã",
        "hồ",
        "ông",
        "giọng",
        "trường",
        "đèo",
        "trùm",
        "nhiều",
        "thư",
        "cục",
        "nước",
        "thôn",
        "bạn",
        "nàng",
        "bệnh",
        "cụm",
        "tướng",
        "buôn",
        "để",
        "anh",
        "lính",
        "với",
        "ngoài",
        "trên",
        "hỏi",
        "sau",
        "đội",
        "gọi",
        "rồi",
        "một",
        "chúc",
        "nhưng",
        "đêm",
        "phó",
        "bỗng",
        "trong",
        "trước",
        "bản",
        "cuốn",
        "chùa",
        "ban",
        "giữa",
        "ngay",
        "lúc",
        "tỉnh",
        "tuy",
        "vẫn",

        "trà",
        "ôi",
        "cặp",
        "taxi",
        "nhiễm",
        "virus",
        "hồi",
        "nghĩa",
        "đọc",
        "nhờ",
        "tới",
        "ong",
        "website",
        "bóng",
        "quít",
        "kungfu",
        "ra",
        "đồng",
        "băng",
        "ba",
        "bầu",
        "hay",
        "giải",
        "giao",
        "cửa",
        "phần",
        "sinh",
        "vietcombank",
        "vàng",
        "fred",
        "tập",
        "toyota",
        "bế",
        "tuồng",
        "nguồn",
        "phường",
        "làm",
        "tuyển",
        "đền",
        "mong",
        "nghỉ",
        "hầm",
        "trán",
        "dắt",
        "sợ",
        "chỗ",
        "lái",
        "xem",
        "chủ",
        "chứ",
        "đợt",
        "đoạn",
        "đồn",
        "trục",
        "tự",
        "neil",
        "điện",
        "trạm",
        "gần",
        "giặc",
        "cúng",
        "dù",
        "vịnh",
        "quân",
        "dãy",
        "pha",
        "toàn",
        "tháp",
        "quĩ",
        "đĩa",
        "gà",
        "lao",
        "bốn",
        "họ",
        "họp",
        "đèn",
        "cũng",
        "động",
        "mặt",
        "đầm",
        "cống",
        "nơi",
        "tùng",
        "phố",
        "đầu",
        "vượt",
        "sao",
        "cách",
        "hoặc",
        "của",
        "hết",
        "đỉnh",
        "kênh",
        "quyền",
        "bar",
        "chống",
        "khắp",
        "sách",
        "wikipedia",
    ])
    VN_MIDDLE_NAMES = set([
        "thúy",
        "bao",
        "thùy",
        "mạnh",
        "mỹ",
        "an",
        "hoa",
        "nữ",
        "trường",
        "vĩnh",
        "đắc",
        "minh",
        "thanh",
        "thi",
        "thu",
        "ninh",
        "đình",
        "hải",
        "tuấn",
        "bội",
        "thuý",
        "việt",
        "nguyễn",
        "bá",
        "phương",
        "bé",
        "tố",
        "quốc",
        "nguyệt",
        "tử",
        "cảnh",
        "trọng",
        "huy",
        "nam",
        "chí",
        "thái",
        "thành",
        "chính",
        "đinh",
        "mai",
        "thiên",
        "tôn",
        "phi",
        "hà",
        "khắc",
        "trúc",
        "lan",
        "doãn",
        "nhất",
        "huỳnh",
        "quỳnh",
        "diễm",
        "khánh",
        "hữu",
        "tấn",
        "anh",
        "hoành",
        "hoàng",
        "diệu",
        "lê",
        "phú",
        "duy",
        "bảo",
        "huyền",
        "nguyên",
        "bích",
        "ánh",
        "công",
        "mộng",
        "lệnh",
        "cẩm",
        "phúc",
        "nhật",
        "ngọc",
        "thời",
        "sơn",
        "thuỳ",
        "văn",
        "vân",
        "qui",
        "hồng",
        "thế",
        "kim",
        "thị",
        "danh",
        "hoài",
        "tiến",
        "tú",
        "bửu",
        "trung",
        "thiện",
        "tuyết",
        "đăng",
        "như",
        "hùng",
        "vô",
        "miên",
        "quý",
        "quang",
        "đức",
        "ưng",
        "tường",
        "kiều",
        "thảo",
        "xuân",
        "viết",
        "vũ",
        "kế",
        "gia",
        "phước",
        "linh",
        "cao",
        "lệ",
    ])
    VN_FAMILY_NAMES = set([
        "bảo",
        "phan",
        "lý",
        "bao",
        "huyền",
        "lưu",
        "nguyên",
        "diêu",
        "vĩnh",
        "ngô",
        "công",
        "giang",
        "đào",
        "bùi",
        "hông",
        "ngọc",
        "chi",
        "bưu",
        "tạ",
        "nguyễn",
        "văn",
        "qui",
        "hồng",
        "quy",
        "từ",
        "trân",
        "hường",
        "tô",
        "mạc",
        "bửu",
        "đặng",
        "huyên",
        "lâm",
        "võ",
        "đinh",
        "miên",
        "mai",
        "hương",
        "lương",
        "hồ",
        "tôn",
        "ưng",
        "la",
        "thân",
        "hà",
        "dương",
        "trịnh",
        "tằng",
        "lan",
        "doãn",
        "vinh",
        "trần",
        "huỳnh",
        "vương",
        "vũ",
        "cao",
        "phạm",
        "hoàng",
        "đỗ",
        "trương",
        "đoàn",
        "diệp",
        "lê",
    ])
