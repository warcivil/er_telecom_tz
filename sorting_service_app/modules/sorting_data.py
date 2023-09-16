from sorting_service_app.utils.sorted_by_version import version_compare
import rest_framework.exceptions as exceptions

def sort_and_process_data(data):
    """
    Сортирует словарь данных по версиям и обрабатывает поле "value".

    Args:
        data (dict): Словарь данных, содержащий информацию для сортировки и обработки.

    Returns:
        dict: Словарь данных, в котором версии отсортированы по возрастанию, а поле "value" преобразовано
              в массив слов, удалены лишние пробелы вокруг слов.

    Raises:
        ValueError: Если формат входных данных (JSON) неверен.
        Exception: Если возникла другая ошибка при обработке данных.
    """
    try:
        if 'data' in data and isinstance(data['data'], dict):
            sorted_data = {
                key: {
                    'ident': item['ident'],
                    'value': item['value'].strip().split()
                }
                for key, item in sorted(data['data'].items(), key=lambda x: version_compare(x[1]['ident']))
            }
            data['data'] = sorted_data
        else:
            raise exceptions.ValidationError('Invalid JSON format')
    except Exception as e:
        raise exceptions.APIException('Error in module')
    return data
