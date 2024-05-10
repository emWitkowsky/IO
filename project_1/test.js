// const fs = require('fs');
//
// // Funkcja do zapisu do pliku
// function zapiszDoPliku(nazwaPliku, zawartosc) {
//   fs.writeFile(nazwaPliku, zawartosc, (err) => {
//     if (err) {
//       console.error('Błąd podczas zapisywania do pliku:', err);
//       return;
//     }
//     console.log('Zapisano do pliku', nazwaPliku);
//   });
// }
//
// // Przykładowa zawartość, którą chcesz zapisać do pliku
// const zawartoscDoZapisu = `
// Kolumna1,Kolumna2,Kolumna3
// Wartość1,Wartość2,Wartość3
// Wartość4,Wartość5,Wartość6
// `;
//
// // Wyświetlenie zawartości w konsoli
// console.log(zawartoscDoZapisu);
//
// // Zapisanie do pliku
// zapiszDoPliku('test.csv', zawartoscDoZapisu);


// Funkcja do pobierania i zapisywania zawartości konsoli do localStorage
function zapiszZawartoscDoLocalStorage() {
  // Pobranie zawartości konsoli
  const zawartoscKonsoli = captureConsole();

  // Pobranie istniejącej zawartości z localStorage, jeśli istnieje
  const istniejacaZawartosc = localStorage.getItem('zawartoscKonsoli') || '';

  // Łączenie nowej i istniejącej zawartości
  const nowaZawartosc = istniejacaZawartosc + '\n' + zawartoscKonsoli;

  // Zapisanie do localStorage
  localStorage.setItem('zawartoscKonsoli', nowaZawartosc);

  // Informacja o zapisie
  console.log('Zapisano zawartość konsoli do localStorage.');
}

// Funkcja pomocnicza do przechwytywania zawartości konsoli
function captureConsole() {
  const log = console.log;
  let capturedText = '';

  console.log = function (message) {
    capturedText += message + '\n';
    log.apply(console, arguments);
  };

  return capturedText;
}

// Uruchomienie interwału co 40 sekund
setInterval(zapiszZawartoscDoLocalStorage, 40000);
