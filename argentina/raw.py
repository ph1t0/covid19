import logging
import pandas as pd
from io import StringIO
from subprocess import check_output
from pathlib import Path


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

DEFAULT_RAW_ANNOTATED_PATH = Path('argentina/raw_annotated.md')

DISTRITOS = '''
    JUJUY         FORMOSA
    SALTA                             CHACO     MISIONES
    CATAMARCA TUCUMAN SANTIAGODELESTERO   CORRIENTES
    LARIOJA           CORDOBA         SANTAFE ENTRERIOS
    SANJUAN SANLUIS
    MENDOZA         LAPAMPA             PCIABSAS CABA
    NEUQUEN RIONEGRO
            CHUBUT
            SANTACRUZ
            TIERRADELFUEGO
    '''.split()


def _make_df_from_md(md_path=DEFAULT_RAW_ANNOTATED_PATH):
    print(f'Reading {md_path}')
    csv_bytes = check_output(['./make_csv_from_md', md_path])
    df = pd.read_csv(StringIO(csv_bytes.decode()))
    return df


def _fix_index(df):
    date_index = pd.to_datetime(df[['year', 'month', 'day']].apply(lambda x: "-".join((map(str, x.values))),
                                                                   axis=1),
                                format="%Y-%m-%d")
    df = df.set_index(date_index)[['case', 'place', 'new']]
    return df


def distritos_afectados(df):
    da = df.place.unique()
    # Chequeo que no haya typos en los nombres de los lugares
    assert all(d in DISTRITOS for d in da), da
    return da


date_indexed_raw = _fix_index(_make_df_from_md())
