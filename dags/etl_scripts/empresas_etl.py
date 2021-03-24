import dask.dataframe as dd
from brazilnum.cnpj import format_cnpj, validate_cnpj

df = dd.read_csv(r"csv_data/empresas.csv")


def call_format_cnpj(cnpj):
    cnpj_to_s = str(cnpj)
    if len(cnpj_to_s) > 13:
        return format_cnpj(cnpj_to_s)

    return None


df['cnpj_formated'] = df.apply(lambda row: call_format_cnpj(
    row['cnpj']), axis=1, meta=(None, 'object'))


def root_cnpj(cnpj):
    if cnpj is None:
        return None

    root, _ = cnpj.split('/')
    return root


df['root_cnpj'] = df.apply(lambda row: root_cnpj(
    row['cnpj_formated']), axis=1, meta=(None, 'object'))

df = df.drop(['cnpj'], axis=1)

df.to_parquet(path='out/empresas_formated.parquet')
