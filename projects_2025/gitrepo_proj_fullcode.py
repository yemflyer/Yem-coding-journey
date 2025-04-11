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
    write_file(os.path.join(repo, '.git', 'HEAD'), 
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
"""
"""
"""
"""
"""