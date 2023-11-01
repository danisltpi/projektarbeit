# Einführung

Code Llama ist ein neues State of the Art Sprachmodell, spezialisiert zur
Generierung von Code und natürlicher Sprache über Code. Dazu akzeptiert sie
sowohl Prompts, die Code enthalten als auch welche, die natürliche Sprache enthalten.

Entwickelt wurde sie von Meta, der Muttergesellschaft von Facebook und ist frei
zu Forschungs- und Kommerziellen Zwecken nutzbar.
Veröffentlicht wurde Code Llama am 24. August und ist, ein
auf Programmiercode spezialisierte Version von Llama 2, welches durch
ein erweitertes, längeres Training des bestehenden Code-Datensatzes entstand. [@IntroducingCodeLlama]

Als Ergebnis, kann Code Llama Code generieren, und unterstützt zudem

In dieser Projektarbeit wird Code Llama auf die beworbenen Fähigkeiten getestet
und auf die Nutzbarkeit in der echten Welt geprüft.

# Über Code Llama

Code Llama gibt es in verschiedenen Varianten:

- Default
- Instruct
- Python
- Unnatural

Diese unterscheiden sich in erster Linie
durch den Datensatz, die zum Trainieren der
Modelle verwendet wurde.

Die Default-Variante ist die Standardvariante
mit dem Datensatz,
die vorher beschrieben wurde, basiert.

Bei der Python-Variante wurde mehr Python-Code zum feintunen verwendet, somit kann dieses Modell in der Theorie besser mit Python umgehen.

Bei der Instruct Variante handelt es sich um
ein Modell, welches mit menschlichen Instruktions-Datensätzen
fein getunt worden ist. Man nennt dies dann
aligned, dies bedeutet die Ausgabe des Modells ist konsistent zu dem, wie es ein Mensch erwarten würde, dies ermöglicht es dem Modell, z.B. auf
Fragen zu antworten oder andere menschenähnliche
Interaktionen zu erzeugen.
Somit ist das die nutzerfreundlichste Version
von Code Llama.

Es gibt auch noch eine Variante, die
als Unnatural Code Llama bezeichnet
wird. Diese Version wird der
Öffentlichkeit leider (noch) nicht zur
Verfügung gestellt.
Sie schneidet im Vergleich zu den anderen
Sprachmodellen, die im Research Paper
verglichen wurden in allen bis auf einer Rubrik
am besten ab und dürfte somit
Metas mächtigstes Sprachmodell für Code sein.
Erschaffen wurde es, indem Code Llama - Python
anhand von 15.000 unnatürlichen Instruktionen feingetunt worden ist, also ein Datensatz,
der vollkommen synthetisch und automatisiert
mithilfe von anderen Sprachmodellen erzeugt
wurde.

jedoch gibt es, bis auf eine
kurze Erwähnung in der
Vergleichstabelle, dazu keine
näheren Informationen über dieses Modell.

Diese verschiedenen Variationen gibt es dann nochmal in der 7b, 13b und
der 34b Version, welche die Größe des Sprachmodells
beschreibt. A

Es gibt viele Sprachmodelle, oder genauer bezeichnet „Large Language Models“ (LLM), die
in Konkurrenz mit Code Llama stehen wie z.B. GPT-4, die im selben bzw. anderen Bereichen besser performen können.

Dazu gibt es verschiedene Kennzahlen, um diese Perfomance zu evaluieren.

In der Tabelle, die im Research Paper
auftaucht, kann man erkennen, dass

![Code LLama im Vergleich zu anderen LLMs [@roziereCodeLlamaOpen]](assets/img/comparison.png)

# Einrichten von Code Llama

# Durchführung

Um die Fähigkeiten der Code- und Sprachgenerierung von Code Llama auszuprobieren und zu testen,
könnten folgende Nutzzwecke Interessant sein:

- Schreiben von Code anhand einer Beschreibung in natürlicher Sprache
- Code Reviews
- Dokumentation
- Verbessern von bestehendem Code (Refactoring)
- Zusammenfassung von Code
- Potenzielle Bugs erkennen und Hilfestellung bei Debugging leisten

# Vergleich mit anderen Chatbots

# Ergebnisse

# Fazit

\newpage \setlength\parindent{0pt}

# Referenzen
