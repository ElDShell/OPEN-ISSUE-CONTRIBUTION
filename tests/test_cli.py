from Training.cli import main

def test_string_length(capsys):
    # Test the --string-length argument
    test_length = 15
    main_args = ["--string-length", str(test_length)]
    main(main_args)
    captured = capsys.readouterr()
    assert f"The length of the string is: {len(str(test_length))}" in captured.out

def test_string_length_accepts_text(capsys):
    main(["--string-length", "hello"])
    captured = capsys.readouterr()
    assert "The length of the string is: 5" in captured.out

def test_version(capsys):
    # Test the --version argument
    main_args = ["--version"]
    try:
        main(main_args)
    except SystemExit as e:
        assert e.code == 0
    captured = capsys.readouterr()
    assert "Training 0.1.0" in captured.out