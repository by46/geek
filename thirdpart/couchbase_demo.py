import couchbase.subdocument as SD
from couchbase.bucket import Bucket


def update():
    bucket = Bucket("couchbase://localhost:8091/default", quiet=True)
    key = 'wendy'

    entity = bucket.get(key)
    print dir(entity)
    print entity.success
    if not entity.success:
        bucket.upsert(key, {})
    bucket.mutate_in(key,
                     SD.upsert("address.sex", "female", create_parents=True),
                     SD.upsert("address.name", "benjamin", create_parents=True),
                     SD.upsert("address.name1", "benjamin", create_parents=True),
                     SD.upsert("address.name2", "benjamin", create_parents=True),
                     SD.upsert("address.name3", "benjamin", create_parents=True),
                     SD.upsert("address.name4", "benjamin", create_parents=True),
                     SD.upsert("address.name11", "benjamin", create_parents=True),
                     SD.upsert("address.name12", "benjamin", create_parents=True),
                     SD.upsert("address.name13", "benjamin", create_parents=True),
                     SD.upsert("address.name14", "benjamin", create_parents=True),
                     SD.upsert("address.name15", "benjamin", create_parents=True),
                     SD.upsert("address.name16", "benjamin", create_parents=True),
                     SD.upsert("address.name17", "benjamin", create_parents=True),
                     SD.upsert("address.name18", "benjamin", create_parents=True),
                     SD.upsert("address.name19", "benjamin", create_parents=True),
                     SD.upsert("address.name20", "benjamin", create_parents=True))
    bucket.touch(key, 5)


def main():
    bucket = Bucket("couchbase://localhost:8091/default", quiet=True)
    # bucket.mutate_in('name', SD.upsert('path2', 'value2'))
    bucket.upsert("name1", {"age": 21, "address": {"name1": "chongqing"}})
    bucket.upsert_multi({'scmesos01': {'ip': '10.16.78.81'}, 'scmesos02': {'ip': '10.16.78.82'}})
    # bucket.upsert("name", {"age": 21, "address": {"sex": "female"}})
    # SD.upsert("name.address", "Chongqing")
    # res = bucket.get('name.address')
    # print(res.value)
    bucket.mutate_in("name", SD.upsert("address.sex", "female"),
                     SD.upsert("address.name", "benjamin"))
    print bucket.lookup_in("name", SD.get("address"))
    item = bucket.get('scmesos01')
    print item

    rv = bucket.lookup_in('name',
                          SD.get('address'),
                          SD.get('address.name1'),
                          SD.exists('address.name2'))
    print rv[0], rv[1]
    print rv.exists(2)


if __name__ == '__main__':
    update()
