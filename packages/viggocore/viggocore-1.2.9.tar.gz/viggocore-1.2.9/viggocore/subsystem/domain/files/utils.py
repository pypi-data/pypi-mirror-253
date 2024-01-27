import os
from viggocore.common import exception


def get_size(domain_id):
    size = 0

    folderpath = os.environ.get('VIGGOCORE_FILE_DIR_SIZE', '')
    if len(folderpath) == 0:
        raise exception.BadRequest('VIGGOCORE_FILE_DIR_SIZE not found')

    for ele in os.scandir(folderpath):
        if '.' not in ele.name:
            for ele2 in os.scandir(f'{folderpath}/{ele.name}'):
                if '.' not in ele2.name:
                    for ele3 in os.scandir(f'{folderpath}/{ele.name}/{ele2.name}'):
                        if ele3.name == domain_id:
                            for ele4 in os.scandir(f'{folderpath}/{ele.name}/{ele2.name}/{ele3.name}'):
                                for ele5 in os.scandir(f'{folderpath}/{ele.name}/{ele2.name}/{ele3.name}/{ele4.name}'):
                                    size += os.path.getsize(ele5)

    response_dict = {}

    # montandos as respostas
    conversoes = ['BYTES', 'KBYTES', 'MEGAS', 'GIGAS', 'TERAS']
    for conversao in conversoes:
        response_dict.update({conversao: size})
        size /= 1024

    return response_dict
