from __future__ import annotations

from functools import cached_property
from typing import Optional

from qctrlworkflowclient import ApiRouter
from segment.analytics import Client as SegmentClient

from fireopal.config import get_config

# Note: The Segment analytics write key is not private
# and thus can live within the Fire Opal Client. Please
# see: https://github.com/segmentio/Analytics-CSharp/issues/69
_SEGMENT_ANALYTICS_WRITE_KEY = "gPMCMpFYrKuDXOFQgPn99ZzeGZUgf8Jw"


def _get_user_email(router: Optional[ApiRouter] = None) -> str:
    """
    Grabs the user email embedded into the
    user's access token.

    Parameters
    ----------
    router : ApiRouter, optional
        The ApiRouter instance connected to the user. Defaults to None.

    Returns
    -------
    str
        The user's email for identification and tracking.
    """
    if router is None:
        router = get_config().get_router()
    assert isinstance(router, ApiRouter)
    # pylint: disable=protected-access
    return router._client._auth._get_payload(router._client.get_access_token())["email"]


def _check_for_remote_router() -> bool:
    """
    Check to see if it is a local or remote version
    of the Fire Opal client.

    Returns
    -------
    bool
        True if it is the remote Fire Opal client.
    """
    router = get_config().get_router()
    # pylint: disable=protected-access
    if isinstance(router, ApiRouter) and router._client._auth is not None:
        return True
    return False


class _BaseEventTracker:  # pylint:disable=too-few-public-methods
    """Base class for implementing event tracking."""

    def __init__(
        self, analytics_write_key: str, debug: bool = False, send: bool = True
    ):
        self._analytics_write_key = analytics_write_key
        self._analytics_options = {"debug": debug, "send": send}

    @cached_property
    def _client(self) -> SegmentClient:
        """Returns the configured Segment client."""
        return SegmentClient(self._analytics_write_key, **self._analytics_options)


class _FireOpalEventTracker(_BaseEventTracker):
    """
    Implements the Fire Opal client tracking events.
    """

    def track_get_result(self, user_email: str, action_id: int | str) -> None:
        """
        Tracker for the get_result function.

        Parameters
        ----------
        user_email : str
            The user's email address that will be used to uniquely identify this event.
        action_id : int or str
            The action_id which uniquely identifies the result. It is an input to
            `get_result` function.
        """
        self._client.identify(user_email, {"requested_get_result": True})
        self._client.track(
            user_email,
            event="requested_get_result",
            properties={"action_id": action_id},
        )

    def track_activity_monitor(
        self, user_email: str, limit: int, offset: int, status: Optional[str]
    ) -> None:
        """
        Tracker for activity monitor.

        Parameters
        ----------
        user_email : str
           The user's email address that will be used to uniquely identify this event.
        limit : int
            The number of actions to fetch. Cannot exceed 50.
        offset : int
            The number of recent actions to ignore before starting to fetch.
        status : str or None, optional
            The filter for action status. If None, fetches actions of all
            statuses.
        """
        self._client.identify(user_email, {"requested_activity_monitor": True})
        self._client.track(
            user_email,
            event="requested_activity_monitor",
            properties={"limit": limit, "offset": offset, "status": status},
        )

    def track_get_action_metadata(
        self, user_email: str, limit: int, offset: int, status: Optional[str]
    ) -> None:
        """
        Tracker the get_action_metadata function.

        Parameters
        ----------
        user_email : str
           The user's email address that will be used to uniquely identify this event.
        limit : int
            The number of actions to fetch. Cannot exceed 50.
        offset : int
            The number of recent actions to ignore before starting to fetch.
        status : str or None, optional
            The filter for action status. If None, fetches actions of all
            statuses.
        """
        self._client.identify(user_email, {"requested_get_action_metadata": True})
        self._client.track(
            user_email,
            event="requested_get_action_metadata",
            properties={"limit": limit, "offset": offset, "status": status},
        )

    def track_configure_organization(
        self, user_email: str, organization_slug: str
    ) -> None:
        """Tracks the configure_org monitor."""
        self._client.identify(user_email, {"requested_configure_org": True})
        self._client.track(
            user_email,
            event="requested_configure_org",
            properties={"organization_slug": organization_slug},
        )

    def track_make_credentials_for_ibmq(self, user_email: str) -> None:
        """Tracks the credential creation for IBMQ."""
        self._client.identify(user_email, {"requested_make_ibmq_credentials": True})
        self._client.track(user_email, event="requested_make_ibmq_credentials")

    def track_make_credentials_for_ibm_cloud(self, user_email: str) -> None:
        """Tracks the credential creation for IBM cloud."""
        self._client.identify(
            user_email, {"requested_make_ibm_cloud_credentials": True}
        )
        self._client.track(user_email, event="requested_make_ibm_cloud_credentials")


_EVENT_TRACKER = _FireOpalEventTracker(
    analytics_write_key=_SEGMENT_ANALYTICS_WRITE_KEY,
    debug=False,
    send=True,
)
