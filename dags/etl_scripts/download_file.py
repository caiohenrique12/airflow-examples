import requests
import os
import errno
import gzip
import shutil

base_path = f'{os.getcwd()}/csv_data'


def create_folder():
    try:
        print('create folder for receive csv data')
        os.makedirs(f'{os.getcwd()}/csv_data')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def make_download_file(file_name):
    print(f'Starting {file_name} csv donwload')
    req = requests.get(f'https://data.brasil.io/dataset/socios-brasil/{file_name}.csv.gz',
                       allow_redirects=True)

    open(f'{base_path}/{file_name}.csv.gz', 'wb').write(req.content)
    print(f'Finished!')


def unzip_csv(file_name):
    print(f'Unzip {file_name}')
    with gzip.open(f'{base_path}/{file_name}.csv.gz', 'rb') as f_in:
        with open(f'{base_path}/{file_name}.csv', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def removing_file(file_name):
    print(f'Removing {file_name}.gz file')
    os.remove(f'{base_path}/{file_name}.csv.gz')


def start_proccess_to_download():
    print('Make Download csvs')
    for file in ['empresas', 'socios']:
        make_download_file(file)
        unzip_csv(file)
        removing_file(file)


create_folder()
start_proccess_to_download()
