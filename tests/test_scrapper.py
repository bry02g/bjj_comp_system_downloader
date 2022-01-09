import pytest
from bjj_comp_system_scrapper.scrapper import (
    get_current_timestamp,
    create_timestamp_folder,
)

from unittest.mock import patch, Mock


def test_get_current_timestamp():
    with patch("bjj_comp_system_scrapper.scrapper.datetime") as mock_datetime:
        mock_datetime.datetime.utcnow.return_value = "2021-12-24 01:48:51.896888"

        timestamp = get_current_timestamp()

        assert timestamp == "2021-12-24_01-48-51"


def test_create_timestamp_folder_with_valid_path():
    with patch("bjj_comp_system_scrapper.scrapper.os") as mock_os:
        mock_os.mkdir.return_value = None

        save_location = create_timestamp_folder("~/test/save/path/for/data/")

        assert save_location != None


def test_create_timestamp_folder_with_invalid_path():
    with patch("bjj_comp_system_scrapper.scrapper.os") as mock_os:
        mock_os.mkdir.side_effect = Exception("Could Not Create Folder")

        with pytest.raises(Exception):
            save_location = create_timestamp_folder(
                "~/some/invalid/path/that/does/not/exist"
            )

            mock_os.mkdir.assert_called_once()
