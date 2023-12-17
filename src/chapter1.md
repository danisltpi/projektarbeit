# Einführung

Code Llama ist ein neues State of the Art Sprachmodell, spezialisiert zur
Generierung von Code und natürlicher Sprache über Code. Dazu akzeptiert sie
sowohl Prompts, die Code enthalten als auch welche, die natürliche Sprache enthalten.

Entwickelt wurde sie von Meta, der Muttergesellschaft von Facebook und ist frei
zu Forschungs- und Kommerziellen Zwecken nutzbar.
Veröffentlicht wurde Code Llama am 24. August und ist, ein
auf Programmiercode spezialisierte Version von Llama 2, welches durch
ein erweitertes, längeres Training des bestehenden Code-Datensatzes entstand. [@IntroducingCodeLlama]

In dieser Projektarbeit wird Code Llama auf die beworbenen Fähigkeiten getestet
und auf die Nutzbarkeit in der echten Welt geprüft.

# Über Code Llama

Code Llama gibt es in verschiedenen Varianten:

- Default
- Instruct
- Python
- Unnatural

Diese unterscheiden sich in erster Linie
durch den Datensatz, die zum Trainieren verwendet wurde.

Die Default-Variante ist die Standardvariante, die auf dem Datensatz, die vorher beschrieben wurde, basiert.

Bei der Python-Variante wurde mehr Python-Code zum feintunen verwendet, somit kann dieses Modell in der Theorie besser mit Python-Code umgehen.

Bei der Instruct Variante handelt es sich um
ein Modell, welches mit menschlichen Instruktionsdatensätzen
fein getunt worden ist. Man nennt dies dann
aligned, dies bedeutet die Ausgabe des Modells ist konsistent zu dem, wie es ein Mensch erwarten würde und ermöglicht es dem Modell, z.B. auf
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
mithilfe von anderen Sprachmodellen erzeugt wurde.

Diese verschiedenen Variationen gibt es dann nochmal in der 7b, 13b und
der 34b Version. Diese unterscheiden sich vor allem in der Größe des Sprachmodells oder um genau zu sein
wurden diese jeweils mit 7 Milliarden, 13 Milliarden
und 34 Milliarden verschiedenen Parametern trainiert.

Damit dürfte die 34b Version die besten
Ergebnisse liefern während die 7b
und 13b Versionen schneller sind und
sich daher eher für Echtzeit Code-Completion
eignen.

Es gibt viele Sprachmodelle, oder genauer bezeichnet „Large Language Models“ (LLM), die
in „Konkurrenz“ mit Code Llama stehen wie z.B. GPT-4, die im selben oder auch anderen Bereichen besser performen können.
Um das auszuwerten, gibt es verschiedene Kennzahlen, um diese Perfomance zu messen.

In der Tabelle, die im Research Paper
auftaucht, werden verschiedene
Sprachmodelle miteinander anhand von verschiedenen Metriken verglichen.
Je höher die Zahl in der Kategorie,
desto besser hat dieses Sprachmodell
in der Evaluation performt.

Code Llama - Python 34b hat beispielsweise
bei der Pass@1 HumanEval Kategorie ein
Ergebnis von 53,7% erreicht, während
GPT-4, das beste Modell in dieser Kategorie, 67% erreicht hat. Das ist in anbetracht der Größe
der jeweiligen Modelle äußerst bemerkenswert,
da Code Llama nur mit einem Bruchteil der Größe
von GPT-4 (mindestens 1 Billion Parameter) bereits ähnlich gute Ergebnisse liefert.

![Code LLama im Vergleich zu anderen LLMs [@roziereCodeLlamaOpen]](assets/img/comparison.png)
