from textwrap import dedent

from src.mailing.send_email import send_email
from src.models import UserOrm


async def send_email_confirmed(
    user: UserOrm,
):
    recipient = user.email
    subject = "Email confirmed"

    plain_content = dedent(
        f"""\
        Dear {recipient},

        Your email has been confirmed.

        Your site admin,
        © 2026
        """
    )

    await send_email(
        recipient=recipient,
        subject=subject,
        plain_content=plain_content,
        html_content=None,
    )