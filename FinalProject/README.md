Detalii aplicatie testata: 
Tip: Server Flask
Scop: Simulează un API simplu pentru a furniza informații despre postări, comentarii, sarcini și utilizatori.
Sursa datelor: Datele sunt simulate și returnate de la https://jsonplaceholder.typicode.com.

Structura aplicației:

Clasa EndpointTester:
Descriere: Gestionarea testelor automate pentru endpoint-uri.
Metoda test(param_name, expected_status):
Parametri:
param_name: Numele endpoint-ului de testat.
expected_status: Statusul HTTP așteptat pentru răspuns.
Acțiuni:
Realizează o cerere GET către endpoint-ul specificat.
Verifică dacă statusul răspunsului corespunde celui așteptat.
Verifică dacă datele au fost primite corect.
Returnează datele pentru a permite teste suplimentare sau analize ulterioare.

Clasa APITestingApp:
Descriere: Implementarea principală a aplicației Flask.
Constructor:
Inițializează un obiect Flask.
Setează un URL de bază pentru a accesa datele simulare.
Definește o listă de endpoint-uri disponibile.
Metoda index():
Returnează un mesaj de prezentare pentru a indica funcționarea corectă a serverului.
Metoda test_endpoint(tester):
Parametru:
tester: Un obiect EndpointTester utilizat pentru testarea unui endpoint specific.
Acțiuni:
Efectuează un test pe endpoint-ul /posts.
Returnează datele pentru a fi utilizate într-un răspuns JSON.

Metoda run():
Rulează serverul Flask pe http://127.0.0.1:5000/.

Exemple de endpoint-uri:
/posts: Returnează informații despre postări.
/comments: Returnează informații despre comentarii.
/todos: Returnează informații despre sarcini.
/users: Returnează informații despre utilizatori.
