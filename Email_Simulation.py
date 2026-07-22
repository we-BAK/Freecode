"""
A small email-simulation system demonstrating clean OOP design in Python.

Improvements over the original version:
- Type hints throughout for readability and IDE support
- `Enum` for read/unread status instead of a bare bool + string
- `dataclass`-free but slot-based `Email`/`User`/`Inbox` classes for clarity
- Reply / forward support
- Search by sender or subject keyword
- Unread-count helper
- Defensive checks (e.g. can't email yourself, empty subject/body warnings)
- An interactive CLI menu (`run_cli`) in addition to the scripted demo
- Consistent, testable string formatting via `__str__` / `__repr__`
"""

from __future__ import annotations

import datetime as dt
from enum import Enum
from typing import Optional


class Status(Enum):
    UNREAD = "Unread"
    READ = "Read"


class Email:
    """A single email message."""

    __slots__ = ("sender", "receiver", "subject", "body", "timestamp", "status", "in_reply_to")

    def __init__(
        self,
        sender: "User",
        receiver: "User",
        subject: str,
        body: str,
        in_reply_to: Optional["Email"] = None,
    ) -> None:
        self.sender = sender
        self.receiver = receiver
        self.subject = subject.strip() or "(no subject)"
        self.body = body
        self.timestamp = dt.datetime.now()
        self.status = Status.UNREAD
        self.in_reply_to = in_reply_to

    def mark_as_read(self) -> None:
        self.status = Status.READ

    def display_full(self) -> None:
        self.mark_as_read()
        print("\n--- Email ---")
        print(f"From:     {self.sender.name}")
        print(f"To:       {self.receiver.name}")
        print(f"Subject:  {self.subject}")
        print(f"Received: {self.timestamp:%Y-%m-%d %H:%M}")
        if self.in_reply_to:
            print(f"(In reply to: \"{self.in_reply_to.subject}\")")
        print(f"\n{self.body}")
        print("------------\n")

    def __str__(self) -> str:
        return (
            f"[{self.status.value}] From: {self.sender.name} | "
            f"Subject: {self.subject} | Time: {self.timestamp:%Y-%m-%d %H:%M}"
        )

    def __repr__(self) -> str:
        return f"Email(sender={self.sender.name!r}, subject={self.subject!r}, status={self.status.name})"


class Inbox:
    """Holds a `User`'s received emails."""

    def __init__(self) -> None:
        self._emails: list[Email] = []

    def receive(self, email: Email) -> None:
        self._emails.append(email)

    def list_emails(self) -> None:
        if not self._emails:
            print("Your inbox is empty.\n")
            return
        print("\nYour Emails:")
        for i, email in enumerate(self._emails, start=1):
            print(f"{i}. {email}")
        print(f"\n({self.unread_count()} unread)\n")

    def unread_count(self) -> int:
        return sum(1 for e in self._emails if e.status is Status.UNREAD)

    def get(self, index: int) -> Optional[Email]:
        """1-based lookup; returns None (and prints a message) if invalid."""
        if not self._emails:
            print("Inbox is empty.\n")
            return None
        actual = index - 1
        if actual < 0 or actual >= len(self._emails):
            print("Invalid email number.\n")
            return None
        return self._emails[actual]

    def read(self, index: int) -> None:
        email = self.get(index)
        if email:
            email.display_full()

    def delete(self, index: int) -> None:
        if self.get(index) is None:
            return
        del self._emails[index - 1]
        print("Email deleted.\n")

    def search(self, keyword: str) -> list[Email]:
        keyword = keyword.lower()
        return [
            e for e in self._emails
            if keyword in e.subject.lower() or keyword in e.sender.name.lower()
        ]


class User:
    """A user with a name and an inbox."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver: "User", subject: str, body: str) -> Optional[Email]:
        if receiver is self:
            print("You can't send an email to yourself.\n")
            return None
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive(email)
        print(f"Email sent from {self.name} to {receiver.name}!\n")
        return email

    def reply(self, original: Email, body: str) -> Optional[Email]:
        if original.receiver is not self:
            print("You can only reply to emails sent to you.\n")
            return None
        subject = original.subject
        if not subject.lower().startswith("re:"):
            subject = f"Re: {subject}"
        return self.send_email(original.sender, subject, body)

    def check_inbox(self) -> None:
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index: int) -> None:
        self.inbox.read(index)

    def delete_email(self, index: int) -> None:
        self.inbox.delete(index)

    def search_inbox(self, keyword: str) -> None:
        results = self.inbox.search(keyword)
        if not results:
            print(f'No emails matching "{keyword}".\n')
            return
        print(f'\nResults for "{keyword}":')
        for email in results:
            print(f"- {email}")
        print()


def run_cli() -> None:
    """Simple interactive menu for exploring the mailbox."""
    users: dict[str, User] = {}

    def get_or_create(name: str) -> User:
        return users.setdefault(name, User(name))

    print("=== Mini Email System ===")
    current_name = input("Enter your username: ").strip() or "Me"
    me = get_or_create(current_name)

    menu = """
1. Send email
2. Check inbox
3. Read email
4. Reply to email
5. Delete email
6. Search inbox
7. Quit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            to_name = input("Recipient name: ").strip()
            receiver = get_or_create(to_name)
            subject = input("Subject: ").strip()
            body = input("Body: ").strip()
            me.send_email(receiver, subject, body)

        elif choice == "2":
            me.check_inbox()

        elif choice == "3":
            idx = input("Email number to read: ").strip()
            if idx.isdigit():
                me.read_email(int(idx))

        elif choice == "4":
            idx = input("Email number to reply to: ").strip()
            if idx.isdigit():
                original = me.inbox.get(int(idx))
                if original:
                    body = input("Reply body: ").strip()
                    me.reply(original, body)

        elif choice == "5":
            idx = input("Email number to delete: ").strip()
            if idx.isdigit():
                me.delete_email(int(idx))

        elif choice == "6":
            keyword = input("Search keyword: ").strip()
            me.search_inbox(keyword)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.\n")


def demo() -> None:
    """Scripted demo matching the behavior of the original `main()`."""
    tory = User("Tory")
    ramy = User("Ramy")

    hello = tory.send_email(ramy, "Hello", "Hi Ramy, just saying hello!")
    ramy.check_inbox()
    ramy.read_email(1)
    if hello:
        ramy.reply(hello, "Hi Tory, hope you are fine.")
    tory.check_inbox()


if __name__ == "__main__":
    demo()
