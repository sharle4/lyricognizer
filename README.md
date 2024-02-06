# lyricognizer
I.A. de détection d’artistes

**Idée :**
Créer une IA qui reçoit un texte de musique en entrée et qui doit donner le chanteur en sortie. L’IA sera entraînée sur un dataset contenant plusieurs textes de quelques artistes choisis au préalable. Elle fonctionnera en calculant la distance de compression (NCD) entre le texte entré et ses données d’entraînement, et fera la moyenne par artiste.

**Processus :**
1. [ ] Collecte de données (API Genius)
2. [ ] Pré-traitement des données 
    - [x] Nettoyage et normalisation du texte
    - [ ] Suppression de mots inutiles (le, la, ...)
    - [ ] Racinisation des mots
3. [ ] Séparation des données (80% entraînement, 20% test)
4. [ ] Calcul du NCD à l’aide de plusieurs méthodes de compression
    - [x] zlib
    - [ ] gzip
    - [ ] bzip2
    - [ ] lzma
5. [ ] Retour d’un classement des artistes les plus probables

**Choix des artistes :**
- [ ] Nekfeu