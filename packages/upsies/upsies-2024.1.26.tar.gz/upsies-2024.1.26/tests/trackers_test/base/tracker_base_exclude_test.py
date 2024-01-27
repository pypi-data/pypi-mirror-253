import re

import pytest

from upsies.trackers.base import exclude


@pytest.mark.parametrize(
    argnames='path, exp_match',
    argvalues=(
        # Release names that must match
        ('/path/to/Foo.2012.BluRay.x264-ASDF.sfv', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.SFV', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.Sfv', True),
        # Release names that must not match
        ('/path/to/sfv.2012.bluray.x264-asdf.mkv', False),
    ),
)
def test_checksums(path, exp_match):
    regex = re.compile(exclude.checksums)
    match = regex.search(path)
    assert bool(match) is exp_match


@pytest.mark.parametrize(
    argnames='path, exp_match',
    argvalues=(
        # Release names that must match
        ('/path/to/Foo.S01.BluRay.x264-ASDF/Foo.S01.Extras.DVDRip.x264-ASDF', True),
        ('/path/to/Foo.S02.Extras.BluRay.x264-ASDF', True),
        ('/path/to/Foo.S03.720p.BluRay.x264-ASDF/Extras/Foo.S03.Extras.S03.720p.BluRay.DD2.0.x264-ASDF.mkv', True),
        ('/path/to/Foo.S04.720p.BluRay.x264-ASDF/Extras/Foo.S04.Extras.Topic.S03.720p.BluRay.DD2.0.x264-ASDF.mkv', True),
        ('/path/to/Foo.S05.720p.BluRay.x264-ASDF/Foo.S05.Extra.1.720p.BluRay.x264-EbP.mkv', True),

        # Release names that must not match
        ('/path/to/Extras.S01.720p.BluRay.x264-ASDF', False),
        ('/path/to/Foo.S06.720p.BluRay.x264-ASDF/Foo.S06E01.Extraordinary.720p.BluRay-ASDF.mkv', False),
        ('/path/to/Foo.S07.720p.BluRay.x264-ASDF/Foo.S07E02.Extra.Ordinary.720p.BluRay-ASDF.mkv', False),


        ('/path/to/the.extractors.2019.720p.bluray.x264-brmp.mkv', False),
    ),
)
def test_extras(path, exp_match):
    regex = re.compile(exclude.extras)
    match = regex.search(path)
    assert bool(match) is exp_match


@pytest.mark.parametrize(
    argnames='path, exp_match',
    argvalues=(
        ('/path/to/Foo.2012.BluRay.x264-ASDF.png', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.PNG', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.jpg', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.Jpg', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.jpeg', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.jPEG', True),
    ),
)
def test_images(path, exp_match):
    regex = re.compile(exclude.images)
    match = regex.search(path)
    assert bool(match) is exp_match


@pytest.mark.parametrize(
    argnames='path, exp_match',
    argvalues=(
        ('/path/to/Foo.2012.BluRay.x264-ASDF.nfo', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.NFO', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.Nfo', True),
    ),
)
def test_nfo(path, exp_match):
    regex = re.compile(exclude.nfo)
    match = regex.search(path)
    assert bool(match) is exp_match


@pytest.mark.parametrize(
    argnames='path, exp_match',
    argvalues=(
        # Release names that must match
        ('/path/to/Foo.2012.BluRay.x264-ASDF/!Sample/Foo.2012.BluRay.x264-ASDF.sample.mkv', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF/!sample.mkv', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF/Foo.2012.BluRay.x264-ASDF sample.mkv', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF/SAMPLE-Foo.2012.BluRay.x264-ASDF.mkv', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF/Sample/Foo.2012.BluRay.x264-ASDF.sample.mkv', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF/Sample/f-foo-x264-sample.mkv', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF/asdf-foo.sample.mkv', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF/foo.2012.bluray.x264.sample-asdf.mkv', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF/sample.mkv', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF/sample/Foo.2012.BluRay.x264-ASDF.sample.mkv', True),
        # Release names that must not match
        ('/path/to/Sample.2012.BluRay.x264-ASDF.mkv', False),
        ('/path/to/Sample.2012.BluRay.x264-ASDF/Sample.2012.BluRay.x264-ASDF.mkv', False),
        ('/path/to/The.Sample.2012.BluRay.x264-ASDF.mkv', False),
        ('/path/to/The.Sample.2012.BluRay.x264-ASDF/The.Sample.2012.BluRay.x264-ASDF.mkv', False),
    ),
)
def test_samples(path, exp_match):
    regex = re.compile(exclude.samples)
    match = regex.search(path)
    assert bool(match) is exp_match


@pytest.mark.parametrize(
    argnames='path, exp_match',
    argvalues=(
        ('/path/to/Foo.2012.BluRay.x264-ASDF.srt', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.SRT', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.Srt', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.sub', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.SUB', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.sUb', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.idx', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.IDX', True),
        ('/path/to/Foo.2012.BluRay.x264-ASDF.idX', True),
    ),
)
def test_subtitles(path, exp_match):
    regex = re.compile(exclude.subtitles)
    match = regex.search(path)
    assert bool(match) is exp_match
