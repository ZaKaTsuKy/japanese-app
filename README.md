# Application d'aide à l'apprentissage du japonais

Merci de tout lire avant d'utiliser l'application.\n
Cette application a été créée dans un cadre personnel dans deux buts précis. Premièrement m'aider à apprendre le japonais en m'entraînant quotidiennent avec les kanji et d'autres que j'immplémenterai à l'avenir afin d'avoir l'application la plus complète et autonome possible. La seconde chose est d'implémenter des modules d'automatisation et d'intelligence artificielle afin de développer mes compétences dans le domaine. L'utilisation de mon code est disponible à qui veut, vous pouvez le modifier comme vous voulez mais aucune démarche commerciale dessus n'est tolérée.

## Installation des librairies

Il y est nécessaire de posséder certaines librairies (et bien évidemment python 3.10+). Pour ce faire, une fois le git téléchargé, rendez-vous via le terminal dans le dossier contenant le `requirements.txt` et tapez `pip install -r requirements.txt`. Cela installera les librairies manquantes nécessaires.


## Comment utiliser l'application

Allez dans le dossier contenant les différents fichiers via le terminal, puis lancez l'application en faisant `py mimi4.py`. Des numéros sont affiliés à chaque option possible. Entrez le numéro puis appuyez sur la touche "enter" du clavier. Vous pouvez ainsi naviguer partout.

<img width="960" alt="image" src="https://github.com/ZaKaTsuKy/japanese-app/assets/74179251/5095a6ac-7a67-43f2-bfd1-090e07d57c7b">


## Règles d'utilisation

Différents modes sont proposés, ci-après l'explication de chaque mode.


# Lecture 

Chaque entraînement vous demandera combien d'éléments (Hiragana, Katakana, Kanji) vous voudrez dans votre série. Rentrez un entier et appuyez sur "enter".
Pour l'entraînement à la lecture des kanji, le programme vous demandera de rentrer un niveau de JLPT, si vous ne savez pas ce que c'est, google vous renseignera. Par défaut, laissez vide et tout niveau vous sera proposé. Autrement, rentrez les niveaux que vous avez envie (ex : `4` ou `4 5`, seuls les niveaux proposés seront respectivement le JLPT N4 et le JLPT N4 N5).

<img width="960" alt="image" src="https://github.com/ZaKaTsuKy/japanese-app/assets/74179251/06b7bf9a-61ec-44cf-8e17-493b967d41be">


Pour répondre aux questions écrivez la version romaji et appuyez sur "enter", autrement cela vous donnera faux.

<img width="960" alt="image" src="https://github.com/ZaKaTsuKy/japanese-app/assets/74179251/99e40513-b209-4bb2-9217-ed3327dc45b1">

Si vous bloquez, laissez le champs vide, appuyez sur "enter", cela vous donnera la réponse. Cependant vous aurez faux. Pour voir les conséquences sur le fait d'avoir faux, rendez-vous [ici](#calculs).


# Compréhension

Module non implémenté à l'heure actuelle. 


# Audio

Ce module va vous permettre d'écouter les kanjis présent dans le fichier `kanji.csv` à l'oral et d'écrire ce qu'ils veulent dire en romaji. Si vous n'avez pas compris, vous pouvez laisser le champs vide et directement appuyer sur "enter" pour répéter l'audio, cela n'affectera pas votre taux de réussite. Si vous ne savez pas, appuyez sur "espace" puis sur "enter", cela vous affichera la réponse, mais vous aurez faux.. Il sera également possible à l'avenir de le faire avec des phrases, ce module n'est pas encore implémenté. 


# Expression

Module non implémenté à l'heure actuelle. 


# Nombre

Ce module va vous permettre de vous entraîner avec les nombres. Il propose 3 fonctionnalités :
- Lecture : Le module va vous afficher un nombre entre 1 et 99 999 écrit avec les nombres japonais, à vous de le traduire en alphanumérique.
- Ecriture : Le module va vous écrire un nombre en alphanumérique entre 1 et 99 999, à vous de l'écrire en caractère japonais.
- Audio : Le module va dire à l'oral un nombre compris entre 1 et 99 999, à vous de l'écrire en alphanumérique.
**<ins>Exemple</ins>**
  
<img width="960" alt="image" src="https://github.com/ZaKaTsuKy/japanese-app/assets/74179251/151d2a93-a636-4b98-a1b8-fcefe57a2464">


# Paramètres

Les paramètres vous permettent plusieurs choses :
- Ajouter des kanji dans le fichier `kanji.csv` afin de les apprendre à leur tour. Pour ce faire, vous devrez entrer le kanji, le romaji et sa traduction sous la forme : `kanji romaji traduction`, avec simplement des espaces entre chaque élément.
<img width="960" alt="image" src="https://github.com/ZaKaTsuKy/japanese-app/assets/74179251/78ba361d-d8b4-48f4-9e27-ce1bd49a12b9">
Vous pouvez de cette manière ajouter autant de kanji que vous voulez. Une fois l'opération terminée, validez la en appuyant sur "enter".

- Remettre les compteurs des scores et des taux à 0. 
- Afficher les statistiques d'apparitions des kana et des kanji.


## Conseils

Si vous êtes débutants, commencez par apprendre les hiragana. Une fois ceux-ci maîtrisés, passez aux katakana. Et une fois ceux-ci également maîtrisés, vous pouvez passez aux kanji. Ne faîtes rien d'autres tant que les kana ne sont pas maîtrisés à 100%.
Dans le fichier `kanji.csv`, vous trouverez une liste par défaut d'une centaine de kanji. Au début, je vous conseille de garder les vingts premiers et d'en rajouter au fur et à mesure. Pour ajouter des kanjis, vous avez deux possibilités :
- Vous les ajouter manuellement dans le csv (il faut respecter les conventions d'écriture du csv)
- Vous les ajouter via l'application qui fera tout le travail de normalisation pour vous, voir [comment ajouter des kanji](#paramètres) dans les paramètres.
Je vous conseille également d'installer le clavier japonais windows, il vous sera utile dans certains modules.

## Calculs

A chaque kana et à chaque kanji, un score natif leur est affilié `10`. Lorsque vous avez bon, le score diminue `-2`. Et lorsque vous avez faux, le score augmente `+5`.
En fonction du score est calculé le taux d'apparition. La valeur de ce dernier influe donc sur le taux d'apparition de tous les kana et kanji. Plus vous avez faux sur un kana/kanji, plus son taux d'apparition va augmenter, plus vous allez tomber sur celui-ci, plus vous allez vous entraîner dessus, mieux vous allez le mémoriser, plus vous aurez bon, moins il apparaitra, etc.


## Problèmes connus

Il se peut que sous Windows 10, l'affichage des caractères japonais ne se fassent pas. Le cas échéant, bah rip à vous. Etat inconnu sous MacOS et Linux.
Il se peut qu'à l'oral, certains kanji sont pronocés avec leur version kunyomi ou onyomi, cependant dans le fichier `kanji.cscv`, seul l'un des deux est présent. Si cela survient, soit vous changez le romaji associé soit vous laissez.


## NB

Le taux d'apparition des kana et des kanji est calculé seulement et uniquement dans le mode lecture, avoir faux dans les autres modes n'impacte que faux score final qui est affiché, cela ne change rien dans les différents fichier csv.


## Ajouts futur

- génération de texte aléatoire
- Interface graphique 
- module de conjugaison
- module de grammaire
- Implémentation d'une IA ayant une voix artificielle japonaise réaliste.
- Un milliere de kanji trié par niveau nécessaire au passage du JLPT avec leur lecture onyomi et kunyomi.

