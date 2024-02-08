# lyricognizer
I.A. de détection d’artistes

**Idée :**
Créer une IA qui reçoit un texte de musique en entrée et qui doit donner le chanteur en sortie. L’IA sera entraînée sur un dataset contenant plusieurs textes de quelques artistes choisis au préalable. Elle fonctionnera en calculant la distance de compression (NCD) entre le texte entré et ses données d’entraînement, et fera la moyenne par artiste.

**Processus :**
1. [x] Collecte de données (API Genius)
2. [x] Pré-traitement des données 
    - [x] Nettoyage et normalisation du texte
    - [x] Suppression de mots inutiles (le, la, ...) 
    - [x] Racinisation des mots
3. [x] Séparation des données (80% entraînement, 20% test)
4. [ ] Calcul du NCD à l’aide de plusieurs méthodes de compression
    - [x] zlib
    - [ ] gzip
    - [ ] bzip2
    - [x] lzma
5. [ ] Calcul du NGD
5. [ ] Retour d’un classement des artistes les plus probables

**Choix des artistes :**
- [x] Charles Aznavour
- [x] B.B. Jacques
- [x] Damso
- [x] Drake
- [x] Freeze Corleone
- [x] Gazo
- [x] Lomepal
- [x] Mylène Farmer
- [x] Nekfeu
- [x] Soolking