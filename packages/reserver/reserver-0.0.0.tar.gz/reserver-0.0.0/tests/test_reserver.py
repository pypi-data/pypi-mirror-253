from reserver import Uploader
from reserver.reserver_func import get_random_name

# main pypi account - to be removed.
# pypi_token = "pypi-AgEIcHlwaS5vcmcCJDRmNThmNDFkLTZhNTYtNDU2Ny05YjhlLTM4YzNkNTczMDA4NgACKlszLCJiMjNmNjZlYS1iZGEzLTQ4NzYtYTdmNy02ZjZlYjYwM2I4NTMiXQAABiAqGQglXAgXzZUL5Ik-NsC1R8TidtKtZRZzbA32C8KiCA"
# main pypi account new password: "kwhM8Pp$S@sCx6m"

# test.pypi account
# test_pypi_token = "pypi-AgENdGVzdC5weXBpLm9yZwIkMTFkZDhjNWMtMTY2My00OWMyLTlmZGItZWZkMzU2NDQxMWJlAAIqWzMsIjJhYjkwZjE4LWQ1ODItNGFiNy05NTYwLWUxN2ZiZTcwY2Y2NyJdAAAGIDVymuINEbiyhSBeB_-ysIapdi_wHTTjD9vpV6mFGzvu"
# test pypi account new password: "fgtwwU64X7yEE6z"

# AHReccese reserver token: 

import os
test_pypi_token = os.environ.get("TEST_PYPI_PASSWORD")

def test_package_exists():
    # test reserved name
    uploader = Uploader(test_pypi_token, is_test_pypi_account= True)
    assert uploader.upload_to_pypi("numpy") == False

def test_valid_package_invalid_credentials():
    # test not reserved name -> wrong credentials
    wrong_pypi_token = "pypi-wrong-api-token"
    uploader = Uploader(wrong_pypi_token, is_test_pypi_account= True)
    assert uploader.upload_to_pypi(get_random_name()) == False

def test_valid_package_valid_credentials():
    # test not reserved name -> correct credentials
    pypi_token = "pypi-AgEIcHlwaS5vcmcCJDExMWY5NjljLWQ1MDktNGY3YS1hM2IxLTQ0NDdjMjUzMmM1NAACKlszLCI4YWI5MmU3Mi02ZTJiLTQzM2EtYjA4Ni0wNzYxNGU4NTM2Y2MiXQAABiAGihGds9jq0FdriHsw1q9jq4UY-LmjEyNFgT8lNkaxCg"
    uploader = Uploader(pypi_token)
    uploader.upload_to_pypi("reserver")
    # assert True == True
test_valid_package_valid_credentials()