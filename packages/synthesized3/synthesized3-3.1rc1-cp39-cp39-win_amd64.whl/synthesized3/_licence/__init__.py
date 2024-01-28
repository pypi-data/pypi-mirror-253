"""Synthesized Licence and feature flagging subpackage.

This subpackage contains the licence and feature flagging functionality for Synthesized.
It is used to load the licence key, verify the licence, and check that given features are
enabled.

The order of license events that occur on startup is as follows:
- Check if the licence key is set as an environment variable or in the default file location.
  If not
    - prompt the user to obtain a trial licence licence key
    - save the licence key.
- Verify the licence key:
    - Check the licence signature and date are both valid.

The public functions and attribAUtes of this subpackage are:

    - `licence.EMAIL`: The email address associated with the licence.
    - `licence.EXPIRY_DATE`: The expiry date of the licence.
    - `licence.FEATURES`: The features enabled by the licence.
    - `verify`: A function that verifies the licence is valid for a given feature.
    - `track`: A decorator used throughout the sdk to potentially send analytics events.

The variables are never used directly when evaluating the licence. Instead, these
variables are always redetermined from `_KEY` – an RSA encrypted string. This way user can't
change available features or expiry date,

Modules:
    analytics.py: Util functions for our tracking libraries.
    exceptions.py: Possible licence exceptions.
    features.py: Optional features are defined here.
    licence.py: Licence loading and verifying functions.
"""
from synthesized3._licence.exceptions import (
    FeatureUnavailableError,
    LicenceError,
    LicenceExpiredError,
    LicenceSignatureError,
    LicenceWarning,
)
from synthesized3._licence.features import MAX_FREE_COLUMNS, OptionalFeature
from synthesized3._licence.prompt import prompt_for_licence

from .analytics import track

from synthesized3._licence import licence  # isort:skip  # pylint: disable=wrong-import-order


verify = licence.verify

if not licence.is_key_set():
    key = prompt_for_licence()
    if key:
        licence.try_set_licence_key(key)

verify()
licence.maybe_print_free_version_message()


__all__ = [
    "verify",
    "track",
    "OptionalFeature",
    "MAX_FREE_COLUMNS",
    "LicenceError",
    "LicenceExpiredError",
    "LicenceWarning",
    "FeatureUnavailableError",
    "LicenceSignatureError",
]
