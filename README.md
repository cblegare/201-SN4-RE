420-611-BT * Intelligence Artificielle 2
========================================

# **Plan de cours : Intelligence Artificielle**

Ce cours vise à développer les compétences pratiques et théoriques nécessaires
pour concevoir, implémenter et évaluer des systèmes d'intelligence artificielle
en Python.

## Chapitre 1 : Résolution de problèmes par la recherche

Indispensable en développement de jeux vidéo pour le calcul de chemins
(pathfinding) et pour programmer l'intelligence artificielle d'adversaires
dans les jeux au tour par tour en anticipant les coups.

- Distinguer l'efficacité des algorithmes de recherche non informés (DFS vs BFS).
- Retracer l'exploration des nœuds d'un graphe à l'aide d'algorithmes informés (Greedy, A\*).
- Justifier l'utilisation d'un algorithme Minimax à profondeur limitée pour réduire l'espace d'états.
- Calculer la valeur d'un nœud dans un arbre de jeu Minimax.

## Chapitre 2 : Connaissances et raisonnement logique

Base des moteurs de règles d'entreprise et de la gestion de l'état du monde
dans les jeux. Permet de valider des conditions de quêtes complexes et de
générer dynamiquement des énigmes logiques.

- Déduire la véracité d'une implication logique entre propositions.
- Traduire des contraintes exclusives (OU exclusif) en formules logiques
  formelles.
- Convertir des énoncés en langage naturel en propositions logiques
  formelles.
- Formuler des requêtes complexes en logique du premier ordre.

## Chapitre 3 : Gestion de l'incertitude

Permet aux programmes et personnages non-joueurs de prendre des décisions
avec des informations imparfaites (ex: brouillard de guerre).
Alimente la conception de systèmes aléatoires contrôlés comme l'attribution
de butins.

- Calculer des probabilités d'événements inclusifs, conjoints et
  conditionnels.
- Interpréter l'indépendance conditionnelle au sein d'un réseau bayésien.
- Appliquer les probabilités conditionnelles à des scénarios de diagnostic
  ou de génétique.

## Chapitre 4 : Optimisation

Crucial pour équilibrer la charge des serveurs, planifier des processus et
gérer les comportements logistiques complexes
(ex: jeux de gestion de type SimCity).

- Prévoir le comportement d'un algorithme de recherche locale
  (ascension de colline).
- Formuler une fonction objectif pour un problème d'allocation de ressources.
- Définir mathématiquement des contraintes restrictives d'un problème.
- Exécuter un algorithme de consistance d'arcs (AC-3) pour résoudre des
  problèmes de satisfaction de contraintes.

## Chapitre 5 : Apprentissage automatique

Essentiel pour construire des systèmes de jumelage (matchmaking),
détecter la triche, prédire le comportement des joueurs et entraîner des
bots adaptatifs.

- Catégoriser les cas d'usage (supervisé, non supervisé, par renforcement).
- Calculer la perte globale (L1/L2) d'un modèle de régression et évaluer
  le surapprentissage.
- Contrôler le compromis exploration/exploitation (epsilon-greedy) dans
  l'apprentissage par renforcement.

## Chapitre 6 : Réseaux de neurones et vision

Révolutionne le rendu graphique et la vision par ordinateur, essentiels
en réalité virtuelle ou augmentée pour le suivi des mouvements et l'analyse
visuelle de l'environnement physique.

- Calculer la valeur de sortie d'un neurone artificiel selon différentes
  fonctions d'activation (Step, ReLU).
- Dimensionner les paramètres d'une architecture de réseau fully connected
  multicouche.
- Sélectionner la topologie de réseau récurrent adéquate selon le flux
  de données (Many-to-One, etc.).
- Simuler l'application d'un filtre de max-pooling sur une image matricielle.

## Chapitre 7 : Traitement du Langage Naturel

Facilite les interactions textuelles naturelles avec les personnages, la
création d'assistants virtuels, la modération automatique des chats et
l'analyse massive de données textuelles.

- Valider la syntaxe d'une phrase via une grammaire hors contexte.
- Critiquer les encodages discrets (One-Hot) vs les représentations
  distribuées de mots.
- Justifier l'utilité du lissage (smoothing) dans les classificateurs
  probabilistes.
- Extraire systématiquement des n-grammes d'une chaîne de caractères.

## Chapitre 8 : Développement d'outils MCP

Passerelle standardisée entre les grands modèles de langage et les applications
métiers. Permet d'intégrer l'IA dans un moteur de jeu ou de créer des agents
capables d'interagir avec des bases de données et des APIs en temps réel.

- Expliquer l'architecture client-serveur du protocole Model Context Protocol
  (MCP).
- Concevoir un serveur MCP fonctionnel en Python.
- Interfacer de manière sécurisée un modèle de langage avec des outils
  et systèmes externes.
