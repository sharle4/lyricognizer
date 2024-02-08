res = {
    'artiste1': {
        'chanson1': [
            rank_artiste1,
            {
                'artiste1': similitude_artiste1,
                'artiste2': similitude_artiste2,
                ...
            }
        ],
        'chanson2': [
            rank_artiste1,
            {
                'artiste1': similitude_artiste1,
                'artiste2': similitude_artiste2,
                ...
            }
        ],
        ...
    },
    'artiste2': {
        'chanson1': [
            rank_artiste2,
            {
                'artiste1': similitude_artiste1,
                'artiste2': similitude_artiste2,
                ...
            }
        ],
        'chanson2': [
            rank_artiste2,
            {
                'artiste1': similitude_artiste1,
                'artiste2': similitude_artiste2,
                ...
            }
        ],
        ...
    },
    ...
    'moyenne': [moyenne_rank_auteur]
}
