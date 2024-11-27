<div>
	<script>
		const xlyokaviziray = () => {
			let stoynost = document.getElementById("tekstovo-pole").value;

			stoynost = stoynost.replaceAll("а", "a");
			stoynost = stoynost.replaceAll("б", "b");
			stoynost = stoynost.replaceAll("в", "v");
			stoynost = stoynost.replaceAll("г", "g");
			stoynost = stoynost.replaceAll("д", "d");
			stoynost = stoynost.replaceAll("е", "e");
			stoynost = stoynost.replaceAll("ж", "j");
			stoynost = stoynost.replaceAll("з", "z");
			stoynost = stoynost.replaceAll("и", "i");
			stoynost = stoynost.replaceAll("й", "y");
			stoynost = stoynost.replaceAll("к", "k");
			stoynost = stoynost.replaceAll("л", "l");
			stoynost = stoynost.replaceAll("м", "m");
			stoynost = stoynost.replaceAll("н", "n");
			stoynost = stoynost.replaceAll("о", "o");
			stoynost = stoynost.replaceAll("п", "p");
			stoynost = stoynost.replaceAll("р", "r");
			stoynost = stoynost.replaceAll("с", "s");
			stoynost = stoynost.replaceAll("т", "t");
			stoynost = stoynost.replaceAll("у", "u");
			stoynost = stoynost.replaceAll("ф", "f");
			stoynost = stoynost.replaceAll("х", "h");
			stoynost = stoynost.replaceAll("ц", "c");
			stoynost = stoynost.replaceAll("ч", "q");
			stoynost = stoynost.replaceAll("ш", "x");
			stoynost = stoynost.replaceAll("щ", "xt");
			stoynost = stoynost.replaceAll("ъ", "w");
			stoynost = stoynost.replaceAll("ь", "y");
			stoynost = stoynost.replaceAll("ю", "yu");
			stoynost = stoynost.replaceAll("я", "ya");

			stoynost = stoynost.replaceAll("А", "A");
			stoynost = stoynost.replaceAll("Б", "B");
			stoynost = stoynost.replaceAll("В", "V");
			stoynost = stoynost.replaceAll("Г", "G");
			stoynost = stoynost.replaceAll("Д", "D");
			stoynost = stoynost.replaceAll("Е", "E");
			stoynost = stoynost.replaceAll("Ж", "J");
			stoynost = stoynost.replaceAll("З", "Z");
			stoynost = stoynost.replaceAll("И", "I");
			stoynost = stoynost.replaceAll("Й", "Y");
			stoynost = stoynost.replaceAll("К", "K");
			stoynost = stoynost.replaceAll("Л", "L");
			stoynost = stoynost.replaceAll("М", "M");
			stoynost = stoynost.replaceAll("Н", "N");
			stoynost = stoynost.replaceAll("О", "O");
			stoynost = stoynost.replaceAll("П", "P");
			stoynost = stoynost.replaceAll("Р", "R");
			stoynost = stoynost.replaceAll("С", "S");
			stoynost = stoynost.replaceAll("Т", "T");
			stoynost = stoynost.replaceAll("У", "U");
			stoynost = stoynost.replaceAll("Ф", "F");
			stoynost = stoynost.replaceAll("Х", "H");
			stoynost = stoynost.replaceAll("Ц", "C");
			stoynost = stoynost.replaceAll("Ч", "Q");
			stoynost = stoynost.replaceAll("Ш", "X");
			stoynost = stoynost.replaceAll("Щ", "Xt");
			stoynost = stoynost.replaceAll("Ъ", "W");
			stoynost = stoynost.replaceAll("Ь", "Y");
			stoynost = stoynost.replaceAll("Ю", "Yu");
			stoynost = stoynost.replaceAll("Я", "Ya");

			document.getElementById("tekstovo-pole").value = stoynost;
		}

		const kiriliziray = () => {
			let stoynost = document.getElementById("tekstovo-pole").value;

			stoynost = stoynost.replaceAll("ya", "я");
			stoynost = stoynost.replaceAll("Ya", "Я");

			stoynost = stoynost.replaceAll("yu", "ю");
			stoynost = stoynost.replaceAll("Yu", "Ю");

			stoynost = stoynost.replaceAll("xty", "щь");
			stoynost = stoynost.replaceAll("Xty", "Щь");

			stoynost = stoynost.replaceAll("by", "бь");
			stoynost = stoynost.replaceAll("vy", "вь");
			stoynost = stoynost.replaceAll("gy", "гь");
			stoynost = stoynost.replaceAll("dy", "дь");
			stoynost = stoynost.replaceAll("jy", "жь");
			stoynost = stoynost.replaceAll("zy", "зь");
			stoynost = stoynost.replaceAll("ky", "кь");
			stoynost = stoynost.replaceAll("ly", "ль");
			stoynost = stoynost.replaceAll("my", "мь");
			stoynost = stoynost.replaceAll("ny", "нь");
			stoynost = stoynost.replaceAll("py", "пь");
			stoynost = stoynost.replaceAll("ry", "рь");
			stoynost = stoynost.replaceAll("sy", "сь");
			stoynost = stoynost.replaceAll("ty", "ть");
			stoynost = stoynost.replaceAll("fy", "фь");
			stoynost = stoynost.replaceAll("hy", "хь");
			stoynost = stoynost.replaceAll("cy", "ць");
			stoynost = stoynost.replaceAll("qy", "чь");
			stoynost = stoynost.replaceAll("xy", "шь");

			stoynost = stoynost.replaceAll("By", "Бь");
			stoynost = stoynost.replaceAll("Vy", "Вь");
			stoynost = stoynost.replaceAll("Gy", "Гь");
			stoynost = stoynost.replaceAll("Dy", "Дь");
			stoynost = stoynost.replaceAll("Jy", "Жь");
			stoynost = stoynost.replaceAll("Zy", "Зь");
			stoynost = stoynost.replaceAll("Ky", "Кь");
			stoynost = stoynost.replaceAll("Ly", "Ль");
			stoynost = stoynost.replaceAll("My", "Мь");
			stoynost = stoynost.replaceAll("Ny", "Нь");
			stoynost = stoynost.replaceAll("Py", "Пь");
			stoynost = stoynost.replaceAll("Ry", "Рь");
			stoynost = stoynost.replaceAll("Sy", "Сь");
			stoynost = stoynost.replaceAll("Ty", "Ть");
			stoynost = stoynost.replaceAll("Fy", "Фь");
			stoynost = stoynost.replaceAll("Hy", "Хь");
			stoynost = stoynost.replaceAll("Cy", "Ць");
			stoynost = stoynost.replaceAll("Qy", "Чь");
			stoynost = stoynost.replaceAll("Xy", "Шь");

			stoynost = stoynost.replaceAll("xt", "щ");
			stoynost = stoynost.replaceAll("Xt", "Щ");

			stoynost = stoynost.replaceAll("a", "а");
			stoynost = stoynost.replaceAll("b", "б");
			stoynost = stoynost.replaceAll("v", "в");
			stoynost = stoynost.replaceAll("g", "г");
			stoynost = stoynost.replaceAll("d", "д");
			stoynost = stoynost.replaceAll("e", "е");
			stoynost = stoynost.replaceAll("j", "ж");
			stoynost = stoynost.replaceAll("z", "з");
			stoynost = stoynost.replaceAll("i", "и");
			stoynost = stoynost.replaceAll("y", "й");
			stoynost = stoynost.replaceAll("k", "к");
			stoynost = stoynost.replaceAll("l", "л");
			stoynost = stoynost.replaceAll("m", "м");
			stoynost = stoynost.replaceAll("n", "н");
			stoynost = stoynost.replaceAll("o", "о");
			stoynost = stoynost.replaceAll("p", "п");
			stoynost = stoynost.replaceAll("r", "р");
			stoynost = stoynost.replaceAll("s", "с");
			stoynost = stoynost.replaceAll("t", "т");
			stoynost = stoynost.replaceAll("u", "у");
			stoynost = stoynost.replaceAll("f", "ф");
			stoynost = stoynost.replaceAll("h", "х");
			stoynost = stoynost.replaceAll("c", "ц");
			stoynost = stoynost.replaceAll("q", "ч");
			stoynost = stoynost.replaceAll("x", "ш");
			stoynost = stoynost.replaceAll("w", "ъ");

			stoynost = stoynost.replaceAll("A", "А");
			stoynost = stoynost.replaceAll("B", "Б");
			stoynost = stoynost.replaceAll("V", "В");
			stoynost = stoynost.replaceAll("G", "Г");
			stoynost = stoynost.replaceAll("D", "Д");
			stoynost = stoynost.replaceAll("E", "Е");
			stoynost = stoynost.replaceAll("J", "Ж");
			stoynost = stoynost.replaceAll("Z", "З");
			stoynost = stoynost.replaceAll("I", "И");
			stoynost = stoynost.replaceAll("Y", "Й");
			stoynost = stoynost.replaceAll("K", "К");
			stoynost = stoynost.replaceAll("L", "Л");
			stoynost = stoynost.replaceAll("M", "М");
			stoynost = stoynost.replaceAll("N", "Н");
			stoynost = stoynost.replaceAll("O", "О");
			stoynost = stoynost.replaceAll("P", "П");
			stoynost = stoynost.replaceAll("R", "Р");
			stoynost = stoynost.replaceAll("S", "С");
			stoynost = stoynost.replaceAll("T", "Т");
			stoynost = stoynost.replaceAll("U", "У");
			stoynost = stoynost.replaceAll("F", "Ф");
			stoynost = stoynost.replaceAll("H", "Х");
			stoynost = stoynost.replaceAll("C", "Ц");
			stoynost = stoynost.replaceAll("Q", "Ч");
			stoynost = stoynost.replaceAll("X", "Ш");
			stoynost = stoynost.replaceAll("W", "Ъ");

			document.getElementById("tekstovo-pole").value = stoynost;
		}
	</script>

	<textarea style="width: 100%; resize: vertical" id="tekstovo-pole"></textarea>
	<br>
	<button onclick="xlyokaviziray()">xlyokaviziray!</button>
	<button onclick="kiriliziray()">кирилизирай!</button>
</div>

Xlyokavicata e nerazdelna i interesna qast ot bwlgarskata kultura. V tazi statiya razglejdam
razliqni stilove, predlagam nov takwv i davam cyalostnoto si mnenie za fenomena, vwpreki qe nikoy
ne mi go e iskal.

Statiyata e napisana na predlojeniyat stil, zaxtoto e tematiqno.

## Tehniqeski predpostavki

Osnovnata azbuka na telekomunikacionnite sistemi (telefoni, internet i dr.) e angliyskata latinica.
Tova veroyatno se dwlji na golemiyat prinos na Xtatite kwm razvitieto im, no az ne swm istorik i xte
ostavya istoriqeskiyat analiz drugimu. Pri vsiqki sluqai, navlizaneto na sistemi, poddwrjaxti
na pwrvo myasto angliyskata latinica, v sredi, kwdeto tya е nedostatwqna, swzdava izvestni problemi.
Problemi se swzdavat dori za ispancite, koito priemat _ñ_ za bukva, korenno razliqna ot _n_.

Osven telekomunikacionnite sistemi, (kato cyalo) nay-bogatite i kulturni dwrjavi pixat na latinica,
taka qe pone imenata si tryabva da mojem da napixem na tyahnata azbuka.

## Kulturni predpostavki

Ograniqeniyata na telekomunikacionnite sistemi veqe poqti ne swxtestvuvat, a obiknoveniyat qovek
ryadko tryabva da si napixe imeto, taka qe qujdenec da go proqete. Gledayki samo tezi dva priznaka,
bihme oqakvali qe poqti nikoy ne pixe na xlyokavica v dnexno vreme. Tova ne e taka.

Vyarvam qe xlyokavicata ima golyama kulturna i izrazna potrebnost. Neynite potrebiteli qesto ya
polzvat, za da pridadat neseriozen/priyatelski ton na napisanoto. V tozi smiswl, neynoto izpolzvane
e podobno na izpuskaneto na prepinatelni znaci, izpolzvaneto na malka bukva v naqaloto na
izreqenieto i izpolzvaneto na jargonni dumi i frazi.

Podobno na jargona, toqniyat stil xlyokavica moje da e priznak na podkultura, kwm koyato prinadleji
swotvetniyat potrebitel -- qovek izpolzvaxt _4_ i _6_ za _ч_ i _ш_ veroyatno e na nad 25 godixna
vwzrast i baya si e pisal po skype navremeto. Novi stilove izpolzvat _x_ i _y_ za _х_ i _у_, no az
ne prinwdleja kwm podkulturite koito gi polzvat, taka qe ne bih mogwl da kaja na kakvo sa priznak.

Estestveno vseki qovek ima sobstven stil na pisane. V tozi smiswl pisaneto na xlyokavica e
sebeizrazyavane, koeto ne moje da bwde izpwlneno qrez pisaneto na kirilica.

## Kultirni _ne_postavki

Bwlgarskiyat narod i ezik sa iztoqnikwt na kirilicata, koyato pwk e swzdadena specialno za nego.
Osven qe kirilicata e kulturno nasledstvo na Bwlgariya, tya prosto e po-udobna. Da ya sravnyavame s
latinicata e kato da sravnyavame kustyum, premeren i uxit za toqno opredelen qovek, s kustyum ot
magazina -- kirilicata e premerena i uxita za nas i e po-udobna. Poradi tezi priqini mnogo hora,
vklyuqitelno i az, sa protiv pisaneto na xlyokavica.

Edinstvenoto, koeto protivnicite na xlyokavicata mogat da napravyat, e da ne ya polzvat. Tova obaqe
nyama da spre drugite. Vwpreki qe swm protiv xlyokavicata, swm rexil da uqastvam v neynoto razvitie,
zaxtoto mi e intersno.

## Stilove i razswjdeniya po tyah

V Bwlgarskiyat ezik priswstvat ~12 bukvi, koito trudno se xlyokavizirat. Razliqnite stilove
sa kombinaciya ot izbori za izpisvaneto na vsyaka ot tyah.

- ж -- j, zh, ž
- й -- j, y, i
- у -- u, y, ou _spored nyakakwv si Andrey Danqev_
- х -- h, x, kh _spored Velikobritaniya_
- ц -- c, ts
- ч -- ch, č, 4
- ш -- sh, š, 6
- щ -- sht, št, 6t
- ъ -- u, a, e _napr, v imeto Dimit**e**r_
- ь -- j, y, izyadena
- ю -- yu, iu, ju, u
- я -- ya, ia, ja, q

Osven tozi katalog, ima i
[zakon za transliteraciyata](https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=16943).
Zakonwt za transliteraciyata realno pokriva samo xlyokaviziraneto na imena, no az xte go razglejdam
vse edno e cyalosten stil na xlyokavica.

Spored men, dobro xlyokavizirane ima slednite priznaci:

- Vwzmojno nay-malko _dvuznaci_ t.e. dve bukvi, znaqexti edin zvuk. Dvuznacite ne sa problem za
  zapisvaneto na _я_, _ю_, i _щ_, twy kato te sa dva zvuka.
- Vwzmojno nay-malko izklyuqeniya ot obxtoto pravilo.
- **Lesno _otxlyokavizirane_** -- dokolkoto znam az swm pwrviyat koyto twrsi takova. Pod
  _otxlyokavizirane_ imam predvid vwzmojnostta da se vwzstanovi originalniya tekst. Stilovete,
  otgovaryaxti na tozi priznak mogat da bwdat mnogo polezni za tehniqeski celi.
- Izpolzvane samo na angliyskata latinica

Ot gorniya spiswk az bih izbral slednata strategiya:

- ж -- j
- й -- y
- у -- u
- х -- h
- ц -- c
- ч -- ch
- ш -- sh
- щ -- sht
- ъ -- u
- ь -- y
- ю -- yu
- я -- ya

Strategiyata ne e perfektna. Ima dva dvuznaka i _u_ se izpolzva za dva zvuka. Zaradi tova e trudna
za otxlyokavizirane. Davam nyakolko primera:

- kurvi -- курви, кърви
- shema -- шема, схема

Strategiyata e mnogo po-dobra ot zakona za transliteraciyata. Zakonwt glasi slednoto:

- ж -- zh
- й -- y
- у -- u
- х -- h
- ц -- ts
- ч -- ch
- ш -- sh
- щ -- sht
- ъ -- a, osven v dumata _B**u**lgaria_
- ь -- y
- ю -- yu
- я -- ya, osven v kraya na dumata v swyuza _ия_, когато се пише _ia_

Tova e ot nay-loxite vwzmojni strategii. Ima qetiri dvuznaka, _a_ se izpolzva za dva zvuka i dve
izklyuqeniya. Liqno az mislya, qe _a_ e ujasno xlyokavizirane na _ъ_. Zakonwt yavno misli swxtoto,
zaxtoto tam e edno ot izklyuqeniyata. Osobeno twpo e xlyokaviziraneto na _ц_, twy kato pozvolyava
dvusmislieto _otselvane → оцелване, отселване_. Izklyuqenieto, kasaexto _я_, e nenujno i samo
uslojnyava sistemata. Az imam teoriya, qe tazi xlyokavizaciya e naroqno izmislena da e kolkoto se
moje, po-loxa...

## Predlojeniyat ot men stil

Kakto vidyahme ni ostavat tri problema -- _ч -- ch_, _ш -- sh_ и _ъ -- u_. Osven tyah ima i tri
neizpolzvani bukvi ot latinicata -- _q_, _x_ i _w_. Nablyudatelniyat qitatel e zabelyazal qe az
izpolzvam sledniya stil:

- ж -- j
- й -- y
- у -- u
- х -- h
- ц -- c
- ч -- q
- ш -- x
- щ -- xt
- ъ -- w
- ь -- y
- ю -- yu
- я -- ya

Tozi stil e **swvwrxen** spored zadadenite iziskvaniya. Osobeno udoben e kogato krwxtavam faylove na
kompyutwra si. Naprimer zaglaviyata na statiite v tazi stranica se pazyat na xlyokavica i se
otxlyokavizirat za da izlizat na kirilica. Izpolzvam go i kogato me mwrzi da si smenya ezika na
klaviaturata. Swxtestvuva problemwt qe e malko neintuitiven za novi qitateli i qesto me pitat dali
swm piyan kogato pixa s nego.
