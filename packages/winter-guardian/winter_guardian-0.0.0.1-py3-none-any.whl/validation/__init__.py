class DeferredValidationRegistry:
    _registry = []

    @classmethod
    def register(cls, validation_function):
        cls._registry.append(validation_function)

    @classmethod
    def run_validations(cls):
        for validation in cls._registry:
            validation()
