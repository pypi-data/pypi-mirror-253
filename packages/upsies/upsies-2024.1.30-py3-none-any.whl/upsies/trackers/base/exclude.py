checksums = r'\.(?i:sfv|md5)$'

extras = (
    r'(?i:'
    # Anything with the word "extras" with another word in front of it. This
    # should exclude the show "Extras".
    r'/.+[\. ]extras[\.]'
    r'|'
    # Numbered extras (e.g. "Foo.S01.Extra1.mkv", "Foo.S01.Extra.2.mkv", .etc)
    r'/.+[\. ]extra[\. ]?\d+[\.]'
    r')'
)

images = r'\.(?i:png|jpg|jpeg)$'

nfo = r'\.(?i:nfo)$'

samples = (
    r'(?i:'
    # Sample directory
    r'/[!_0-]?sample/'
    r'|'
    # Sample file name starts with release name
    r'[^/][\.\-_ ]sample\.mkv'
    r'|'
    # Sample file name ends with release name
    r'/sample[\!\-_].+\.mkv'
    r'|'
    # Sample file name starts with release name and ends with "sample-RLSGRP.mkv"
    r'[\.\-_!]?sample-[a-zA-Z0-9]+\.mkv'
    r'|'
    # Sample file name starts with "<characters that top-sort>sample"
    r'/[!#$%&*+\-\.]?sample\.mkv'
    r')'
)

subtitles = r'\.(?i:srt|idx|sub)$'
