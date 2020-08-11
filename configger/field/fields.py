"""
Classes of config fields, description of standard models of config fields.
"""
import pprint


class DefaultConfigField:
    """Config field containing any value"""
    def __init__(self, name: str, value: any = None):
        self.name = name
        self._value = value

    @property
    def value(self, value: any = None):
        if value is not None:
            self._value = value
        return self._value

    def __repr__(self):
        return f"(default) {self.name}: {self.value}"

    def __str__(self):
            return f"(default) {self.name}: {self.value}"


class ImmutableConfigField(DefaultConfigField):
    """Immutable config field"""
    def __init__(self, name: str, value: any = None):
        super(ImmutableConfigField, self).__init__(name, value)

    @property
    def value(self, value):
        if self._value is None:
            self._value = value
            return value
        return self._value


class SecretConfigField(DefaultConfigField):
    """Config Secret (Encrypted)"""
    ...
