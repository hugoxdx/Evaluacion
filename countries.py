from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router= APIRouter()

class country(BaseModel):
    code:str
    surface_area: int
    population: int
    life_expectancy:float
    local_name:str
    government_form:str
    heaf_state:str

country_list=[country(code="AGO", surface_area=1246700, population=12678000, life_expectancy=38.3, local_name="Angola", government_form="Republic", heaf_state="Jose Eduardo Dos Santos"),
              country(code="BDI", surface_area=27834, population=6695000, life_expectancy=46.2, local_name="Burundi/uburundi", government_form="Republic", heaf_state="Pierre Buyoya"),
              country(code="BEN", surface_area=112622, population=6097000, life_expectancy=50.2, local_name="Benin", government_form="Republic", heaf_state="Mathieu Kerekou"),
              country(code="BFA", surface_area=274000, population=11937000, life_expectancy=46.7, local_name="Buskina Faso", government_form="Republic", heaf_state="Blaise Compaore"),
              country(code="BWA", surface_area=581730, population=1622000, life_expectancy=39.3, local_name="Botswana", government_form="Republic", heaf_state="Festus G. Mogae"),
              country(code="CAF", surface_area=622984, population=3615000, life_expectancy=44, local_name="Centrafrique/Be-Afrika", government_form="Republic", heaf_state="Ange-Felix Patasse"),
              country(code="CIV", surface_area=322463, population=14786000, life_expectancy=45.2, local_name="Cote dIvoire", government_form="Republic", heaf_state="Laurent Gbagbo"),
              country(code="CMR", surface_area=475442, population=15085000, life_expectancy=54.8, local_name="Cameroun", government_form="Republic", heaf_state="Paul Biya"),
              country(code="COD", surface_area=2344858, population=51654000, life_expectancy=48.8, local_name="Republique Democratique du Congo", government_form="Republic", heaf_state="Joseph Kabila"),
              country(code="COG", surface_area=342000, population=2943000, life_expectancy=47.4, local_name="Congo", government_form="Republic", heaf_state="Denis Sassou-Nguesso"),
              country(code="COM", surface_area=1862, population=578000, life_expectancy=60, local_name="Comores", government_form="Republic", heaf_state="Azali Assoumani"),
              country(code="CPV", surface_area=4033, population=428000, life_expectancy=68.9, local_name="Cabo Verde", government_form="Republic", heaf_state="Antonio Mascarenhas Monteiro"),
              country(code="DJI", surface_area=23200, population=638000, life_expectancy=50.8, local_name="Jibuti", government_form="Republic", heaf_state="Ismail Omar Guelleh"),
              country(code="DZA", surface_area=2381741, population=31471000, life_expectancy=69.7, local_name="Al-Jazair/Algerie", government_form="Republic", heaf_state="Abdelaziz Bouteflika"),
              country(code="EGY", surface_area=1001449, population=68470000, life_expectancy=63.3, local_name="Misr", government_form="Republic", heaf_state="Hosni Mubarak"),
              country(code="ERI", surface_area=117600, population=3850000, life_expectancy=55.8, local_name="Ertra", government_form="Republic", heaf_state="Isayas Afewerki"),
              country(code="ESH", surface_area=266000, population=293000, life_expectancy=49.8, local_name="As-Sahrawiya", government_form="Occupied by Marocco", heaf_state="Mohammed Abdel Aziz"),
              country(code="ETH", surface_area=1104300, population=62565000, life_expectancy=45.2, local_name="YeItyop iya", government_form="Republic", heaf_state="Negasso Gidada"),
              country(code="GAB", surface_area=267668, population=1226000, life_expectancy=50.1, local_name="Le Gabon", government_form="Republic", heaf_state="Omar Bongo"),
              country(code="GHA", surface_area=238533, population=20212000, life_expectancy=57.4, local_name="Ghana", government_form="Republic", heaf_state="John Kufuor"),
              country(code="GIN", surface_area=245857, population=7430000, life_expectancy=45.6, local_name="Guinee", government_form="Republic", heaf_state="Lansana Conte"),
              country(code="GMB", surface_area=11295, population=1305000, life_expectancy=53.2, local_name="The Gambia", government_form="Republic", heaf_state="Yahya Jammeh"),
              country(code="GNB", surface_area=36125, population=1213000, life_expectancy=49, local_name="Guine-Bissau", government_form="Republic", heaf_state="Kumba lala"),
              country(code="GNQ", surface_area=28051, population=4530000, life_expectancy=53.6, local_name="Guinea Ecuatorial", government_form="Republic", heaf_state="Teodoro Obiang Nguema Mbasogo"),
              country(code="IOT", surface_area=78, population=0, life_expectancy=0, local_name="British Indian Ocean Territory", government_form="Dependent Territory of the uK", heaf_state="Elisabeth II"),
              country(code="KEN", surface_area=580367, population=30080000, life_expectancy=48, local_name="Kenya", government_form="Republic", heaf_state="Daniel arap Moi"),
              country(code="LBR", surface_area=111369, population=3154000, life_expectancy=51, local_name="Liberia", government_form="Republic", heaf_state="Charles Taylor"),
              country(code="LBY", surface_area=1759540, population=5605000, life_expectancy=75.4, local_name="Libiya", government_form="Socialistic State", heaf_state="Muammar al-Qadhafi"),
              country(code="LSO", surface_area=30355, population=2153000, life_expectancy=50.8, local_name="Lesotho", government_form="Constitutional Monarchy", heaf_state="Letsie III"),
              country(code="MAR", surface_area=446550, population=28351000, life_expectancy=69.1, local_name="Al-Maghrib", government_form="Constitutional Monarchy", heaf_state="Mohammed VI"),
              country(code="MDG", surface_area=587041, population=15942000, life_expectancy=55, local_name="Madagascar", government_form="Federal Republic", heaf_state="Didier Ratsiraka"),
              country(code="MLI", surface_area=1240192, population=11234000, life_expectancy=46.7, local_name="Mali", government_form="Republic", heaf_state="Alpha Oumar Konare"),
              country(code="MOZ", surface_area=801590, population=19680000, life_expectancy=37.5, local_name="Mocambique", government_form="Republic", heaf_state="JoaquIm A. Chissano"),
              country(code="MRT", surface_area=1025520, population=2670000, life_expectancy=50.8, local_name="Muritaniya/Mauritanie", government_form="Republic", heaf_state="Maaouiya Ould Sid Ahmad Taya"),
              country(code="MuS", surface_area=2040, population=1158000, life_expectancy=71, local_name="Mauritius", government_form="Republic", heaf_state="Cassam uteem"),
              country(code="MWI", surface_area=118484, population=10925000, life_expectancy=37.6, local_name="Malawi", government_form="Republic", heaf_state="Bakili Muluzi"),
              country(code="MYT", surface_area=373, population=149000, life_expectancy=59.5, local_name="Mayotte", government_form="Territorial Collectivity of France", heaf_state="Jacques Chirac"),
              country(code="NAM", surface_area=824292, population=1726000, life_expectancy=42.5, local_name="Namibia", government_form="Republic", heaf_state="Sam Nujoma"),
              country(code="NER", surface_area=1267000, population=10730000, life_expectancy=41.3, local_name="Niger", government_form="Republic", heaf_state="Mamadou Tandja"),
              country(code="NGA", surface_area=923768, population=111506000, life_expectancy=51.6, local_name="Nigeria", government_form="Federal Republic", heaf_state="Olusegun Obasanjo"),
              country(code="REu", surface_area=2510, population=699000, life_expectancy=72.7, local_name="Reunion", government_form="Overseas Department of France", heaf_state="Jacques Chirac"),
              country(code="RWA", surface_area=26338, population=7733000, life_expectancy=39.3, local_name="Rwanda", government_form="Republic", heaf_state="Paul Kagame"),
              country(code="SDN", surface_area=2505813, population=29490000, life_expectancy=56.6, local_name="As-Sudan", government_form="Islamic Republic", heaf_state="Omar Hassan Ahmad al-Bashir"),
              country(code="SEN", surface_area=196722, population=9481000, life_expectancy=62.2, local_name="Senegal", government_form="Republic", heaf_state="Abdoulaye Wade"),
              country(code="SHN", surface_area=314, population=6000, life_expectancy=76.8, local_name="Saint Helena", government_form="Dependent Territory of the uK", heaf_state="Elisabeth II"),
              country(code="SLE", surface_area=71740, population=4854000, life_expectancy=45.3, local_name="Sierra Leone", government_form="Republic", heaf_state="Ahmed Tejan Kabbah"),
              country(code="SOM", surface_area=637657, population=10097000, life_expectancy=46.2, local_name="Soomaaliya", government_form="Republic", heaf_state="Abdiqassim Salad Hassan"),
              country(code="STP", surface_area=964, population=147000, life_expectancy=65.3, local_name="Sao Tome e PrIncipe", government_form="Republic", heaf_state="Miguel Trovoada"),
              country(code="SWZ", surface_area=17364, population=1008000, life_expectancy=40.4, local_name="kaNgwane", government_form="Monarchy", heaf_state="Mswati III"),
              country(code="SYC", surface_area=455, population=77000, life_expectancy=70.4, local_name="Seychelles", government_form="Republic", heaf_state="France-Albert Rene"),
              country(code="TCD", surface_area=1284000, population=7651000, life_expectancy=50.5, local_name="TCHAD TSHAD", government_form="REPUBLIC", heaf_state="IDRISS DEBY"),
            country(code="TGO", surface_area=56785, population=4629000, life_expectancy=54.7, local_name="TOGO", government_form="REPUBLIC", heaf_state="GNASSINGBE EYADEMA"),
            country(code="TUN", surface_area=163610, population=9586000, life_expectancy=73.7, local_name="TUNIS TUNISIE", government_form="REPUBLIC", heaf_state="ZINE AL ABIDINE BEN ALI"),
            country(code="TZA", surface_area=883749, population=33517000, life_expectancy=52.3, local_name="TANZANIA", government_form="REPUBLIC", heaf_state="BENJAMIN WILLIAM MKAPA"),
            country(code="UGA", surface_area=241038, population=21778000, life_expectancy=42.9, local_name="UGANDA", government_form="REPUBLIC", heaf_state="YOWERI MUSEVENI"),
            country(code="ZAF", surface_area=1221037, population=40377000, life_expectancy=51.1, local_name="SOUTH AFRICA", government_form="REPUBLIC", heaf_state="THABO MBEKI"),
            country(code="ZMB", surface_area=752618, population=9169000, life_expectancy=37.2, local_name="ZAMBIA", government_form="REPUBLIC", heaf_state="FRDERICK HILUBA"),
            country(code="ZWE", surface_area=390757, population=11669000, life_expectancy=37.8, local_name="ZIMBABWE", government_form="REPUBLIC", heaf_state=""),
            country(code="ATA", surface_area=13120000, population=0, life_expectancy= 0, local_name="NA", government_form="", heaf_state=""),
            country(code="ATF", surface_area=7780, population=0, life_expectancy=0, local_name="TERRES AUSTRALES FRANCAISES", government_form="CO ADMINISTRATED", heaf_state="JACQUES CHIRAC"),
            country(code="BVT", surface_area=59, population=0, life_expectancy=0, local_name="BOUVETOYA", government_form="NONMETROPOLITAN TERRITC JACQUES CHIRAC", heaf_state="HARALD V"),
            country(code="HMD", surface_area=359, population=0, life_expectancy=0, local_name="HEARD AND MCDONALD ISNLAND", government_form="TERRITORY OF AUSTRALIS", heaf_state="ELISABETH II"),
            country(code="SGS", surface_area=3903, population=0, life_expectancy=0, local_name="SOUTH GEORGIA AND THE SOUTH SANDWICH ISLA", government_form="DEPENDENT TERRITORY", heaf_state="ELISABETH II"),
            country(code="AFG", surface_area=652090, population=22720000, life_expectancy=45.9, local_name="AFGANISTAN", government_form="ISLAMIC EMIRATE", heaf_state="MOHAMMAD OMAR"),
            country(code="ARE", surface_area=83600, population=2441000, life_expectancy=74.1, local_name="AL IMARAT AL ARABIYA AL MUTTAHIDA", government_form="EMIRATE FEDERATION", heaf_state="ZAYID BIN SULTAN AL NAHAYAN"),
            country(code="ARM", surface_area=29800, population=3520000, life_expectancy=66.5, local_name="HAJASTAN", government_form="REPUBLIC", heaf_state="ROBERT KOTSARJAN"),
            country(code="AZE", surface_area=86600, population=7734000, life_expectancy=62.9, local_name="AZARBAYCAN", government_form="FEDERAL REPUBLIC", heaf_state="HEYDAR ALIYEV"),
            country(code="BGD", surface_area=143998, population=129155000, life_expectancy=60.2, local_name="BANGLADESH", government_form="REPUBLIC", heaf_state="SHAHABUDDIN AHMAD"),
            country(code="BHR", surface_area=694, population=617000, life_expectancy=73, local_name="AL BAHRAYN", government_form="MONARCHY EMIRATES", heaf_state="HAMAD IBN ISA AL KHALIFA"),
            country(code="BRN", surface_area=5765, population=328000, life_expectancy=73.6, local_name="BRUNEI DARUSSALAM", government_form="MONARCHY SULTANATE", heaf_state="HAJI JASSAN AL BOLKIAH"),
            country(code="BTN", surface_area=47000, population=2124000, life_expectancy=52.4, local_name="DRUK YUL", government_form="MONARCHY", heaf_state="JIGME SINGYE WANGCHUK"),
            country(code="CHN", surface_area=9572900, population=1277558000, life_expectancy=71.4, local_name="ZHOPQUO", government_form="PEOPLES REPUBLIC", heaf_state="JIANG ZEMIN"),
            country(code="CYP", surface_area=9251, population=754700, life_expectancy=76.7, local_name="KYPROS", government_form="REPUBLIC", heaf_state="GLAFKOS KLERIDES"),
            country(code="GEO", surface_area=69700, population=4968000, life_expectancy=64.5, local_name="SAKARTVELO", government_form="REPUBLIC", heaf_state="ADUARD SEVARDNADZE"),
            country(code="HKG", surface_area=1075, population=6782000, life_expectancy=79.5, local_name="XIANGGANG", government_form="SPECIAL ADMINISTRATIVE REGION", heaf_state="JIANG ZEMIN"),
            country(code="IDN", surface_area=1904569, population=2122107000, life_expectancy=68, local_name="INDONESIA", government_form="REPUBLIC", heaf_state="ADBSURRAHMAN WAHIH"),
            country(code="IND", surface_area=3287263, population=1013662000, life_expectancy=62.5, local_name="BHARAT", government_form="FEDERAL REPUBLIC", heaf_state="KOCHERIL RAMAN NARATANAN"),
            country(code="IRN", surface_area=1648195, population=67702000, life_expectancy=69.7, local_name="IRAN", government_form="ISLAMIC REPUBLIC", heaf_state="ALI MOHAMMAD KHATAMI ARDAKAR"),
            country(code="IRQ", surface_area=438317, population=23115000, life_expectancy=66.5, local_name="AL IRAQ", government_form="REPUBLIC", heaf_state="SADDAM HUSSEIN AL TAKRITI"),
            country(code="ISR", surface_area=21056, population=6217000, life_expectancy=78.6, local_name="YISTAEL", government_form="REPUBLIC", heaf_state="MOSHE KATZAV"),
            country(code="JOR", surface_area=88946, population=5083000, life_expectancy=77.4, local_name="AL URDUNN", government_form="CONSTITUCIONAL MONARCHY", heaf_state="ABDULLAH II"),
            country(code="JPN", surface_area=377829, population=126714000, life_expectancy=80.7, local_name="NIHON", government_form="CONSTITUTIONAL MONARCHY", heaf_state="AKIHITO"),
            country(code="KAZ", surface_area=2724900, population=16223000, life_expectancy=63.2, local_name="QAZAQSTAN", government_form="REPUBLIC", heaf_state="NURSULTAN NAZARBAJEV"),
            country(code="KGZ", surface_area=199900, population=4699000, life_expectancy=63.4, local_name="KRGYZSTAN", government_form="REPUBLIC", heaf_state="ASKAR AKAJEV"),
            country(code="KHM", surface_area=181035, population=11168000, life_expectancy=56.5, local_name="KAMPUCHA", government_form="CONSTITUTIONAL MONARCHY", heaf_state="NORODOM SIHANOUK"),
            country(code="KOR", surface_area=99434, population=46844000, life_expectancy=74.4, local_name="TAEHAN MINGUK", government_form="REPUBLIC", heaf_state="KIM DAE JUNG"),
            country(code="KWT", surface_area=17818, population=1972000, life_expectancy=76.1, local_name="AL KUWAYT", government_form="CONSTITUIONAL MONARCHY EMIRATOS ARABES", heaf_state="JABIR AL AHMAD AL JABIR AL SABAH"),
            country(code="LAO", surface_area=236800, population=5433000, life_expectancy=53.1, local_name="LAO", government_form="REPUBLIC", heaf_state="KHAMTAY SIPHANDONE"),
            country(code="LBN", surface_area=10400, population=3282000, life_expectancy=71.3, local_name="LUBNAN", government_form="REPUBLIC", heaf_state="EMILE LAHOUD"),
            country(code="LKA", surface_area=65610, population=18827000, life_expectancy=71.8, local_name="SRI LANKA", government_form="REPUBLIC", heaf_state="CHANDRIKA KUMARATUNGA"),
            country(code="MAC", surface_area=18, population=473000, life_expectancy=81.6, local_name="MACAU", government_form="SPECIAL ADMINISTRATIVE REGION", heaf_state="JIANG ZEMIN"),
            country(code="MDV", surface_area=298, population=286000, life_expectancy=62.2, local_name="DHIVEHI RAAJJE", government_form="REPUBLIC", heaf_state="MAUMOON ABDUL GAYOOM"),
            country(code="MMR", surface_area=676578, population=45611000, life_expectancy=54.8, local_name="MYANMA PYE", government_form="REPUBLIC", heaf_state="KENRAALI THAN SHWE"),
            country(code="MNG", surface_area=1566500, population=2662000, life_expectancy=67.3, local_name="MONGOL", government_form="REPUBLIC", heaf_state="NATSAGIIN BAGABADI"),
            country(code="MYS", surface_area=329758, population=22244000, life_expectancy=70.8, local_name="MALAYSIA", government_form="CONSTITUTIONAL MONARCHY FEDERATION", heaf_state="SALAHUDDIN ABDUL AZIZ SHAH ALHA"),
            country(code="NPL", surface_area=147181, population=23930000, life_expectancy=57.8, local_name="NEPAL", government_form="CONSTITUTIONAL MONARCHY", heaf_state="GYANENDRA BIR BIKRAM"),
            country(code="OMN", surface_area=309500, population=2542000, life_expectancy=71.8, local_name="UMAN", government_form="MONARCHY SULTANATE", heaf_state="QABUS IBN SA ID"),
            country(code="PAK", surface_area=796095, population=156483000, life_expectancy=61.1, local_name="PAKISTAN", government_form="REPUBLIC", heaf_state="MAHAMMAD RAFIW TARAR"),
            country(code="PHL", surface_area=300000, population=7596000, life_expectancy=67.5, local_name="PILIPINAS", government_form="REPUBLIC", heaf_state="GLORIA MACAPAGAL ARROYO"),
            country(code="PRK", surface_area=120538, population=24039000, life_expectancy=70.5, local_name="CHOSON MINJUJUUI LN MIN", government_form="SOCIALISTIC REPUBLIC", heaf_state="KIM JONG IL"),
            country(code="PSE", surface_area=6257, population=3101000, life_expectancy=71.4, local_name="FILASTIN", government_form="AUTONOMOUS AREA", heaf_state="YASSER ARAFAT"),
            country(code="QAT", surface_area=11000, population=599000, life_expectancy=72.4, local_name="QATAR", government_form="MONARCHY", heaf_state="HAMAD IBN KHALIFA AL THANI"),
            country(code="SAu", surface_area=214690, population=21607000, life_expectancy=67.8, local_name="Al- Arabiya as-Sa udiya", government_form="MONARCHY", heaf_state="Fahd ibn Abdul-Aziz al-Sa ud"),
            country(code="SGP", surface_area=618, population=3567000, life_expectancy=80.1, local_name="Singapur", government_form="Republic", heaf_state="Sellapan Rama Nathan"),
            country(code="SYR", surface_area=185180, population=16125000, life_expectancy=68.5, local_name="Suriya", government_form="Republic", heaf_state="Bashar al-Assad"),
            country(code="THA", surface_area=513115, population=61399000, life_expectancy=68.6, local_name="Prathet Thai", government_form="Constitutional MONARCHY", heaf_state="Bhumibol Adulyadej"),
            country(code="TJK", surface_area=143100, population=6188000, life_expectancy=64.1, local_name="Tocikiston", government_form="Republic", heaf_state="Emomali Rahmonov"),
            country(code="TKM", surface_area=488100, population=4459000, life_expectancy=60.9, local_name="Turkmenostan", government_form="Republic", heaf_state="Saparmurad Nijazov"),
            country(code="TMP", surface_area=14874, population=885000, life_expectancy=46, local_name="Timor Timur", government_form="Administrated by the uN", heaf_state="Jose Alexandre Gusmao"),
            country(code="TuR", surface_area=774815, population=66591000, life_expectancy=71, local_name="Turkiye", government_form="Republic", heaf_state="Ahmet Necdet Sezer"),
            country(code="TWN", surface_area=36188, population=22256000, life_expectancy=76.4, local_name="Tai-wan", government_form="Republic", heaf_state="Chen Shui-bian"),
            country(code="uZB", surface_area=447400, population=24318000, life_expectancy=63.7, local_name="uzbekiston", government_form="Republic", heaf_state="Islam Karimov"),
            country(code="VNM", surface_area=331689, population=79832000, life_expectancy=69.3, local_name="Viet Nam", government_form="Socialistic Republic", heaf_state="Tran Duc Luong"),
            country(code="YEM", surface_area=527968, population=18112000, life_expectancy=59.8, local_name="Al-Yaman", government_form="Republic", heaf_state="Ali Abdallah Salih"),
            country(code="ALB", surface_area=28748, population=3401200, life_expectancy=71.6, local_name="Shqiperia", government_form="Republic", heaf_state="Rexhep Mejdani"),
            country(code="AND", surface_area=468, population=78000, life_expectancy=83.5, local_name="Andorra", government_form="Parliamentary Coprincipality", heaf_state=""),
            country(code="AuT", surface_area=83859, population=8091800, life_expectancy=77.7, local_name="osterreich", government_form="Federal Republic", heaf_state="Thomas Klestil"),
            country(code="BEL", surface_area=30518, population=10239000, life_expectancy=77.8, local_name="Belgique", government_form="Constitutional Monarchy, Federation", heaf_state="Albert II"),
            country(code="BGR", surface_area=110994, population=8190900, life_expectancy=70.9, local_name="Balgarija", government_form="Republic", heaf_state="Petar Stojanov"),
            country(code="BIH", surface_area=51197, population=3972000, life_expectancy=71.5, local_name="Bosna", government_form="Federal Republic", heaf_state="Ante Jelavic"),
            country(code="BLR", surface_area=207600, population=10236000, life_expectancy=68, local_name="Belarus", government_form="Republic", heaf_state="Aljaksandr LukaSenka"),
            country(code="CHE", surface_area=41284, population=7160400, life_expectancy=79.6, local_name="Schweiz", government_form="Federation", heaf_state="Adolf Ogi"),
            country(code="CZE", surface_area=78866, population=10278100, life_expectancy=74.5, local_name="esko", government_form="Republic", heaf_state="Vaclav Havel"),
            country(code="DEu", surface_area=357022, population=82164700, life_expectancy=77.4, local_name="Deutschland", government_form="Federal Republic", heaf_state="Johannes Rau"),
            country(code="DNK", surface_area=43094, population=5330000, life_expectancy=76.5, local_name="Danmark", government_form="Constitutional Monarchy", heaf_state="Margrethe II"),
            country(code="ESP", surface_area=505992, population=39441700, life_expectancy=78.8, local_name="Espana", government_form="Constitutional Monarchy", heaf_state="Juan Carlos I"),
            country(code="EST", surface_area=45227, population=1439200, life_expectancy=69.5, local_name="Eesti", government_form="Republic", heaf_state="Lennart Meri"),
            country(code="FIN", surface_area=338145, population=5171300, life_expectancy=77.4, local_name="Suomi", government_form="Republic", heaf_state="Tarja Halonen"),
            country(code="FRA", surface_area=551500, population=59225700, life_expectancy=78.8, local_name="France", government_form="Republic", heaf_state="Jacques Chirac"),
            country(code="FRO", surface_area=1399, population=43000, life_expectancy=78.4, local_name="Foroyar", government_form="Part Of Denmark", heaf_state="Margrethe II"),
            country(code="GBR", surface_area=242900, population=59623400, life_expectancy=77.7, local_name="united Kingdom", government_form="Constitutional Monarchy", heaf_state="Elisabeth II"),
            country(code="GIB", surface_area=6, population=25000, life_expectancy=79, local_name="Gibraltar", government_form="Dependent Territory of the uK", heaf_state="Elisabeth II"),
            country(code="GRC", surface_area=131626, population=1054700, life_expectancy=78.4, local_name="Ellada", government_form="Republic", heaf_state="Kostis Stefanopoulos"),
            country(code="HRV", surface_area=56538, population=4473000, life_expectancy=73.7, local_name="Hrvatska", government_form="Republic", heaf_state="Stipe Mesic"),
            country(code="HuN", surface_area=93030, population=10043200, life_expectancy=71.4, local_name="Magyarorszag", government_form="Republic", heaf_state="Ferenc Madl"),
            country(code="IRL", surface_area=70273, population=3775100, life_expectancy=76.8, local_name="Ireland", government_form="Republic", heaf_state="Mary McAleese"),
            country(code="ISL", surface_area=103000, population=279000, life_expectancy=72.4, local_name="Island", government_form="Republic", heaf_state="olafur Ragnar GrImsson"),
            country(code="ITA", surface_area=301316, population=57680000, life_expectancy=79, local_name="Italia", government_form="Republic", heaf_state="Carlo Azeglio Ciampi"),
            country(code="LIE", surface_area=160, population=32300, life_expectancy=78.8, local_name="Liechtenstein", government_form="Constitutional Monarchy", heaf_state="Hans-Adam II"),
            country(code="LTu", surface_area=65301, population=3698500, life_expectancy=69.1, local_name="Lietuva", government_form="Republic", heaf_state="Valdas Adamkus"),
            country(code="LuX", surface_area=2586, population=435700, life_expectancy=77.1, local_name="Luxembourg", government_form="Constitutional Monarchy", heaf_state="Henri"),
            country(code="LVA", surface_area=64589, population=2424200, life_expectancy=68.4, local_name="Latvija", government_form="Republic", heaf_state="Vaira Vike-Freiberga"),
            country(code="MCO", surface_area=2, population=34000, life_expectancy=78.8, local_name="Monaco", government_form="Constitutional Monarchy", heaf_state="Rainier III"),
            country(code="MDA", surface_area=33851, population=4380000, life_expectancy=64.5, local_name="Moldova", government_form="Republic", heaf_state="Vladimir Voronin"),
            country(code="MKD", surface_area=25713, population=2024000, life_expectancy=73.8, local_name="Makendonija", government_form="Republic", heaf_state="Boris Trajkovski"),
            country(code="MLT", surface_area=316, population=380200, life_expectancy=77.9, local_name="Malta", government_form="Republic", heaf_state="Guido de Marco"),
            country(code="NLD", surface_area=41526, population=15864000, life_expectancy=78.3, local_name="Nederland", government_form="Constitutional Monarchy", heaf_state="Willem-Alexander"),
            country(code="NOR", surface_area=323877, population=4478500, life_expectancy=78.7, local_name="Norge", government_form="Constitutional Monarchy", heaf_state="Harald V"),
            country(code="POL", surface_area=323250, population=38653600, life_expectancy=73.2, local_name="Polska", government_form="Republic", heaf_state="Aleksander Kwasniewski"),
            country(code="PRT", surface_area=91982, population=9997600, life_expectancy=75.8, local_name="Portugal", government_form="Republic", heaf_state="Jorge Sampaio"),
            country(code="ROM", surface_area=238391, population=22455500, life_expectancy=69.9, local_name="Romania", government_form="Republic", heaf_state="Ion Iliescu"),
        country(code="RuS", surface_area=17075400, population=146934000, life_expectancy=67.2, local_name="Rossija", government_form="Federal republic",heaf_state="vladimir putin"),
            country(code="SJM", surface_area=62422, population=3200, life_expectancy=0, local_name="svalbard og jan Mayen", government_form="Dependent territory of norway", heaf_state="Harald V"),
            country(code="SMR", surface_area=61, population=27000, life_expectancy=81.1,local_name="San Marino", government_form="Republic",heaf_state="NuLL"),
            country(code="SVK", surface_area=49012, population=5398700, life_expectancy=73.7, local_name="Slovensko", government_form="Republic", heaf_state="rudolf Schuster"),
            country(code="SVN", surface_area=20256, population=1987800, life_expectancy=74.9, local_name="Slovenjia", government_form="Republic", heaf_state="Milan Kucan"),
            country(code="SWE", surface_area=449964, population=8861400, life_expectancy=79.6, local_name="Sverige", government_form="constitucional Monarchy", heaf_state="Carl XVI Gustaf"),
            country(code="uKR", surface_area=603700, population=50456000, life_expectancy=66, local_name="ukrajina", government_form="republic", heaf_state="leonid kusma"),
            country(code="VAT", surface_area=0.4, population=1000, life_expectancy=0, local_name="santa sede/ cita del vatinaco", government_form="independent church state", heaf_state="johannes paravali ll"),
            country(code="YuG", surface_area=102173, population=1064000, life_expectancy=72.4, local_name="jugoslavia", government_form="federal republic", heaf_state="vojislav kostunica"),
            country(code="ABW", surface_area=193, population=103000, life_expectancy=78.4, local_name="aruba", government_form="nonmetropolitan territory of the netherlands", heaf_state="willem alexander"),
            country(code="AIA", surface_area=96, population=8000, life_expectancy=86.1, local_name="Anguilla", government_form="Dependent territory of the uk", heaf_state="elisabeth ll"),
            country(code="ANT", surface_area=800, population=217000, life_expectancy=74.7, local_name="nederlandse antillen", government_form="nonmetropolitan territory of the netherland", heaf_state="willem alexander"),
            country(code="ATG", surface_area=442, population=68000, life_expectancy=70.5, local_name="antigua and barbuda", government_form="constitutional monarchy", heaf_state="elisabeth ll"),
            country(code="BHS", surface_area=13878, population=307000, life_expectancy=71.1, local_name="the bahamas", government_form="constitucional monarchy", heaf_state="elisabethll"),
            country(code="BLZ", surface_area=22696, population=241000, life_expectancy=70.09, local_name="beLize", government_form="constitucional monarchy", heaf_state="elisabeth ll"),
            country(code="BMu", surface_area=53, population=65000, life_expectancy=76.9, local_name="bermuda", government_form="dependent territory of the uk", heaf_state="elisabeth ll"),
            country(code="BRB", surface_area=430, population=27000, life_expectancy=73, local_name="barbados", government_form="constitucional monarchy", heaf_state="elisabeth ll"),
            country(code="CAN", surface_area=9970610, population=31147000, life_expectancy=79.4, local_name="canada", government_form="constitucional monarchy federation", heaf_state="elisabeth ll"),
            country(code="CRI", surface_area=51100, population=4023000, life_expectancy=78.8, local_name="costa rica", government_form="republic", heaf_state="miguel angel rodriguez"),
            country(code="CuB", surface_area=110861, population=11201000, life_expectancy=76.2, local_name="cuba", government_form="socialistic republic", heaf_state="fidel castro ruz"),
            country(code="CYM", surface_area=264,population=38000, life_expectancy=78.9, local_name="cayman island", government_form="dependent territory of the ok", heaf_state="elisabeth ll"),
            country(code="DMA", surface_area=751, population=71000, life_expectancy=73.4, local_name="dominica", government_form="republic", heaf_state="vernon shaw"),
            country(code="DOM", surface_area=48511, population=8495000, life_expectancy=73.2, local_name="republica dominicana", government_form="republic", heaf_state="hipolito mejia dominguez"),
            country(code="GLP", surface_area=1705, population=456000, life_expectancy=77, local_name="guadeloupe", government_form="oversar department of france", heaf_state="jacques chirac"),
            country(code="GRD", surface_area=344, population=94000, life_expectancy=64.5, local_name="grenada", government_form="constitucional monarchy", heaf_state="elisabeth ll"),
            country(code="GRL", surface_area=2166090, population=56000, life_expectancy=68.1, local_name="kalaallit nunaat gronland", government_form="part of denmark", heaf_state="margrethe ll"),
            country(code="GTM", surface_area=108889,population=1138500, life_expectancy=66.2, local_name="guatemala", government_form="republic", heaf_state="alfonso bertrand aristide"),
            country(code="HND", surface_area=112088, population=6485000, life_expectancy=69.9, local_name="honduras", government_form="republic", heaf_state="carlos roberto flores"),
            country(code="HTI", surface_area=27750, population=8222000, life_expectancy=49.2, local_name="hait dayti", government_form="republic", heaf_state="jean bertland aritse"),
            country(code="JAM", surface_area=10990, population=2583000, life_expectancy=75.2, local_name="jamaica", government_form="constitucional monarchy", heaf_state="elisabeth ll"),
            country(code="KNA", surface_area=261, population=38000, life_expectancy=70.7, local_name="saint kits and nevis", government_form="constitucional monarchy", heaf_state="elizabeth ll"),
            country(code="LCA", surface_area=622, population=154000, life_expectancy=72.3, local_name="saint lucia", government_form="constitucional monarchy", heaf_state="elizabeth ll"),
            country(code="MEX", surface_area=1958201, population=98881000, life_expectancy=71.5, local_name="mexico", government_form="federal republic", heaf_state="vicente fox quesada"),
            country(code="MSR", surface_area=102, population=11000, life_expectancy=78, local_name="montserrat", government_form="dependent territory of the uk", heaf_state="elisabeth ll"),
            country(code="MTQ", surface_area=1102, population=395000, life_expectancy=78.3, local_name="martinique", government_form="overseas department of france", heaf_state="jaques chirac"),
            country(code="NIC", surface_area=1130000, population=5074000, life_expectancy=68.7, local_name="nicaragua", government_form="repubic", heaf_state="arnoldo aleman lacayo"),
            country(code="PAN", surface_area=75517, population=2856000, life_expectancy=75.5, local_name="panama", government_form="republic", heaf_state="mireya elisa moscoco"),
            country(code="PRI", surface_area=8875, population=3869000, life_expectancy=75.6, local_name="puerto rico", government_form="comonweath of the us", heaf_state="george w bush"),
            country(code="SLV", surface_area=21041, population=6276000, life_expectancy=69.7, local_name="el salvador", government_form="republic", heaf_state="francisco guillermo"),
            country(code="SPM", surface_area=242, population=7000, life_expectancy=77.6, local_name="saint pierre et miquelon", government_form="territorial collectivity of france", heaf_state="jacques chirac"),
            country(code="TCA", surface_area=430, population=17000, life_expectancy=73.3, local_name="the turks and caicos island", government_form="dependent territory of the uk", heaf_state="elisabeth ll"),
            country(code="TTO", surface_area=5130, population=1295000, life_expectancy=68, local_name="trinidad and tobago", government_form="republic", heaf_state="arthur n r robinson"),
            country(code="uSA", surface_area=9363520, population=278357000, life_expectancy=77.1, local_name="united states", government_form="federal republic", heaf_state="george w bush"),
            country(code="VCT", surface_area=388, population=114000, life_expectancy=72.3, local_name="saint vincent and the grenadine", government_form="constitucional monarchy", heaf_state="elisabeth ll"),
            country(code="VGB", surface_area=151, population=21000, life_expectancy=75.4, local_name="british virgi island", government_form="dependent territory of the uk", heaf_state="elisabeth ll"),
            country(code="VIR", surface_area=347, population=93000, life_expectancy=78.1, local_name="virgin islands of the united state", government_form="territory", heaf_state="george w bush"),
            country(code="ASM", surface_area=199, population=68000, life_expectancy=75.1, local_name="america samoa", government_form="us territory", heaf_state="george w bush"),
            country(code="AuS", surface_area=7741200,  population=18886000, life_expectancy=79.8, local_name="australia", government_form="constitucional monarchy federation", heaf_state="elisabeth ll"),
            country(code="CCK", surface_area=14, population=600, life_expectancy=0, local_name="cocos (keeling)island", government_form="territory of australia", heaf_state="elisabeth ll"),
            country(code="CCK", surface_area=14, population=600, life_expectancy=0, local_name="COCOS (KEELING) ISLANDS", government_form="TERRITORY OF AUSTRALIA", heaf_state="ELISABETH II"),
            country(code="CXR", surface_area=135, population=2500, life_expectancy=0, local_name="CHRISTMAS ISLANDS", government_form="TERRITORY OF AUSTRALIA", heaf_state="ELISABETH II"),
            country(code="NFK", surface_area=36, population=2000, life_expectancy=0, local_name="NORFOLK ISLANDS", government_form="TERRITORY OF AUSTRALIA", heaf_state="ELISABETH II"),
            country(code="NZL", surface_area=270534, population=3862000, life_expectancy=77.8, local_name="NEW ZEALAND/AOTEAROA", government_form="CONSTITUTIONAL MONARCHY", heaf_state="ELISABETH II"),
            country(code="FJI", surface_area=18274, population=817000, life_expectancy=67.9, local_name="FIJI ISLANDS", government_form="REPUBLIC", heaf_state="JOSEFA ILOILO"),
            country(code="NCL", surface_area=18575, population=214000, life_expectancy=72.8, local_name="NOUVELLE-CALEDONIE", government_form="NONMETROPOLITAN TERRITORY OF FRANCE", heaf_state="JACQUES CHIRAC"),
            country(code="PNG", surface_area=462840, population=4807000, life_expectancy=63.1, local_name="Papua New Guinea/Papua Niugini", government_form="Constitutional Monarchy", heaf_state="Elisabeth II"),
            country(code="SLB", surface_area=28896, population=444000, life_expectancy=71.3, local_name="Solomon Islands", government_form="Constitutional Monarchy", heaf_state="Elisabeth II"),
            country(code="VuT", surface_area=12189, population=190000, life_expectancy= 60.6, local_name="Vanuatu", government_form="Republic", heaf_state="John Bani"),
            country(code="FSM", surface_area=702, population=119000, life_expectancy=68.6, local_name="Micronesia", government_form="Federal Republic", heaf_state="Leo A. Falcam"),
            country(code="GuM", surface_area=549, population=168000, life_expectancy=77.8, local_name="Guam", government_form="uS Territory", heaf_state="George W. Bush"),
            country(code="KIR", surface_area=726, population=83000, life_expectancy=59.8, local_name="Kiribati", government_form="Republic", heaf_state="Teburoro Tito"),
            country(code="MHL", surface_area=181, population=64000, life_expectancy=65.5, local_name="Marshall Islands/Majol", government_form="Republic", heaf_state="Kessai Note"),
            country(code="MNP", surface_area=464, population=78000, life_expectancy=75.5, local_name="Northern Mariana Islands", government_form="Commonwealth of the uS", heaf_state="George W. Bush"),
            country(code="NRU", surface_area=21, population=12000, life_expectancy=60.8, local_name="Naoero/Nauru", government_form="Republic", heaf_state="Bernard Dowiyogo"),
            country(code="PLW", surface_area=459, population=19000, life_expectancy=68.6, local_name="Belau/Palau", government_form="Republic", heaf_state="Kuniwo Nakamura"),
            country(code="UMI", surface_area=16, population=0, life_expectancy=0, local_name="united States Minor Outlying Islands", government_form="Dependent Territory of the uS", heaf_state="George W. Bush"),
            country(code="COK", surface_area=236, population=20000, life_expectancy=71.1, local_name="The Cook Islands", government_form="Nonmetropolitan Territory of New Zealand", heaf_state="Elisabeth II"),
            country(code="NIU", surface_area=260, population=2000, life_expectancy=0, local_name="Niue", government_form="Nonmetropolitan Territory of New Zealand", heaf_state="Elisabeth II"),
            country(code="PCN", surface_area=49, population=50, life_expectancy=0, local_name="Pitcairn", government_form="Dependent Territory of the uK", heaf_state="Elisabeth II"),
            country(code="PYF", surface_area=4000, population=235000, life_expectancy=74.8, local_name="Polynesie francaise", government_form="Nonmetropolitan Territory of France", heaf_state="Jacques Chirac"),
            country(code="TKL", surface_area=12, population=2000, life_expectancy=0, local_name="Tokelau", government_form="Nonmetropolitan Territory of New Zealand", heaf_state="Elisabeth II"),
            country(code="TON", surface_area=650, population=99000, life_expectancy=67.9, local_name="Tonga", government_form="Monarchy", heaf_state="Taufa'ahau Tupou IV"),
            country(code="TUV", surface_area=26, population=12000, life_expectancy=66.3, local_name="Tuvalu", government_form="Constitutional Monarchy", heaf_state="Elisabeth II"),
            country(code="WLF", surface_area=200, population=15000, life_expectancy=0, local_name="Wallis-et-Futuna", government_form="Nonmetropolitan Territory of France", heaf_state="Jacques Chirac"),
            country(code="WSM", surface_area=2831, population=180000, life_expectancy=69.2, local_name="Samoa", government_form="Parlementary Monarchy", heaf_state="Malietoa Tanumafili II"),
            country(code="ARG", surface_area=2780400, population=37032000, life_expectancy=75.1, local_name="Argentina", government_form="Federal Republic", heaf_state="Fernando de la Rua"),
            country(code="BOL", surface_area=1098581, population=8329000, life_expectancy=63.7, local_name="Bolivia", government_form="Republic", heaf_state="Hugo Banzer Suarez"),
            country(code="BRA", surface_area=8547403, population=170115000, life_expectancy=62.9, local_name="Brasil", government_form="Federal Republic", heaf_state="Fernando Henrique CardosoI"),
            country(code="CHL", surface_area=756626, population=15211000, life_expectancy=75.7, local_name="Chile", government_form="Republic", heaf_state="Ricardo Lagos Escobar"),
            country(code="COL", surface_area=1138914, population=42321000, life_expectancy=70.3, local_name="Colombia", government_form="Republic", heaf_state="Andres Pastrana Arango"),
            country(code="ECU", surface_area=283561, population=12646000, life_expectancy=71.1, local_name="Ecuador", government_form="REPUBLIC", heaf_state="Gustavo Noboa Bejarano"),
            country(code="FLK", surface_area=12173, population=2000, life_expectancy=0, local_name="Falkland Islands", government_form="Dependent Territory of the uK", heaf_state="Elisabeth II"),
            country(code="GUF", surface_area=90000, population=181000, life_expectancy=76.1, local_name="Guyane francaise", government_form="Overseas Department of France", heaf_state="Jacques Chirac"),
            country(code="GUY", surface_area=214969, population=861000, life_expectancy=64, local_name="Guyana", government_form="Republic", heaf_state="Bharrat Jagdeo"),
            country(code="PER", surface_area=1285216, population=25662000, life_expectancy=70, local_name="Peru/Piruw", government_form="Republic", heaf_state="Valentin Paniagua Corazao"),
            country(code="PRY", surface_area=406752, population=5496000, life_expectancy=73.7, local_name="Paraguay", government_form="Republic", heaf_state="Luis angel Gonzalez Macchi"),
            country(code="SUR", surface_area=163265, population=417000, life_expectancy=71.4, local_name="Suriname", government_form="REPUBLIC", heaf_state="Ronald Venetiaan"),
            country(code="URY", surface_area=175016, population=3337000, life_expectancy=75.2, local_name="LUBNAN", government_form="REPUBLIC", heaf_state="Jorge Batlle Ibanez"),
            country(code="VEN", surface_area=912050, population=24170000, life_expectancy=73.1, local_name="Venezuela", government_form="Federal Republic", heaf_state="Hugo Chavez FrIas"),
            ]
             



@router.get("/continent/region/country/")
async def imprimir():
    return (country_list)


#checar
@router.get("/continent/region/country/")
async def imprimir():
    return (country_list)
@router.get("/continent/region/country/")
async def imprimir():
    return (country_list)

@router.get("/continent/region/country/{id}")
async def imprimir(code:str):
    users=filter (lambda user: user.code == code, country_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

@router.get("/continent/region/country/")
async def imprimir(code:str):
    users=filter (lambda user: user.code == code, country_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}


@router.post("/continent/region/country/")
async def imprimir(user:country):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(country_list):
        if saved_user.code == user.code:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        country_list.append(user)
        return user
    
@router.put("/continent/region/country/")
async def imprimir(user:country):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(country_list):
        if saved_user.code == user.code:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           country_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/continent/region/country/{code}")
async def imprimir(code:str):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(country_list):
        if saved_user.code ==code:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del country_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
        return {"error":"No se ha eliminado el usuario"}