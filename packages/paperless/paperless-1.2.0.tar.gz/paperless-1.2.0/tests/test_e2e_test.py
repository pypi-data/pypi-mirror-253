from os import getcwd
from paperless.paperless import Paperless
import pytest
from paperless.paperless import Paperless


def test_e2e_process(*args, **kwargs):
    """
    This is a test function for end-to-end processing.
    """
    Paperless(
        notebook_path=f'gs://pdp-cicd-test/test_go_gcs/prd/TopApps/test.ipynb').\
        configure().\
        wait_for_session().\
        verify().\
        execute(args,kwargs).\
        shutdown()
