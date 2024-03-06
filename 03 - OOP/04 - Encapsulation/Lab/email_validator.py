import re
from typing import List


class EmailValidator:
    email_pattern = re.compile(r"@|\.")

    def __init__(
        self, min_length: int, mails: List[str], domains: List[str]
    ) -> None:
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, username: str) -> bool:
        return len(username) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email: str) -> bool:
        username, mail, domain = self.email_pattern.split(email)

        return all((
            self.__is_name_valid(username),
            self.__is_mail_valid(mail),
            self.__is_domain_valid(domain),
        ))
