# the data was acquired by scraping https://www.forbes.com/celebrities/
names = [
    "KYLIE JENNER",
    "KANYE WEST",
    "ROGER FEDERER",
    "CRISTIANO RONALDO",
    "LIONEL MESSI",
    "TYLER PERRY",
    "NEYMAR",
    "HOWARD STERN",
    "LEBRON JAMES",
    "DWAYNE JOHNSON",
    "RUSH LIMBAUGH",
    "ELLEN DEGENERES",
    "BILL SIMMONS",
    "ELTON JOHN",
    "JAMES PATTERSON",
    "STEPHEN CURRY",
    "ARIANA GRANDE",
    "RYAN REYNOLDS",
    "GORDON RAMSAY",
    "JONAS BROTHERS",
    "THE CHAINSMOKERS",
    "DR. PHIL MCGRAW",
    "ED SHEERAN",
    "KEVIN DURANT",
    "TAYLOR SWIFT",
    "TIGER WOODS",
    "KIRK COUSINS",
    "POST MALONE",
    "J.K. ROWLING",
    "RYAN SEACREST",
    "CARSON WENTZ",
    "ROLLING STONES",
    "MARK WAHLBERG",
    "TYSON FURY",
    "MARSHMELLO",
    "RUSSELL WESTBROOK",
    "BEN AFFLECK",
    "SEAN COMBS",
    "SHAWN MENDES",
    "VIN DIESEL",
    "LEWIS HAMILTON",
    "JAY-Z",
    "BILLIE EILISH",
    "RORY MCILROY",
    "SIMON COWELL",
    "JERRY SEINFELD",
    "BTS",
    "KIM KARDASHIAN WEST",
    "DRAKE",
    "JARED GOFF",
    "JUDY SHEINDLIN",
    "AKSHAY KUMAR",
    "CONOR MCGREGOR",
    "JAMES HARDEN",
    "GIANNIS ANTETOKOUNMPO",
    "JENNIFER LOPEZ",
    "ANTHONY JOSHUA",
    "PINK",
    "DEONTAY WILDER",
    "DAVID COPPERFIELD",
    "RIHANNA",
    "LUKE BRYAN",
    "LIN-MANUEL MIRANDA",
    "BACKSTREET BOYS",
    "TOM BRADY",
    "PHIL COLLINS",
    "DREW BREES",
    "NOVAK DJOKOVIC",
    "WILL SMITH",
    "BLAKE SHELTON",
    "SEAN HANNITY",
    "SOFÍA VERGARA",
    "CELINE DION",
    "KYRIE IRVING",
    "THE EAGLES",
    "ADAM SANDLER",
    "PHIL MICKELSON",
    "JULIO JONES",
    "METALLICA",
    "JACKIE CHAN",
    "RAFAEL NADAL",
    "HEIDI KLUM",
    "TRAVIS SCOTT",
    "KEVIN HART",
    "KLAY THOMPSON",
    "KATY PERRY",
    "LADY GAGA",
    "BON JOVI",
    "U2",
    "NAOMI OSAKA",
    "CANELO ALVAREZ",
    "DAMIAN LILLARD",
    "PAUL MCCARTNEY",
    "OPRAH WINFREY",
    "DJ KHALED",
    "KISS",
    "SEBASTIAN VETTEL",
    "SERENA WILLIAMS",
    "ANGELINA JOLIE",
    "MOHAMED SALAH"
]

urls = [
    "https://specials-images.forbesimg.com/imageserve/5ed55c763dbc9800060b27d5/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed00f17d4a99d0006d2e738/416x416.jpg?background=000000&cropX1=154&cropX2=4820&cropY1=651&cropY2=5314",
    "https://specials-images.forbesimg.com/imageserve/5ed53e8fa40c3d0007ed25b3/416x416.jpg?background=000000&cropX1=509&cropX2=1693&cropY1=78&cropY2=1262",
    "https://specials-images.forbesimg.com/imageserve/5ec593cc431fb70007482137/416x416.jpg?background=000000&cropX1=1321&cropX2=3300&cropY1=114&cropY2=2093",
    "https://specials-images.forbesimg.com/imageserve/5ec595d45f39760007b05c07/416x416.jpg?background=000000&cropX1=989&cropX2=2480&cropY1=74&cropY2=1564",
    "https://specials-images.forbesimg.com/imageserve/5ecc520236d6f40008dcdd7d/416x416.jpg?background=000000&cropX1=622&cropX2=3127&cropY1=5&cropY2=2509",
    "https://specials-images.forbesimg.com/imageserve/5ec59a8cda48890006292eee/416x416.jpg?background=000000&cropX1=845&cropX2=2277&cropY1=97&cropY2=1528",
    "https://specials-images.forbesimg.com/imageserve/5ed55ed6b14861000600bb71/416x416.jpg?background=000000&cropX1=15&cropX2=1067&cropY1=26&cropY2=1078",
    "https://specials-images.forbesimg.com/imageserve/5ecc5358798e4c00060d2274/416x416.jpg?background=000000&cropX1=1184&cropX2=3286&cropY1=30&cropY2=2130",
    "https://specials-images.forbesimg.com/imageserve/5b3a90cba7ea4353dd3f9804/416x416.jpg?background=000000&cropX1=186&cropX2=3092&cropY1=449&cropY2=3354",
    "https://specials-images.forbesimg.com/imageserve/5ed560617fe4060006bbce1a/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed560d07fe4060006bbce1e/416x416.jpg?background=000000&cropX1=422&cropX2=1300&cropY1=0&cropY2=879",
    "https://specials-images.forbesimg.com/imageserve/5ed556cb570be80006474215/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed561437fe4060006bbce2a/416x416.jpg?background=000000&cropX1=49&cropX2=1056&cropY1=73&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed561a23dbc9800060b2803/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ece6eed1061240006af3da0/416x416.jpg?background=000000&cropX1=1271&cropX2=3410&cropY1=153&cropY2=2290",
    "https://specials-images.forbesimg.com/imageserve/5ed562613dbc9800060b280b/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed017eb2d65910007477d79/416x416.jpg?background=000000&cropX1=1221&cropX2=4507&cropY1=0&cropY2=3289",
    "https://specials-images.forbesimg.com/imageserve/5ed53f23da1f770006140c3c/416x416.jpg?background=000000&cropX1=1567&cropX2=3494&cropY1=155&cropY2=2083",
    "https://specials-images.forbesimg.com/imageserve/5ed558d119427200062f281d/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed01cf12d65910007477dd5/416x416.jpg?background=000000&cropX1=754&cropX2=3582&cropY1=1226&cropY2=4055",
    "https://specials-images.forbesimg.com/imageserve/5ed5634db14861000600bb9a/416x416.jpg?background=000000&cropX1=19&cropX2=1057&cropY1=42&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed564163dbc9800060b2829/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ece6f50938ec500060aac25/416x416.jpg?background=000000&cropX1=0&cropX2=3648&cropY1=133&cropY2=3784",
    "https://specials-images.forbesimg.com/imageserve/5ed56484570be8000647428e/416x416.jpg?background=000000&cropX1=414&cropX2=1670&cropY1=0&cropY2=1255",
    "https://specials-images.forbesimg.com/imageserve/5ece6ffa89ee2f0006814bfd/416x416.jpg?background=000000&cropX1=0&cropX2=2074&cropY1=14&cropY2=2087",
    "https://specials-images.forbesimg.com/imageserve/5ecc5f0a798e4c00060d233c/416x416.jpg?background=000000&cropX1=710&cropX2=2526&cropY1=28&cropY2=1842",
    "https://specials-images.forbesimg.com/imageserve/5ed56515570be8000647429a/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed56d114231c70006c8f37b/416x416.jpg?background=000000&cropX1=0&cropX2=654&cropY1=96&cropY2=750",
    "https://specials-images.forbesimg.com/imageserve/5ed568c68b3c370006234bde/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ecc60a1fd6d6700060f84ff/416x416.jpg?background=000000&cropX1=1058&cropX2=2516&cropY1=31&cropY2=1488",
    "https://specials-images.forbesimg.com/imageserve/5ed53feedb5de00007f1dce4/416x416.jpg?background=000000&cropX1=850&cropX2=1830&cropY1=270&cropY2=1250",
    "https://specials-images.forbesimg.com/imageserve/5ed569ec19427200062f291d/416x416.jpg?background=000000&cropX1=20&cropX2=1051&cropY1=49&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ecc644736d6f40008dcde32/416x416.jpg?background=000000&cropX1=1349&cropX2=3954&cropY1=78&cropY2=2685",
    "https://specials-images.forbesimg.com/imageserve/5ed56b6ab14861000600bbb1/416x416.jpg?background=000000&cropX1=301&cropX2=955&cropY1=0&cropY2=654",
    "https://specials-images.forbesimg.com/imageserve/60b7c67d9eb11eecab7dd319/416x416.jpg?background=000000&cropX1=737&cropX2=3019&cropY1=10&cropY2=2291",
    "https://specials-images.forbesimg.com/imageserve/5ed56c73ab6ff10006ab459b/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed56d858b3c370006234c06/416x416.jpg?background=000000&cropX1=0&cropX2=654&cropY1=43&cropY2=697",
    "https://specials-images.forbesimg.com/imageserve/5ed56f207fe4060006bbce9a/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed56fff8b3c370006234c1c/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ece723454886200073da1eb/416x416.jpg?background=000000&cropX1=0&cropX2=3003&cropY1=199&cropY2=3200",
    "https://specials-images.forbesimg.com/imageserve/5ed554fab14861000600baf1/416x416.jpg?background=000000&cropX1=53&cropX2=739&cropY1=114&cropY2=800",
    "https://specials-images.forbesimg.com/imageserve/5ed029877e1af600061fd4b0/416x416.jpg?background=000000&cropX1=0&cropX2=3540&cropY1=62&cropY2=3600",
    "https://specials-images.forbesimg.com/imageserve/5ecc696936d6f40008dcdee2/416x416.jpg?background=000000&cropX1=8&cropX2=1931&cropY1=139&cropY2=2063",
    "https://specials-images.forbesimg.com/imageserve/5ed574ad8b3c370006234c27/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed575a07fe4060006bbcec8/416x416.jpg?background=000000&cropX1=186&cropX2=840&cropY1=0&cropY2=654",
    "https://specials-images.forbesimg.com/imageserve/5ed57684b14861000600bc59/416x416.jpg?background=000000&cropX1=115&cropX2=993&cropY1=0&cropY2=879",
    "https://specials-images.forbesimg.com/imageserve/5ed57844b14861000600bc5d/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed578988b3c370006234c35/416x416.jpg?background=000000&cropX1=43&cropX2=1074&cropY1=49&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ecc6c2336d6f40008dcdefc/416x416.jpg?background=000000&cropX1=1228&cropX2=2402&cropY1=128&cropY2=1302",
    "https://specials-images.forbesimg.com/imageserve/60aecc8b915439415ba7d176/416x416.jpg?background=000000&cropX1=2&cropX2=1080&cropY1=0&cropY2=1078",
    "https://specials-images.forbesimg.com/imageserve/5ed579d37bd7a20006bef454/416x416.jpg?background=000000&cropX1=485&cropX2=1365&cropY1=0&cropY2=880",
    "https://specials-images.forbesimg.com/imageserve/5ecc702ffd6d6700060f85d1/416x416.jpg?background=000000&cropX1=1215&cropX2=2867&cropY1=37&cropY2=1690",
    "https://specials-images.forbesimg.com/imageserve/60b7cdf3dcbf78a22786c057/416x416.jpg?background=000000&cropX1=796&cropX2=1652&cropY1=42&cropY2=897",
    "https://specials-images.forbesimg.com/imageserve/5ecc72a1c67cd60006c787e1/416x416.jpg?background=000000&cropX1=611&cropX2=1714&cropY1=61&cropY2=1163",
    "https://specials-images.forbesimg.com/imageserve/5ed65800570be80006474843/416x416.jpg?background=000000&cropX1=154&cropX2=810&cropY1=0&cropY2=655",
    "https://specials-images.forbesimg.com/imageserve/5ece784289ee2f0006814c41/416x416.jpg?background=000000&cropX1=1552&cropX2=3366&cropY1=165&cropY2=1980",
    "https://specials-images.forbesimg.com/imageserve/5ed65a8953104f0007d6ef89/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ecc74fcfd6d6700060f862b/416x416.jpg?background=000000&cropX1=1080&cropX2=2250&cropY1=111&cropY2=1281",
    "https://specials-images.forbesimg.com/imageserve/5ed65b31dd5d320006caf73c/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed6604bdd5d320006caf816/416x416.jpg?background=000000&cropX1=697&cropX2=1566&cropY1=8&cropY2=878",
    "https://specials-images.forbesimg.com/imageserve/5ed660c99e384f0007b7db21/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ecc7638798e4c00060d248d/416x416.jpg?background=000000&cropX1=1853&cropX2=4404&cropY1=51&cropY2=2600",
    "https://specials-images.forbesimg.com/imageserve/5ed6620f570be8000647494a/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/60b8efae858d6a01f2936962/416x416.jpg?background=000000&cropX1=429&cropX2=1798&cropY1=65&cropY2=1433",
    "https://specials-images.forbesimg.com/imageserve/5ecc77ff798e4c00060d24bc/416x416.jpg?background=000000&cropX1=1978&cropX2=2916&cropY1=697&cropY2=1634",
    "https://specials-images.forbesimg.com/imageserve/5ece82c589ee2f0006814cf7/416x416.jpg?background=000000&cropX1=464&cropX2=1341&cropY1=78&cropY2=955",
    "https://specials-images.forbesimg.com/imageserve/5ece884dbdf23b00084e577b/416x416.jpg?background=000000&cropX1=460&cropX2=1949&cropY1=185&cropY2=1672",
    "https://specials-images.forbesimg.com/imageserve/5ed663d153104f0007d6f014/416x416.jpg?background=000000&cropX1=15&cropX2=1047&cropY1=48&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed6657ddd5d320006caf873/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed666bb570be80006474969/416x416.jpg?background=000000&cropX1=1661&cropX2=3510&cropY1=0&cropY2=1849",
    "https://specials-images.forbesimg.com/imageserve/5ed666361b732a00060ba263/416x416.jpg?background=000000&cropX1=466&cropX2=1344&cropY1=0&cropY2=879",
    "https://specials-images.forbesimg.com/imageserve/5ecc7b321c89960006721a32/416x416.jpg?background=000000&cropX1=1047&cropX2=2392&cropY1=175&cropY2=1521",
    "https://specials-images.forbesimg.com/imageserve/5ecc7b8285e6c7000617c7e2/416x416.jpg?background=000000&cropX1=422&cropX2=1492&cropY1=283&cropY2=1352",
    "https://specials-images.forbesimg.com/imageserve/5ed6688e8b3c37000623526e/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed66dcf570be80006474a20/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ece8970938ec500060aae2c/416x416.jpg?background=000000&cropX1=1037&cropX2=3127&cropY1=219&cropY2=2308",
    "https://specials-images.forbesimg.com/imageserve/5ecc7d3afd6d6700060f8691/416x416.jpg?background=000000&cropX1=1042&cropX2=3239&cropY1=14&cropY2=2209",
    "https://specials-images.forbesimg.com/imageserve/5ed5563a19427200062f280c/416x416.jpg?background=000000&cropX1=1222&cropX2=2543&cropY1=289&cropY2=1609",
    "https://specials-images.forbesimg.com/imageserve/5ed66ef9d1db3e000665f5da/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ece8a5c938ec500060aae37/416x416.jpg?background=000000&cropX1=503&cropX2=2965&cropY1=156&cropY2=2616",
    "https://specials-images.forbesimg.com/imageserve/5ed55afbd83fc00007e06dc5/416x416.jpg?background=000000&cropX1=370&cropX2=1231&cropY1=16&cropY2=879",
    "https://specials-images.forbesimg.com/imageserve/5ed670179e384f0007b7db8f/416x416.jpg?background=000000&cropX1=1032&cropX2=3642&cropY1=186&cropY2=2795",
    "https://specials-images.forbesimg.com/imageserve/5ecc7f2c24677c000765fe20/416x416.jpg?background=000000&cropX1=1126&cropX2=2835&cropY1=194&cropY2=1903",
    "https://specials-images.forbesimg.com/imageserve/5ed67bfe1b732a00060ba321/416x416.jpg?background=000000&cropX1=905&cropX2=2535&cropY1=77&cropY2=1706",
    "https://specials-images.forbesimg.com/imageserve/5ecc802e36d6f40008dcdfe0/416x416.jpg?background=000000&cropX1=752&cropX2=1749&cropY1=178&cropY2=1175",
    "https://specials-images.forbesimg.com/imageserve/5ed6716cdd5d320006caf933/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed6a1bb9be86200074e6a56/416x416.jpg?background=000000&cropX1=113&cropX2=1234&cropY1=24&cropY2=1145",
    "https://specials-images.forbesimg.com/imageserve/5ed671f1570be80006474a37/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ec6d2d6b619e600065eb1d1/416x416.jpg?background=000000&cropX1=366&cropX2=3042&cropY1=96&cropY2=2770",
    "https://specials-images.forbesimg.com/imageserve/5ece91d089ee2f0006814e6b/416x416.jpg?background=000000&cropX1=867&cropX2=2726&cropY1=727&cropY2=2587",
    "https://specials-images.forbesimg.com/imageserve/5ece92f41f4c83000768d787/416x416.jpg?background=000000&cropX1=421&cropX2=1694&cropY1=37&cropY2=1310",
    "https://specials-images.forbesimg.com/imageserve/5ecc828f85e6c7000617c817/416x416.jpg?background=000000&cropX1=154&cropX2=2258&cropY1=13&cropY2=2119",
    "https://specials-images.forbesimg.com/imageserve/5ed6730fc6ade40006ffd657/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed677cfdd5d320006caf9cd/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ed55b93d0754f0007a3486a/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/60b8ea7550405735ae936962/416x416.jpg?background=000000&cropX1=442&cropX2=2511&cropY1=205&cropY2=2276",
    "https://specials-images.forbesimg.com/imageserve/5ecc8412798e4c00060d2536/416x416.jpg?background=000000&cropX1=86&cropX2=1960&cropY1=0&cropY2=1876",
    "https://specials-images.forbesimg.com/imageserve/5ed67918c6ade40006ffd6db/416x416.jpg?background=000000&cropX1=537&cropX2=1617&cropY1=0&cropY2=1080",
    "https://specials-images.forbesimg.com/imageserve/5ece9582c65052000615e18d/416x416.jpg?background=000000&cropX1=1908&cropX2=3897&cropY1=365&cropY2=2353"
]

import requests

for i in range(len(names)):
    res = requests.get(urls[i]).content
    name = names[i].lower().replace(" ", "-")
    with open(f"faces/{name}.jpg", "wb+") as f:
        f.write(res)