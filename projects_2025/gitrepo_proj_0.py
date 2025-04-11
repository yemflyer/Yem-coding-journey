#Git repo project https://benhoyt.com/writings/pygit/ ²²
"""
Initializing a local Git repo simply involves creating the .git directory and a few files and directories under it. 
After defining read_file and write_file helper functions, we can write init():
The .git Directory is where Git stores all its internal data (like commits, branches, and configuration).
"""
def init(repo):
    """Create directory for repo and initialize .git directory."""
    os.mkdir(repo)#Create the Repository Directory
    os.mkdir(os.path.join(repo, '.git')) #Create the .git Directory
    for name in ['objects', 'refs', 'refs/heads']:
        os.mkdir(os.path.join(repo, '.git', name)) #(os.path.join(repo, '.git', 'HEAD') creates the full path for each subdirectory (e.g., my_project/.git/objects).
    write_file(os.path.join(repo, '.git', 'HEAD'), # writting the HEAD file ,the HEAD file is a text file that points to the current branch.
               b'ref: refs/heads/master')
    print('initialized empty repository: {}'.format(repo))

'''Failure management : You’ll note that there’s not a whole lot of graceful error handling. 
This is a 500-line subset, after all. If the repo directory already exists, it’ll fail hard with a traceback.'''

"""
Hashing objects
The hash_object function hashes and writes a single object to the .git/objects “database”. 
There are three types of objects in the Git model: blobs (ordinary files), commits, and trees (these represent the state of a single directory).

Each object has a small header including the type and size in bytes. 
This is followed by a NUL byte and then the file’s data bytes. This whole thing is zlib-compressed and written to .git/objects/ab/cd..., where ab are the first two characters of the 40-character SHA-1 hash and cd... is the rest.

Notice the theme of using Python’s standard library for everything we can (os and hashlib). Python comes with “batteries included”.
"""
def hash_object(data, obj_type, write=True):
    """Compute hash of object data of given type and write to object store
    if "write" is True. Return SHA-1 object hash as hex string.
    """
    header = '{} {}'.format(obj_type, len(data)).encode()
    full_data = header + b'\x00' + data
    sha1 = hashlib.sha1(full_data).hexdigest()
    if write:
        path = os.path.join('.git', 'objects', sha1[:2], sha1[2:])
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            write_file(path, zlib.compress(full_data))
    return sha1

"""
The git index
The next thing we want to be able to do is add files to the index, or staging area. 
The index is a list of file entries, ordered by path, each of which contains path name, 
modificiation time, SHA-1 hash, etc. Note that the index lists all files in the current tree, not just the files being staged for commit right now.

The index, which is a single file at .git/index, is stored in a custom binary format. 
It’s not exactly complicated, but it does involve a bit of struct usage, 
plus a bit of a dance to get to the next index entry after the variable-length path field.

The first 12 bytes are the header, the last 20 a SHA-1 hash of the index, 
and the bytes in between are index entries, each 62 bytes plus the length of the path and some padding. 
Here’s our IndexEntry namedtuple and read_index function:
"""
# Data for one entry in the git index (.git/index)
IndexEntry = collections.namedtuple('IndexEntry', [
    'ctime_s', 'ctime_n', 'mtime_s', 'mtime_n', 'dev', 'ino', 'mode',
    'uid', 'gid', 'size', 'sha1', 'flags', 'path',
])

def read_index():
    """Read git index file and return list of IndexEntry objects."""
    try:
        data = read_file(os.path.join('.git', 'index'))
    except FileNotFoundError:
        return []
    digest = hashlib.sha1(data[:-20]).digest()
    assert digest == data[-20:], 'invalid index checksum'
    signature, version, num_entries = struct.unpack('!4sLL', data[:12])
    assert signature == b'DIRC', \
            'invalid index signature {}'.format(signature)
    assert version == 2, 'unknown index version {}'.format(version)
    entry_data = data[12:-20]
    entries = []
    i = 0
    while i + 62 < len(entry_data):
        fields_end = i + 62
        fields = struct.unpack('!LLLLLLLLLL20sH',
                               entry_data[i:fields_end])
        path_end = entry_data.index(b'\x00', fields_end)
        path = entry_data[fields_end:path_end]
        entry = IndexEntry(*(fields + (path.decode(),)))
        entries.append(entry)
        entry_len = ((62 + len(path) + 8) // 8) * 8
        i += entry_len
    assert len(entries) == num_entries
    return entries

"""
"""
"""
"""