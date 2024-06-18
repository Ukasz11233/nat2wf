# NAT2WF

Nat2wf to prototyp prostej strony internetowej, która generuje grafy przepływu pracy na podstawie zadanego tekstu, w języku naturalnym, opisującego proces.

Obecnie program korzysta z modelu LLM, który przetwarza zapytania w języku naturalnym na grafy w formacie mermaid. W efekcie otrzymane grafy nie są deternimistyczne, a jedynie przybliżone do zadanego tekstu. Czasami mogą zawierać błędy.


## Uruchamianie

```bash
python -m flask --app flaskr run --debug
```