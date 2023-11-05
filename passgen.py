import string, random, datetime, sys, math, os, getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:l:", ["header", "pool", "linenumbers",])
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit()

allChars = {
    "latin_lower":"abcdefghijklmnopqrstuvwxyz",
    "latin_upper":"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "arabic_numbers":"0123456789",
    "symbols":"\"\'€!§%&/()=?`´[￥]{}@#*+~><_-|\\:.;,°^£$",
    "ascii":"¡¦¨©«¬®¯±¶·¸»¿×÷¤¢¥¹½¼²³¾ªáÁàÀâÂåÅäÄãÃæÆçÇðÐéÉèÈêÊëËíÍìÌîÎïÏñÑºòÒôÔöÖõÕøØßúÚÙûÛüÜýÝÿþÞµծ",
    "cyrillic":"АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя",
    "japanese":"ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ゗゛゜ゝゞゟー「」。ㇰㇱㇲㇳㇴㇵㇶㇷㇸㇹㇺㇻㇼㇽㇾㇿ゠ァアィイゥウェエォカガキギグケゲコゴサザシジスズセゼソゾタダチヂッツヅデトドナニヌハバパヒビピフブプヘベペボポミモャヤュョヨリルレロヮワヰヱヲンヴヵヶヷヸヹヺ・ヽヾヿ",
    "polish":"żŻŹźśŚóÓńŃłŁęĘćĆąĄ",
    "arabic":"بجدهوزحطيكلمنصعفضقرستثخذظغشء",
    "hebrew":"אבּבגדהוזחטיכּלמנסעפּפצקרשׁשׂתּת",
    "thai":"กขคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ",
    # "cursed":"؄۞۝Ԕ",
    "kanji":"オクテネノホマムメユラ一丁七万丈三上下不与世丘丙両並中丶丸丹主丼乃久之乏乗乙九也乱乳乾亀了予争事二云互五井亜亡交亨京亭亮人仁今介仏仕他付仙代令以仮仰仲件任企伊伎伏休会伝伯伴伸伺似但位低住佐体何余作佳併使例侍供依価侮侵便係促俊俗保信修俯俳俺倉個倍倒候借値倫倹偉偏停健側偵偶偽傍傘備催債傷傾働像僕僚僧儀億償優元兄充兆先光克免児党入全八公六共兵其具典兼内円冊再冒冗写冠冬冷凄凍凝凡処凶出刀刃分切刈刊刑列初判別利到制刷券刺刻則削前剖剛剣剤剥副剰割創劇力功加劣助努励労効勇勉動勘務勝募勢勤勧勾勿匂包化北匠匹区医匿十千午半卑卒卓協南単博占印危即却卵卸厄厚原厭厳去参又及友双反収叔取受口古句叩叫召可台叱史右叶号司各合吉吊同名吐向君否含吸吹吾呂呆呉告呑呟周呪味呼命和咥咲咳哀品哉員哲唄唇唐唯唱唾商問啓善喉喋喚喜喧喫営嗅嘆嘉嘘嘩嘲噂噛器噴囚四回因団困囲図固国國圏園土圧在圭地坂均坊坦坪垂型垢垣埃埋城域執培基埼堀堂堅堕堤堪報場堵塀塁塊塔塗塚塞塩塵塾境墓増墜壁壇壊士壮声売変夏夕外多夜夢大天太夫央失奇奈奉奏契套奥奨奪奮女奴好如妄妊妙妥妨妬妹妻姉始姓委姦姫姿威娘娠娯婆婚婦媒媛嫁嫌嬉嬢子孔孕字存孝季孤学孫宅宇守安完宏宗官宙定宛宜宝実客宣室宮宰害宴家容宿寂寄密富寒寛寝察寧審寮寸寺対寿封専射将尊尋導小少尚就尺尻尼尽尾尿局居屈届屋展属層履屯山岐岡岩岬岳岸峰島崎崩嵐嶋巌川州巡巣工左巧巨差己巷巻巾市布帆希帝師席帯帰帳常帽幅幌幕幡干平年幸幹幻幼幽幾庁広床序底店府度座庫庭庶康廃廊延廷建廻弁弊式弓引弘弟弥弦弧弱張強弾当彙形彦彩彫彰影役彼往征径待律後徐徒従得御復循微徳徴徹心必忍志忘忙応忠快念怒怖思怠急性怪怯恋恐恒恥恨恩息恵悔悟悠患悦悩悪悲悶情惑惚惜惨想愁愉意愚愛感慈態慌慎慢慣慨慮慰慶憂憎憤憧憩憲憶憾懐懸懺成我戒戚戦戯戴戸戻房所扁扇扉手才打払扱批承技抄把抑投抗折抜択披抱抵押抽担拉拍拐拒拓拗拘招拝拠拡括拭拳拶拷拾持指挑挙挟挨挫振挿捉捕捜捨捻掃授掌排掘掛採探接控推措掲掴掻揃描提揚換握揮援揺損搭携摂摘摩撃撒撤撫播撮撲操擦擬攣支改攻放政故敏救敗教敢散敦敬数整敵敷文斉斎斐料斜斤斬断新方施旅旋族旗既日旦旧旨早旬昆昇明易昔星映春昧昨昭是昼時晋晒晩普景晴晶智暇暑暖暗暦暫暮暴曇曖曜曰曲曳更書曽替最月有朋服朗望朝期木未末本札朱朴机杉李材村束条来杯東松板析枕林枚果枝枠枯架柄某染柔柱柳柴柵査栃栄栗校株核根格栽桁桂桃案桐桑桜梅梗梢梨械梶棄棋棒棚棟森棺椅植椎検椿業極楽概構様槻槽標模権横樫樹橋橘機檎欄欠次欣欧欲欺歌歓止正武歩歪歯歳歴死殆殊残殖殴段殺殻殿毅母毎毒比毛氏民気水氷永汁求汎汗汚江池汲決沈沖沙没沢河沸油治沼沿況泉泊法泡波泣泥注泰泳洋洒洗洞津洪活派流浅浜浦浩浪浮浴海浸消涙涯液涼淀淡深淳混添清渇済渉渋減渡渦温測港湖湘湧湯湾湿満源準溜溝溢溶滅滋滑滝滞滲滴漁漂漏演漠漢漫漬潔潜潟潤潮潰澄澤激濁濃濡濯瀬火灯灰災炊炎炬炭点為烈焚無焦然焼煙照煩煮煽熊熟熱燃燥燵爆爪父爺片版牛牧物牲特犠犬犯状狂狙狩独狭狼猛猥猫献猿獄獣獲玄率玉王珍珠班現球理琉琢琴瑞璧環瓜甘甚生産用甫田由甲申男町画界畑留畜略番異畳畿疎疑疲疾病症痙痛痢痩痴痺瘍療癒癖発登白百的皆皇皮皺皿盆益盗盛盟監盤盧目盲直相盾省眉看県真眠眩眺眼着睡督睨瞬瞳瞼矛矢知矩短石砂研砕砲破硝硬碁確磁磨礎示礼社祈祉祖祝神祥票祭禁福秀私秋科秒秘秩称移程税稚種稲稼稽稿穂積穏穫穴究空突窃窓窮立竜章童端競竹笑笠符第笹筆筈等筋筒答策箇算管箱箸節範篇築簡簿籍米粉粋粒粗粘粧精糖糞糸系紀約紅紋納紐純紙級紛素索紫累細紳紹紺終組経結絞絡給統絵絶絹継続維綱網綴綺綾綿緊総緑緒線締編緩緯練縁縄縛縦縮績繁繊繋織繕繰缶罪置罰署羅羊美群羨義羽翅翌習翔翻翼老考者耐耳聖聞聡聴職肉肌肖肝股肢肥肩肪肯育肺胃胆背胞胡胸能脂脅脆脇脈脚脱脳腐腕腫腰腹腺膚膜膝膨臆臓臣臨自臭至致興舌舎舐舗舞舟航般船艦良色艶芋芝芦花芳芸芽苗苛若苦英茂茄茨茶草荒荘荷菅菊菌菓菜華菱萌落葉著葛葬蒸蒼蓄蓋蓑蔵薄薗薦薬藍藤藩藻蘇蘭虎虐虚虫虹蚊蛇蛍蝶融蟻血衆行術街衛衝衡衣表衰袋袖被裁裂装裏裕補裸製裾複褒襲西要覆覇見規視覗覚覧親観角解触言訂計訊討訓託記訝訟訪設許訳訴診証詐評詞試詩詫詮詰話該詳誇誉誌認誓誕誘語誠誤説読誰課調談請論諦諭諸諾謀謎謙講謝謡識譜警議譲護谷豆豊豚象豪貌貝貞負財貢貧貨販貫責貯貰貴貶買貸費貼貿賀賃賄資賊賑賛賞賠賢質賭購贅贈赤走赴起超越趣足距跡路跳践踊踏蹴躇躊躍身車軌軍軒軟転軸軽較載輔輝輩輪輸辛辞辱農辺込辿迎近返迫述迷追退送逃逆透途這通速造連逮週進逸遂遅遇遊運遍過道達違遠遣遥適遭遮遷選遺避還那邦邪郊郎郡部郭郵郷都配酒酔酷酸醒醜釈里重野量金針釣釧鈍鈴鉄鉢鉱銀銃銅銘銭鋭錆錯録鍋鍛鍵鎌鎖鎮鏡鑑長門閉開間関閣閥閲闇闘阜阪防阻阿陀附降限院陣除陥陰陳陶陸険陽隅隆隊階随隔隙際障隠隣雀雄雅集雇雌雑離難雨雪雰雲零雷電需震霊霜霞霧露青靖静非面革靴鞄韓音韻響頁頂頃項順須預頑頓領頬頭頷頻頼題額顎顔顕願類顧風飛食飢飯飲飴飼飽飾養餌館首香馬馴駄駅駆駐駿騎騒験騙驚骨高髪髭鬱鬼魁魂魅魔魚魯鮮鯉鳥鳩鳴鶴鷹鹸鹿麗麦麺麻黄黒黙鼓鼻齢龍"
}

oFile = f"/dev/shm/pass-gen.txt" # Output file destination
charPoolUsed = []

def getRandomString(charPool, intLen):
    returnString = ""
    k = 0
    if type(charPool) == list:
        while k < intLen:
            pickedPool = charPool if len(charPool) == 1 else random.choice(charPool)
            returnString += ''.join(random.choice(pickedPool))
            checkAddToPool(pickedPool)
            k += 1
    else:
        returnString += ''.join(random.choice(charPool) for i in range(intLen))
    return returnString
def shuffleString(toShuffleString):
    if type(toShuffleString) == list:
        toShuffleString = ''.join(toShuffleString)
    return ''.join(random.sample(toShuffleString,len(toShuffleString)))
def checkAddToPool(charPool):
    if includePoolUsedInHeader and writeHeaderInfo and charPool not in charPoolUsed:
        charPoolUsed.append(charPool)
def getCustomRandomChars(charLen, excludeList = []):
    thisPass = ""
    for index, item in allChars.items(): 
        if index in excludeList: continue
        thisPass += getRandomString(item, charLen)
    return thisPass

pCache = ""
pCacheLimit = 500 # Max. amount of passwords stored in cache before the cache is written to file
pCacheCount = 0

maxPass = 1 # Max. number of passwords to generate
singlePasswordLength = 26 # Length of one single password, per line
currentPassCount = 0

allTogether = []
for index, item in allChars.items():
    allTogether.append(item)

base_len = 0

addLineNumbers = False # Add line numbers to output
writeHeaderInfo = False # Write info about this generated password batch to output
includePoolUsedInHeader = False # Include list of pool used to generate password in the header
outputToSTDOUT = True # Print output to stdout instead of to a file

if len(opts) > 0:
    for opt, arg in opts:
        if opt == "-n":
            maxPass = int(arg)
            continue
        if opt == "-l":
            singlePasswordLength = int(arg)
            continue
        if opt == "--header":
            writeHeaderInfo = True
            continue
        if opt == "--pool":
            includePoolUsedInHeader = True
            continue
        if opt == "--linenumbers":
            addLineNumbers = True
            continue

if not outputToSTDOUT and os.path.isfile(oFile):
    os.remove(oFile)
if not outputToSTDOUT: f = open(oFile, "a")
while currentPassCount < maxPass: # Where the magic happens. Main loop to generate passwords
    pCacheCount += 1
    currentPassCount += 1
    finalPass = ""

    # Add one single character from everygroup
    basePass = ""
    for item in allTogether:
        randStr = getRandomString(item, 1)
        checkAddToPool(item)
        basePass += randStr
    finalPass += basePass
    base_len = len(basePass)

    finalPass += getRandomString(allTogether,singlePasswordLength-base_len)

    finalWritePass = shuffleString(finalPass)
    if len(finalWritePass) <= 0:
        print("ABORTED: Generated password length seems to be 0")
        sys.exit()
    if addLineNumbers:
        finalWritePass = f"{currentPassCount}. {finalWritePass}"
    pCache += f"{finalWritePass}\n" # Write password to cache

    # Write cache to file if:
    # - Cache limit reached
    # - Max. number of generated passwords reached
    if (pCacheCount == pCacheLimit) or (currentPassCount == maxPass):
        if writeHeaderInfo:
            writeHeaderInfo = False
            writeCache = ""
            writeCache += f"# Passwords in total: {maxPass}\n"
            writeCache += f"# Single password length: {len(finalPass)}"
            if includePoolUsedInHeader:
                tempVar = "".join(charPoolUsed)
                writeCache += f"\n# Character pool ({len(tempVar)}): {tempVar}"
            if not outputToSTDOUT:
                f.write(writeCache + "\n")
            else:
                print(writeCache + "\n")
        pCacheCount = 0
        if not outputToSTDOUT:
            f.write(pCache)
        else:
            print(pCache)
        pCache = ""
if not outputToSTDOUT:
    f.close()
    print(f"Generated {maxPass} password(s) in file '{oFile}'")
