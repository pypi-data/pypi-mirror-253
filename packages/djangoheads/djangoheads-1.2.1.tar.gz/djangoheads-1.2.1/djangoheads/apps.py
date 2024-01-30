from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class DjangoheadsConfig(AppConfig):
    """DjangoHeads app config."""

    name = "djangoheads"
    verbose_name = "DjangoHeads Core Library"

    def ready(self) -> None:
        """Initializes the app."""
        self.init_sentry_sdk()

    def init_sentry_sdk(self) -> None:
        """Initializes sentry_sdk if SENTRY_DSN is set."""
        sentry_dsn = getattr(settings, "SENTRY_DSN", None)
        if not sentry_dsn:
            return

        try:
            import sentry_sdk  # noqa: PLC0415
            from sentry_sdk.integrations.django import DjangoIntegration  # noqa: PLC0415
        except ImportError:
            raise ImproperlyConfigured("sentry_sdk is not installed but SENTRY_DSN is set")

        sentry_sdk.init(
            dsn=sentry_dsn,
            integrations=[
                DjangoIntegration(),
            ],
            traces_sample_rate=getattr(settings, "SENTRY_TRACES_SAMPLE_RATE", 0.1),
            send_default_pii=settings.DEBUG,
            release=getattr(settings, "SENTRY_RELEASE", "service@release-undefined"),
        )
