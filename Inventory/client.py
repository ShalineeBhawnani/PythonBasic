class SongSerializer:
    def serialize(self, song, format):
        serializer = get_serializer(format)
        print(serializer)
        return serializer(song)


def get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    else:
        raise ValueError(format)


def _serialize_to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)
class ObjectSerializer:
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()