# Virtual Window — Unreal Engine 5 & OpenTrack

## 🪟 Idea Projektu
System wykorzystuje zjawisko **paralaksy**, reagując nie tylko na obroty głowy, ale przede wszystkim na jej przesunięcia (translacja X, Y, Z). Gdy użytkownik wychyla się przed monitorem lub przybliża do ekranu, perspektywa w Unreal Engine 5 zmienia się adekwatnie, pozwalając na "zaglądanie za obiekty" i ocenę głębi sceny bez użycia gogli VR.

## 🏗️ Architektura Systemu
System działa w oparciu o trzy główne moduły połączone sieciowo (localhost):

1.  **OpenTrack:** Śledzi pozycję głowy w czasie rzeczywistym i wysyła surowe dane 6DOF protokołem UDP (port 4242).
2.  **Most Komunikacyjny (Python):** Autorski skrypt pełniący rolę tłumacza. Odbiera pakiety binarne UDP, wyodrębnia informacje o pozycji oraz rotacji i przesyła uporządkowany wektor danych do silnika gry w formacie OSC.
3.  **Odbiornik (Unreal Engine 5):** Klasa `BP_HeadCamera`, która przekształca dane z czujników na ruch wirtualnej kamery (symulacja perspektywy off-axis).

## 💻 Implementacja Techniczna

### Konfiguracja Mostu (Python)
Skrypt odbiera dane z OpenTrack i rozpakowuje je do formatu czytelnego dla silnika. Kluczowe jest przekazanie pełnych 6 stopni swobody:
* **Translacja:** x, y, z (kluczowe dla efektu paralaksy)
* **Rotacja:** yaw, pitch, roll

### Logika Blueprint (UE5)
Blueprint odpowiada za matematyczne przekształcenie ruchów użytkownika na ruchy wirtualnej kamery. Główne elementy to:
* **Inwersja osi:** Dostosowanie kierunków ruchu, aby przesunięcie głowy w lewo powodowało naturalną zmianę perspektywy (zgodnie z zasadą działania okna).
* **Skalowanie:** Wzmocnienie sygnału, aby niewielkie ruchy przed monitorem przekładały się na wyraźne zmiany perspektywy w środowisku 3D.
* **Centrowanie (Reset):** Możliwość ustalenia "punktu zerowego" dla idealnego zsynchronizowania wirtualnej kamery z fizyczną pozycją monitora.

## 📈 Wyniki i Wnioski
Projekt zakończył się sukcesem. System poprawnie interpretuje wychylenia użytkownika, tworząc przekonującą iluzję głębi i trójwymiarowości na standardowym monitorze 2D. Rozwiązanie to znacząco zwiększa immersję podczas eksploracji wirtualnej przestrzeni bez konieczności używania gogli VR.

## 📁 Struktura Repozytorium
* `/Opentrack_osc_bridge` — Skrypt mostu komunikacyjnego.
* `/UE5_Project` — Projekt Unreal Engine 5 z logiką Blueprint.
* `/Raport` — Pełny raport końcowy oraz dokumentacja konfiguracji OpenTrack.
