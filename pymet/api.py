import collections
import pandas as pd
from typing import Dict, List

from pymet.utils import constants


class Met:
    _path_to_csv: str = constants.CsvPaths.COLLECTION

    def __init__(self):
        self.data = pd.read_csv(self._path_to_csv, encoding='utf8')
        self._clean_columns()

    def _clean_columns(self) -> None:
        self.data.columns = [
            col.lower().replace(' ', '_') for col in self.data.columns
        ]


class MetPaintings(Met):
    _path_to_csv: str = constants.CsvPaths.PAINTINGS

    def __init__(self):
        super().__init__()
        self.data = self._drop_null_artists()
        self.lookup = self._create_artist_lookup()

    def _drop_null_artists(self) -> pd.DataFrame:
        data = self.data.copy()
        data = data[constants.Columns.ARTIST_COLUMNS]
        return data.dropna(
            axis=0,
            subset=[constants.Columns.ARTIST_ALPHA_SORT]
        ).reset_index(drop=True)

    def _create_artist_lookup(self) -> Dict[str, List[str]]:
        lookup = collections.defaultdict(list)
        for artist in self.data.loc[:, constants.Columns.ARTIST_ALPHA_SORT]:
            last_name = artist.split(',')[0].lower()
            lookup[last_name].append(artist)
        return lookup

    def contains_artist(self, artist: str) -> bool:
        return artist.lower() in self.lookup.keys()

    def works_by_artist(self, artist: str) -> pd.DataFrame:
        if not self.contains_artist(artist):
            raise RuntimeError(
                f'Artist request {artist} not found in lookup of Met artists. '
                'Please try submitting only the artist\'s last name.'
            )
        rows = []
        for alpha_name in self.lookup[artist.lower()]:
            rows.append(
                self.data[self.data.artist_alpha_sort == f'{alpha_name}']
            )
        return pd.concat(rows, sort=False)
