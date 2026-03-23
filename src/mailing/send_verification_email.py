from textwrap import dedent

from src.mailing.send_email import send_email
from src.models import UserOrm


async def send_verification_email(
    user: UserOrm,
    verification_link: str,
    verification_token: str,
):
    recipient = user.email
    subject = "Confirm your email for online-shop.com"

    plain_content = dedent(
        f"""\
        Dear {recipient},
            
        Please follow the link to verify your email:
        {verification_link}
        
        Use this token to verify your email:
        {verification_token}
        
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