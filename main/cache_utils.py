from django.core.cache import cache

cache.set('key', 'value', timeout=300)

value = cache.get('key')

cache.delete('key')

cache.clear()

def get_cached_data(key, default_value):
    data = cache.get(key)
    if data is None:
        cache.set(key, default_value, timeout=300)
    return data