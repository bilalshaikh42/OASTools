import json
import yaml
import yaml.parser
from enum import Enum
from .errors import NotImplementedError
from .errors import ParseError


class FileType(Enum):
    UNKWN = 0
    JSON = 1
    YAML = 2


def parse_file(path):
    type = __get_file_type(path)

    with open(path) as f:
        spec_str = f.read()
        if(type == FileType.JSON):
            return __parse_json(spec_str)
        elif(type == FileType.YAML):
            return __parse_yaml(spec_str)


def __get_file_type(path):

    yml_ext = path.rfind(".yml")
    yaml_ext = path.rfind(".yaml")
    js_ext = path.rfind(".js")
    json_ext = path.rfind(".json")

    if(path[yml_ext:] == ".yml" or path[yaml_ext:] == ".yaml"):
        return FileType.YAML
    elif(path[js_ext:] == ".js" or path[json_ext:] == ".json"):
        return FileType.JSON
    else:
        raise ValueError("Unsupported File Type. File:" +
                         path + " is not JSON or YAML")


def __parse_yaml(spec_str):

    try:
        return yaml.safe_load(spec_str)
    except yaml.parser.ParserError as err:
        raise ParseError(str(err))


def __parse_json(spec_str):
    try:
        return json.loads(spec_str)
    except ValueError as err:
        raise ParseError(str(err))


def __serialize_yaml(spec_dict):

    dump = yaml.dump(spec_dict,
                     allow_unicode=True,
                     encoding=None,
                     default_flow_style=False)
    return dump


def __serialize_json(spec_dict):

    dump = json.dumps(spec_dict, ensure_ascii=False, indent=4)
    return dump
