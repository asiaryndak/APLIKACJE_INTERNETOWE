# APLIKACJE_INTERNETOWE
Aplikacja do wizualizacji wyników eksploracji (np. grupowanie, klasyfikacja) danych

Dokumentacja wstępna 
“Aplikacja do wizualizacji wyników eksploracji (np. grupowanie, klasyfikacja) danych”

1. Założenia projektu dotyczące planowanych funkcjonalności

- porównywanie danych dla różnych zakresów
- wyświetlanie wykresów na podstawie wybranych typów danych(użytkownik ma możliwość wybrania najbardziej interesującego go zakresu i typu danych, z rodzajów danych obsługiwanych przez aplikację)
- wybranie przez użytkownika sposobu prezentacji wybranych danych ( kilka rodzajów wykresów do wyboru - np. pomiędzy słupkowym, a kołowym, czy też punktowym)



2. Wykorzystywane technologie
	Tworzona przez nas aplikacja internetowa powstanie przy użyciu frameworka Django. Będziemy też korzystać z CSS3, HTML5, Bootstrap 3 oraz jQuery. Zebrane informacje będziemy przechowywać w bazie danych typu SQLite.
	Na tym etapie planowania aplikacji, trudno nam dokładnie sprecyzować zakres wykorzystania poszczególnych technologii, ponieważ dopiero zaczynamy się zagłębiać w temat Pythona, jako języka do tworzenia aplikacji webowych, jak i używania Django. 
 Prawdopodobnie w trakcie realizacji projektu wykorzystamy także biblioteki języka Python, służące do wizualizacji danych, jak na przykład matplotlib, ggplot czy też Plotly lub SciPy. (tutaj w zależności od wizji aplikacji, biblioteki mogą ulec zmianom). 

3. Metody testowania
 Do testowania naszej aplikacji planujemy użycie standardowej biblioteki unittest, do tworzenia zwykłych , prostych testów jednostkowych, pozwalających na szybkie wykrycie błędów w tworzonym oprogramowaniu. https://docs.python.org/3/library/unittest.html#module-unittest

 Do testowania naszej aplikacji planujemy także użycie frameworku Selenium, służącego do tworzenia testów automatycznych dla aplikacji webowych. 


 DANE DO WIZUALIZACJI - POMYSŁY : 


- Dane giełdowe na przestrzeni X lat wstecz, dotyczące kursów poszczególnych, wybranych walut
- Dane dotyczące cen paliw, na przestrzeni lat - porównania różnorakich stacji paliwowych, wpływu ceny baryłki ropy na cenę benzyny.


 DANE DLA KTÓRYCH ZNALEŹLIŚMY POKRYCIE W INTERNECIE : 
- http://archive.ics.uci.edu/ml/datasets.html - źródło gotowych danych do przetwarzania
- Dane pochodzące ze strony GUS-u( np. zmiana wykształcenia na przestrzeni lat, średnie płace, w podziale na miejsce zamieszkania, płeć, wiek, itp.)	
