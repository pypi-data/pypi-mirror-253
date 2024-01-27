from pydantic import BaseModel


class GoogleAccountData(BaseModel):
    id: int
    name: str
    email: str
    profile_photo_url: str

    def __str__(self):
        return f"{self.email} (id={self.id})"

    @classmethod
    def from_account_list(cls, account_list: list):
        account_data = account_list[1][0]
        return cls(
            name=account_data[2],
            email=account_data[3],
            profile_photo_url=account_data[4],
            id=account_data[10],
        )
