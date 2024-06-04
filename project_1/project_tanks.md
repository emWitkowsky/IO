```js
console.log(tankBrown, tankGreen, bulletsBrown, bulletsGreen);
fs.appendFile(
	"data-logs.csv",
	getParams(tankBrown, tankGreen, bulletsBrown, bulletsGreen),
	function (err) {
		if (err) throw err;
		console.log("Saved!");
	}
);
```
Witam






Zapraszam na niezapomnianą podróż w głąb projektu o czołgach, bytach bardzo opornych
na naukę.

## Trudne początki

Pierwszym krokiem jaki należało poczynić było zrozumienie jak czołgi mają działać.
Co wydaje im rozkazy, jakie są ich możliwości, jakie są ich ograniczenia (nie licząc ograniczeń intelektualnych).
Dostajemy dataset z informacjami o czołgach, ich poruszaniu, ogólnie rzecz biorąc wszystkich ich parametrach.

Ale jak to dostajemy? No właśnie, nie ma tak łatwo. Dataset musimy sobie sami stworzyć. A raczej wygenerować!
Grając w czołgi dane o grze są co parę milisekund drukowane w konsoli przeglądarki. 

Ciekawostką jest, że nie da się zapisywać automatycznie danych z konsoli przeglądarki. A już na pewno nie tak
by to porządnie zautomatyzować.

Trzeba więc było zrobić grę! Odwzorować ją w kodzie tak, aby działała na lokalnej maszynie, dzięki temu łatwiej było pozyskać
informacje o czołgach. Oczywiście byłoby zbyt prosto, gdyby wszystko działało jednym prostym skryptem, prawda?

Do tego służą nam nasze "narzędzia" w katalogu tools
- merger.py
- remover.py

odpowiedzialne kolejno za łączenie logów poszczególnych gier oraz "oczyszczanie ich" z niepotrzebnych linii, 
które sprawiłyby, że plik nie nadaje się do użycia jako dataset w formacie .csv.

## Mamy dataset! To koniec problemów, prawda? PRAWDA!?

Otóż nie do końca. Dataset zrobiony, ale przecież nieużyty, czyż nie? Więc trzeba stworzyć program który
ładnie nam pokieruje czołgiem

## Trudne małżeństwo Javascriptu i Pythona, czyli podejście do problemu z użyciem sieci neuronowych.

Na pierwszy ogień poszły sieci neuronowe. W końcu to one były podłożem tego projektu dla innych roczników.
Ale jak to zrobić? Sieci neuronowe w Pythonie, a czołgi i ich sterowanie to czysty javascript? Wybory były dwa,
albo dziwna abominacja rodem z horroru front-endowca, czyli tensorflow.js, albo tak jak używaliśmy na laboratoriach -
tensorflow w pythonie. Padło na to drugie. A więc musimy jakoś połączyć te dwa światy. Dataset oczywiście importujemy do pythona,
przerabiamy usuwając wszystkie niepotrzebne kolumny, a następnie trenujemy sieć. Ale jak to zrobić, by móc użyć jej w javascript?
Możemy zapisywać wszystkie nasze wartościowe rzeczy do osobnego pliku z którego następnie będziemy mogli
wygodnie przenosić do javascripta. Ale czego tak naprawdę potrzebujemy? Wag oraz biasów.


```js
function(e) {

    var response = {};
    var enemy = e.data.enemyTank;
    var me = e.data.myTank;

    var input = [me.x/500.0, me.y/500.0, me.rotation/360.0];

    var weights1 = [[0.469707190990448, 0.015171557664871216, -1.0566596984863281, -0.03467557579278946], [-0.26583370566368103, -0.05403166264295578, 0.828546941280365, -0.13687510788440704], [-0.14759941399097443, 0.22920820116996765, 0.1436581313610077, -0.33593568205833435], [0.12857216596603394, -0.39240580797195435, 0.2858048677444458, 0.3360889256000519], [-0.33789029717445374, -0.024244673550128937, 0.7948184609413147, -0.17035016417503357], [-0.1365824192762375, -0.08542539179325104, -0.5259692668914795, 0.15220661461353302]]
    var bias1 = [1.0032048225402832, -0.322238028049469, 1.5959007740020752, -0.290200799703598];

    var hidden = [0,0,0];

    var i,j;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            hidden[i] = input[j] * weights1[i*3+j];
        }
        hidden[i] = hidden[i] + bias1[i];
        hidden[i] = 1/(1 + Math.pow(Math.E, -hidden[i]));
    }

    var weights2 = [[2.0227553844451904], [-0.23896346986293793], [0.9771156311035156], [-0.30267131328582764]];
    var bias2 = [0.8896425366401672];

    var output = [0,0,0,0];

    for (i = 0; i < 4; i++) {
        for (j = 0; j < 3; j++) {
            output[i] = hidden[j] * weights2[i*3+j];
        }
        output[i] = output[i] + bias2[i];
        output[i] = 1/(1 + Math.pow(Math.E, -output[i]))
        output[i] = Math.round(output[i]);
    }

    // output[2] = 1;
    // output[3] = 1;
    response.turnLeft = output[0];
    response.turnRight = output[1];
    response.goForward = output[2];
    response.goBack = output[3];

    self.postMessage(response);

}
```

Nasz podsawowy kod, który będzie ewoluował wraz z naszymi postępami w nauce. Warto zauważyć, że to na co patrzymy, to 
w zasadzie ręcznie zrobiony model sieci neuronowej, który w zasadzie nie ma nic wspólnego z tym co zrobiliśmy w pythonie.
Brak mu tylko wag, które musieliśmy stworzyć sami w pythonie (a raczej nasz cudowny model za nas).

## Co się stanie gdy ego twórcy bierze górę?

### Zaczyna on konkurować z własnym dziełem, uważając, że jest lepszy od niego...

I w taki oto sposób, sam stworzyłem własny skrypt, który miał za zadanie "zmierzyć" się z siecią neuronową.
