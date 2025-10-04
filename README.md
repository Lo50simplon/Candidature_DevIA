# Qu'est-ce que c'est ?

Ceci est un projet de visualisation de données, qui utilise le langage de programmation Pyhton.
Il utilise deux outils : [pandas](https://pandas.pydata.org/about/) et [plotly](https://plotly.com/python/).

- Pandas va nous permettre de télécharger un fichier de données CSV depuis une URL.
- Plotly va nous permettre de générer des graphiques puis de les exporter en page web (au format HTML).

# Démarrer le projet dans GitHub Codespaces
* Cliquez sur "Utiliser ce modèle" ("Use this template") en haut à droite de la page, puis sur "Créer un nouveau dépôt". [Voici les étapes pour créer un dépôt](https://docs.github.com/fr/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template). Si vous n'avez pas de compte GitHub, il vous sera demandé d'en créer un avant de pouvoir créer le dépôt.
* Une fois dans votre dépôt, ouvrez le site dans un Codespace en cliquant sur Code > Codespaces, puis créez un nouveau Codespace sur votre branche principale.

<img alt="Créer un Codespace" src="https://github.com/user-attachments/assets/cb29a8da-d1ac-42f5-962c-7d43b8011324" width="400px"/><br/>

## Attendez que l’environnement de travail sur Codespace soit prêt

L'environnement de travail Codespace va se construire automatiquement au premier lancement. Cela peut prendre plusieurs minutes.

L’environnement est prêt lorsque vous voyez apparaître en bas de la page les boutons suivants :

    💬 MESSAGE DE BIENVENUE

    💻 TERMINAL

    🔎 SPLIT

    🏠 PREVIEW

➡️ Ne touchez à rien pendant le chargement.

# Le projet
## Comment ça marche ?

* `README.md`: Il s'agit de ce fichier, que vous lisez en ce moment même.

* `app.py`: ceci est un fichier python, le coeur du projet.

Pour executer le fichier Python et ainsi générer un graphique sous forme de page web, cliquez sur le bouton "💻 TERMINAL" depuis la barre d'outils en bas de page.

Puis écrivez la commande suivante : `python3 app.py`.

Cette commande se divise en deux partie : 
- d'abord "python3" qui indique que l'on souhaite utiliser Python, et plus précisemment, la version 3.
- Puis "app.py" qui indique que l'on souhaite exécuter le programme python contenu dans le fichier "app.py" (avec Python3 donc).

Appuyez sur la touche `Entrée` de votre clavier, après quelques secondes d'exécution, vous devriez obtenir un message de succès.

## Observer son résultat

Cliquez sur le bouton "🏠 PREVIEW" depuis la barre d'outils en bas de page.
Depuis la nouvelle fenêtre de votre navigateur qui vient de s'ouvrir, sélectionner le fichier "ventes-par-region.html".

Vous venez d'ouvrir le graphique en version web généré par le fichier "app.py" exécuté avec Python3 !

Prenez le temps de lire, d'analyser voir même de bidouiller le fichier "app.py" puis lancez-vous dans les consignes du projet pour la sélection Simplon !

# Publier vos modifications sur votre propre dépôt GitHub
Une fois que vous avez terminé de travailler sur les consignes du projet et que vous souhaitez publier vos modifications dans votre dépôt, vous devrez suivre les étapes décrites dans la section « Validation (commit) de vos modifications » de [cette ressource](https://docs.github.com/fr/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace#validation-commit-de-vos-modifications
).
