# Uczenie-si-ze-wzmocnieniem-pojekt# TrackMania Reinforcement Learning

## Opis projektu

Projekt realizowany w ramach przedmiotu **Uczenie się ze wzmocnieniem** na Politechnice Rzeszowskiej w roku akademickim 2026/2027.

Celem projektu jest zaprojektowanie, implementacja i analiza agenta wykorzystującego uczenie ze wzmocnieniem (Reinforcement Learning) do autonomicznego sterowania pojazdem w grze **TrackMania 2020**.

Agent będzie uczył się samodzielnego pokonywania wyznaczonej trasy poprzez podejmowanie decyzji dotyczących przyspieszania, hamowania oraz skręcania. Podstawą podejmowanych decyzji będą dane telemetryczne opisujące aktualny stan pojazdu oraz jego położenie względem trasy.

Głównym celem jest opracowanie strategii jazdy pozwalającej na uzyskanie możliwie krótkiego czasu przejazdu przy jednoczesnym ograniczeniu błędów, takich jak kolizje i wypadanie poza trasę.

## Wykorzystywane technologie

- **Python** – główny język programowania.
- **TrackMania 2020** – środowisko, w którym będzie działał agent.
- **TrackmaniaRL** – biblioteka wykorzystywana do komunikacji z grą i odczytu danych telemetrycznych.
- **PyTorch** – framework do implementacji modeli uczenia maszynowego.
- **Gymnasium** – interfejs środowiska uczenia ze wzmocnieniem.
- **NumPy** – operacje numeryczne.
- **Pandas** – analiza i przetwarzanie wyników eksperymentów.
- **Matplotlib** – wizualizacja wyników i procesu uczenia.

## Założenia projektu

Agent będzie wykorzystywał dane telemetryczne, zamiast bezpośredniej analizy obrazu z ekranu.

Wstępnie planowane informacje wykorzystywane przez agenta:

- pozycja pojazdu,
- aktualna prędkość,
- orientacja pojazdu,
- położenie względem trasy,
- geometria najbliższego fragmentu toru,
- postęp na trasie.

Planowane działania agenta:

- przyspieszanie,
- hamowanie,
- skręcanie w lewo,
- skręcanie w prawo,
- utrzymywanie kierunku jazdy.

Dokładna reprezentacja stanu, przestrzeni akcji oraz funkcji nagrody zostanie ustalona po weryfikacji dostępnych danych telemetrycznych i pierwszych testach środowiska.

## Planowane etapy realizacji

1. Przygotowanie środowiska i integracja z biblioteką TrackmaniaRL.
2. Odczyt i analiza danych telemetrycznych.
3. Przygotowanie formalizacji problemu jako MDP.
4. Implementacja środowiska i agenta bazowego.
5. Implementacja algorytmu uczenia ze wzmocnieniem.
6. Przeprowadzenie eksperymentów i analiza wyników.
7. Przygotowanie sprawozdania projektowego.

## Struktura projektu

```text
trackmania-reinforcement-learning/
│
├── report/             # Sprawozdanie LaTeX
│
├── src/                # Kod źródłowy projektu
│
├── experiments/        # Konfiguracje i skrypty eksperymentów
│
├── results/            # Wyniki i dane eksperymentalne
│
├── README.md
├── requirements.txt
└── .gitignore
```

Struktura będzie rozwijana wraz z kolejnymi etapami realizacji projektu.

## Biblioteka TrackmaniaRL

Projekt wykorzystuje otwartą bibliotekę TrackmaniaRL:

https://github.com/TrackmaniaRL/TrackmaniaRL

Biblioteka stanowi podstawę integracji z grą i dostępu do danych wykorzystywanych podczas uczenia agenta.

## Status projektu

**Etap E1 – temat, repozytorium i wstępna formalizacja problemu.**

Projekt znajduje się na etapie przygotowania koncepcji i założeń technicznych. Implementacja oraz eksperymenty zostaną przeprowadzone w kolejnych etapach.

## Autor

Sebastian Gęborys

Politechnika Rzeszowska  
Wydział Elektrotechniki i Informatyki  
Rok akademicki 2026/2027

---

Projekt realizowany w ramach przedmiotu Uczenie się ze wzmocnieniem.
