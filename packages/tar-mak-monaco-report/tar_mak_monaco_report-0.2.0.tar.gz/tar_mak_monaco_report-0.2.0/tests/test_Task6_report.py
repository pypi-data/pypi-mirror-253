import shutil
from src.tar_mak_monaco_report.Task6_report import *
import pytest
from unittest.mock import patch
from datetime import timedelta


@pytest.fixture
def temp_abbr_file(tmp_path):
    data = "FAM_Fernando Alonso_MCLAREN RENAULT\nCSR_Carlos Sainz_RENAULT"
    temp_file = tmp_path / "temp.txt"
    temp_file.write_text(data)
    return temp_file


@pytest.fixture
def temp_start_file(tmp_path):
    data = "FAM2018-05-24_12:13:04.512\nCSR2018-05-24_12:03:15.145"
    temp_file = tmp_path / "temp_start.txt"
    temp_file.write_text(data)
    return temp_file


@pytest.fixture
def temp_end_file(tmp_path):
    data = "FAM2018-05-24_12:14:17.169\nCSR2018-05-24_12:04:28.095"
    temp_file = tmp_path / "temp_end.txt"
    temp_file.write_text(data)
    return temp_file


@pytest.fixture
def fake_folder(tmp_path, temp_abbr_file, temp_end_file, temp_start_file):
    folder_path = tmp_path / "data_folder"
    folder_path.mkdir()

    shutil.copy(temp_abbr_file, folder_path / "abbreviations.txt")
    shutil.copy(temp_end_file, folder_path / "end.log")
    shutil.copy(temp_start_file, folder_path / "start.log")
    return folder_path


def test_build_report(temp_abbr_file, temp_end_file, temp_start_file):
    paths = [Path(temp_abbr_file), Path(temp_end_file), Path(temp_start_file)]
    assert build_report(paths=paths) == [{'abbr': 'FAM',
                                          'name': 'Fernando Alonso',
                                          'car': 'MCLAREN RENAULT',
                                          'time': timedelta(seconds=72, microseconds=657000),
                                          'place': '1.'},
                                         {'abbr': 'CSR',
                                          'name': 'Carlos Sainz',
                                          'car': 'RENAULT',
                                          'time': timedelta(seconds=72, microseconds=950000),
                                          'place': '2.'}]


def test_parse_abbr(temp_abbr_file):
    assert parse_abbr(temp_abbr_file) == [{'abbr': 'FAM', 'name': 'Fernando Alonso', 'car': 'MCLAREN RENAULT'},
                                          {'abbr': 'CSR', 'name': 'Carlos Sainz', 'car': 'RENAULT'}]


def test_parse_log(temp_start_file, temp_end_file):
    assert (parse_log(start_log=Path(temp_start_file), end_log=Path(temp_end_file)) ==
            {'FAM': timedelta(seconds=72, microseconds=657000), 'CSR': timedelta(seconds=72, microseconds=950000)})


def test_print_report(capsys, temp_abbr_file, temp_end_file, temp_start_file):
    paths = [Path(temp_abbr_file), Path(temp_end_file), Path(temp_start_file)]
    print_report(paths=paths)
    captured = capsys.readouterr()
    assert "1. Fernando Alonso | MCLAREN RENAULT | 0:01:12.657\n2. Carlos Sainz | RENAULT | 0:01:12.950" in captured.out


def test_main_with_files_arg(capsys, fake_folder):
    test_args = ['main.py', '--files', str(fake_folder)]
    with patch('sys.argv', test_args):
        main()
    captured = capsys.readouterr()
    assert "1. Fernando Alonso | MCLAREN RENAULT | 0:01:12.657" in captured.out


def test_main_with_driver_arg(capsys, fake_folder):
    test_args = ['main.py', '--files', str(fake_folder), '--driver', "Fernando Alonso"]
    with patch('sys.argv', test_args):
        main()
    captured = capsys.readouterr()
    assert "1. Fernando Alonso | MCLAREN RENAULT | 0:01:12.657" in captured.out


def test_main_with_desc_arg(capsys, fake_folder):
    test_args = ['main.py', '--files', str(fake_folder), '--desc']
    with patch('sys.argv', test_args):
        main()
    captured = capsys.readouterr()
    assert "2. Carlos Sainz | RENAULT | 0:01:12.950\n1. Fernando Alonso | MCLAREN RENAULT | 0:01:12.657" in captured.out
