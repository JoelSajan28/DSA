from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from abc import ABC, abstractmethod
from typing import Iterable, Dict, List, Optional


class Priority(Enum):
    LOW = "low"
    HIGH = "high"


@dataclass(frozen=True)
class Notification:
    title: str
    body: str
    priority: Priority = Priority.LOW


@dataclass(frozen=True)
class Recipient:
    user_id: str
    email: Optional[str] = None
    phone: Optional[str] = None
    device_token: Optional[str] = None
    preferred_channels: tuple[str, ...] = ("email",)


@dataclass(frozen=True)
class SendResult:
    channel: str
    success: bool
    error: Optional[str] = None


class Channel(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def send(self, notification: Notification, recipient: Recipient) -> None:
        """Raise an exception on failure."""


class EmailChannel(Channel):
    name = "email"

    def send(self, notification: Notification, recipient: Recipient) -> None:
        if not recipient.email:
            raise ValueError("Missing recipient email")
        # send email (stub)
        # print(f"EMAIL to {recipient.email}: {notification.title}")


class SmsChannel(Channel):
    name = "sms"

    def send(self, notification: Notification, recipient: Recipient) -> None:
        if not recipient.phone:
            raise ValueError("Missing recipient phone")
        # send sms (stub)


class PushChannel(Channel):
    name = "push"

    def send(self, notification: Notification, recipient: Recipient) -> None:
        if not recipient.device_token:
            raise ValueError("Missing device token")
        # send push (stub)


class RetryPolicy:
    def __init__(self, max_attempts: int = 3):
        self.max_attempts = max_attempts

    def attempts_for(self, notification: Notification) -> int:
        # simple rule: high priority gets retries, low priority only 1 attempt
        return self.max_attempts if notification.priority == Priority.HIGH else 1


class NotificationDispatcher:
    def __init__(self, channels: Iterable[Channel], retry_policy: RetryPolicy):
        self._channels: Dict[str, Channel] = {c.name: c for c in channels}
        self._retry_policy = retry_policy

    def dispatch(self, notification: Notification, recipient: Recipient) -> List[SendResult]:
        results: List[SendResult] = []
        attempts = self._retry_policy.attempts_for(notification)

        for channel_name in recipient.preferred_channels:
            channel = self._channels.get(channel_name)
            if not channel:
                results.append(SendResult(channel=channel_name, success=False, error="Unknown channel"))
                continue

            last_err = None
            for _ in range(attempts):
                try:
                    channel.send(notification, recipient)
                    results.append(SendResult(channel=channel_name, success=True))
                    last_err = None
                    break
                except Exception as e:
                    last_err = str(e)

            if last_err is not None:
                results.append(SendResult(channel=channel_name, success=False, error=last_err))

        return results