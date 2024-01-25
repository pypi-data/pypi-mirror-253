# -*- coding: utf-8 -*-

from pathlib_mate import Path

dir_python_lib = Path.dir_here(__file__)

dir_project_root = dir_python_lib.parent

# ------------------------------------------------------------------------------
# Virtual Environment Related
# ------------------------------------------------------------------------------
dir_venv = dir_project_root / ".venv"
dir_venv_bin = dir_venv / "bin"

# virtualenv executable paths
bin_pytest = dir_venv_bin / "pytest"

# test related
dir_htmlcov = dir_project_root / "htmlcov"
path_cov_index_html = dir_htmlcov / "index.html"
dir_unit_test = dir_project_root / "tests"


# ------------------------------------------------------------------------------
# ${HOME}/.aws_console_url_search/ dir related
# ------------------------------------------------------------------------------
dir_home = Path.home()
dir_aws_console_url_search = dir_home.joinpath(".aws_console_url_search")
dir_index = dir_aws_console_url_search.joinpath(".index")
dir_cache = dir_aws_console_url_search.joinpath(".cache")
path_config = dir_aws_console_url_search.joinpath("config.json")
path_current_region = dir_aws_console_url_search.joinpath("current_region.txt")

# ------------------------------------------------------------------------------
# ${dir_project_root}/aws_console_url_search/
# ------------------------------------------------------------------------------
path_data_json = dir_python_lib.joinpath("data.json")
path_region_json = dir_python_lib.joinpath("region.tsv")

dir_code = dir_python_lib.joinpath("code")
path_console_urls_json = dir_code.joinpath("console-urls.json")
