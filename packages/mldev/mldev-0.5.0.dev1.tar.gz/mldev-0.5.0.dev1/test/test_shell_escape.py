from mldev.utils import shell_escape


def test_basic():
    assert "mldev run -f experiment.yml" ==  shell_escape("mldev run -f experiment.yml")

    assert "echo ${program}" == shell_escape("echo ${program}")

    assert "{\\\"name\\\":\\\"value\\\", \\\"another\\\":2}" == \
        shell_escape("{\"name\":\"value\", \"another\":2}")

def test_shell_chaining():
    assert " a && b" == shell_escape(" a && b")

    assert "a ; b" == shell_escape("a ; b")


def test_quotes():
    assert "\\\\" == shell_escape("\\")

    assert "\\\"abc\\\"" == shell_escape('"abc"')

    assert "\\\'abc\\\'" == shell_escape("'abc'")

    assert "\\\'\\\"\\\'\\\"" == shell_escape("'\"'\"")


def test_json():
    import json
    data = dict(t=123, d="123")
    assert "\\'{\\\"t\\\": 123, \\\"d\\\": \\\"123\\\"}\\'" == \
           shell_escape(f"'{json.dumps(data)}'")

