import pytest
from oastools.utils import files as Files
import os.path

parsed_file = {'openapi': '3.0.2', 'info': {'title': 'API Title',
                                            'version': '1.0'}, 'servers': [{
                                                'url': 'https://api.server.test/v1'}],
               'paths': {'/test': {'get': {'responses': {
                   '200': {'description': 'OK'}}}}}}

file_base = "./tests/fixtures/OpenAPI"

files = [file_base+".js", file_base+".json",
         file_base+".yaml", file_base+".yml", file_base+"doc", file_base+"bad"+".yml"]


def test_parse_file():

    for f in files[0:4]:
        path = os.path.abspath(f)
        parsed = Files.parse_file(path)
        assert(isinstance(parsed, dict))
        assert(parsed == parsed_file)
    with pytest.raises(ValueError):
        Files.parse_file(os.path.abspath(files[4]))
    with pytest.raises(FileNotFoundError):
        Files.parse_file(os.path.abspath(files[5]))


def test_get_file_type():
    for f in files[0:2]:
        assert(Files.__get_file_type(f) == Files.FileType.JSON)
    for f in files[2:4]:
        assert(Files.__get_file_type(f) == Files.FileType.YAML)
    for f in files[5]:
        with pytest.raises(ValueError):
            Files.__get_file_type(f)
