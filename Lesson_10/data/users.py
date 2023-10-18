import dataclasses
import datetime

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birthdate: datetime.date
    subject: str
    hobby: str
    picture: str
    current_address: str
    state: str
    city: str
