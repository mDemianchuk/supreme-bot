class BillingInfo:
    def __init__(
            self,
            full_name: str,
            email: str,
            phone: str,
            address: str,
            unit: str,
            zip_code: str,
            state: str,
            cc_number: str,
            exp_month: str,
            exp_year: str,
            cvv: str
    ):
        self.full_name = full_name.strip()
        self.email = email.strip()
        self.phone = phone.strip()
        self.address = address.strip()
        self.unit = unit.strip()
        self.zip_code = zip_code.strip()
        self.state = state.strip()
        self.cc_number = cc_number.strip()
        self.exp_month = exp_month.strip()
        self.exp_year = exp_year.strip()
        self.cvv = cvv.strip()
