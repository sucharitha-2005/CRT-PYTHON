class ATM:
    def __init__(self, pin):
        self.__pin = pin  # private attribute

    def verify_pin(self, pin):
        """Check if entered PIN matches stored PIN"""
        return self.__pin == pin

    def change_pin(self, old_pin, new_pin):
        """Change PIN only if old PIN is correct"""
        if self.verify_pin(old_pin):
            self.__pin = new_pin
            return "PIN changed successfully"
        else:
            return "Incorrect old PIN"