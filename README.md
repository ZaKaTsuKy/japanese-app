# Application d'aide à l'apprentissage du japonais

Merci de tout lire avant d'utiliser l'application


## Comment utiliser l'application

Des numéros sont affiliés à chaque option possible. Entrez la numéro puis appuyez sur la touche "enter" du clavier. Vous pouvez ainsi naviguer partout.
<img width="960" alt="image" src="https://github.com/ZaKaTsuKy/japanese-app/assets/74179251/5095a6ac-7a67-43f2-bfd1-090e07d57c7b">


## Règles d'utilisation

Différents modes sont proposés, ci-après l'explication de chaque mode.


# Lecture 

Chaque entraînement vous demandera combien d'éléments vous voudrez dans votre série. Rentrez un entier et appuyez sur "enter".
Pour l'entraînement à la lecture des kanji, le programme vous demandera de rentrer un niveau de JLPT, si vous ne savez pas ce que c'est, google vous renseignera. Par défaut, laissez vide et tout niveau vous sera proposé. Autrement, rentrez les niveaux que vous avez envie (ex : `4` ou `4 5`, seul les niveaux proposés seront respectivement le JLPT N4 et le JLPT N4 N5).
<img width="960" alt="image" src="https://github.com/ZaKaTsuKy/japanese-app/assets/74179251/06b7bf9a-61ec-44cf-8e17-493b967d41be">

Pour répondre aux questions écrivez la version romaji et appuyez sur "enter", autrement cela vous donnera faux.
<img width="960" alt="image" src="https://github.com/ZaKaTsuKy/japanese-app/assets/74179251/99e40513-b209-4bb2-9217-ed3327dc45b1">

Si vous bloquez, laissez le champs vide, appuyez sur "enter", cela vous donnera la réponse. Cepedant vous aurez faux. Pour voir les conséquences sur le fait d'avoir faux, rendez-vous [ici](#calculs).


# Compréhension

Module non implémentée à l'heure actuelle. 


# Audio

Ce module va vous permettre d'écouter les kanjis de votre liste à l'oral et d'écrire ce qu'ils veulent dire en romaji. Si vous n'avez pas compris, vous pouvez laisser le champs vide et directement appuyer sur "enter" pour répéter l'audio, cela n'affectera pas votre taux de réussite. Il sera également possible à l'avenir de le faire avec des phrases, ce module n'est pas encore implémenté.


# Expression

Module non implémentée à l'heure actuelle. 


# Nombre

Ce module va vous permettre de vous entraîner avec les nombres. Il propose 3 fonctionnalités :
- Lecture : Le module va vous afficher un nombre entre 1 et 99 999 écrit avec les nombres japonais, à vous de le traduire en alphanumérique.
- Ecriture : Le module va vous écrire un nombre en alphanumérique entre 1 et 99 999, à vous de l'écrire en caractère japonais.
- Audio : Le module va dire à l'oral un nombre compris entre 1 et 99 999, à vous de l'écrire en alphanumérique.
**<ins>Exemple</ins>**
<img width="960" alt="image" src="https://github.com/ZaKaTsuKy/japanese-app/assets/74179251/151d2a93-a636-4b98-a1b8-fcefe57a2464">

# Paramètres

Les paramètres vous permettent plusieurs choses :
- Ajouter des kanjis. Pour ce faire, vous devrez entrer le kanji, le romaji et sa traduction sous la forme : `kanji romaji traduction`, avec simplement des espaces entre chaque élément.
- Remettre les compteurs des scores et des taux à 0. 
- Afficher les statistiques d'apparitions des kana et des kanji.


## Conseils

Si vous êtes débutants, commencez par faire les hiragana. Une fois ceux-ci maîtrisés, passez aux katakana. Et une fois ceux-ci également maîtrisés, vous pouvez passez aux kanji. Ne faîtes rien d'autres tant que les kana ne sont pas maîtrisés à 100%.
Dans le fichier `kanji.csv`, vous trouverez une liste par défaut d'une centaine de kanji. Au début, je vous conseille de garder les vingts premiers et d'en rajouter au fur et à mesure. Pour ajouter des kanjis, vous avez deux possibilités :
- Vous les ajouter manuellement dans le csv (il faut respecter les conventions d'écriture du csv)
- Vous les ajouter via l'application qui fera tout le travail de normalisation pour vous, voir [comment ajouter des kanji](#paramètres) dans les paramètres.


## Calculs

A chaque kana et à chaque kanji, un score natif leur est affilié `10`. Lorsque vous avez bon, le score diminue `-2`. Et lorsque vous avez faux, le score augmente `+5`.
En fonction du score est calculé est taux d'apparition. La valeur de ce dernier influe donc sur le taux d'apparition de tous les kana et kanji. Plus vous avez faux, plus le taux d'apparition va augmenter, plus vous allez tomber sur celui-c, plus vous allez vous entraîner, mieux vous allez le mémoriser, plus vous arez bon, moins il apparaitra, etc.


## Problèmes connus

Il se peut que sur Windows 10, l'affichage des caractères japonais ne se fassent pas. Le cas échéant, bah rip à vous. 
Il se peut qu'à l'oral, certains kanji sont pronocés avec leur version sino-japonaise et non purement japonaise. Si cela survient, soit vous changez le romaji associé soit vous laissez.

