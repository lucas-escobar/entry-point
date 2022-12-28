import pytest
import arghandler

parser = arghandler.arghandler.get_argparser()

create_test_vals = [
    ('', False), ('-d', False), ('-z', False), ('-c', True), ('--create', True)
]
directory_test_vals = [
    ('/', True), ('./', True), ('/tmpdir', True), ('/tmpdir/', True),
    ('/tmpdir/file.txt', False), ('/tmpdir/file', False), (__file__, True)
]


@pytest.mark.parametrize('args, expected', create_test_vals)
def test_create_state(args, expected):
    """Verify arg value for create option is equal to True only if
    the -c or --create flags are used
    """
    try:
        state = parser.parse_args([args]).create
    except:
        state = False
    assert state == expected


@pytest.mark.parametrize('args, expected', directory_test_vals)
def test_directory(args, expected):
    """Verify that the path to the journal root directory is changed
    when -d or --directory flag is set
    """

