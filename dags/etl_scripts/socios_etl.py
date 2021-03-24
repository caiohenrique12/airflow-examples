import dask.dataframe as dd
from brazilnum.cnpj import format_cnpj, validate_cnpj

df = dd.read_csv(r"csv_data/socios.csv")


def call_format_cnpj(cnpj):
    cnpj_to_s = str(cnpj)
    if len(cnpj_to_s) > 13:
        return format_cnpj(cnpj_to_s)

    return None


df['cnpj_formated'] = df.apply(lambda row: call_format_cnpj(
    row['cnpj']), axis=1, meta=(None, 'object'))

df = df.drop(['cnpj'], axis=1)

df.to_parquet(path='out/socios_formated.parquet')
