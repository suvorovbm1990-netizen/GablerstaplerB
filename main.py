import streamlit as st
import os

st.set_page_config(
    page_title="Gabelstapler Quiz-Trainer",
    page_icon="🚜",
    layout="centered"
)

# --- QUIZ DATA ---
QUESTIONS = [
    {
        "id": 1,
        "question": "1. Wie befährt man mit einem beladenen Gabelstapler bergab ein Gefälle?",
        "options": [
            "a) Vorwärts, mit nach vorne geneigtem Hubgerüst",
            "b) Rückwärts, mit nach hinten geneigtem Hubgerüst",
            "c) Vorwärts, mit nach hinten geneigtem Hubgerüst",
            "d) Rückwärts, mit nach vorne geneigtem Hubgerüst"
        ],
        "correct": 1,
        "image": None
    },
    {
        "id": 2,
        "question": "2. Die aufzunehmende Last ist länger als die Gabeln des Gabelstaplers. Was können Sie tun?",
        "options": [
            "a) Gabelschuhe bzw. Zinkenverlängerungen montieren",
            "b) Verlängerungen an die Zinken schweißen lassen",
            "c) Hubmast beim Einfahren nach hinten neigen",
            "d) Man braucht nichts zu verändern, das passt auch so"
        ],
        "correct": 0,
        "image": "imagesq2_gabelzinken.png"
    },
    {
        "id": 3,
        "question": "3. Ihr Gabelstapler droht zu kippen. Wie verhalten Sie sich richtig?",
        "options": [
            "a) Sie springen schnellstmöglich vom Gabelstapler ab",
            "b) Sie springen in Kipprichtung vom Gabelstapler ab",
            "c) Sie verlagern ihr Gewicht",
            "d) Sie bleiben sitzen, halten das Lenkrad fest, stemmen die Füße gegen die Bodenplatte und lassen den Beckengurt angelegt"
        ],
        "correct": 3,
        "image": None
    },
    {
        "id": 4,
        "question": "4. Mit welcher Faustformel lässt sich der Schwerpunkt der Ladung im Normalfall bestimmen?",
        "options": [
            "a) Länge der Last geteilt durch 2",
            "b) Gewicht der Last geteilt durch 4",
            "c) Gewicht mal Länge der Last geteilt durch 2",
            "d) Gewicht der Last geteilt durch 2"
        ],
        "correct": 0,
        "image": None
    },
    {
        "id": 5,
        "question": "5. Was müssen Sie bei Kurvenfahrten beachten?",
        "options": [
            "a) Sie dürfen keine Last aufgenommen haben",
            "b) Das Hubgerüst muss nach vorn geneigt sein",
            "c) Mit angemessener Geschwindigkeit fahren",
            "d) Immer mit akustischem Signal warnen"
        ],
        "correct": 2,
        "image": None
    },
    {
        "id": 6,
        "question": "6. Was muss ein Gabelstapler besitzen, wenn er am öffentlichen Straßenverkehr teilnimmt?",
        "options": [
            "a) Außenspiegel",
            "b) Schild mit dem Namen des Fahrers",
            "c) Empfänger für Verkehrsfunk",
            "d) Scheinwerfer"
        ],
        "correct": [0, 3],
        "image": None
    },
    {
        "id": 7,
        "question": "7. Welche der folgenden Aussagen ist/sind richtig?",
        "options": [
            "a) Zu lange Gabelzinken sind besser als zu kurze",
            "b) Bei zu langen Gabelzinken besteht die Gefahr, dass Lagergut und Regale beschädigt werden",
            "c) Die Gabelzinken sollten für maximale Sicherheit die Last so breit wie möglich unterfahren",
            "d) Bei Verwendung von Europaletten spielt die Länge der Gabelzinken keine Rolle"
        ],
        "correct": [1, 2],
        "image": None
    },
    {
        "id": 8,
        "question": "8. Sie entdecken einen eingerissenen Gabelzinken. Was ist zu tun?",
        "options": [
            "a) Das ist nicht weiter tragisch und kann bei der nächsten Inspektion behoben werden",
            "b) Hersteller informieren",
            "c) Gabelzinken sofort auswechseln lassen, anderenfalls Gerät stilllegen und absichern",
            "d) Vorgesetzten informieren, wenn Auswechslung nicht möglich ist"
        ],
        "correct": 2,
        "image": None
    },
    {
        "id": 9,
        "question": "9. Welche der Bildfolgen beim Stapeln von Lasten ist die richtige?",
        "options": [
            "a) Bildfolge a",
            "b) Bildfolge b",
            "c) Bildfolge c"
        ],
        "correct": 0,
        "image": "imagesq9_stapeln_reihenfolge.png"
    },
    {
        "id": 10,
        "question": "10. Wo findet man die berufsgenossenschaftlichen Unfallverhütungsvorschriften beim Umgang mit Flurförderzeugen zu beachten sind?",
        "options": [
            "a) In der Straßenverkehrsordnung",
            "b) Im Arbeitsschutzgesetz",
            "c) In der DGUV Vorschrift 68",
            "d) In der Arbeitsstättenverordnung"
        ],
        "correct": 2,
        "image": None
    },
    {
        "id": 11,
        "question": "11. Ab welcher Hubhöhe ist ein Fahrerschutzdach vorgeschrieben?",
        "options": [
            "a) Ab 2,10 m",
            "b) Ab 1,80 m",
            "c) Ab 1,50 m",
            "d) Ab 1,00 m"
        ],
        "correct": 1,
        "image": None
    },
    {
        "id": 12,
        "question": "12. In welchen der hier abgebildeten Situationen ist der Gabelstapler kippgefährdet?",
        "options": [
            "a) Situation a",
            "b) Situation b",
            "c) Situation c",
            "d) Situation d"
        ],
        "correct": [0, 1, 2],
        "image": "imagesq12_kippgefahr.png"
    },
    {
        "id": 13,
        "question": "13. Der Motor Ihres Elektrogabelstaplers lässt sich nicht mehr ausschalten. Wie verhalten Sie sich in diesem Falle richtig?",
        "options": [
            "a) Ich springe ab und bringe mich in Sicherheit",
            "b) Ich fahre den Gabelstapler so lange im Betrieb herum, bis die Batterie leer ist",
            "c) Ich bitte Kollegen, den Stapler irgendwie zu stoppen",
            "d) Ich betätige den Notausschalter"
        ],
        "correct": 3,
        "image": None
    },
    {
        "id": 14,
        "question": "14. Was bedeutet dieses Zeichen?",
        "options": [
            "a) Kennzeichnung des Schwerpunktes bei unsymmetrischem Ladegut",
            "b) EX-geschützter Stapler",
            "c) Anschlagschwerpunkt für die Verkranung",
            "d) Kennzeichnung Ladebuchse"
        ],
        "correct": 0,
        "image": "imagesq14_schwerpunkt_symbol.png"
    },
    {
        "id": 15,
        "question": "15. Wann kippt ein Drehradstapler (Gabelstapler) in Kurven schneller?",
        "options": [
            "a) Mit unverpackter Last",
            "b) Ohne Last",
            "c) Mit abgesenkter Last",
            "d) Ein Gabelstapler kann in Kurven nicht umkippen"
        ],
        "correct": 1,
        "image": None
    },
    {
        "id": 16,
        "question": "16. Was gehört beim Gabelstapler zu den Warneinrichtungen?",
        "options": [
            "a) Hupe",
            "b) Rundumleuchte",
            "c) Sonderlackierung",
            "d) Warnblinker"
        ],
        "correct": [0, 1],
        "image": None
    },
    {
        "id": 17,
        "question": "17. Welche Flurförderzeuge dürfen in explosionsgefährdeten Bereichen fahren?",
        "options": [
            "a) Nur Stapler mit Elektroantrieb",
            "b) Jedes behördlich zugelassene Flurförderzeug",
            "c) Nur Fahrzeuge mit explosionsgeschütztem Motor",
            "d) Fahrzeuge, die mit einem 'EX-Zeichen' versehen sind"
        ],
        "correct": 3,
        "image": None
    },
    {
        "id": 18,
        "question": "18. Wie groß sollte das Lenkspiel eines Gabelstaplers höchstens sein?",
        "options": [
            "a) 5-10 mm",
            "b) 30-40 mm",
            "c) 50 mm",
            "d) Die Lenkung eines Staplers sollte absolut spielfrei sein"
        ],
        "correct": 1,
        "image": None
    },
    {
        "id": 19,
        "question": "19. Was sind mögliche Gefahrenquellen beim Auf- und Absteigen auf den/vom Gabelstapler?",
        "options": [
            "a) Schnee auf der Trittstufe",
            "b) Öl auf der Trittstufe",
            "c) Zündschlüssel vergessen",
            "d) Vom Fahrzeug abspringen"
        ],
        "correct": [0, 1, 3],
        "image": None
    },
    {
        "id": 20,
        "question": "20. Wann dürfen Sie einen Gabelstapler mit angehobener Last verlassen?",
        "options": [
            "a) Wenn Sie die Zündung ausgeschaltet haben",
            "b) Wenn Sie die Zündung ausgeschaltet und die Feststellbremse betätigt haben",
            "c) Wenn Sie einem Vorgesetzten Bescheid gegeben haben",
            "d) Gar nicht, die Last ist beim Verlassen des Fahrzeugs immer zu senken"
        ],
        "correct": 3,
        "image": None
    },
    {
        "id": 21,
        "question": "21. Sie wollen eine Person auf- und abwärts befördern. In welchem Fall dürfen Sie das?",
        "options": [
            "a) Wenn die Person zugestimmt hat und sich auf eigene Gefahr befördern lässt",
            "b) Wenn es Ihr Chef angeordnet hat",
            "c) Wenn Ihr Gabelstapler über eine zulässige Arbeitsbühne verfügt",
            "d) Wenn Sie dazu speziell ausgebildet wurden"
        ],
        "correct": 2,
        "image": None
    },
    {
        "id": 22,
        "question": "22. Welche Aussage/n zu diesem Bild ist/sind richtig?",
        "options": [
            "a) Die Last ist für den Transport zu hoch",
            "b) Die Last ist optimal aufgenommen",
            "c) Es besteht kein Problem",
            "d) Es besteht erhöhte Kippgefahr"
        ],
        "correct": [0, 1, 3],
        "image": "imagesq22_transport_hoehe.png"
    },
    {
        "id": 23,
        "question": "23. Welches Anbaugerät ist auf dem folgenden Foto zu sehen?",
        "options": [
            "a) Mehrpalettengabel",
            "b) Abschieber",
            "c) Drehgerät",
            "d) Zinkenverstellgerät"
        ],
        "correct": 1,
        "image": "imagesq23_anbaugeraet.png"
    },
    {
        "id": 24,
        "question": "24. Welche Aussage/n für die angehobene Last ist/sind richtig?",
        "options": [
            "a) Je höher die Last angehoben wird, umso leichter kann der Gabelstapler kippen",
            "b) Beim Stapeln in großer Höhe muss man nichts weiter beachten",
            "c) Bei angehobener Last verschiebt sich der Gesamtschwerpunkt",
            "d) Der Hubmast muss vor Fahrtbeginn nach vorne geneigt sein"
        ],
        "correct": [0, 2],
        "image": None
    },
    {
        "id": 25,
        "question": "25. Eine Europalette mit den Maßen 800 x 1200 mm hat ein Gewicht von 1.100 kg. Sie soll in ein Hochregal auf einen Fachboden in 5 Meter Höhe gestapelt werden. Ist das mit diesem Gabelstapler möglich?",
        "options": [
            "a) Ja",
            "b) Nein"
        ],
        "correct": 0,
        "image": "imagesq25_tragfaehigkeitsdiagramm.png"
    },
    {
        "id": 26,
        "question": "26. Sie entdecken an Ihrem Gabelstapler einen undichten Hydraulikschlauch. Was ist zu tun?",
        "options": [
            "a) Sie müssen vermehrt aufpassen und kontrollieren",
            "b) Sie stellen das Gerät ab und ziehen den Zündschlüssel ab, damit kein anderer mehr damit fahren kann",
            "c) Sie informieren Ihren Vorgesetzten",
            "d) Sie reparieren den Schlauch vorläufig mit Klebeband, um Zeit zu sparen"
        ],
        "correct": [1, 2],
        "image": None
    },
    {
        "id": 27,
        "question": "27. Wie muss eine Arbeitsbühne beschaffen sein?",
        "options": [
            "a) Rutschfester, ebener Boden ohne größere Öffnungen",
            "b) Sie muss eine Umwehrung von mind. 1 Meter Höhe haben, bestehend aus Handlauf und mindestens einer Knie- und Fußleiste",
            "c) Sie muss über einen Rückenschutz verfügen",
            "d) Sie muss mindestens 2 Personen aufnehmen können"
        ],
        "correct": [0, 1, 2],
        "image": None
    },
    {
        "id": 28,
        "question": "28. Das Umkippen des Staplers führt häufig zu Todesfällen. Was kann zu einem solchen Unfall führen?",
        "options": [
            "a) Zu hohe Geschwindigkeit in Kurven",
            "b) Der Fahrer ist übergewichtig",
            "c) Der Hubmast ist beim Fahren stark nach hinten geneigt",
            "d) Der Lastschwerpunkt wurde nicht berücksichtigt"
        ],
        "correct": [0, 3],
        "image": None
    },
    {
        "id": 29,
        "question": "29. In welcher der hier abgebildeten Situationen ist der Gabelstapler richtig geparkt?",
        "options": [
            "a) Situation a",
            "b) Situation b",
            "c) Situation c",
            "d) Situation d"
        ],
        "correct": 3,
        "image": "imagesq29_geparkt.png"
    },
    {
        "id": 30,
        "question": "30. Welche der folgenden Aussagen ist/sind richtig?",
        "options": [
            "a) Die Fliehkraft bei Kurvenfahrten ist umso kleiner, je kleiner der Kurvenradius ist",
            "b) Die Fliehkraft bei Kurvenfahrten ist umso größer, je höher die Kurvengeschwindigkeit ist"
        ],
        "correct": 1,
        "image": None
    },
    {
        "id": 31,
        "question": "31. Um wie viel Prozent darf die Tragfähigkeit bei Lastaufnahme überschritten werden?",
        "options": [
            "a) 5 %",
            "b) 10 %",
            "c) 15 %",
            "d) 0 %"
        ],
        "correct": 3,
        "image": None
    },
    {
        "id": 32,
        "question": "32. Worauf muss ich beim Transport hängender Lasten besonders achten?",
        "options": [
            "a) Anschlagmittel gegen Verschieben sichern",
            "b) Personen dürfen sich nicht vor der Last aufhalten",
            "c) Personen dürfen nicht durch das Pendeln der Last gefährdet werden",
            "d) Hängende Lasten stets rückwärts transportieren"
        ],
        "correct": [0, 1, 2],
        "image": None
    },
    {
        "id": 33,
        "question": "33. Bei welcher Lastverteilung ist davon auszugehen, dass der Schwerpunkt nicht in der Mitte der Palette liegt?",
        "options": [
            "a) Abbildung a",
            "b) Abbildung b",
            "c) Abbildung c",
            "d) Abbildung d"
        ],
        "correct": [1, 2],
        "image": "imagesq33_schwerpunkt_palette.png"
    },
    {
        "id": 34,
        "question": "34. Was ist wichtig, um das Kippen des Gabelstaplers nach vorn zu verhindern?",
        "options": [
            "a) Vorsichtiges Bremsen",
            "b) Die regelmäßige Pflege der Achsen",
            "c) Maximale Hubhöhe beachten",
            "d) Geringe Entfernung der Last vom Gabelrücken"
        ],
        "correct": [0, 2, 3],
        "image": None
    },
    {
        "id": 35,
        "question": "35. Bei welcher dieser Abbildungen ist die Gefahr, dass der Gabelstapler nach vorn kippt, am größten?",
        "options": [
            "a) Abbildung a",
            "b) Abbildung b",
            "c) Abbildung c"
        ],
        "correct": 2,
        "image": "imagesq35_kippgefahr_vorne.png"
    },
    {
        "id": 36,
        "question": "36. Was gehört nicht zur persönlichen Schutzausrüstung (PSA)?",
        "options": [
            "a) Helm",
            "b) Feuerlöscher",
            "c) Handschutz",
            "d) Gehörschutz"
        ],
        "correct": 1,
        "image": None
    },
    {
        "id": 37,
        "question": "37. Was bedeutet das Hebelgesetz für den Umgang mit Last?",
        "options": [
            "a) Die aufnehmbare Last wird umso geringer, je weiter sich der Lastschwerpunkt vom Drehpunkt (der Vorderachse) entfernt",
            "b) Die maximale Hubhöhe wird umso geringer, je weiter hinten sich der Schwerpunkt des Staplers befindet"
        ],
        "correct": 0,
        "image": "imagesq37_hebelgesetz.png"
    },
    {
        "id": 38,
        "question": "38. Wie muss eine Ladebrücke beschaffen sein?",
        "options": [
            "a) Sie muss genauso breit sein wie der Gabelstapler",
            "b) Sie muss deutlich breiter sein als der Gabelstapler",
            "c) Sie muss auf jeden Fall waagerecht sein",
            "d) Sie muss eine ausreichende Tragfähigkeit besitzen"
        ],
        "correct": [1, 3],
        "image": None
    },
    {
        "id": 39,
        "question": "39. Wann müssen Sie hinsichtlich der Sicherheit und des Gesundheitsschutzes am Arbeitsplatz unterwiesen werden?",
        "options": [
            "a) Vor der ersten Arbeitsaufnahme",
            "b) Mindestens einmal jährlich",
            "c) Alle drei Jahre",
            "d) Es gibt dazu keine festen Zeitvorgaben"
        ],
        "correct": [0, 1],
        "image": None
    },
    {
        "id": 40,
        "question": "40. Welche Breite muss eine Laderampe mindestens aufweisen, damit sie mit einem Gabelstapler befahren werden kann?",
        "options": [
            "a) Breite des Gabelstaplers plus 0,5 Meter links und rechts",
            "b) Breite des Gabelstaplers plus Geländerbreite",
            "c) Mindestens 0,8 Meter",
            "d) Es gibt keine Mindestbreite - das Augenmaß des Fahrers ist entscheidend"
        ],
        "correct": 0,
        "image": None
    },
    {
        "id": 41,
        "question": "41. Auf was müssen Sie beim Einstapeln von Lasten in ein Palettenregal achten?",
        "options": [
            "a) Die zulässigen Fach- und Feldlasten",
            "b) Montage eines zusätzlichen Gegengewichts am Stapler",
            "c) Die zulässige Hubhöhe des Gabelstaplers",
            "d) Es gibt nichts Besonderes zu beachten"
        ],
        "correct": [0, 2],
        "image": None
    },
    {
        "id": 42,
        "question": "42. Schauen Sie sich das folgende Traglastdiagramm an: Wie schwer darf eine Last höchstens sein, die mit diesem Gabelstapler transportiert wird?",
        "options": [
            "a) 6.150 kg",
            "b) 1.200 kg",
            "c) 700 kg",
            "d) 4.250 kg"
        ],
        "correct": 1,
        "image": "imagesq42_traglastdiagramm.png"
    },
    {
        "id": 43,
        "question": "43. Von wo aus wird der Lastschwerpunkt beim Gabelstapler gemessen?",
        "options": [
            "a) Von der Vorderachse des Staplers aus",
            "b) Vom Gesamtschwerpunkt des Staplers aus",
            "c) Vom Gabelrücken aus",
            "d) Vom Gegengewicht aus"
        ],
        "correct": 2,
        "image": None
    },
    {
        "id": 44,
        "question": "44. Sie transportieren eine große Last, die Ihre Sicht nach vorn behindert. Was können Sie tun?",
        "options": [
            "a) Sie fahren rückwärts",
            "b) Sie schauen seitlich an der Last vorbei",
            "c) Sie dürfen eine so große Last nie transportieren",
            "d) Sie lassen sich von einem Einweiser unterstützen"
        ],
        "correct": [0, 3],
        "image": None
    },
    {
        "id": 45,
        "question": "45. Womit müssen Gabelstapler ausgestattet sein, die in Kühlhäusern zum Einsatz kommen?",
        "options": [
            "a) Mit Vollkabine",
            "b) Mit Sitzheizung",
            "c) Mit Klimaanlage",
            "d) Mit Dieselantrieb"
        ],
        "correct": 0,
        "image": None
    },
    {
        "id": 46,
        "question": "46. Ab welcher bauartbedingten Höchstgeschwindigkeit sind Gabelstapler für den Betrieb im öffentlichen Verkehrsraum zulassungspflichtig?",
        "options": [
            "a) Ab 10 km/h",
            "b) Ab 15 km/h",
            "c) Ab 20 km/h",
            "d) Ab 30 km/h"
        ],
        "correct": 2,
        "image": None
    },
    {
        "id": 47,
        "question": "47. Was muss vor Benutzung des Gabelstaplers täglich erfolgen?",
        "options": [
            "a) Rundgang um den Gabelstapler mit Sichtprüfung",
            "b) Antrieb ca. 5 Minuten laufen lassen",
            "c) Gabelstapler waschen",
            "d) Allgemeine Funktionsprüfung"
        ],
        "correct": [0, 3],
        "image": None
    },
    {
        "id": 48,
        "question": "48. Was beschreibt dieses Traglastdiagramm?",
        "options": [
            "a) Höchstgeschwindigkeit des Gabelstaplers",
            "b) Maximale Tragfähigkeit",
            "c) Tragfähigkeit bei unterschiedlichen Hubhöhen",
            "d) Gesamtgewicht des Gabelstaplers"
        ],
        "correct": [1, 2],
        "image": "imagesq48_traglastdiagramm.png"
    },
    {
        "id": 49,
        "question": "49. Wie nennt man ein Hubgerüst, das aus einem Innenmast, Mittelmast und Außenmast besteht?",
        "options": [
            "a) Einfach-Hubgerüst",
            "b) Dreifach-Hubgerüst",
            "c) Zweifach-Hubgerüst",
            "d) Außenmast-Hubgerüst"
        ],
        "correct": 1,
        "image": None
    },
    {
        "id": 50,
        "question": "50. Ab wann dürfen Sie das Flurförderzeug im Unternehmen fahren?",
        "options": [
            "a) Wenn Sie eine theoretische und praktische Ausbildung absolviert haben und Ihre Fähigkeiten in Theorie und Praxis nachgewiesen haben",
            "b) Wenn Sie mit einem Kollegen eine Einweisung gemacht haben",
            "c) Wenn Sie vom Unternehmer schriftlich beauftragt wurden",
            "d) Wenn Sie die persönliche Eignung nachgewiesen haben"
        ],
        "correct": [0, 2, 3],
        "image": None
    }
]

# --- SESSION STATE INITIALIZATION ---
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False

st.title("🚜 Gabelstapler Prüfungstrainer (50 Fragen)")
st.write("Интерактивный тренажер для подготовки к экзамену на погрузчик.")

# Progress bar
progress = (st.session_state.current_index + 1) / len(QUESTIONS)
st.progress(progress)
st.caption(f"Вопрос {st.session_state.current_index + 1} из {len(QUESTIONS)}")

# Current Question Data
q = QUESTIONS[st.session_state.current_index]

st.subheader(q["question"])

# Display image if exists
if q["image"]:
    if os.path.exists(q["image"]):
        st.image(q["image"], use_container_width=True)
    else:
        st.info(f"🖼 Изображение: `{q['image']}` не найдено.")

is_multiselect = isinstance(q["correct"], list)

if is_multiselect:
    st.warning("⚠️ Внимание: несколько правильных ответов!")
    user_choices = []
    for idx, opt in enumerate(q["options"]):
        checked = st.checkbox(opt, key=f"q_{q['id']}_opt_{idx}")
        if checked:
            user_choices.append(idx)
else:
    user_choice = st.radio(
        "Выберите ответ:",
        options=range(len(q["options"])),
        format_func=lambda idx: q["options"][idx],
        key=f"q_{q['id']}_radio"
    )
    user_choices = user_choice

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Проверить ответ", type="primary"):
        st.session_state.submitted = True
        if is_multiselect:
            correct_set = set(q["correct"])
            user_set = set(user_choices)
            is_correct = (correct_set == user_set)
        else:
            is_correct = (user_choices == q["correct"])
            
        st.session_state.answers[q["id"]] = is_correct

if st.session_state.submitted:
    if is_multiselect:
        correct_set = set(q["correct"])
        user_set = set(user_choices)
        if correct_set == user_set:
            st.success("✅ Отлично! Все правильные варианты выбраны.")
        else:
            st.error("❌ Неверно. Правильные варианты:")
            for idx in q["correct"]:
                st.write(f"- {q['options'][idx]}")
    else:
        if user_choices == q["correct"]:
            st.success("✅ Правильно!")
        else:
            st.error(f"❌ Неверно. Правильный ответ: {q['options'][q['correct']]}")

st.divider()

# Navigation buttons
nav_col1, nav_col2, nav_col3 = st.columns([1, 1, 1])

with nav_col1:
    if st.button("⬅️ Назад", disabled=st.session_state.current_index == 0):
        st.session_state.current_index -= 1
        st.session_state.submitted = False
        st.rerun()

with nav_col3:
    if st.session_state.current_index < len(QUESTIONS) - 1:
        if st.button("Вперёд ➡️"):
            st.session_state.current_index += 1
            st.session_state.submitted = False
            st.rerun()
    else:
        if st.button("🎉 Завершить тест"):
            st.balloons()
            score_count = sum(1 for v in st.session_state.answers.values() if v)
            st.success(f"Тест завершён! Ваш результат: {score_count} / {len(QUESTIONS)}")
